import clr
clr.AddReferenceByName("RhinoCommon")

from Algorithm.model import rhinoSpace

from EtoUsr.EtoForms import requestOccupantNumber

from RhinoUsr.rhinoSrf import srfPrimitive

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import scriptcontext as sc
################################################################################
# PARAMETERS:

'Rhino Layers'
daylightModelLayer = 'Daylight Model'
furniturePrototypeLayer = 'FurnitureStyle1'
################################################################################

# 1 Eto starts
# num = requestOccupantNumber()

# 2 get furniture objects
# {subLayerName: GUID object}
furnitureDic = rhinoSpace.accessRhinoLayers(furniturePrototypeLayer)
arrayFurObjects = furnitureDic.values() # a 2d list

bBox = rg.BoundingBox.Unset # initiate an empty boundingbox set
for array in arrayFurObjects:
    for object in array:
        object = rs.coercebrep(object)
        boundingBox = srfPrimitive.getBoundingBox(object)
        bBox.Union(boundingBox)

# visualize the bounding box and 
# sc.doc.Objects.AddBrep(bBox.ToBrep())
# sc.doc.Objects.AddPoint(bBox.Center)
# sc.doc.Views.Redraw()

bBoxBrep = bBox.ToBrep()
FurnitureBaseGUID = rs.ExtractSurface(bBoxBrep, 4, False) # this is a list
FurnitureBaseObj = rs.coercebrep(FurnitureBaseGUID[0])
# visualization debugging
# sc.doc.Objects.AddBrep(FurnitureBaseObj)
vertices = rg.Brep.DuplicateVertices(FurnitureBaseObj) # Array[Point3d]
vertex = vertices[0]
centerBase = rs.SurfaceAreaCentroid(FurnitureBaseObj)[0]
centerBasePt = rs.CreatePoint(centerBase[0], centerBase[1], centerBase[2])
# visualization debugging
sc.doc.Objects.AddPoint(vertex)
sc.doc.Objects.AddPoint(centerBasePt)
circle = rs.AddCircle(centerBasePt, rs.Distance(vertex, centerBasePt))





