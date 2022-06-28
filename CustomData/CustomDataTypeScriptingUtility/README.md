# Custom Data Type Scripting
Allows users to interactively script custom data types by defining a LabVIEW type definition.  The code automatically updates the generated data type code and adds the functionality to the four Polymorphic VIs 

## Dependencies
A VIPC has been included within the _Dependencies_ folder which includes the following packages:
![image](https://user-images.githubusercontent.com/15633959/136422512-9aeaaff5-aa47-4107-9cd3-67af49f0e801.png)


## Project Overview
![image](https://user-images.githubusercontent.com/15633959/136422336-6daadcf1-7285-4ec7-8440-dba8ea909b81.png)
### Data Type Scripting Module\Data Type Scripting.lvlib
DQMH module which uses the Scripting APIs to automate the creation and removal of custom data types.
### Scripting APIs
Various scripting APIs which help automate the creation and removal of custom data types.
#### Poly Management
These VIs are used for managing the four polymorphic VIs that call Read/Write/Deserialize/Serialize of teh custom data types.
#### Template Updates
These VIs are used to update Process Data.ctl (type definition) and test_serialize_deserialize.vi (Test VI) after the custom data type is generated.
#### XML
Development test VI for parsing capabililty of data type XML definition (using LabVIEW Schema).
##### Data Type
These VIs will eventually be used if the user provides an XML definition for a custom data type.

### Data Type Scripting Main UI.vi
This is the main UI that users interact with the create custom data types.  
![image](https://user-images.githubusercontent.com/15633959/134547146-96596919-32bd-4601-be2d-06893e9a1e1f.png)
Upon running, this starts the DQMH module and loads the template custom data type and polymorphic VIs.  On the right is a status message indicator.  

The "Poly VI Info" tab shows information about the four polymorphic VIs and their members.  It also allows the user to quickly open the Poly.

![image](https://user-images.githubusercontent.com/15633959/134547366-7d4606d3-2d45-4b24-b379-c78272fff055.png)
When the "Add New Type" tab is selected, a LabVIEW control window will open.  This is where the user drops down any controls/indicators that make up their custom data type.  They must also give it a unique Data Type Name, Menu Name and Selector Name - they can be the same but cannot match any existing data types.  Once that is complete, the user can select "Create New Data Type" :
![image](https://user-images.githubusercontent.com/15633959/134547693-aa4bff5e-84db-4e44-8cb1-a16736cec1dd.png)
When the data type has been created, the control window will close and the new data type will appear in the "Data Types" list on the "Remove Type" tab:
![image](https://user-images.githubusercontent.com/15633959/134547945-09c1956e-3f60-418c-a195-b764938c21ff.png)
This is also where Custom Data Types can be removed.  Removing through this utility removes them from the Polymorphic VIs and disk (if enabled).
