from honeybee.model import Model
from honeybee_radiance.properties.model import ModelRadianceProperties

class assign:
    
    @staticmethod
    def viewOrGridToModel(model, view, grid):
        assert isinstance(model, Model), \
            'Expected Honeybee Model. Got {}.'.format(type(model))
        hbModel = model.duplicate()  # duplicate to avoid editing the input
        if grid != None:
            finalModel = ModelRadianceProperties(hbModel, sensor_grids = None, views = None)
            finalModel.add_sensor_grid(grid)             
        if view != None:
            # finalModel = ModelRadianceProperties(hbModel, sensor_grids = None, views = None)
            # finalModel.add_view(view)    
            hbModel.properties.radiance.add_view(view)
        return hbModel  