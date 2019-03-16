import sys
import asyncio
import os
import shutil
import re

import argparser
import webclient
import mod

def ProgramQuit(status : str):
    print(f"Program terminated: {status}. Press return to continue.")
    input()
    exit()

def IterateData(data : list):
    for element in data:
        yield element

async def main():
    if sys.platform == 'win32':
        runMode = argparser.GetRunmode(["main.py", "install", "-o", "mods", "-f", "none", "tconstruct", "ic2"])
        print(runMode)
        if runMode['logLevel'] == 'silent':#    Silent loglevel
            ProgramQuit('Failed: Loglevel not implemented')
        elif runMode['logLevel'] == 'default':# Default loglevel
            if runMode['command'] == 'install':
                httpClient = webclient.WebClient("192.168.0.100:8080")
                modInstallPath = 'mods'
                nonInstalledMods = []

                if '-o' in runMode:
                    modInstallPath = runMode['-o']
                
                if '-l' in runMode:
                    installedMods = []

                    for root, dirs, files in os.walk(f'.\\{modInstallPath}'):
                        for file in files:
                            if file.endswith('.jar'):
                                print(file)
                                installedMods.append(file)

                elif '-r' in runMode:

                    modsToInstall = set()

                    for info in runMode['data']:
                        mod = info.split('||')[0]
                        version = ""

                        try:
                            version = info.split('||')[1]
                        except IndexError as e:
                            pass
                        if version.lower() == 'max' or version == '':
                                version = await httpClient.Get({
                                    'requestType':'modVersionCheck',
                                    'mod':mod,
                                    'data':'max'
                                    })['version']
                                if re.search('^([0-9]+\.?)*[0-9]+$', version) == None:
                                    ProgramQuit(f"Failed: Invalid mod version data: '{version}'")

                                modDependencies = await httpClient.Get({
                                    'requestType':'getDependencies',
                                    'mod':mod,
                                    'data':''
                                })['dependencies']

                                for dependency in modDependencies:
                                    modsToInstall.add(mod.ModDependency(dependency['name'], dependency['minVersion'], dependency['maxVersion']))



                    
                    for file in os.listdir(modInstallPath):
                        filePath = os.path.join(modInstallPath, file)
                        try:
                            if os.path.isfile(filePath):
                                os.unlink(filePath)
                            elif os.path.isdir(filePath):
                                shutil.rmtree(filePath)
                        except Exception as e:
                            ProgramQuit(f"Failed: Couldn't empty directory '{modInstallPath}': {e}")

                   

                        

                            

                                



                
            ProgramQuit("Success")
        elif runMode['logLevel'] == 'verbose':# Verbose loglevel 
            pass
            ProgramQuit("Success")

        print(runMode)
        ProgramQuit(f"Failed: Invalid loglevel: '{runMode['logLevel']}'")
   
    else:
        ProgramQuit(f"Failed: Unsupported os platform: '{sys.platform}'")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())