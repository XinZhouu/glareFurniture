'''
STEP:5 extract glare direction and metrics from evalglare report
'''

import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from Tools.osUtil import *
from Tools.dirLocation import *
from Tools.winPrompt import *
from Radiance.evalglare import *


########################################
# FILE PATH
########################################
hdrFdr = Dir.results + '\\' + 'acceleRad_HDR'

########################################
# RUN EVALGLARE
########################################
'create a new folder for raw evalglare data'
rawEvalglare = Dir.results + '\\' + 'evalglare_Data' # absolute path
# win.createFolder(rawEvalglare)

'collect hdr image paths'
hdrDic = osUtil.collectWinPath(hdrFdr)
evalglare.batchRun(hdrDic, rawEvalglare)



