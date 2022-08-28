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
    
    # dic syntax: {path: keyword}
    @staticmethod
    def searchFile(dic):
        for folderPath in dic:
            keyword = dic[folderPath]
            for subPath in (os.scandir(folderPath)):
                if subPath.is_file():
                    fileName = subPath.name
                    if keyword[0] in fileName:
                        return subPath.path, keyword[1]
                    
                    
    @staticmethod                
    def searchUseListDir(dic):
        for folderPath in dic:
            keyword = dic[folderPath]

            lst = os.listdir(folderPath)
            for fileName in lst:
                
                path = folderPath + '\\' + fileName
                if os.path.isfile(path):
                    if keyword[0] in fileName:
                        return path, keyword[1]
        
                    
                    
                    
class pyUtil:
    
    # cannot read .ill file
    @staticmethod
    def readSimpleFile(filePath):
        with open(filePath, 'r') as f:
            lines = f.readlines()
            lines = [line.replace('\n', '') for line in lines]
        return lines
            