# IO Plugin Tutorial  
The purpose of this tutorial is to walk new IO plugin developers through the creation of three different IO plugins that can be run without hardware.  Once the tutorial is complete, developers will have three separate IO plugins that can be used together with Data Record AD.

<img src="https://user-images.githubusercontent.com/15633959/154979199-e8fb5515-37d2-403d-aa80-6da8e54fdd91.png" width="300">

The first plugin will generate random numbers.  The second plugin will save the generated numbers to disk as a text file.  The final plugin can be injected between the random number generator and the text file logger and it will allow the user to scale the random numbers.


## Update IO Plugin Project Template
To assist developers with creating IO plugins, a LabVIEW Project Template has been created.  This project template is installed with the Data Record AD Development Suite.

The source code for the project template also exists within this GitHub repository.  It is a good idea to update your project template from GitHub to ensure you are starting with the latest template code.

Navigate to /../IO Plugin Creation Tool.  You'll find the necessary files and a python script that can be used to copy them to the appropriate location.

![image](https://user-images.githubusercontent.com/15633959/154981043-fc8a9235-24d5-463d-92d9-a583ac46eaac.png)

To use the python script, simply open a command prompt and type the script name.  Use _-f_ to force the script to copy.  You must have python installed to use the script.  For more information on installing/using python please visit https://www.python.org/.

<img src="https://user-images.githubusercontent.com/15633959/154981599-a488b1dd-7108-46d8-b802-3ac69c51abdc.png" width="1000">


## Create a Branch
Before creating any plugins, if you want to work within the Data Record AD repository, it is necessary to create a branch to work in.  The recommended branch name for this tutorial is _users/<yourname>/sandbox/tutorial._  If this is your first time creating a branch, you may find [this tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) helpful.


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

### Update Mutate Configuration to Current VI
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
The majority of your plugin behavior is typically implemented within the _Process_ state.
  
![image](https://user-images.githubusercontent.com/15633959/155199131-e7e2b189-9b37-4508-8410-465d4e879bac.png)

  
  
#### Cleanup Session

#### Configure Session


  
## Create Data Sink IO Plugin - Text File

## Create Data Processor IO Plugin - Scaling Factor


## Modify Random Number Generator to Support a Plugin-Targeted gRPC Message

