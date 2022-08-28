#! ironPython (press F2 to run the file)
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

from HoneybeeUsr.hbGrid import grid
from HoneybeeUsr.hbAssign import *
from HoneybeeUsr.hbEpw import *
from HoneybeeUsr.hbRecipe import *
from HoneybeeUsr.hbVis import *
from HoneybeeUsr.hbSDA import *

from Algorithm.model import rhinoSpace
from Algorithm.rhinoData import *
from Algorithm.rhinoVis import canvas, vis
from Algorithm.rhinoCurve import curve

from Tools.dirLocation import *
from Tools.osUtil import *
from Tools.winPrompt import *
from Tools.dataCtl import *

import rhinoscriptsyntax as rs
import scriptcontext as sc

################################################################################
# PARAMETERS

# model
north = 0 # positive Y axis
# sensorgrid
gridSize = 0.5
offsetDistance = 1.2

# simulation
'imageless annual glare'
viewDirectionsCounts = 8
viewStartVector = (0, -1, 0)

glareThresh = 0.4
luminanceFactor = 2000 #cd/m2
run = True
silence = False

################################################################################
# MODEL PREPARATION
################################################################################

# 'from rhino model to honeybee model'
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
# hbGrid:
#   a class object (SensorGrid: SensorGrid_2ede2a0a [3520 sensors])
# sensors: 
#   a tuple of readable points(location and direction)
# points:
#   a list of [Rhino.Geometry pt3D object]
# vectors:
#   a list of [Rhino.Geometry.Vector3d object]
# mesh:
#   a list of [Rhino.Geometry.Mesh]
hbGrid, sensors, points, vecs, mesh = grid.HBRadialGrid(None, samplePts, viewDirectionsCounts, viewStartVector, None)
# # # get point tuple (location + direction)
# # hbGrid = hbGrid.sensors
# # # transfer tuple to list
# # hbGrid = list(hbGrid)
hbModelWithGrid = assign.viewOrGridToModel(hbModel, None, hbGrid)

################################################################################
# WEATHER FILE
################################################################################
wea = epw.epwToWea(Dir.epwPath, None, '')

################################################################################
# RUN ANNUAL GLARE IMAGLESS
################################################################################
# resultPath:
#   absolute path to the result
# GA:
#   a data tree [tree {3520}]
resultPath, GA = battery.annualGlareImageless(hbModelWithGrid, 
                                            wea, 
                                            north, 
                                            glareThresh, 
                                            luminanceFactor, 
                                            None, 
                                            '', 
                                            '',  
                                            run,
                                            silence)
################################################################################
# resultPath = result[0]
# rawDataPathLst = result[1] # ['ill, sunhour.txt]
# DA = result[2]
# cDA = result[3]
# UDI = result[4]
# UDILow = result[5]
# UDIUp = result[6]

# ghLst = result[7] # [ghResults, ghDA, ghCDA, ghUDI, ghUDILOW, ghUDIUP]
# ghDA = ghLst[1] # this is a tree: tree {440}
# ################################################################################
# # move files to the project folder
# ################################################################################
# daylitFolder = resultPath + '\\annual_daylight'
# metricsFolder = daylitFolder + '\\metrics'
# modelFolder = daylitFolder + '\\model'

# illFolder = {daylitFolder + '\\results': ['.ill', 'raw.ill']}
# sunFolder = {daylitFolder + '\\results': ['.txt', 'sun.txt']}
# gridPtFolder = {modelFolder + '\\grid': ['.pts', 'grid.pts']}
# cdaFolder = {metricsFolder + '\\cda': ['.cda', 'cda.cda']}
# daFolder = {metricsFolder + '\\da': ['.da', 'da.da']}
# udiFolder = {metricsFolder + '\\udi': ['.udi', 'udi.udi']}
# udiLowFolder = {metricsFolder + '\\udi_lower': ['.udi', 'udilow.udi']}
# udiUpperFolder = {metricsFolder + '\\udi_upper': ['.udi', 'udiupp.udi']}

# # create a new folder in results folder
# folderName = 'daylight_avail'
# targetFolder = Dir.results + '\\' + folderName
# win.createFolder(targetFolder)

# lst = [illFolder, sunFolder, gridPtFolder, cdaFolder, daFolder, udiFolder, udiLowFolder, udiUpperFolder]
# for file in lst:
#     filePath, fileName = osUtil.searchUseListDir(file)
#     targetPath = targetFolder + '\\' + fileName
#     win.copyFile(filePath, list(illFolder.keys())[0], targetPath)

# dayAvilFolder = Dir.results + '\\' + 'daylight_avail'
# udiPath = dayAvilFolder + '\\' + 'udi.udi'
# udilowPath = dayAvilFolder + '\\' + 'udilow.udi'
# udiupPath = dayAvilFolder + '\\' + 'udiup.udi'
# cdaPath = dayAvilFolder + '\\' + 'cda.cda'
# daPath = dayAvilFolder + '\\' + 'da.da'
# rawpath = dayAvilFolder + '\\' + 'raw.ill'
# ################################################################################
# # sDA
# ################################################################################
# passTree, passLst, sDAVal = sDA.simulateSDA(ghDA, targetTime, sampleMeshes)
# sDAValue = sDAVal[0]
# passLst = passLst[0]

# ################################################################################
# # annual-glare imageless


# ################################################################################
# # 'visualize UDI(middle range)'
# # da = pyUtil.readSimpleFile(daPath)
# # da = strUtil.batchFromStrToFloat(da)
# # mesh, legend, colors, legendPara = hbVis.spatialHeatMap(da, sampleMesh, [0, 0], None, '%', None)

# # # mesh type: <Rhino.Geometry.Mesh object at 0x0000000000009577 [Rhino.Geometry.Mesh]>
# # sc.doc.ActiveDoc.Objects.Add(mesh)
# # sc.doc.ActiveDoc.Views.Redraw