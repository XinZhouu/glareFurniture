from dataCtl import *
from directory import *
import subprocess
import os

# external modules

# converting image types (CLI)
# brew install imagemagick


# pathProgram = "/System/Applications/Utilities/Terminal.app"
# subprocess.call(["/usr/bin/open", "-W", "-n", "-a", pathProgram])

# using radiance CLI to simulate daylighting models

class Gen():

    @staticmethod
    def genBox():
        cmd = 'genbox wood testBox 5 5 3 > testBox.rad'
        subprocess.call(cmd, 
                        shell = True, 
                        executable = dir.CMD, 
                        cwd = dir.root) 

# class Trans():

#     @staticmethod
#     def objToRad(model):

#         # transfer .obj to .rad
#         name = strUtil.filterFileName(model)
#         newName = name + '.rad'
#         cmd = 'obj2rad -f ' + model + ' > ' + Sys.radDir + '/' + newName
#         print('obj->rad: ', cmd)
#         subprocess.call(cmd,
#                         shell = True,
#                         executable = Sys.terminal,
#                         cwd = Sys.objDir)
    
#     # batch automation
#     def batchAuto(modelType):

#         entries = os.scandir(Sys.objDir)
#         for entry in entries:
#             name = entry.name

#             # ignore the temporary file
#             if name != '.DS_Store':

#                 if modelType  == 'obj':
#                     Trans.objToRad(name)


# class Debug():

#     def openRadFile(radFile):
#         cmd = 'code ' + radFile
#         subprocess.call(cmd,
#                         shell = True,
#                         executable = Sys.terminal ,
#                         cwd = Sys.radDir)  

#     def boundingBox(radFile):
#         '''
#         correct boundingbox format:
#         xmin      xmax      ymin      ymax      zmin      zmax
#         0         5         0         5         0         3
#         '''

#         cmd = 'getbbox ' + radFile # get size and location
#         print ('debug ' + radFile + ':' , cmd)
#         subprocess.call(cmd,
#                         shell = True,
#                         executable = Sys.terminal,
#                         cwd = Sys.radDir) 
                        
#     def objInLine(radFile):
#         cmd = 'objline ' + radFile + ' | x11meta -r &'
#         subprocess.call(cmd,
#                         shell = True,
#                         executable = Sys.terminal,11
#                         cwd = Sys.radDir) 





# ##################################################
# # SCENE2
# ##################################################
# def createSky():
#        # time format: month/day/hour(standard time)
#        time = '12 09 14:00 '
#        # location
#        lat = '-a 51 '
#        lon = '-o 0 '
#        median = '-m 0 '
#        # sky condition
#        '''
#        -s: sunny sky without sun (standard CIE clear day)
#        +s: sunny sky with sun (a source of sun is generated)
#        -c: cloudy sky (standard CIE overcast day)
#        -i: intermediate sky without sun. (standard CIE intermediate day)
#        +i: intermediate sky with sun.
#        -u: uniform cloudy day
#        '''
#        sky = '+s '
       
#        # combine all the data
#        txtMat = 'gensky ' + time + sky + lat + lon + median
#        print(txtMat)
#        txtObj = 'gensky ' + time + lat + lon + median
#        cmds = [txtMat + '> sky.mat', 'code sky.mat',
#                txtObj + '> sky.rad', 'code sky.rad']
#        for cmd in cmds:
#               subprocess.call(cmd,
#                             shell = True,
#                             executable = pathTerminal,
#                             cwd = pathFiles)
       
#        cmds = ['oconv sky.mat sky.rad > sky.oct', 'rvu sky.oct']
#        for cmd in cmds:
#               subprocess.call(cmd,
#                      shell = True,
#                      executable = pathTerminal,
#                      cwd = pathFiles)

