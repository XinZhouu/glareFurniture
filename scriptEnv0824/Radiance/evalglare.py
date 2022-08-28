# call radiance evalglare program
import subprocess

import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from Tools.dirLocation import *
from Tools.dataCtl import *


class evalglare:
    
    @staticmethod
    def run(filePath, outPath):
        cmd = ('evalglare.exe -d ' + filePath + ' > ' + outPath)
        subprocess.call(cmd,
                        shell = True,
                        executable = Dir.CMD,
                        cwd = Dir.exeRad)
        
    @staticmethod
    def batchRun(fileDic, outPath):
        for path in fileDic:
            fileName = fileDic[path]
            extractName = strUtil.extractTargetStrLayer(fileName, '.', 1, 'left')
            output = outPath + '\\' + extractName + '.txt'
            evalglare.run(path, output)