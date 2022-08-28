import os
# data analysis testing


class fileTest:
    
    @staticmethod
    def hdrNumMatch(hdrFolder, skyFolder):
        
        skyLen = len(os.listdir(skyFolder))
        hdrLen = len(os.listdir(hdrFolder))
        
        if hdrLen == skyLen *2:
            return True
        else:
            diff = abs(hdrLen-skyLen)
            fileTest.findMissingFile(hdrFolder, skyFolder)
            print(f'hdr images are not complete, there are {diff} missing!')
            return False
        
    @staticmethod
    def findMissingFile(hdrFolder, skyFolder):
        skyLen = len(os.listdir(skyFolder))
        hdrLen = len(os.listdir(hdrFolder))        