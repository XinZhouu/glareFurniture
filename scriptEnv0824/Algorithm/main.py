from directory import *
from transGeo import *
from rhinoCtl import *
from dataCtl import *
from hbView import *
from hbAssign import *
from hbSky import *
from hbRecipe import *


import timeit

#########################################################
# view based simulation
#########################################################

# USER INPUT
# get viewpoint (interacting with rhino)
viewPoint = rhCTL.getViewPosition()

# relative path
epwFile = '.\\file\\weather\\USA_MA_Boston-Logan.Intl.AP.725090_TMY3.epw'
month = 12
day = 21
hour = 16
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


unit = rhUtil.identifyModelUnit()
newViewPt = rhAnys.reconstructViewPoint(unit, viewPoint)


# get objects in each layer that is on
rhCTL.objByLayers()
objDic = rhCTL.dic

# parsing objDic
newObjDic = dict()
for key in objDic:
    
    layerName = strUtil.extractTargetStrLayer(key, ':', 2, 'right')
    if layerName not in newObjDic:
        newObjDic[layerName] = objDic[key]
        
# time calculation start
start = timeit.default_timer()

# create honeybee recognized models

walModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'PARTITION')
flrModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'FLOOR')
ceilModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'CEILING')

# model list for simulation
winModLst = HBGeo.HBWindow(newObjDic, '', True)
faceLst = walModLst + flrModLst + ceilModLst

HBModel = HBGeo.modelForSim(faceLst, winModLst, '')

# HB view
hbView = viewHB.customizedView('', newViewPt, (1,0,0), (0,0,1), 'h', None, None)

# assign view to model
finalModel = assign.viewOrGridToModel(HBModel, hbView, None)

# define the sky
finalSky = sky.createCIESky(epwFile, month, day, hour)

# run simulation
metric = '2'
resolution = '800'
radParameter = '-ab 2 -aa 0.25 -ad 512 -ar 16'
outputPath = battery.viewBasedSim(finalModel,
                                  finalSky,
                                  metric, 
                                  resolution, 
                                  None, 
                                  None, 
                                  radParameter, 
                                  True)
# time calculation ends
stop = timeit.default_timer()
executTime = stop - start
print(executTime)
print(outputPath)