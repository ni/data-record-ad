import argparse
import os
import shutil
import sys
import time

startTime = time.time()

# hardcoded paths
vilibPath = 'C:/Program Files/National Instruments/LabVIEW 2020/vi.lib/'
pathSuffix = 'ADAS Record/'
relPathToCustomData = 'CustomDataTypes/'

# argparse
parser = argparse.ArgumentParser(description="After branch checkout, move CustomDataTypes to vi.lib. If making modifications or adding new CustomDataTypes, use this script with the -r switch to move in the reverse direction.")
parser.add_argument("-r", "--reverse", action='store_true', help = "Move CustomDataTypes back into the repo from vi.lib.")
parser.add_argument("-f", "--force", action='store_true', help = "Force overwrite of <vilib>/ADAS Record/CustomDataTypes if it's not empty.")
args = parser.parse_args()

# path to script, CustomDataTypes calculated relatively
scriptPath = os.path.dirname(os.path.realpath(sys.argv[0])) + '/'

# repo folder to vi.lib
if not args.reverse:
    if not os.path.exists(scriptPath + relPathToCustomData):
        print(f"{scriptPath}{relPathToCustomData} is empty or may already have been moved. No action taken.")
        exit()
    print("Moving CustomDataTypes from repo to <vilib>")
    try:
        shutil.move(scriptPath + relPathToCustomData, vilibPath + pathSuffix)
    except shutil.Error:
        if args.force:
            print("Target folder not empty, force flag enabled. Attempting to overwrite.")
            print(f"Deleting {vilibPath}{pathSuffix}{relPathToCustomData}...")
            shutil.rmtree(vilibPath + pathSuffix + relPathToCustomData)
            print("Moving CustomDatatypes from repo folder...")
            shutil.move(scriptPath + relPathToCustomData, vilibPath + pathSuffix)
        else:
            print(f"<vilib>/{pathSuffix}{relPathToCustomData} was not empty, no files moved. If intending to overwrite, run this script with -f option.")
            exit()
    print("CustomDataTypes folder moved to <vilib> successfully.")

# vi.lib to repo folder
elif args.reverse:
    if not os.path.exists(vilibPath + pathSuffix + relPathToCustomData):
        print(f"{vilibPath}{pathSuffix}{relPathToCustomData} is empty or may already have been moved. No action taken.")
        exit()
    print("Moving CustomDataTypes from <vilib> into repo")
    try:
        shutil.move(vilibPath + pathSuffix + relPathToCustomData, scriptPath)
    except shutil.Error:
        if args.force:
            print("Target folder not empty, force flag enabled. Overwriting.")
            print(f"Deleting {scriptPath}{relPathToCustomData}...")
            shutil.rmtree(scriptPath + relPathToCustomData)
            print("Moving CustomDataTypes from <vilib>")
            shutil.move(vilibPath + pathSuffix + relPathToCustomData, scriptPath )
        else:
            print(f"{scriptPath}/CustomDataTypes was not empty. If intending to overwrite, run this script with -f option.")
            exit()
    print("CustomDataTypes folder moved into repo successfully.")

endTime = time.time()

print(f"{parser.prog} ran in {(endTime - startTime):.4f} seconds.")
