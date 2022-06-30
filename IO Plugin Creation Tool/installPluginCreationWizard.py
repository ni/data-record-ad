import argparse
import os
import shutil

# hardcoded paths, sources relative to this script location
srcScripting = os.path.join(os.path.dirname(__file__),'IO PE Creation Wizard', 'IO PE Creation MDO')
srcIcon = os.path.join(os.path.dirname(__file__), 'IO PE Creation Wizard', 'Images')
srcTemplate = os.path.join(os.path.dirname(__file__),'PE Template')

dstScripting = os.path.abspath("C:/Program Files/National Instruments/LabVIEW 2020/ProjectTemplates/Source/ADAS/ADAS IO Template/Scripting/IO PE Creation MDO/")
dstTemplate = os.path.abspath("C:/Program Files/National Instruments/LabVIEW 2020/ProjectTemplates/Source/ADAS/ADAS IO Template/PE Template")
dstIcon = os.path.abspath("C:/Program Files/National Instruments/LabVIEW 2020/ProjectTemplates/Source/ADAS/ADAS IO Template/Images")

# script options
parser = argparse.ArgumentParser(description="")
parser.add_argument("-f", "--force", action='store_true', help = "Force overwrite of Data Record AD Plugin Creation Wizard if it was already installed.")
args = parser.parse_args()

if __name__ == '__main__':
    try:
        shutil.copytree(srcTemplate, dstTemplate)
        shutil.copytree(srcScripting, dstScripting)
        shutil.copytree(srcIcon, dstIcon)
        print("Data Record AD Plugin Creation Wizard installed successfully.")
    except FileExistsError:
        if args.force:
            print("Data Record AD Plugin Creation Wizard was already installed, force flag enabled. Removing existing installation.")
            shutil.rmtree(dstTemplate)
            shutil.rmtree(dstScripting)
            shutil.rmtree(dstIcon) 
            shutil.copytree(srcTemplate, dstTemplate)
            shutil.copytree(srcScripting, dstScripting)
            shutil.copytree(srcIcon, dstIcon)
            print("Data Record AD Plugin Creation Wizard installed successfully.")
        else:
            print("Data Record AD Plugin Creation Wizard already installed on this machine. Rerun with --force flag if intending to overwrite.")

