from directory import *

import subprocess

class dir():
    # root folder
    rtDir = '/Users/xinzhou/Desktop/research/glareDetection/raytraverse'
    # subfolders
    objDir = rtDir + '/obj'
    radDir = rtDir + '/rad'
    octDir = rtDir + '/octree'
    weaDir = rtDir + '/wea'
    outDir = rtDir + '/outdir'

class Ray():
    
    def samplingArea(planeRad):
        cmd = ('raytraverse area' + 
                ' -zone ' + planeRad + 
                ' -ptres 2.0' + 
                ' --printdata True' + 
                ' --debug')

        print('Ray - sampling area: ', cmd)
        subprocess.call(cmd,
                    shell = True,
                    executable = Sys.terminal,
                    cwd = dir.radDir)
    
    # creates outdir and outdir/scene.oct
    def sceneCreation(scene):
        cmd = ('raytraverse scene' +
                ' -out ' + 'outdir' +
                ' -scene ' + scene +
                ' --debug'
                )
        print('create .oct: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = Sys.terminal,
                        cwd = dir.rtDir)

    def solarSampling(epwFile):
        cmd = ('raytraverse suns' +
                ' -loc ' + epwFile +
                ' --epwloc' +
                ' --printdata'
                )
        print('ray solarSampling: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = Sys.terminal,
                        cwd = dir.rtDir)

    def skydata(epwFile):
        cmd = ('raytraverse skydata' +
                ' -skyres 10' +
                ' -wea ' + epwFile +
                ' --debug'
                )
        print('ray skydata: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = Sys.terminal,
                        cwd = dir.outDir)   

    def createSkyOct():
        cmd = ('raytraverse skyengine' +
                ' -accuracy 2.0' +
                ' -skyres 10'
                )
        print('ray sky->.oct: ', cmd)
        subprocess.call(cmd,
                        shell = True,
                        executable = Sys.terminal,
                        cwd = dir.rtDir)  



    def run():
        cmd = 'raytraverse -c options.cfg skyrun directskyrun sunrun evaluate'
        #cmd = 'raytraverse -c options.cfg skyrun directskyrun sunrun evaluate pull'
        subprocess.call(cmd,
                        shell = True,
                        executable = Sys.terminal,
                        cwd = dir.rtDir)