import sys
sys.path.append('C:\\Users\\zxin1\\Desktop\\Glare\\scriptEnv')



from HoneybeeUsr.hbEpw import *
from HoneybeeUsr.LBDataCtl import *
from HoneybeeUsr.LBSolar import *
from HoneybeeUsr.LBTime import *

from RhinoUsr.rhinoDataCtl import *

from Tools.dirLocation import *
from Tools.dataCtl import *
from Tools.mathUsr import *

################################################################################
# parameters
startMonth = 1
startDay = 1
startHour = 9
endMonth = 12
endDay = 31
endHour = 17
daylightThreshold = 1000 #lux
windowTransmittance = 0.6

################################################################################
# weather
################################################################################
loc, directNormalIll, diffuseHorIll = epw.weatherForASE(Dir.epwPath)

'hourly continuous data'
# header = lbData.deconstructLBData(diffuseHorIll)
# value = 0
# repeat = 8760
# lst = rhDataCtl.duplicateDataToList(value, repeat)
# annualHourData = lbData.constructLBData(header, lst) # ladybug collection object
dirSolarIllum = solar.directIllumInHorizPlane(loc, directNormalIll, diffuseHorIll, 
                                                None, None, None, False)
print(dirSolarIllum)

period, hoys, dates = LBTime.analysisPeriod(startMonth, startDay, startHour, endMonth, 
                                     endDay, endHour, 1)

hoys = mathUsr.batchRoundHalfUp(hoys)
# # make a statement to remove sun vectors below an illuminance threshold
# illumanceThreshold = daylightThreshold * ((1/windowTransmittance))
# statement = "a>" + str(illumanceThreshold)

# # get sun vectors for hours above threshold
# sunVectors = hbSun.sunVectorsForHours(None, loc, hoys, None, False, None,
#                 0.2, None, totalSolarIllum, statement)

# # print(sunVectors)