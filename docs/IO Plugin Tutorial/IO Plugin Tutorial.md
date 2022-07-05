# IO Plugin Tutorial  
The purpose of this tutorial is to walk new IO plugin developers through the creation of three different IO plugins that can be run without hardware.  Once the tutorial is complete, developers will have three separate IO plugins that can be used together with Data Record AD.

<img src="https://user-images.githubusercontent.com/15633959/154979199-e8fb5515-37d2-403d-aa80-6da8e54fdd91.png" width="300">

The first plugin will generate random numbers.  The second plugin will save the generated numbers to disk as a text file.  The third plugin can be injected between the random number generator and the text file logger and it will allow the user to scale the random numbers.

As developers move through the tutorial they should note that less detailed instructions are provided for the second and third plugins - this is intentional.  If there are questions, the instructions for the first tutorial should be referenced.

# Table of Contents
1. [Update IO Plugin Project Template](./IO%20Plugin%20Tutorial.md#update-io-plugin-project-template)
1. [Create a Branch](./IO%20Plugin%20Tutorial.md#create-a-branch)
1. [Create Data Source IO Plugin - Random Number Generator](./IO%20Plugin%20Tutorial.md#create-data-source-io-plugin---random-number-generator)
1. [Create Data Sink IO Plugin - Text File](./IO%20Plugin%20Tutorial.md#create-data-sink-io-plugin---text-file)
1. [Create Data Processing IO Plugin - Scaling Factor](./IO%20Plugin%20Tutorial.md#create-data-processor-io-plugin---scaling-factor)
1. [Create Data Publisher IO Plugin - gRPC](./IO%20Plugin%20Tutorial.md#create-data-publisher-io-plugin---grpc)
1. [Modify IO Plugin to Support Plugin-Targeted gRPC Messages]([./IO%20Plugin%20Tutorial.md#modify-io-plugin-to-support-a-plugin-targeted-grpc-message)
1. [Additional Developer Features](./IO%20Plugin%20Tutorial.md#additional-developer-features)


## Update IO Plugin Project Template
To assist developers with creating IO plugins, a LabVIEW Project Template has been created.  This project template is installed with the Data Record AD Development Suite.

The source code for the project template also exists within this GitHub repository.  It is a good idea to update your project template from GitHub to ensure you are starting with the latest template code.

Navigate to /../IO Plugin Creation Tool.  You'll find the necessary files and a python script that can be used to copy them to the appropriate location.

![image](https://user-images.githubusercontent.com/15633959/154981043-fc8a9235-24d5-463d-92d9-a583ac46eaac.png)

To use the python script, simply open a command prompt and type the script name.  Use _-f_ to force the script to copy.  You must have python installed to use the script.  For more information on installing/using python please visit https://www.python.org/.

<img src="https://user-images.githubusercontent.com/15633959/154981599-a488b1dd-7108-46d8-b802-3ac69c51abdc.png" width="1000">

[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Create a Branch
Before creating any plugins, if you want to work within the Data Record AD repository, it is necessary to create a branch to work in.  The recommended branch name for this tutorial is _users/\<yourname>/sandbox/tutorial._  If this is your first time creating a branch, you may find [this tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) helpful.

[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Create Data Source IO Plugin - Random Number Generator
### Create Project
Launch LabVIEW and select _Create Project_:

<img src="https://user-images.githubusercontent.com/15633959/154990689-c1e1e95a-d72f-4759-8514-5ed28a276732.png" width="600">
  
Select _ADAS IO Plugin Template_ from the list.
  
<img src="https://user-images.githubusercontent.com/15633959/154991045-051586f8-3c22-4972-b5e4-563f09f9e91a.png" width="600">

Complete the information for the template as provided.  The _IO Plugin Name_ should be _RandomNumberGenerator_.  The _IO Plugin Directory_ should be _<Checkout Directory)/IO Plugins/RandomNumberGenerator_.  It is also a good idea to update the icon to be more representative of the plugin purpose.  When you are finished updating the information, select _Finish_.

<img src="https://user-images.githubusercontent.com/15633959/154993224-3c26ad00-a073-49da-a570-4de32a146a9a.png" width="800">

LabVIEW will now generate your project from the template code.  A progress bar will appear showing the current status:
  
<img src="https://user-images.githubusercontent.com/15633959/155002416-24d5c8bd-df32-4a47-87fe-ec3d194d197a.png" width="800">

When the project is completely generated, a Windows Explorer window will open at the location specicified within the project template:  
<img src="https://user-images.githubusercontent.com/15633959/155002647-97bed789-8c7e-424b-91ac-835cc45d9695.png" width="600">

### Edit IO Plugin Configuration Parameters
Open the generated project.  Navigate down to the Configuration.ctl type definition (PE >> RandomNumberGenerator.lvlib >> RandomNumberGenerator.lvclass >> Types).  Modify the type definition to have four numeric controls as shown here:
  
![image](https://user-images.githubusercontent.com/15633959/155005939-c421a0d3-e5e8-4105-a198-0c3651ef40c4.png)

Two of these configuration parameters were selected because we plan to use the _Random Number (range).vi_ from the Numeric palette to be able to generate random doubles:
  
![image](https://user-images.githubusercontent.com/15633959/155004828-9ae3b8bc-2dee-48ac-9891-f1a42b9dbdfb.png)

### Set Default Configuration Parameters  
Setting the current values to default for the type definition controls does not set the default values for the controls within the Data Record AD System Configuration Editor.  To set default values for the controls you need to edit _Default Configuration Parameters.vi_.  The default values must be set on the block diagram - there is a note on the front panel to remind the user.
  
![image](https://user-images.githubusercontent.com/15633959/176756576-7a1601a3-4c89-4a07-a0e2-5a82161fe553.png)
 
  
### Update Mutate Configuration to Current
Removing the string from the type definition will cause the _Mutate Configuration to Current.vi_ to break.
  
![image](https://user-images.githubusercontent.com/15633959/155006182-eb805d84-166c-4fb6-bf09-7e6a2138a159.png)

<img src="https://user-images.githubusercontent.com/15633959/155187451-624f328c-c056-42f8-aa62-2e0982c9c083.png" width="1000">
  
The purpose of this VI is to mutate configurations if they are changed in future releases of the plugin.  For example, if the configuration used to be a full file path but it changes to a directory and file name, the original file path could be split into two components and the old configuration would work with the updated plugin.
  
In our case, we have not released the plugin so we do not need to worry about mutating the configuration.  The simplest thing to do right now would be to simply pass through the cluster:
  
<img src="https://user-images.githubusercontent.com/15633959/155187904-dff1afa7-677d-4cb1-8652-84b5ef83527b.png" width="1000">

### Update States
Expanding the states folder will show the core states the IO plugin will cycle through.  The project will have the states listed alphabetically but some developers find it helpful to rearrange them to better correlate to their order of operation:
  
<img src="https://user-images.githubusercontent.com/15633959/155188525-423e2b7f-38cd-4d00-b432-fa8f296f517e.png" width="800">

#### Initialize
Initialize is the first state an IO plugin executes.  It's purpose is to initialize global lifetime resources for the plugin.  If your plugin involves hardware you may open a reference to the hardware in Initialize.
  
![image](https://user-images.githubusercontent.com/15633959/155189729-8f141733-c2f0-46f3-8012-afabcc3fd156.png)

Typically the timing parameters of the _Process_ state are set in _Initialize_ unless the timing is user configurable.  Timing options include Periodic, Immediate or OnDataReday. Triggered is not implemented for IO Plugins and should not be used.
  
In the plugin we are developing, we allow the user to set the update rate for periodic generation.  We should remove the _Write Timing Parameters.vi_ as we need to read our configuration before we can set the value.
  
![image](https://user-images.githubusercontent.com/15633959/155191068-241b9adc-4698-41e9-bd5f-2ef1475b8fcd.png)

#### Read Parameters
It is rare that this state requires any modifications.  It simply populates the IO plugin class with the configuration data.  We will not make any changes.
  
![image](https://user-images.githubusercontent.com/15633959/155192964-2d2eab2a-9171-46ee-8c59-72e361b99d51.png)
  
#### Configure Session
All of the configuration parameters have been populated into the IO plugin class.  We can now configure the timing parameters using the configuration parameter.  The _Write Timing Paramters.vi_ can be found in Dependencies >> vi.lib >> PluginSDK.lvlibp >> Processing Element.lvclass >> Properties >> Timing Parameters:

![image](https://user-images.githubusercontent.com/15633959/155196177-91879c25-4d1c-44e4-bad0-90924564a4b0.png)

You may also find it easier to navigate to the PPL on disk: C:\Program Files\National Instruments\LabVIEW 2020\vi.lib\FlexLogger\SDK\PluginSDK.lvlibp
 
Unbundle the _Update Rate (ms)_ from the configuration and bundle it into _Timing Period (ms)_:

![image](https://user-images.githubusercontent.com/15633959/155197870-db047b0d-e038-4d2c-8a7a-1c7fbded79d9.png)

#### Process
The majority of your plugin behavior is typically implemented within the _Process_ state.  Process runs repeatedly in a loop until Data Record AD is shutdown.  The loop rate depends upon your timing parameters previously set.  The template code contains helpful bookmarks discussing _Custom Data_ but no actual code.
  
![image](https://user-images.githubusercontent.com/15633959/155199131-e7e2b189-9b37-4508-8410-465d4e879bac.png)

For our plugin, we want to generate user specified _n_ random numbers between the user specified lower and upper bound.  We will use the _Random Number (Range).vi_ with type _DBL_ to generate these numbers.  We need to write these numbers to the Data Record AD engine.  The _Write ADAS Data.vi_ polymorphic custom data VI should be used to write the data.  It can be found in _C:\Program Files\National Instruments\LabVIEW 2020\vi.lib\ADAS Record\CustomDataTypes_.  We will use the _Double_ type.
  
![image](https://user-images.githubusercontent.com/15633959/155559435-22a9decf-f67e-499e-952b-b185332044ef.png)

One important input to the _Write ADAS Data.vi_  is the _Terminal_ input.  We have a constant "Output" here.  This is the text that will appear in the Data Record AD System Configuration Editor.  You can change the _Terminal_ name as shown below:

<img src="https://user-images.githubusercontent.com/15633959/155561982-b06662fe-344c-4a07-a52a-b9ead3c28b87.png" width="600">

If you change the _Terminal_ name to anything other than the default you will need to update _RandomNumberGenerator.lvlib:RandomNumberGenerator Controller.lvclass:Read Output Streams.vi_:
  
![image](https://user-images.githubusercontent.com/15633959/155562804-8445a207-18ef-40c4-a370-6c4c4c5a15c4.png)

<img src="https://user-images.githubusercontent.com/15633959/155563213-51f3553a-9ce0-4882-b24b-fa4ab907ba98.png" width="800">
 
#### Cleanup Session
This is the state that runs before reconfigure and/or after process while shutting down.  It is where you should close/cleanup any session resources that were opened in _Configure Session_.  No changes are necessary to _Cleanup Session_ for our plugin.  

![image](https://user-images.githubusercontent.com/15633959/155563913-7a1c308e-4968-42a7-994c-ac2d5a5abaca.png)

#### Finalize
This is the final state that runs before Data Record AD shuts down.  It is where you should close/cleanup any resources that were opened in _Initialize_.  No changes are necessary to _Finalize_ for our plugin.
  
![image](https://user-images.githubusercontent.com/15633959/155564078-727fc455-8f05-4e26-b5bd-95ea6e3b7d0c.png)

#### Handle Message
This state handles asynchronous plugin-targeted gRPC messages.  The Data Record AD engine simply forwards incoming messages to all plugins and it is up to each plugin to handle incoming messages.  The initial tutorial plugins do not utilize plugin-targted gRPC messages.

### Build IO Plugin 
Expand the Build Specifications in the LabVIEW project.  The IO Plugin Project Template includes a predefined build specification for a Packed Project Library.  The build specification does not need any modifications.  Changing names may actual result in an unfunctional plugin.  

The destination directory is set to be the default directory for IO plugins.  This makes it easy to test your plugin immediately.  This field could be modified if you are not working on a system with Data Record AD but wish to build a plugin for later installation.

![image](https://user-images.githubusercontent.com/15633959/176742219-74ae714e-39d5-416d-ba1e-d8b44b5b763b.png)

One modification that may be required is to add dependencies. If your plugin depends upon an exteral DLL or other file, you will need to add it to your project and specify it in _Source Files_ as an always included file.
  
Right-click on the specification and select _Build_.

![image](https://user-images.githubusercontent.com/15633959/176740984-40480d7c-c721-408d-8a8d-25855b104bf6.png)

### Test IO Plugin
Launch the Data Record AD System Configuration Editor.  Create a new project.  Open the project's ADAS System Configuration.  From the IO Plugin palette, find your recently created _Random Number Generator_ IO plugin and add it to the configuration. 
  
![image](https://user-images.githubusercontent.com/15633959/176757516-664ade01-8890-4440-a5a8-3f516b4adf6a.png)

In the configuration pane on the right verify that the default values you entered for the IO plugin configuration parameters are correct.  You can rename the plugin (i.e _New plugin instance_ --> _Random Number_), modify the configuration parameters and/or edit the description if you'd like.
  
Generate the configuration.  You can do this by switching from the Item to the Document pane in the configuration pane or by simple selecting the _Generate Configuration_ shortcut.

![image](https://user-images.githubusercontent.com/15633959/176758274-045dd93f-5928-4114-929b-271bfd734cfc.png)

Launch Data Record AD.  You should be able to see the IO Plugin name listed on the main Data Record AD application user interface.  You should also see it listed in the array of _Processing Element Statistics_ in the Data Record AD Debug Panel.  The _State_ of the IO Plugin should be _Processing_ and _Channel Segement Bytes_ and _Total Memory (MB)_ should not be static.
  
![image](https://user-images.githubusercontent.com/15633959/176759039-20b83c31-19b9-4b15-8d6c-236571c8b37e.png)

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


[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Create Data Processor IO Plugin - Scaling Factor
### Create Project
### Edit IO Plugin Configuration Parameters
### Set Default Configuration Parameters  
### Update Mutate Configuration to Current  
### Update States
#### Initialize
#### Read Parameters
#### Configure Session
#### Process
#### Cleanup Session
#### Finalize
#### Handle Message
### Build IO Plugin
### Test IO Plugin 

[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Create Data Publisher IO Plugin - gRPC 
### Create Project
### Edit IO Plugin Configuration Parameters
### Set Default Configuration Parameters  
### Update Mutate Configuration to Current  
### Update States
#### Initialize
#### Read Parameters
#### Configure Session
#### Process
#### Cleanup Session
#### Finalize
#### Handle Message
### Build IO Plugin
### Test IO Plugin 

[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Modify IO Plugin to Support a Plugin-Targeted gRPC Message
### Open Project
### Update States
#### Handle Message
#### Process
### Build IO Plugin
### Test IO Plugin 

[Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents)

## Additional Developer Features
### Icons
If no icons are specified, the default plugin icon is used:
  
![image](https://user-images.githubusercontent.com/15633959/176736748-6c0fc8fe-0d2c-44e1-9dd0-cf43d901ef09.png)

Users can also specify custom icons such as this:

![image](https://user-images.githubusercontent.com/15633959/176736857-363df4f0-60f5-48d4-bf20-fadfa5c1f82d.png)

To use a custom icon, create a 40x40 pixel image and save it as PluginIcon.png.  Colors and transparency are supported.  The file needs to reside within the deployed plugin directory:
 
 _C:\Users\Public\Documents\National Instruments\ADAS\Plugins\IOPlugins\\<PluginName>\PluginIcon.png_
  
 [Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents) 