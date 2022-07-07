# Overview  
This is part 4 of a five part tutorial.  It contains instructions on creating an IO plugin that publishes the random number as a gRPC message.

[Return to IO Plugin Tutorial](../IO%20Plugin%20Tutorial.md#io-plugin-tutorial)

# Create Data Publisher IO Plugin - gRPC 
## Create Project
Launch LabVIEW and create a new ADAS IO Plugin Template project. Complete the information for the template as provided. The IO Plugin Name should be _RandomNumberPublisher_. The IO Plugin Directory should be _\<Checkout Directory>/IO Plugins/RandomNumberPublisher_. It is also a good idea to update the icon to be more representative of the plugin purpose. When you are finished updating the information, select Finish.

![image](https://user-images.githubusercontent.com/15633959/177646655-228974a4-97da-4f29-aee0-efe35082d284.png)

## Edit IO Plugin Configuration Parameters
Open the generated project. Navigate down to the Configuration.ctl type definition (PE >> RandomNumberPublisher.lvlib >> RandomNumberPublisher.lvclass >> Types). Modify the type definition to have three controls as shown here:

![image](https://user-images.githubusercontent.com/15633959/177657499-5726d8f0-ceff-4d47-a69d-385881703640.png)

## Set Default Configuration Parameters
Edit the default configuration parameters _(RandomNumberPublisher.lvlib:RandomNumberPublisher.lvclass:Default Configuration Parameters.vi_): 
<br>Server Address: localhost
<br>Server Port: 50219 (or any unused port on your system)
<br>Topic Name: RandomData

## Update Mutate Configuration to Current 
If the original string control was simply repurposed for the _Server Address_, it is likely that Mutate Configuration to Current is not broken. If you removed it and/or added the controls in a different order you may need to fix this VI before building the plug-in.

## Update States
### Initialize
This plugin is intended to read numeric values and publish them via a gRPC server. 

The timing parameters for this plugin should reflect that behavior. In Initialize, update the Timing Method to be On Data Ready.

![image](https://user-images.githubusercontent.com/15633959/177658231-16e44cfc-478f-429c-8ee4-2f2f6680078c.png)

We can also initialize the gRPC server and store the ServerRef in the class private data as shown.  Note that the _LVCreateServer.vi_ and _ServerRef_ type definition are part of the _DatastreamGrpc.lvlib_ which can be found in _\<vi.lib>\DatastreamGrpc_ directory.

![image](https://user-images.githubusercontent.com/15633959/177658308-80e1c0cc-a347-43c6-8461-394dd77b6b7e.png)

### Read Parameters
No changes required for _Read Parameters_.

### Configure Session
In _Configure Session_ we will want to start our server.  One of the inputs to _LVStartServer.vi_ is the server address.  It is expected to be a string in the format x.x.x.x:yyyyy where x is the IP address of the server and y is the port.  No verification of the user configurable server address/port is performed here but it is recommended to verify user configurable items such as this in real plugins.

![image](https://user-images.githubusercontent.com/15633959/177658836-c5297f46-eaee-44b9-a587-c123eba4bce6.png)

### Process
In _Process_ we need to publish all incoming data to the user specified topic.  First we need to read the incoming random numbers using the Custom Data polymoprhic VI.  Next we can use the _Serialize ADAS Data_ VI to flatten the data to a string.  Finally we publish the data to the user specified topic.

![image](https://user-images.githubusercontent.com/15633959/177659600-491c2bd6-7878-4e89-b3f9-9ac46bdc6762.png)

### Cleanup Session
In _Cleanup Session_ we should do the opposite of what we did in _Configure Session_.  In our case we will want to stop the server.

![image](https://user-images.githubusercontent.com/15633959/177660121-f9b2ea5e-6a89-42dd-803c-47a53d64083b.png)

### Finalize
In _Finalize_ we should do the opposite of waht we did in _Initialize_.  In our case we will want to destroy the server.

![image](https://user-images.githubusercontent.com/15633959/177660260-659cdb6b-eecf-43cb-8b4a-6826f0f50975.png)

### Handle Message
No changes required for _Handle Message_.

## Build IO Plugin
This IO plugin actually has additional dependencies.  _DatastreamGrpc.lvlib_ uses two DLLs which can be found in _\<vi.lib>\DatastreamGrpc\External_.  These files need added to your project and to the build specification.  Once the necessary modifications have been made to the project and build specification, click _Build_.

![image](https://user-images.githubusercontent.com/15633959/177660781-29668f57-21cf-4918-a87e-909025451868.png)

## Test IO Plugin 
Launch the Data Record AD System Configuration Editor. Open the ADAS project modified in the last tutorial. Open the project's ADAS System Configuration. From the IO Plugin palette, find your recently created Random Number Publisher IO plugin and add it to the configuration.

Branch the wire from the output of the _Random Number Generator_ and connect it to the input of the _Random Number Publisher_.  Hint: You can branch the wire by pressing the _Control_ key.

![image](https://user-images.githubusercontent.com/15633959/177661849-a3115b27-4ae3-457e-8a08-91c0dbe79325.png)

Verify the configuration settings for the _Random Number Publisher_ - the default values should be acceptable.

Generate the configuration and launch Data Record AD. You should be able to see the IO Plugin names listed on the main Data Record AD application user interface. You should also see them listed in the array of _Processing Element Statistics_ in the Data Record AD Debug Panel. The _State_ of the IO Plugins should be _Processing_ and no errors should be listed.

To verify the gRPC publishing functionality you will need a gRPC client.  It isn't too difficult to create a simple example such as the one shown below using the _DatastreamGrpc.lvlib_ client VIs.  It is important to note that the gRPC client must be started after the server is already running or an error will occur.

![image](https://user-images.githubusercontent.com/15633959/177662353-c1e70cb8-bf27-4dd3-92a9-c0b730242145.png)


