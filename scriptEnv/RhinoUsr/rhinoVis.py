import rhinoscriptsyntax as rs
import Rhino
import scriptcontext as sc

class canvas:
    
    @staticmethod
    def enableRedraw():
        'use scriptcontext'
        sc.doc.Views.RedrawEnabled = True
        'use rhinoscriptsyntax'
        # rs.EnableRedraw(True)
        
    @staticmethod
    def disableRedraw():
        'use scriptcontext'
        sc.doc.Views.RedrawEnabled = False      
        
    @staticmethod
    def redraw():
        sc.doc.Views.Redraw()

class vis:
    
    @staticmethod
    def points(pointList):
        rs.AddPoints(pointList)
        canvas.redraw()
        

    @staticmethod
    def polyline(polyline):
        if isinstance(polyline, Rhino.Geometry.Polyline):
            if polyline.IsValid: 
                curve = polyline.ToNurbsCurve()
                sc.doc.Objects.AddCurve(curve)
                canvas.redraw()
        