# Custom Data Types
## Overview
One of the main tasks of the Data Record AD framework is to serve as a data repository.  IO plugins can write or read various data types to/from the engine.  

Installing the **_Data Record AD Development Suite_** installs various LabVIEW libraries to assist with the development of IO plugins, including `CustomData.lvlib` _(\<LabVIEW Installation Directory>\vi.lib\ADAS Record\CustomData)_.

![image](https://user-images.githubusercontent.com/15633959/176258548-21680a5e-ac8e-477d-a2d9-964ab7a001a1.png)

This library has a number of VIMs that allow users to send/receive data to the Data Record AD engine.  It is easy to make a mistake while using these VIMs so these have been abstracted with the use of **_Custom Data Types_**.  It is recommended that developers use the Custom Data Type polymorphic VIs described below over the low-level _CustomData_ library.

## Getting Started
Custom Data Types refers to a series of VIs and a wrapper API to the `CustomData.lvlib` VIs.  The objective is for all data transfer between user plugins to use this API by calling the required instance of the Write or Read ADAS Data polymorphic VI, thereby reducing user error when coupling writer and reader plugins.

### Installing Custom Data Types
Custom Data Types should only reside in the _(\<LabVIEW Installation Directory>\vi.lib\ADAS Record\CustomDataTypes)_ directory.  There is no NIPM or VIPM package for installing this library.  Instead, the latest Custom Data Types must be checked out from this GitHub repository.  A python script exists within the top-level directory, setupEnv_CustomDataTypes.py.  

Run the script to move the necessary files to the appropriate location in vi.lib.  Use the -f flag to overwrite if necessary.

Running the script with the -r flag reverses the action.  It moves Custom Data Types back from vi.lib to your repository checkout location so added/edited/removed files can be checked back in.

![image](https://user-images.githubusercontent.com/15633959/176289108-239acade-c8b1-4340-8f53-a7858d7afc5e.png)


### Creating/Editing/Removing Custom Data Types
See [this README](../CustomData/CustomDataTypeScriptingUtility#readme) for details on using the Custom Data Type Scripting Utility to create, edit and remove Custom Data Types.

## Developer Notes
### Pull Requests for Custom Data Types
If the data type required by a developer does not already exist as a custom data type, a new type should be created following this process:
1. Create a branch called _user/\<yourname>/customdata/\<descripton of custom data type>_
1. Using the utility described above, create the custom data type
1. Create a pull request for the custom data type

Priority will be given to approving PRs for Custom Data Types.

### GIT Hooks
If you would like to automate the calling of the python script for moving the Custom Data Types, please use the githooks provided [here](../Utilities/githooks).
