import subprocess

class gitBash:
    
    # class attributes
    # pay attenation to the '/' and '\' in windows prompt and git bash
    root = 'C:/Users/zxin1/Desktop/research/HB'
    BASH = 'C:/Program Files/Git/bin/bash.exe'
    
    @staticmethod
    def createNewFile(fileName):
        cmd = ('touch ' + fileName)
        subprocess.call([gitBash.BASH, '-c', cmd]) 
        
    @staticmethod
    def createNewFolder(filePath):
        cmd = ('mkdir ' + filePath)     
        subprocess.call([gitBash.BASH, '-c', cmd], cwd = gitBash.root)
        
    # this function will help strip any trailing newlines
    # and echo will add one
    @staticmethod
    def addNewLine(filePath):
        cmd = ('echo "" >> ' + filePath)
        subprocess.call([gitBash.BASH, '-c', cmd], cwd = gitBash.root)
        
    @staticmethod
    def catFileAll(fileList, newFilePath):
        fileString = ' '.join(fileList)
        cmd = ('cat ' + fileString + ' > ' + newFilePath)
        subprocess.call([gitBash.BASH, '-c', cmd], cwd = gitBash.root)