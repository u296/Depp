import re

def GetRunmode(args):
    if len(args) < 2:
        raise Exception

    argumentRequiringOptions = ['-o']

    runMode = {'data':[]}
    args.pop(0)
    runMode['command'] = args[0]
    args.pop(0)

    runMode['logLevel'] = 'default'
    key = ""

    awaitingValue = False

    for arg in args:    # Reserved options
        if arg == '-v' or arg.lower() == '--verbose':
            runMode['logLevel'] = 'verbose'
        elif arg == '-s' or arg.lower() == '--silent':
            runMode['logLevel'] = 'silent'
        elif arg == '-d' or arg.lower() == '--default':
            runMode['logLevel'] = 'default'
            
        elif re.search("^-", arg) != None:  # If argument is an option
            runMode[arg] = ""
            if arg in argumentRequiringOptions: # If option requires an argument
                key = arg
                awaitingValue = True
        elif awaitingValue and re.search(r"^(!?-)", arg) == None:    # If an option is awaiting an argument
            runMode[key] = arg
            awaitingValue = False
        elif awaitingValue:
            raise IndexError
        else:
            runMode['data'].append(arg)
            awaitingValue = False
        
        
    

    return runMode