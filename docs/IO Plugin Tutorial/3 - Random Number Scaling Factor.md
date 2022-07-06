# Overview
This is part 3 of a five part tutorial.  It contains instructions on creating an IO plugin that scales an incoming number and returns the original number and the scaled number.

[Return to IO Plugin Tutorial](./IO%20Plugin%20Tutorial.md#io-plugin-tutorial)

# Create Data Processor IO Plugin - Scaling Factor

## Create Project
Launch LabVIEW and create a new ADAS IO Plugin Template project. Complete the information for the template as provided. The IO Plugin Name should be _RandomNumberScalingFactor_. The IO Plugin Directory should be _\<Checkout Directory>/IO Plugins/RandomNumberScalingFactor_. It is also a good idea to update the icon to be more representative of the plugin purpose. When you are finished updating the information, select Finish.

![image](https://user-images.githubusercontent.com/15633959/177416334-f0acc7ec-9a0c-4a68-b5f9-608a685c0c0e.png)

## Edit IO Plugin Configuration Parameters
Open the generated project. Navigate down to the Configuration.ctl type definition (PE >> RandomNumberScalingFactor.lvlib >> RandomNumberScalingFactor.lvclass >> Types). Modify the type definition to have one control as shown here:

![image](https://user-images.githubusercontent.com/15633959/177417260-6e37ee04-59fb-4fc1-b048-16e38b78d6a6.png)

## Set Default Configuration Parameters  
Edit the default configuration parameters (_RandomNumberScalingFactor.lvlib:RandomNumberScalingFactor.lvclass:Default Configuration Parameters.vi_):
<br>Scaling Factor: 10

## Update Mutate Configuration to Current  
Removing the string from the type definition will cause the _Mutate Configuration to Current.vi_ to break.  In our case, we have not released the plugin so we do not need to worry about mutating the configuration. The simplest thing to do right now would be to simply pass through the cluster.  See the first IO plugin tutorial, Random Number Generator, for more details.

## Modify Output Streams
In addition to passing through the scaled factor, it might be a good idea to pass through the original value.  This is also an opportunity to showcase how to output more than one result from an IO plugin.  

Open _Read Output Streams.vi_(_RandomNumberScalingFactor.lvlib:RandomNumberScalingFactor Controller.lvclass:Default Configuration Parameters.vi_).  Modify the first element to be _Original_ instead of _Output_.  Add an additional element to the array and name it _Scaled_.  Be sure to include a value for the _Channel_ array or you will have errors.

![image](https://user-images.githubusercontent.com/15633959/177420022-e16a92e3-9ea2-48ef-8734-2185c231ee66.png)

## Update States
### Initialize
This plugin is intended to read numeric values and modify them before passing them on.  The timing parameters for this plugin should reflect that behavior. In _Initialize_, update the _Timing Method_ to be _On Data Ready_.

### Read Parameters
No changes required for _Read Parameters_.

### Configure Session
No changes required for _Configure Session_.

### Process
In _Process_ we want to read the incoming number and pass it out without any modifications and also scale the value before passing it back out.  It is important to note that the _Terminal Names_ should be updated to match the _Output Streams_ specified earlier, _Original_ and _Scaled_.

![image](https://user-images.githubusercontent.com/15633959/177421169-fdec1555-9db4-487f-8529-fb533f1e1c30.png)


### Cleanup Session
No changes required for _Cleanup Session_.

### Finalize
No changes required for _Finalize_.

### Handle Message
No changes required for _Handle Message_.

## Build IO Plugin
Expand the Build Specifications in the LabVIEW project. Right-click on the specification and select Build.

## Test IO Plugin 
Launch the Data Record AD System Configuration Editor. Open the ADAS project created in the first tutorial. Open the project's ADAS System Configuration. From the IO Plugin palette, find your recently created Random Number Scaling Factor IO plugin and add it to the configuration. 

Disconnect the output of the _Random Number Generator_ from the input of the _Random Number Logger_.  Connect the output of the _Random Number Generator_ to the input of the _Random Number Scaling Factor_.  Connect each output from the _Random Number Scaling Factor_ to inputs of two _Random Number Logger_ IO plugins.  Be sure to modify the file name to be different for each _Random Number Logger_ IO plugin:

![image](https://user-images.githubusercontent.com/15633959/177422660-f5c520ab-1d03-4e2e-a97b-dde36baee31a.png)

Generate the configuration and launch Data Record AD. You should be able to see the IO Plugin names listed on the main Data Record AD application user interface. You should also see them listed in the array of _Processing Element Statistics_ in the Data Record AD Debug Panel. The _State_ of the IO Plugins should be _Processing_ and no errors should be listed.

Verify the files are created as expected in the specified directory.

Additional Note:
The Data Record AD System Configuration Editor and Data Record AD engine support the _branching_ of data.  This configuration yields the same results as the above configuraton:
![image](https://user-images.githubusercontent.com/15633959/177422984-85824f57-60e7-4573-b1bb-75659b7e3e37.png)


