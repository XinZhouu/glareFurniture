# This is the main file to run the whole algorithm and interacting with rhino
###############################################
# PROGRAMS 
'''
1. RhinoCommon SDK
2. Ladybug Tools SDK
'''
################################################################################
'''
rhino.inside works in headless mode: 
    It is running in the back and there is no 
    GUI showing the process.
'''
import rhinoinside
rhinoinside.load('C:\Program Files\Rhino 7\System')
################################################################################

import System
import Rhino

dummy_out = System.Int32(0)

# pts = System.Collections.Generic.List[Rhino.Geometry.Point3d]()
# pts.Add(Rhino.Geometry.Point3d(0.0,0.0,0.0))
# pts.Add(Rhino.Geometry.Point3d(1.0,0.0,0.0))
# pts.Add(Rhino.Geometry.Point3d(1.5,2.0,0.0))

# crv = Rhino.Geometry.Curve.CreateInterpolatedCurve(pts,3)
# print (crv.GetLength())