# def createSceneFile():
#        cmds = [
#               'obj2mesh -a wall.rad room.obj > room.rtm',
#               'touch scene.rad',
#               "echo 'void mesh model\n 1 room.rtm\n 0\n 0\n' > scene.rad",
#               'code scene.rad',
#               # for debugging purpose
#               'objview scene.rad'
#               ]

#        # cmds = [
#        #         'obj2rad -n -f room.obj > room.rad',
#        #         'oconv wall.rad room.rad > scene.oct',
#        #         'rvu -vf nice.vf scene.oct'
#        #         ]
#        for cmd in cmds:
#               subprocess.call(cmd,
#                               shell = True,
#                               executable = pathTerminal,
#                               cwd = pathFiles)

# # objects are stored in the 'folder objects'
# def assembleObjects():
# 	# create a scene file
# 	cmd = 'touch scene.rad'
# 	subprocess.call(cmd,
# 					shell = True,
# 					executable = pathTerminal,
# 					cwd = pathFiles)

# 	# navigate to the folder path
# 	path = pathFiles + '/objects'
# 	entries = os.scandir(path)
# 	for entry in entries:
# 		objName = entry.name
# 		if objName != '.DS_Store':
# 			# format
# 			# '!xform ./objects/Ground.rad'
			
# 			# relative path
# 			relPath = '!xform ./objects/'+ objName
# 			relPath = str(relPath)
# 			cmd = ['echo ', relPath, ' >> scene.rad']
# 			cmd = ' '.join(cmd)
# 			subprocess.call(cmd,
# 							shell = True,
# 							executable = pathTerminal,
# 							cwd = pathFiles)

# 	# for debugging
# 	# open scene.rad to double check the string syntax
# 	cmd = 'code scene.rad'
# 	subprocess.call(cmd,
# 					shell = True,
# 					executable = pathTerminal,
# 					cwd = pathFiles)	


# # create view+ambient file
# '''
# -vtv = perspective
# -vtl = parallel
# -vtc = cylindrical
# -vth = hemispherical fisheye
# -vta = angular fisheye
# '''
# def createVFFile(viewPosition, viewType, viewDir, viewUp,hSize, vSize):	
# 	typeV = '-vt' + viewType + ' '
# 	position = '-vp ' + ' '.join(map(str,viewPosition))
# 	direction = ' -vd ' + ' '.join(map(str,viewDir))
# 	up = ' -vu ' + ' '.join(map(str,viewUp))
# 	hRange = ' -vh ' + str(hSize)
# 	vRange = ' -vv ' + str(vSize)
# 	view = typeV + position + direction + up + hRange + vRange

# 	# write this view string to .vf file
# 	cmds = [
# 			'touch view.vf',
# 			'echo ' + view + ' > view.vf',
# 			'code view.vf'
# 			]
# 	for cmd in cmds:
# 		subprocess.call(cmd,
# 						shell = True,
# 						executable = pathTerminal,
# 						cwd = pathFiles)	

# 	return view

# def createAmbient(lightCond, bounceVal, divisionVal,rayWeight):
# 	ambLight = '-av ' + ' '.join(map(str, lightCond))
# 	ambBounce = ' -ab ' + str(bounceVal)
# 	ambDivision = ' -ad '+ str(divisionVal)
# 	rayWgt = ' -lw ' + str(rayWeight)
# 	ambient = ambLight + ambBounce + ambDivision + rayWgt
# 	return ambient


# # quick overview of objects without material definitions(line vector)
# def previewObjects(radFile):
#     cmds= ['getbbox ' + radFile, # get size and location
#            'objline ' + radFile + ' | x11meta -r &']
#     for cmd in cmds:
#        print (cmd)
#        subprocess.call(cmd,
#                       shell = True,
#                       executable = pathTerminal,
#                       cwd = pathFiles)

# # an overview of the objects and materials without light sources
# def previewObjAndMat(radFile):
#        cmd1 = 'objpict ' + radFile + ' | ximage'
#        cmd2 = 'objpict ' + radFile + ' > image.hdr ' + '&& ximage image.hdr'
#        subprocess.call(cmd2,
#                        shell = True,
#                        executable = pathTerminal,
#                        cwd = pathFiles)

