import os
from honeybee.model import Model
from lbt_recipes.recipe import Recipe
from lbt_recipes.settings import RecipeSettings

'''
# precompiled recipe names:

'''

class battery:
    
    @staticmethod
    def viewBasedSim(model,sky,metric, resolution, viewFilter, skipOverture, radParameter, run):
        if run == True:
            # create the recipe and set the input arguments
            recipe = Recipe('point-in-time-view')
            recipe.input_value_by_name('model', model)
            recipe.input_value_by_name('sky', sky)
            recipe.input_value_by_name('metric', metric)
            recipe.input_value_by_name('resolution', resolution)
            recipe.input_value_by_name('view-filter', viewFilter)
            recipe.input_value_by_name('skip-overture', skipOverture)
            recipe.input_value_by_name('radiance-parameters', radParameter)
            
            #silent = True if run == True else False
            path = 'C:\\Users\\zxin1\\ladybug_tools\\python\\Scripts\\queenbee.exe'
            #debugFolder = 'C:\\Users\\zxin1\\Desktop\\research\\HB'
            outputPath = recipe.run(settings = None,
                                    radiance_check = True,
                                    queenbee_path = path,
                                    # debug_folder = debugFolder,
                                    silent = False)  
            
            # ouput info on queenbee.exe
            recipe.luigi_execution_summary()

            #results = recipe.output_value_by_name('results', outputPath)
            return outputPath    
        
    @staticmethod
    def annualDaylight(hbModel, wea, north, thresholds, schedule, gridFilter, radPara, run):
        if run == True:
            # create the recipe and set the input arguments
            recipe = Recipe('annual-daylight')
            recipe.input_value_by_name('model', hbModel)
            recipe.input_value_by_name('wea', wea)
            recipe.input_value_by_name('north', north)
            recipe.input_value_by_name('thresholds', thresholds)
            recipe.input_value_by_name('schedule', schedule)
            recipe.input_value_by_name('grid-filter', gridFilter)
            recipe.input_value_by_name('radiance-parameters', radPara)

            # run the recipe
            project_folder = recipe.run(settings = None, radiance_check=True, silent=False)

            # load the results
            try:
                results = recipe.output_value_by_name('results', project_folder)
                DA = recipe.output_value_by_name('da', project_folder)
                cDA = recipe.output_value_by_name('cda', project_folder)
                UDI = recipe.output_value_by_name('udi', project_folder)
                UDI_low = recipe.output_value_by_name('udi-lower', project_folder)
                UDI_up = recipe.output_value_by_name('udi-upper', project_folder)
            except Exception:
                raise Exception(recipe.failure_message(project_folder))  
            return project_folder
                   