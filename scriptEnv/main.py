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

from HoneybeeUsr.sensorGrid import grid
from HoneybeeUsr.hbAssign import *
from HoneybeeUsr.epw import *
from HoneybeeUsr.hbRecipe import *

from Algorithm.model import rhinoSpace
from Algorithm.rhinoData import *
from Algorithm.rhinoVis import canvas, vis
from Algorithm.rhinoCurve import curve

from Tools.dirLocation import *
from Tools.osUtil import *
from Tools.winPrompt import *

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

# 'from rhino model to honeybee model'
# objDic = rhinoSpace.accessRhinoLayers()
# hbModel = rhinoSpace.rhinoToHoneybee(objDic)

# 'create sampling area'
# # this is a GUID object
# samplingArea = objDic['GRIDS'][0]
# # transfer GUID to Brep object
# samplingObj = transData.GUIDToBrep(samplingArea)
# sampleData = grid.generateSensorGrid(samplingObj, gridSize, offsetDistance, ladybugMesh = True)

# 'extract sampling data'
# samplePts = sampleData[0] # list
# sampleDirections = sampleData[1]
# sampleMeshes = sampleData[3] # class mesh object in a list
# sampleMesh = sampleMeshes[0]

# 'visualize sampling data'
# # canvas.enableRedraw()
# # vis.points(samplePts)
# # for pt in samplePts:
# #     samplePolyline = curve.squareFromCenter(pt, gridSize)
# #     vis.polyline(samplePolyline)

# 'sampling area from rhino to honeybee object'
# # hbGrid is a class object
# hbGrid = grid.HBSensorGrid(None, samplePts, sampleDirections, sampleMesh, samplingObj)
# # # get point tuple (location + direction)
# # hbGrid = hbGrid.sensors
# # # transfer tuple to list
# # hbGrid = list(hbGrid)
# hbModelWithGrid = assign.viewOrGridToModel(hbModel, None, hbGrid)

# ################################################################################
# # WEATHER FILE
# ################################################################################
# wea = epw.epwToWea(Dir.epwPath, None, '')

# ################################################################################
# # RUN ANNUAL DAYLIGHT(Daylight Autonomy)
# ################################################################################
# resultPath = battery.annualDaylight(hbModelWithGrid, wea, north, '', None, '', '', True)

################################################################################
# move files to the project folder
################################################################################
resultPath = 'C:\\Users\\zxin1\\simulation\\unnamed_06045e9c'
daylitFolder = resultPath + '\\annual_daylight'
metricsFolder = daylitFolder + '\\metrics'
modelFolder = daylitFolder + '\\model'

rawResultsFolder = {daylitFolder + '\\results': ['.ini', '.txt']}
gridPtFolder = {modelFolder + '\\grid': '.pts'}
cdaFolder = {metricsFolder + '\\cda': '.cda'}
daFolder = {metricsFolder + '\\da': '.da'}
udiFolder = {metricsFolder + '\\udi': '.udi'}
udiLowFolder = {metricsFolder + '\\udi_lower': '.udi'}
udiUpperFolder = {metricsFolder + '\\udi_upper': '.udi'}


filePath = osUtil.searchFile(rawResultsFolder)
win.copyFile(filePath, rawResultsFolder, twd)