# # an overview of the objects and materials without light sources
# def visualizeObj(radFile):
#        cmd = 'objview ' + radFile
#        subprocess.call(cmd,
#                        shell = True,
#                        executable = pathTerminal,
#                        cwd = pathFiles)   
class radTran:
    @staticmethod
    def radToOctree(folder):
        # combine all the required files
        strComb = ''
        str1 = ''
        str2 = ''
        for path in os.scandir(folder):
            if path.is_file():
                if '.mat' in path.name:
                    str1 += ' ' + path.name
                    
                elif '.rad' in path.name:
                    str2 += ' ' + path.name
            
        strComb = str1 + str2
                
        cmd = 'oconv' + strComb + ' > scene.oct'
        print('rad -> .oct: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = dir.CMD,
                        cwd = folder)
        
    @staticmethod
    def addOctreeInstance(octFile, skyFile, skyName, objFolder, octFolder):
        name = strUtil.extractTargetStrLayer(skyName, '.', 1, 'left')
        cmd = (
                'oconv -i' +
                ' ' + octFile +
                ' ' + skyFile +
                ' > ' + octFolder + '\\' + name + '.oct'
        )
        
        print('.oct + sky -> .oct: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = dir.CMD,
                        cwd = objFolder)        
        

# # interactive visualization
# def rvuScene(viewVFString, debugBool):
# 	cmds = ['rvu ' + viewVFString + ' scene.oct']
# 	# if need debugging, the extra operation needs to be implemented
# 	if debugBool:
# 		cmds += ['rvu -defaults | grep ^-a']
# 	print('rvu commands: ',cmds)
# 	# alternative
# 	# cmd = 'rvu -vf ' + .vf + 'scene.oct'
# 	for cmd in cmds:
# 		subprocess.call(cmd,
# 						shell = True,
# 						executable = pathTerminal,
# 						cwd = pathFiles)  

class render:
    
    # non-interactive visualization
    @staticmethod
    def rpict(viewVF, scene, radPara, fileDir):
            resolution = '-x 800 -y 800'
            name = strUtil.extractTargetStrLayer(scene, '.', 1, 'left') + 'Rad'
            cmd = ('rpict' + 
                    ' -vf' +
                    ' ' + viewVF  + 
                    ' ' + radPara + 
                    ' ' + resolution + 
                    ' ' + scene + 
                    ' ' + '> ' + name +'.hdr')
            
            print('radiance rpict command: ', cmd)
            subprocess.call(cmd,
                            shell = True,
                            executable = dir.CMD,
                            cwd = fileDir)
        

# def displayImage(hdrFile):
#        cmd = 'ximage ' + hdrFile
#        subprocess.call(cmd,
#               shell = True,
#               executable = pathTerminal,
#               cwd = pathFiles)

# def postprocessImage(hdrFile):
# 	cmd = 'pcond'

# def pfiltHDR(hdrFile, exposureRate):
# 	newName = filterHDRName(hdrFile)
# 	targetName = newName + 'Pfilt.hdr'
# 	cmd = 'pfilt ' + '-e ' + str(exposureRate) + ' ' \
# 	      + hdrFile + ' >' + targetName
# 	print('targetName:\n', targetName)
# 	subprocess.call(cmd,
# 				    shell = True,
# 				    executable = pathTerminal,
# 				    cwd = pathFiles)
# 	return targetName	

# def filterHDRName(string):
# 	i = string.index('.')
# 	name = string[:i]
# 	return name

# def HDRToTiffSuffix(newName):
# 	# from .hdr to .tiff
# 	newFileName = newName + '.tif'
# 	print('newFileNameTIF:\n', newFileName)
# 	return newFileName

