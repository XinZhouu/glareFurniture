from ladybug.epw import EPW

'''
future improvement:
1, extract data according to the user input
'''

class epw:
    # return: <class 'ladybug.location.Location'>
    @staticmethod
    def extractData(epwFile):
        # create an epw instance
        epw = EPW(epwFile)
        
        # properties
        loc = epw.location  
        return loc
        
    # other properties
    '''
    annual_heating_design_day_996
    annual_heating_design_day_990
    annual_cooling_design_day_004
    annual_cooling_design_day_010
    heating_design_condition_dictionary
    cooling_design_condition_dictionary
    extreme_design_condition_dictionary
    extreme_hot_weeks
    extreme_cold_weeks
    typical_weeks
    ashrae_climate_zone
    monthly_ground_temperature
    header
    years
    dry_bulb_temperature
    dew_point_temperature
    relative_humidity
    atmospheric_station_pressure
    extraterrestrial_horizontal_radiation
    extraterrestrial_direct_normal_radiation
    horizontal_infrared_radiation_intensity
    global_horizontal_radiation
    direct_normal_radiation
    diffuse_horizontal_radiation
    global_horizontal_illuminance
    direct_normal_illuminance
    diffuse_horizontal_illuminance
    zenith_luminance
    wind_direction
    wind_speed
    total_sky_cover
    opaque_sky_cover
    visibility
    ceiling_height
    present_weather_observation
    present_weather_codes
    precipitable_water
    aerosol_optical_depth
    snow_depth
    days_since_last_snowfall
    albedo
    liquid_precipitation_depth
    liquid_precipitation_quantity
    sky_temperature
    '''
#######################################################################
# TESTING
#######################################################################

# epwFile = '.\\file\\weather\\USA_MA_Boston-Logan.Intl.AP.725090_TMY3.epw'
# loc = epw.extractData(epwFile)
# print(type(loc))
              