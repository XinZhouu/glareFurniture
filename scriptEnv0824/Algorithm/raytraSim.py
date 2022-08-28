from raytraverse import *
from directory import *
from dataCtl import *
from osUtil import *


rayFolderName = 'raytraverse'
objFolder = dir.root +'\\file\\objData'

####################################################
# PREPARE SCENE FILE
####################################################
# create a raytraverse folder
# dir.createFolder(rayFolderName, dir.root)

# # migrate data into .rad file
fileList = ['./file/objData/aperture.mat', 
            './file/objData/envelope.mat',
            './file/objData/aperture.rad',
            './file/objData/envelope.rad']

twd = './raytraverse'
sceneName = 'scene.rad'
bashCwd = gitBash.root
newFilePath = twd + '/' + sceneName

# # erase the content first and then write data into it
# osUtil.eraseContent(newFilePath)
# # # check .rad is empty
# if osUtil.fileIsEmpty(newFilePath):
#     mod.assembleScene(fileList, newFilePath)
# else:
#     print('Cannot write data into the file because of preoccupied data.')

######################################################
# CREATE TEMPLATE FILE FOR RAYTRAVERSE
######################################################

scene = twd + '/' + sceneName
viewPt = '-7.220157,5.90673,1.21'
rayRenderDirName = 'raytraverseRender'
containerName = 'rayt'

secList = ['raytraverse_scene', 
            'raytraverse_area',
            'raytraverse_sourceengine',
            'raytraverse_images']

cfgName = 'raytraverse.cfg'
cfgPath = twd +'/'+ cfgName

rayRenderDirName = 'rayHDR'
rayRenderDir = twd + '/' + rayRenderDirName

srcRun.createCfgFile(cfgPath)
srcRun.setCfgFile(secList, scene, viewPt, cfgPath, twd)

#########################################################
# SET UP LINUX ENV ON WINDOWS
#########################################################
# pay attention to the path syntax, which uses the windows path syntax
# srcRun.wakeLinuxEnv(dir.root, containerName)
# gitBash.createNewFolder(rayRenderDir)

#########################################################
# USE RAYTRAVERSE IN LINUX ENV
#########################################################
skyFolder = './file/skyData'

start = timeit.default_timer()
srcRun.annualRun(skyFolder, secList, cfgPath, containerName, rayRenderDir)
stop = timeit.default_timer()
executTime = stop - start
print(executTime) # 5h


