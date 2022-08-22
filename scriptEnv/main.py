#! ironPython


# This is the main file to run the whole algorithm and interacting with rhino
###############################################
# PROGRAMS 
'''
1. RhinoCommon SDK
2. Ladybug Tools SDK
'''
################################################################################
import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from HoneybeeUsr.annalDaylight import *
from HoneybeeUsr.sensorGrid import grid
from HoneybeeUsr.hbAssign import *
from HoneybeeUsr.epw import *
from HoneybeeUsr.hbRecipe import *

from Algorithm.model import rhinoSpace
from Algorithm.rhinoData import *
from Algorithm.rhinoVis import canvas, vis
from Algorithm.rhinoCurve import curve

from Tools.dirLocation import *

################################################################################
# PARAMETERS

# model
north = 0 # 
# sensorgrid
gridSize = 0.5
offsetDistance = 1.2

################################################################################
# MODEL PREPARATION
################################################################################

'from rhino model to honeybee model'
objDic = rhinoSpace.accessRhinoLayers()
hbModel = rhinoSpace.rhinoToHoneybee(objDic)

'create sampling area'
# this is a GUID object
samplingArea = objDic['GRIDS'][0]
# transfer GUID to Brep object
samplingObj = transData.GUIDToBrep(samplingArea)
sampleData = grid.generateSensorGrid(samplingObj, gridSize, offsetDistance, ladybugMesh = True)

'extract sampling data'
samplePts = sampleData[0] # list
sampleDirections = sampleData[1]
sampleMeshes = sampleData[3] # class mesh object in a list
sampleMesh = sampleMeshes[0]

'visualize sampling data'
# canvas.enableRedraw()
# vis.points(samplePts)
# for pt in samplePts:
#     samplePolyline = curve.squareFromCenter(pt, gridSize)
#     vis.polyline(samplePolyline)

'sampling area from rhino to honeybee object'
# hbGrid is a class object
hbGrid = grid.HBSensorGrid(None, samplePts, sampleDirections, sampleMesh, samplingObj)
# # get point tuple (location + direction)
# hbGrid = hbGrid.sensors
# # transfer tuple to list
# hbGrid = list(hbGrid)
hbModelWithGrid = assign.viewOrGridToModel(hbModel, None, hbGrid)

################################################################################
# WEATHER FILE
################################################################################
wea = epw.epwToWea(Dir.epwPath, None, '')

################################################################################
# RUN ANNUAL DAYLIGHT
################################################################################
battery.annualDaylight(hbModelWithGrid, wea, north, '', '', '', '', True)