import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from HoneybeeUsr.annalDaylight import *


#####################################################
# DAYLIGHT AVAILIBILITY
'''
1. model preparation
'''
#####################################################


###################################
# MODEL
###################################
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