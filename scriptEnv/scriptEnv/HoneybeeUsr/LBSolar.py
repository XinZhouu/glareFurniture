from ladybug.wea import Wea
from ladybug.datacollection import HourlyContinuousCollection
from ladybug.header import Header
from ladybug.datatype.illuminance import Illuminance

class solar:
    
    @staticmethod
    def irradToillum(data):
        """Change the data type of an input collection from irradiane to illuminance."""
        head = data.header
        new_header = Header(Illuminance(), 'lux', head.analysis_period, head.metadata)
        return HourlyContinuousCollection(new_header, data.values) if \
            isinstance(data, HourlyContinuousCollection) else \
            data.__class__(new_header, data.values, data.datetimes)
            
    @staticmethod      
    def directIllumInHorizPlane(loc, dirNormal, diffhorz, srfAzimuth, sefAltit, gdRef, anisotropic):
        # set default values
        az = srfAzimuth if srfAzimuth is not None else 180
        alt = sefAltit if sefAltit is not None else 0
        gref = gdRef if gdRef is not None else 0.2
        isot = not anisotropic

        # create the Wea and output irradaince
        wea = Wea(loc, dirNormal, diffhorz)
        total, direct, diff, reflect = \
            wea.directional_irradiance(alt, az, gref, isot)
        for dat in (total, direct, diff, reflect):
            dat.header.metadata['altitude'] = alt
            dat.header.metadata['azimuth'] = az

        # convert to illuminace if input data was illuiminance
        if isinstance(dirNormal.header.data_type, Illuminance):
            total = solar.irradToillum(total)
            direct = solar.irradToillum(direct)
            diff = solar.irradToillum(diff)
            reflect = solar.irradToillum(reflect)
            
            return total