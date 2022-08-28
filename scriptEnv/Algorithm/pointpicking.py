# this script interacts with rhinoPython(ironPython)!
import rhinoscriptsyntax
import random
import Rhino.Geometry as rg



#class limitingFactor():
#    
#    @staticmethod
#    def isOnTheEdge():
#        
#    

class furniture():
    """
    1, the default massCentroid is (0,0,0)
    2, view direction is the screen normal
    3, radius is from the bounding circle of the furniture
    """
    
    def __init__(self, massCentroid, radius, viewDirection):
        self.massCentroid = massCentroid
        self.radius = radius
        self.viewDirection = viewDirection
        
        self.pts = []
        
    
    def moveTo(self, officePlane, numOfOccupants):
        for i in range(numOfOccupants):
            ptX = random.random()
            ptY = random.random()
            ptZ = 0
            officePlane.PointAt(ptX, ptY, ptZ)
            

        