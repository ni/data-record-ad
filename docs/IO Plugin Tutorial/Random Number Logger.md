# IO Plugin Tutorial  
This is part 2 of a five part tutorial.  

[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Create Data Sink IO Plugin - Text File
### Create Project
Launch LabVIEW and create a new _ADAS IO Plugin Template_ project. Complete the information for the template as provided. The IO Plugin Name should be RandomNumberLogger. The IO Plugin Directory should be <Checkout Directory)/IO Plugins/RandomNumberLogger. It is also a good idea to update the icon to be more representative of the plugin purpose. When you are finished updating the information, select Finish.  

![image](https://user-images.githubusercontent.com/15633959/176764681-25bb4e67-04ba-41d3-889c-61b45672a219.png)

### Edit IO Plugin Configuration Parameters
Open the generated project. Navigate down to the Configuration.ctl type definition (PE >> RandomNumberLogger.lvlib >> RandomNumberLogger.lvclass >> Types). Modify the type definition to have four controls as shown here:
![image](https://user-images.githubusercontent.com/15633959/176767166-3fe47acb-a6e0-44ff-8234-322173eeb1a2.png)

Values for the _File Split_ enum:<br>
0: None <br>
1: Time <br>
2: Size <br>

Note: To complete the tutorial in less time, the file split functionality may be omitted.

### Set Default Configuration Parameters 
Edit the default configuration parameters (_RandomNumberLogger.lvlib:RandomNumberGenerator.lvclass:Default Configuration Parameters.vi_):<br>
Base File Name: Random.txt<br>
File Directory: C:\Data<br>
File Split: Time<br>
Split Time/Size (s/MB): 0.5<br>

### Update Mutate Configuration to Current
If the original string control was simply repurposed for the Base File Name, it is likely that _Mutate Configuration to Current_ is not broken.  If you removed it and/or added the controls in a different order you may need to fix this VI before building the plug-in.

### Update States
#### Initialize
This plugin is intended to save data to disk so the timing parameters for this plugin should reflect that behavior.  In _Initialize_, update the _Timing Method_ to be _On Data Ready_.
![image](https://user-images.githubusercontent.com/15633959/176770255-df26e59b-3a8c-4ff2-bae7-74258916fd58.png)

#### Read Parameters
No changes required for _Read Parameters_.

#### Configure Session
This is where the majority of the initialization code needs to happen.  The first file split path will be built and a reference to that file will be opened. If file split is by time, an intial time should be noted and saved for future use...the big question is what do we do with this data?
![image](https://user-images.githubusercontent.com/15633959/176774506-aa54eae1-2482-48a9-9141-ea242621f1ab.png)

This data needs to be stored as part of the class private data.  Back in the LabVIEW project, open _RandomNumberLogger.ctl_ and add the following three controls:
![image](https://user-images.githubusercontent.com/15633959/176775005-37b9d58b-eef5-47e9-8d0c-e58bfcb70202.png)

The _Configure Session_ VI can also be updated to utilize the new class private data.  Set the _index_ value to _1_ - more information on this value will be discussed in subsequent steps.
![image](https://user-images.githubusercontent.com/15633959/176775609-6d7f733b-80c6-4ecc-b2e5-00321a524330.png)


#### Process
#### Cleanup Session
#### Finalize
#### Handle Message
No changes required for _Handle Message_.
### Build IO Plugin
### Test IO Plugin  


