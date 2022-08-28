import clr
clr.AddReferenceByName("RhinoCommon")

import Rhino.Geometry as rg
import rhinoscriptsyntax as rs


class srfPrimitive:
    
    @staticmethod
    def getBoundingBox(arrayStrObject):
        bBox = arrayStrObject.GetBoundingBox(True)
        return bBox