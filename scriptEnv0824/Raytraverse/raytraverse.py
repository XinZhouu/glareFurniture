from directory import *
from dataCtl import strUtil
import subprocess
import configparser
import timeit
import os

class mod:
    @staticmethod
    def assembleScene(fileList, newFilePath):
        for path in fileList:  
            gitBash.addNewLine(path)
            
        gitBash.catFileAll(fileList, newFilePath)
        
    
class srcRun:
    # create config file
    @staticmethod
    def createCfgFile(name):
        gitBash.createNewFile(name)
        
    @staticmethod
    def setCfgFile(secList, scene, viewPt, filePath, twd):
        config = configparser.RawConfigParser()
        for section in secList:
            if section == 'raytraverse_scene':
                config.add_section(section)
                
                dataOutput = twd + '/' + 'raySim'
                config.set(section, 'out', dataOutput)
                config.set(section, 'scene', scene)
            elif section == 'raytraverse_area':
                config.add_section(section)
                config.set(section, 'name', 'vp')
                config.set(section, 'static_points', viewPt)
            elif section == 'raytraverse_sourceengine':
                config.add_section(section)
                config.set(section, 'source', '')
                config.set(section, 'rayargs', '-ab 2')
                config.set(section, 'srcfile', '')      
            elif section == 'raytraverse_images':
                config.add_section(section)
                
                pts = viewPt + ',1,0,0' + ' ' + viewPt + ',-1,0,0'
                config.set(section, 'sensors', pts)
                config.set(section, 'basename', 'default')
                config.set(section, 'simtype', '')         

        with open(filePath, 'w') as configfile:
            config.write(configfile)
        

    # update cfg file
    # only need to update sourceengine
    @staticmethod
    def updateCfgFile(skyFile, secList, cfgPath, skyName):
        config = configparser.RawConfigParser()
        config.read(cfgPath)
        
        finalSkyName = strUtil.extractTargetStrLayer(skyName, '.', 1, 'left')
        config.set(secList[2], 'source', finalSkyName)
        config.set(secList[2], 'srcfile', skyFile)
        config.set(secList[3], 'simtype', finalSkyName)
        
        with open(cfgPath, 'w') as configfile:
            config.write(configfile)

    @staticmethod
    def wakeLinuxEnv(folderPath, containerName):
        # set up linux
        cmd = ('docker run -it --name ' + containerName + ' ' +
                '--mount type=bind,' +
                'source=' + '"' + folderPath + '"' ',' +
                'target=/working rwt /bin/bash')
        print(cmd)

        subprocess.call(cmd,
                        executable = dir.CMD,
                        shell = True) 
             
    @staticmethod  
    def raytraRender(cfgFile, containerName):

        cmd = ('docker exec ' + containerName + ' ' +
                'raytraverse -c ' +
                cfgFile + ' ' +
                'sourcerun images')

        # cmd = ('docker exec ' + containerName + ' ' +
        #         'raytraverse -c ' +
        #         cfgFile + ' ' +
        #         'images -basename inter -interpolate fast')        
        
        subprocess.call(cmd, 
                        executable = dir.CMD,
                        shell = True)
        
    @staticmethod
    def changeDir(folderPath, targetPath, skyName):
        # change them to the target dir
        num = 0
        for path in (os.scandir(folderPath)):
            if path.is_file():
                hdrPath = path.path
                hdrName = path.name
                if '.hdr' in hdrName:
                    if num < 2:
                        name = skyName + '_' + str(num) + '.hdr'
                        cmd = ('move ' + hdrPath + ' ' + targetPath + '\\' + name)
                        subprocess.call(cmd, 
                                        executable = dir.CMD,
                                        shell = True)    
                        num += 1
    
    @staticmethod
    def annualRun(skyFolder, secList, cfgPath, containerName, rayRenderDir):
        lstNum = len(os.listdir(skyFolder))
        
        i = 0

        for skyPath in os.scandir(skyFolder):
            if skyPath.is_file():
                skyName = skyPath.name
                skyFile = skyFolder +'/' + skyName
                
                if i != lstNum-1:
                    srcRun.updateCfgFile(skyFile, secList, cfgPath, skyName)
                    srcRun.raytraRender(cfgPath, containerName)
                    
                    finalName = strUtil.extractTargetStrLayer(skyName, '.', 1, 'left')
                    srcRun.changeDir(dir.root, rayRenderDir, finalName) 
                    
                    i += 1     
                else:
                    break 
                    