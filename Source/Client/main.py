import sys
import argparser

def ProgramQuit(status : str):
    print(f"Program terminated: {status}. Press return to continue.")
    input()
    exit()

if __name__ == '__main__':
    runMode = argparser.GetRunmode(["main.py", "install", "-v", "-o", "mods", "-f"])
    print(runMode)
    if runMode['logLevel'] == 'silent':#    Silent loglevel
        


        ProgramQuit("Success")
    elif runMode['logLevel'] == 'default':# Default loglevel
        pass
        ProgramQuit("Success")
    elif runMode['logLevel'] == 'verbose':# Verbose loglevel 
        pass
        ProgramQuit("Success")

    print(runMode)
    ProgramQuit(f"Failed: Invalid loglevel: '{runMode['logLevel']}'")