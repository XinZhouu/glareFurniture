from dataCtl import *
from epw import *
from hbSky import *
from hbView import *
from directory import *
# from transGeo import *
# from rhinoCtl import *
from dataCtl import *
from hbAssign import *

import timeit

#########################################################
# view based simulation
#########################################################

rtFolder= dir.root
epwFile = '.\\file\\weather\\USA_MA_Boston-Logan.Intl.AP.725090_TMY3.epw'

skyFolder = '.\\file\\skyData'
viewFolder = '.\\file\\viewData'
objFolder = '.\\file\\objData'

# # USER INPUT
# # get viewpoint (interacting with rhino)
# viewPoint = rhCTL.getViewPosition()

# month = 12
# day = 21
# hour = 9


# unit = rhUtil.identifyModelUnit()
# newViewPt = rhAnys.reconstructViewPoint(unit, viewPoint)


# # get objects in each layer that is on
# rhCTL.objByLayers()
# objDic = rhCTL.dic

# # parsing objDic
# newObjDic = dict()
# for key in objDic:
    
#     layerName = strUtil.extractTargetStrLayer(key, ':', 2, 'right')
#     if layerName not in newObjDic:
#         newObjDic[layerName] = objDic[key]
        
# # time calculation start
# # start = timeit.default_timer()
# #################################################################
# # CREATE SCENE FILE
# #################################################################
# # create honeybee recognized models

# walModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'PARTITION')
# flrModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'FLOOR')
# ceilModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'CEILING')
# mullionModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'MULLION')

# # model list for simulation
# winModLst = HBGeo.HBWindow(newObjDic, '', True)
# faceLst = walModLst + flrModLst + ceilModLst + mullionModLst

# HBModel = HBGeo.modelForSim(faceLst, winModLst, '')
# HBGeo.GeoRhinoToRad(HBModel, objFolder)

###############################################################
# CTEATE VIEW FILE
# using 2 view files to make 360 degree view range

'''
para1: camera type:
v - Perspective
h - Hemispherical fisheye
l - Parallel
c - Cylindrical panorama
a - Angular fisheye
s - Planisphere [stereographic] projection
'''
###############################################################
newViewPt = (-7.220157, 5.90673, 1.21)
view1 = viewHB.customizedView('', newViewPt, (1,0,0), (0,0,1), 'h', 180, 180)
view2 = viewHB.customizedView('', newViewPt, (-1,0,0), (0,0,1), 'h', 180, 180)

viewFileName1 = strUtil.viewCreation('vectorX')
viewFileName2 = strUtil.viewCreation('vectorNegX')
path1 = viewHB.outputPath(view1, viewFolder, viewFileName1, False)
path2 = viewHB.outputPath(view2, viewFolder, viewFileName2, False)
###############################################################
# CREATE SKY FILE
'''
para1: CIE Sky Type.

0 = Sunny with sun.
1 = Sunny without sun.
2 = Intermediate with sun. 
3 = Intermediate without sun. 
4 = Cloudy sky.
5 = Uniform cloudy sky. 
'''
###############################################################
# # file name for sky file

# fileName = strUtil.dateCreation(month, day, hour) + '.sky' 
# cieSky = sky.createCIESky(epwFile, month, day, hour, 1) #refer to para1

# # create a sky file and vis the path to the file
# skyFilePath = sky.outputPath(cieSky, skyFolder,fileName)
# print('sky file path: ', skyFilePath)

# # FOR DEBUGGING
# # skyString = sky.outputString(cieSky)
# # print('gensky: ', skyString)

#################################################################
# OCTREE
#################################################################



