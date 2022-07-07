# Overview
This is part 2 of a five part tutorial.  It walks through the development of an IO plugin that reads numeric values (double custom data type) and saves them to a text file.  It is meant to be used with the _Random Number Generator_ IO plugin.

[Return to IO Plugin Tutorial](../IO%20Plugin%20Tutorial.md#io-plugin-tutorial)

# Create Data Sink IO Plugin - Text File
## Create Project
Launch LabVIEW and create a new _ADAS IO Plugin Template_ project. Complete the information for the template as provided. The IO Plugin Name should be _RandomNumberLogger_. The IO Plugin Directory should be _\<Checkout Directory>/IO Plugins/RandomNumberLogger_. It is also a good idea to update the icon to be more representative of the plugin purpose. When you are finished updating the information, select Finish.  

![image](https://user-images.githubusercontent.com/15633959/176764681-25bb4e67-04ba-41d3-889c-61b45672a219.png)

## Edit IO Plugin Configuration Parameters
Open the generated project. Navigate down to the Configuration.ctl type definition (PE >> RandomNumberLogger.lvlib >> RandomNumberLogger.lvclass >> Types). Modify the type definition to have four controls as shown here:
![image](https://user-images.githubusercontent.com/15633959/176767166-3fe47acb-a6e0-44ff-8234-322173eeb1a2.png)

Values for the _File Split_ enum:<br>
0: None <br>
1: Time <br>
2: Size <br>

Note: To complete the tutorial in less time, the file split functionality may be omitted.

## Set Default Configuration Parameters 
Edit the default configuration parameters (_RandomNumberLogger.lvlib:RandomNumberLogger.lvclass:Default Configuration Parameters.vi_):<br>
Base File Name: Random.txt<br>
File Directory: C:\Data<br>
File Split: Time<br>
Split Time/Size (s/MB): 0.5<br>

## Update Mutate Configuration to Current
If the original string control was simply repurposed for the Base File Name, it is likely that _Mutate Configuration to Current_ is not broken.  If you removed it and/or added the controls in a different order you may need to fix this VI before building the plug-in.

## Update States
### Initialize
This plugin is intended to save data to disk so the timing parameters for this plugin should reflect that behavior.  In _Initialize_, update the _Timing Method_ to be _On Data Ready_.
![image](https://user-images.githubusercontent.com/15633959/176770255-df26e59b-3a8c-4ff2-bae7-74258916fd58.png)

### Read Parameters
No changes required for _Read Parameters_.

### Configure Session
This is where the majority of the initialization code needs to happen.  The first file split path will be built and a reference to that file will be opened. If file split is by time, an intial time should be noted and saved for future use...the big question is what do we do with this data?
![image](https://user-images.githubusercontent.com/15633959/176774506-aa54eae1-2482-48a9-9141-ea242621f1ab.png)

This data needs to be stored as part of the class private data.  Back in the LabVIEW project, open _RandomNumberLogger.ctl_ and add the following four controls:
![image](https://user-images.githubusercontent.com/15633959/177364881-64361dab-56ab-4d51-9733-1fd8433356b8.png)

The _Configure Session_ VI can also be updated to utilize the new class private data.  Set the _index_ value to _1_ - more information on this value will be discussed in subsequent steps.
![image](https://user-images.githubusercontent.com/15633959/177365233-9d16574e-2d89-4e3d-8b2d-e93490abf1fd.png)

### Process
The behavior of _Process_ will be different depending upon the user configuration for file split type.  

All instances will need to read the double value from the Data Record AD engine and format it into a string that can be written to text file.  These are the highlighted sections of code outside of the case structure in the image below.  The _File Split_ configuration enum is wired to the case structure.  

![image](https://user-images.githubusercontent.com/15633959/177379469-72d80f3d-95c5-4cfe-93b2-d366e203fae4.png)

#### File Split: NONE
For the _File Split_ instance of _None_ we only need to write to the original file we opened a reference to in _Configure Session_.  The file ref (and error wire) are simply passed through.  If you do not wish to implement file split you can stop here and move on to the subsequent steps.

![image](https://user-images.githubusercontent.com/15633959/177379590-e6501c49-3917-4dc3-8bdf-d9e82d029748.png)

#### File Split: SIZE
For the _File Split_ instance of _Size_ we need to check the size of the file and decide whether or not we need to split and open a new file.  The code to complete this check is shown below.  In the _False_ case, the file has not yet reached the split size and the old reference is simply passed through.

![image](https://user-images.githubusercontent.com/15633959/177379719-ca6bce17-8ea5-40f3-810b-1faa45a6534a.png)

#### File Split: TIME
For the _File Split_ instance of _Time_ we need to check if the split time has elapsed and if it has we need to close the old file and open a new file reference.  The code to complete this check is shown below.  In the _False_ case, the split time has not elapsed and the old reference and old index value are simply passed through/

![image](https://user-images.githubusercontent.com/15633959/177380935-0d8083fb-f052-4238-acb7-3a9a916e051a.png)

So how does the _Index_ help to determine if time has elapsed? It allows us to compare the current time to the start time and expected elapsed time.  For example, if the split time was 10 seconds and our relative start time was 2519, we would expect the file splits to happen at: 
<br>2529 (2519 + 1\*10) --> Index = 1
<br>2539 (2519 + 2\*10) --> Index = 2
<br>2549 (2519 + 3\*10) --> Index = 3
<br> and so on...

### Cleanup Session
Any references open in _Configure Session_ should be closed in _Cleanup Session_.  For this IO plugin we need to close our file reference.

![image](https://user-images.githubusercontent.com/15633959/177385885-ee2fd231-0673-4634-98e6-09804b612c37.png)

### Finalize
Any references open in _Initialize_ should be closed in _Finalize_.  No changes required for _Finalize_.

### Handle Message
No changes required for _Handle Message_.

## Build IO Plugin
The IO Plugin Project Template includes a predefined build specification for a Packed Project Library. The build specification does not need any modifications. Changing names may actual result in an unfunctional plugin.

The destination directory is set to be the default directory for IO plugins. This makes it easy to test your plugin immediately. This field could be modified if you are not working on a system with Data Record AD but wish to build a plugin for later installation.

No modifications to the build specification to include additional dependencies is required. 

Expand the Build Specifications in the LabVIEW project.  Right-click on the specification and select _Build_.

## Test IO Plugin  
Launch the Data Record AD System Configuration Editor. Open the ADAS project created in the first tutorial. Open the project's ADAS System Configuration. From the IO Plugin palette, find your recently created Random Number Logger IO plugin and add it to the configuration.  Connect the output of the _Random Number Generator_ to the input of the _Random Number Logger_ as shown in the configuration below.

![image](https://user-images.githubusercontent.com/15633959/177414175-1ec65571-c687-43e2-b84f-c1419aeaebc9.png)

Generate the configuration and launch Data Record AD.  You should be able to see the IO Plugin names listed on the main Data Record AD application user interface. You should also see both listed in the array of _Processing Element Statistics_ in the Data Record AD Debug Panel. The _State_ of the IO Plugins should be _Processing_ and no errors should be listed.

Verify the file(s) are created as expected in the specified directory.