# # this function uses the external module called 'imagemagick'
# # this function assumes the hdrfile is pfiltered with proper exposure rate
# def convertFilteredHDR(hdrFile, exposureRate, type):
# 	# pfilter the .HDR
# 	processImg = pfiltHDR(hdrFile, exposureRate)
# 	newName = filterHDRName(processImg)
# 	newFileName = HDRToTiffSuffix(newName)
# 	cmd = 'ra_tiff ' + hdrFile + ' ' + newFileName

# 	# operation
# 	subprocess.call(cmd,
# 					shell = True,
# 					executable = pathTerminal,
# 					cwd = pathFiles)

# 	imageConversion(newName, newFileName, type)
	

# def convertNormHDR(hdrFile, type, folderPath):
# 	newName = filterHDRName(hdrFile)
# 	newFileName = HDRToTiffSuffix(newName)
# 	cmd = 'normtiff ' + hdrFile + ' ' + newFileName

# 	# operation
# 	subprocess.call(cmd,
# 					shell = True,
# 					executable = pathTerminal,
# 					cwd = folderPath)

# 	imageConversion(newName, newFileName, type)

# def imageConversion(newName, newFileName, type):
# 	# 'png': for report or documenting
# 	# 'jpeg': publish images on the Internet
# 	targetFileName = newName + '.' + type
# 	upType = type.upper()
# 	print('targetFileName' + upType +':\n', targetFileName)		
# 	cmds = ['convert ' + '-gamma 2.2 ' + newFileName + ' ' + targetFileName,
# 			'rm ' + newFileName]

# 	for cmd in cmds:
# 		subprocess.call(cmd,
# 						shell = True,
# 						executable = pathTerminal,
# 						cwd = pathFiles)


# def batchConversion(type):
# 	# go to the target folder
# 	folder = pathFiles + '/hdr'
# 	print(folder)
# 	cmd = 'cd ' + folder
# 	subprocess.call(cmd,
# 					shell = True,
# 					executable = pathTerminal,
# 					cwd = folder)	

# 	# loop all the files in the folder
# 	'''
# 	bash commands:
# 	$ cd images
#     $ for file in *.hdr ; do normtiff $file \
#     $(basename $file hdr)tif ; done
#     $ mogrify -gamma 2.2 -format jpg *.tif
#     $ cd ..
# 	$ mogrify -gamma 2.2 -format png images/*.hdr
# 	'''

# class analyseImage():
# 	def __init__(self, image, maxVal, numDivision):
# 		self.image = image
# 		self.maxVal = maxVal
# 		self.numDivision = numDivision
    
# 	def createFalsecolorImg(self):
# 		self.imageName = stringUtil.filterHDRName(self.image)
# 		newImgName = 'fc_' + self.imageName
# 		maxScaleVal = ' -s ' + str(self.maxVal)
# 		numInterval = '-n ' + str(self.numDivision)
# 		self.bar = maxScaleVal + ' ' + numInterval
# 		cmd = 'falsecolor -ip ' + self.image + self.bar + ' > ' + newImgName + '.hdr'
# 		print('falColr command: ', cmd)

# 		subprocess.call(cmd,
# 						shell = True,
# 						executable = pathTerminal,
# 						cwd = pathFiles)	

# 	def createContourLineImg(self, string):
# 		# access variables in createFalsecolorImg()
# 		newImgName = 'fcContour_' + self.imageName

# 		# illuminance map
# 		if string == 'i':
# 			cmd = 'falsecolor -i ' + self.image + \
# 				   ' -p ' + self.image + \
# 					' ' + '-cl ' + self.bar + ' > ' + newImgName + '.hdr'
# 			print('falColrContour_' + string + 'command: ', cmd)
# 		else:
# 			cmd = 'falsecolor -ip ' + self.image + \
# 					' ' + '-cl ' + self.bar + ' > ' + newImgName + '.hdr'            

# 		subprocess.call(cmd,
# 						shell = True,
# 						executable = pathTerminal,
# 						cwd = pathFiles)		
