import rhinoscriptsyntax as rs

class plane:
    
    # attributes
    planeXY = rs.WorldXYPlane()

class pt(plane):
    
    @staticmethod
    def deconstructPt(pt):
        return (pt.X, pt.Y, pt.Z)
    
    @staticmethod
    def constructPt(tuple):
        pt = rs.CreatePoint(tuple[0], tuple[1], tuple[2])
        return pt
    
class transData:
    
    @staticmethod
    def GUIDToBrep(GUID):
        object = rs.coercebrep(GUID)
        return object