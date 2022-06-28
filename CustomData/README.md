# Custom Data Types
## Overview
One of the main tasks of the Data Record AD framework is to serve as a data repository.  IO plugins can write or read various data types to/from the engine.  

Installing the **_Data Record AD Development Suite_** installs various LabVIEW libraries to assist with the development of IO plugins, including `CustomData.lvlib` _(\<LabVIEW Installation Directory>\vi.lib\ADAS Record\CustomData)_.

![image](https://user-images.githubusercontent.com/15633959/176258548-21680a5e-ac8e-477d-a2d9-964ab7a001a1.png)

This library has a number of VIMs that allow users to send/receive data to the Data Record AD engine.  It is easy to make a mistake while using these VIMs so these have been abstracted with the use of **_Custom Data Types_**.  It is recommended that developers use the Custom Data Type polymorphic VIs described below over the low-level _CustomData_ library.

## Getting Started
Custom Data Types 

### Installing Custom Data Types

### Creating/Editing/Removing Custom Data Types



## Developer Notes
### Pull Requests for Custom Data Types
If the data type required by a developer does not already exist as a custom data type, a new type should be created following this process:
1. Create a branch called _user/\<yourname>/customdata/\<descripton of custom data type>_
1. Using the utility described above, create the custom data type
1. Create a pull request for the custom data type

Priority will be given to approving PRs for Custom Data Types.

### GIT Hooks
