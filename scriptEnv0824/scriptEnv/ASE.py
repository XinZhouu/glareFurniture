import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')

from HoneybeeUsr.hbEpw import *
from HoneybeeUsr.LBDataCtl import *

from RhinoUsr.rhinoDataCtl import *

from Tools.dirLocation import *

################################################################################
# parameters


################################################################################
# weather
################################################################################
loc, directNormalIll, diffuseHorIll = epw.weatherForASE(Dir.epwPath)
'hourly continuous collections'
header = lbData.deconstructLBData(diffuseHorIll)
value = 0
repeat = 8760
lst = rhDataCtl.duplicateDataToList(value, repeat)
print(lst)
# annualHourData = lbData.constructLBData(header, lst)