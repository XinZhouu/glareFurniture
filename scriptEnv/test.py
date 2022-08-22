# import rhinoscriptsyntax as rs
# import scriptcontext as sc
# import Rhino

# unit = rs.UnitSystem()
# print(unit)

# unit = Rhino.RhinoDoc.ActiveDoc.ModelUnitSystem.ToString()
# print(unit)

# unit = sc.doc.PageUnitSystem
# print(unit)

import subprocess

# def catFileAll(fileList, cwd, twd):
#     fileString = ' '.join(fileList)
#     newFileName = 'scene.rad'
#     newFile = twd + '\\' + newFileName
    
#     cmd = ('cat ' + 
#             fileString +
#             ' > ' + newFile)
    
#     subprocess.call(cmd,
#                     executable = dir.bash,
#                     shell = True,
#                     cwd = cwd)   
    
cwd = 'C:/Users/zxin1/Desktop/research/HB'

cmd = 'cp -r ' + './file/objData/aperture.mat' + ' ./raytraverse/aperture.mat'

bashDir = 'C:/Program Files/Git/bin/bash.exe'
subprocess.call([bashDir, '-c', cmd], cwd = cwd)

# set PYTHONPATH=%PYTHONPATH%;C:\Users\zxin1\Desktop\Glare\scriptEnv\

