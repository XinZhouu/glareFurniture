# from HoneybeeUsr.hbVis import *
from Tools.dirLocation import *
from Tools.osUtil import *

resultPath = 'C:\\Users\\zxin1\\simulation\\unnamed_06045e9c'
################################################################################
# move files to the project folder
################################################################################
# 'visualize UDI(middle range)'
# dayAvilFolder = Dir.results + '\\' + 'daylight_avail'
# udiPath = dayAvilFolder + '\\' + 'udi.udi'
# udilowPath = dayAvilFolder + '\\' + 'udilow.udi'
# udiupPath = dayAvilFolder + '\\' + 'udiup.udi'
# cdaPath = dayAvilFolder + '\\' + 'cda.cda'
# daPath = dayAvilFolder + '\\' + 'da.da'
# rawpath = dayAvilFolder + '\\' + 'raw.ill'

# da = pyUtil.readSimpleFile(daPath)
# da = strUtil.batchFromStrToFloat(da)
# mesh, legend, colors, legendPara = hbVis.spatialHeatMap(da, sampleMesh, [0, 0], None, '%', None)

# # mesh type: <Rhino.Geometry.Mesh object at 0x0000000000009577 [Rhino.Geometry.Mesh]>
# sc.doc.ActiveDoc.Objects.Add(mesh)
# sc.doc.ActiveDoc.Views.Redraw