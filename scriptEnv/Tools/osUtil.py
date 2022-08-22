import os


class osUtil:
    
    
    @staticmethod
    def fileIsEmpty(filePath):
        if os.path.getsize(filePath) == 0:
            return True
        return False
    
    @staticmethod
    def removeFile(filePath):
        os.remove(filePath)
        
    @staticmethod
    def eraseContent(filePath):
        open(filePath, 'w').close()

    # this function collects all the files path in a folder
    # only compatiable with windows path system
    # return a dict {absolutePath: fileName}
    @staticmethod
    def collectWinPath(filePath):

        pathDic = dict()

        for subPath in (os.scandir(filePath)):
            if subPath.is_file():
                absPath = subPath.path # this path is '..\\..\\..\\'
                fileName = subPath.name
                if absPath not in pathDic:
                    pathDic[absPath] = fileName
        return pathDic
        