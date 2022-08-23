import subprocess
import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from Tools.dirLocation import *

class win:
    
    @staticmethod
    def createFolder(folderPath):
        cmd = 'mkdir ' + folderPath
        subprocess.call(cmd,
                        executable = Dir.CMD,
                        shell = True)           
    
    @staticmethod
    def createFile(fileName, cwd):
        # create an empty file in windows prompt
        cmd = 'type NUL >' + ' ' + fileName
        subprocess.call(cmd,
                        executable = Dir.CMD,
                        shell = True,
                        cwd = cwd)     
        
    @staticmethod
    def copyFile(fileName, cwd, twd):
        cmd = 'copy ' + fileName + ' ' + twd
        subprocess.call(cmd,
                        executable = Dir.CMD,
                        shell = True,
                        cwd = cwd)  
        
    @staticmethod
    def moveFile(fileName, cwd, twd):
        cmd = 'move ' + fileName + ' ' + twd
        subprocess.call(cmd,
                        executable = Dir.CMD,
                        shell = True,
                        cwd = cwd)    
        