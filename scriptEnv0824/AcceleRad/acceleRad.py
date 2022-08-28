from directory import *
from dataCtl import *

import subprocess

class fastRender:
    
    # non-interactive visualization
    @staticmethod
    def AccRpict(viewVF, viewName, scene, sceneName, radPara, objFolder, hdrFolder):
        resolution = '-x 800 -y 800'
        
        scName = strUtil.extractTargetStrLayer(sceneName, '.', 1, 'left')
        vfName = strUtil.extractTargetStrLayer(viewName, '.', 1, 'left')
        vfNameFinal = strUtil.extractTargetStrLayer(vfName, '_', 1, 'right')
        
        outPutName = scName + '_' + vfNameFinal
        
        cmd = ('accelerad_rpict' + 
               ' -vf' +
                ' ' + viewVF  + 
                ' ' + radPara + 
                ' ' + resolution + 
                ' ' + scene + 
                ' ' + '> ' + hdrFolder + '\\' + outPutName + '.hdr')
        
        print('accelerated rpict command: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = dir.CMD,
                        cwd = objFolder)