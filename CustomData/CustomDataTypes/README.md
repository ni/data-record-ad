## Requirements

adas-pef-private >= 1.1.0.24 

# Overview

This project forms the basis of a wrapper API around PEF's CustomData feature. CustomData allows the sending of arbitrary data types through the PEF engine, with automatic tracking of reference type data.
The objective is for all data transfer between user plugins to use this API by calling the required instance of the Write or Read ADAS Data polymorphic VI, thereby reducing user error when coupling writer and reader plugins.

# Contributing

Follow these steps to add a new data type to the project:
1. Branch this repo
1. Open the lvproj
2. Right-click on the NI_ADAS_Generic.lvlib in the project window and select Save As...
3. Choose a new name for your datatype.
4. Apply a new VI Icon for your new library.
5. Modify the Process Data.ctl cluster to fit your data type's needs.
6. Add your type instances into the top-level polymorphs with an appropriate name.
7. Make a pull request into this repo.

# Future State and To-Do's

This feature and all child features are being tracked here: https://github.com/ni/data-record-ad-internal/issues/3
The manual steps above should be scripted, and tests should be added to this repo to ensure compliance of data types to some TBD standard.
The process cluster should be defined from a text-based schema file for easy modification, interop, and recompilation.

