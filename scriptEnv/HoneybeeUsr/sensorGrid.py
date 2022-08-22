from ladybug_geometry.geometry3d.plane import Plane
from ladybug_geometry.geometry3d.face import Face3D
from ladybug_geometry.geometry3d.mesh import Mesh3D
from ladybug_rhino.togeometry import to_gridded_mesh3d, to_mesh3d, to_face3d, to_vector3d
from ladybug_rhino.fromgeometry import from_mesh3d, from_point3d, from_vector3d

from honeybee.typing import clean_and_id_rad_string, clean_rad_string
from honeybee_radiance.sensorgrid import SensorGrid

################################################################################
# CODE SOURCE: 
'''
The following codes are MODIFIED from
orginial official codes from LADYBUG TOOLS: https://github.com/ladybug-tools

The official link above has several respositories, which have open SDKS:
https://discourse.ladybug.tools/pub/ladybug-tools-core-sdk-documentation

Modifications:
1, The script simplifies some of the steps to tailor to the project.
2, The script shortens some of the input parameters.
3, The script paraphrases some of the python syntax to make it more 
   clear and understandable to myself.
4, The script attempts to use CLASS to better control and classify each function.
'''
################################################################################


class daylitModel:
    
    @staticmethod
    def generateSensorGrid(samplingArea, gridSize, offsetDistance):
        # check the input and generate the mesh.
        offsetDistance = offsetDistance or 0
        if quad_only_:  # use Ladybug's built-in meshing methods
            lb_faces = to_face3d(_geometry)
            try:
                x_axis = to_vector3d(quad_only_)
                lb_faces = [Face3D(f.boundary, Plane(f.normal, f[0], x_axis), f.holes)
                            for f in lb_faces]
            except AttributeError:
                pass  # no plane connected; juse use default orientation
            lb_meshes = []
            for geo in lb_faces:
                try:
                    lb_meshes.append(geo.mesh_grid(_grid_size, offset=_offset_dist_))
                except AssertionError:  # tiny geometry not compatible with quad faces
                    continue
            if len(lb_meshes) == 0:
                lb_mesh = None
            elif len(lb_meshes) == 1:
                lb_mesh = lb_meshes[0]
            elif len(lb_meshes) > 1:
                lb_mesh = Mesh3D.join_meshes(lb_meshes)
        else:  # use Rhino's default meshing
            try:  # assume it's a Rhino Brep
                lb_mesh = to_gridded_mesh3d(_geometry, _grid_size, _offset_dist_)
            except TypeError:  # assume it's a Rhino Mesh
                try:
                    lb_mesh = to_mesh3d(_geometry)
                except TypeError:  # unidientified geometry type
                    raise TypeError(
                        '_geometry must be a Brep or a Mesh. Got {}.'.format(type(_geometry)))

        # generate the test points, vectors, and areas.
        if lb_mesh is not None:
            points = [from_point3d(pt) for pt in lb_mesh.face_centroids]
            vectors = [from_vector3d(vec) for vec in lb_mesh.face_normals]
            face_areas = lb_mesh.face_areas
            mesh = [from_mesh3d(lb_mesh)]
        else:
            mesh = []        
    
    @staticmethod
    def createSensorGrid(gridName, ):
        # set the default name and process the points to tuples
        name = clean_and_id_rad_string('SensorGrid') if gridName is None else gridName
        pts = [(pt.X, pt.Y, pt.Z) for pt in _positions]

        # create the sensor grid object
        id  = clean_rad_string(name) if '/' not in name else clean_rad_string(name.split('/')[0])
        if len(_directions_) == 0:
            grid = SensorGrid.from_planar_positions(id, pts, (0, 0, 1))
        else:
            vecs = [(vec.X, vec.Y, vec.Z) for vec in _directions_]
            grid = SensorGrid.from_position_and_direction(id, pts, vecs)

        # set the display name
        if _name_ is not None:
            grid.display_name = _name_
        if '/' in name:
            grid.group_identifier = \
                '/'.join(clean_rad_string(key) for key in name.split('/')[1:])
        if mesh_ is not None:
            grid.mesh = to_mesh3d(mesh_)
        if base_geo_ is not None:
            grid.base_geometry = to_face3d(base_geo_)