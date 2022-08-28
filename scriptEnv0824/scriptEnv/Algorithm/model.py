# this script needs to connect to rhino
'''
STEP:1 prepare model file for simulation

    !!!!!:  this script cannot run in cPython, plz press F2 to transfer
            data to rhino
'''

import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from rhinoCtl import rhCTL
from Tools.dataCtl import *
from HoneybeeUsr.transGeo import *

################################################################################
class rhinoSpace:
    
    # this function assumes that rhino layers of furniture are not on
    @staticmethod
    def accessRhinoLayers():
        # get objects in each layer that is on
        rhCTL.objByLayers()
        objDic = rhCTL.dic

        # parsing objDic
        newObjDic = dict()
        for key in objDic:
            
            layerName = strUtil.extractTargetStrLayer(key, ':', 2, 'right')
            if layerName not in newObjDic:
                newObjDic[layerName] = objDic[key]
        return newObjDic
    
    @staticmethod    
    def rhinoToHoneybee(newObjDic):
        # transfer rhino model to honeybee model   
        walModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'PARTITION')
        flrModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'FLOOR')
        ceilModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'CEILING')
        mullionModLst = HBGeo.HBSurface(newObjDic, '', None, None, 'MULLION')

        # model list for simulation
        winModLst = HBGeo.HBWindow(newObjDic, '', True)
        faceLst = walModLst + flrModLst + ceilModLst + mullionModLst

        HBModel = HBGeo.modelForSim(faceLst, winModLst, '')
        return HBModel
