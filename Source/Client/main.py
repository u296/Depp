import sys
import argparser
import webclient
import asyncio

def ProgramQuit(status : str):
    print(f"Program terminated: {status}. Press return to continue.")
    input()
    exit()

async def main():
    if sys.platform == 'win32':
        runMode = argparser.GetRunmode(["main.py", "install", "-s", "-o", "mods", "-f", "none", "tconstruct", "ic2"])
        print(runMode)
        if runMode['logLevel'] == 'silent':#    Silent loglevel
            if runMode['command'] == 'install':
                httpClient = webclient.WebClient("192.168.0.100:8080")
                modInstallPath = 'mods'

                if '-o' in runMode:
                    modInstallPath = runMode['-o']
                
                installedMods = []

                print(await httpClient.Get(""))



            ProgramQuit("Success")
        elif runMode['logLevel'] == 'default':# Default loglevel
            pass
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