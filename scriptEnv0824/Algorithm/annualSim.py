from dataCtl import *
from directory import *
from hbCLI import *
from radiance import *
from hbSky import *
from acceleRad import *

import timeit
import os


class batchSim:
    @staticmethod
    def createSingleSky(epwFile,month, day, hour, skyFolder):
        fileName = strUtil.dateCreation(month, day, hour) + '.sky' 
        cieSky = sky.createCIESky(epwFile, month, day, hour, 1) #refer to para1

        # create a sky file and vis the path to the file
        skyFilePath = sky.outputPath(cieSky, skyFolder,fileName)
        print('sky file path: ', skyFilePath)
        
    @staticmethod
    def createBatchSky(epwFile, skyFolder):
        
        # check if skyFolder has files
        if sysDir.checkFolderHaveFiles(skyFolder):
            sysDir.delFilesInFolder(skyFolder)
            
        #office hour(9:00 - 17:00) 
        months = 13
        offStart = 9
        offEnd = 18
        # hard-coded days for a given month
        days = [32,29,32,31,32,31,32,32,31,32,31,32]
        for month in range(1,months):
            for day in range(1,days[month-1]):
                for hour in range(offStart,offEnd):
                    batchSim.createSingleSky(epwFile, month, day, hour, skyFolder)
    
    @staticmethod
    def addSkyToOctreeBatch(skyFolder, objFolder, octFolder):
        # check if octFolder has files
        if sysDir.checkFolderHaveFiles(octFolder):
            sysDir.delFilesInFolder(octFolder)
        
        for skyPath in os.scandir(skyFolder):
            if skyPath.is_file():
                skyFile = skyPath.path
                skyName = skyPath.name
                
                for octPath in os.scandir(objFolder):
                    if octPath.is_file():
                        if octPath.name == 'scene.oct':
                            octObject = octPath.path
                            
                            radTran.addOctreeInstance(octObject, skyFile, skyName, objFolder, octFolder)
                            
    @staticmethod
    def collectOctPath(octFolderC):
        pathDic = dict()
        for octPath in (os.scandir(octFolderC)):
            if octPath.is_file():
                scenePath = octPath.path
                sceneName = octPath.name
                if scenePath not in pathDic:
                    pathDic[scenePath] = sceneName
        return pathDic
    
    @staticmethod             
    def collectVFPath(viewFolder):
        viewDic = dict()
        for viewPath in (os.scandir(viewFolder)):
            if viewPath.is_file():
                viewVF = viewPath.path
                viewName = viewPath.name
                if viewVF not in viewDic:
                    viewDic[viewVF] = viewName
        return viewDic
    
    @staticmethod            
    def annualRun(octDic, viewDic, radPara, objFolder, hdrFolder):
        for scenePath in octDic:
            sceneName = octDic[scenePath]

            for viewPath in viewDic:
                viewName = viewDic[viewPath]
                
                fastRender.AccRpict(viewPath, viewName, scenePath, sceneName, radPara, objFolder, hdrFolder)



rtFolder= dir.root
epwFile = '.\\file\\weather\\USA_MA_Boston-Logan.Intl.AP.725090_TMY3.epw'

skyFolder = rtFolder +'\\file\\skyData'
viewFolder = rtFolder +'\\file\\viewData'
objFolder = rtFolder +'\\file\\objData'
octFolder = rtFolder +'\\file\\octData'
# hdrFolder = rtFolder +'\\file\\hdrData'


# low
radPara = '-aa 0.25 -ab 2 -ad 512 -ar 16 -as 128'
# # middle
# radPara = '-aa 0.2 -ab 3 -ad 2048 -ar 64 -as 2048'
#############################################################
# start = timeit.default_timer()

# batchSim.createBatchSky(epwFile, skyFolder)

# stop = timeit.default_timer()
# executTime = stop - start
# print(executTime)# 7.675s
##############################################################
# start = timeit.default_timer()
# batchSim.addSkyToOctreeBatch(skyFolder, objFolder, octFolder)
# stop = timeit.default_timer()
# executTime = stop - start
# print(executTime)# 187.58s
##############################################################
# final rendering
hdrFolder = rtFolder +'\\file\\hdrData'
octDic = batchSim.collectOctPath(octFolder)
viewDic = batchSim.collectVFPath(viewFolder)

start = timeit.default_timer()
batchSim.annualRun(octDic, viewDic, radPara, objFolder, hdrFolder)
stop = timeit.default_timer()
executTime = stop - start
print(executTime)

