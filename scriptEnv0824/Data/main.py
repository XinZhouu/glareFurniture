from dataTest import *


import sys
root = 'C:\\Users\\zxin1\\Desktop\\research\\HB'
sys.path.insert(0, root)
from directory import *


rtFolder = dir.root
skyFolder = rtFolder +'\\file\\skyData'
objFolder = rtFolder +'\\file\\objData'
octFolder = rtFolder +'\\file\\octData'
hdrFolder = rtFolder +'\\file\\hdrData'


# test if annual image-based rendering is complete
fileTest.hdrNumMatch(hdrFolder, skyFolder)
