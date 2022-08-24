import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

class rhDataCtl:
    
    @staticmethod
    def duplicateDataToList(value, num):
        lst = gh.DuplicateData(value, num)
        return lst