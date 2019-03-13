import re

def GetRunmode(args):
    if len(args) < 2:
        raise Exception
    runMode = {}
    args.pop(0)
    runMode['command'] = args[0]
    args.pop(0)

    runMode['logLevel'] = 'default'
    key = ""

    awaitingValue = False

    for arg in args:
        if arg == '-v' or arg.lower() == '--verbose':
            runMode['logLevel'] = 'verbose'
        elif arg == '-s' or arg.lower() == '--silent':
            runMode['logLevel'] = 'silent'
        elif arg == '-d' or arg.lower() == '--default':
            runMode['logLevel'] = 'default'
            
        elif re.search("^-", arg) != None:
            runMode[arg] = ""
            key = arg
            awaitingValue = True
        elif re.search("^(!?-)", arg) == None and awaitingValue:
            runMode[key] = arg
            awaitingValue = False
        else:
            awaitingValue = False
        
        
    

    return runMode