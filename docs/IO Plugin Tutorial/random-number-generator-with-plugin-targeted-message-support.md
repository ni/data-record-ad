# Overview  
This is part 5 of a five part tutorial. It contains instructions on modifying the original _RandomNumberGenerator_ IO plugin to support plugin-targeted messages.  Four different messages will be supported:

|messageName|details|Description|
|--|--|--|
|recordON|N/A|Instructs plugin to pass through data for recording|
|recordOFF|N/A|Instructs plugin to not pass through data so data does not get saved|
|randomMIN|{"MIN":0}|Updates the Lower Bound or minimum random number generated|
|randomMAX|{"MAX":100}|Updates the Upper Bound or maximum random number generated|
|getLast|N/A|Returns latest random number via _DataRecordGrpcConsoleTopic_|

[Return to IO Plugin Tutorial](../IO%20Plugin%20Tutorial.md#io-plugin-tutorial)

# Modify IO Plugin to Support a Plugin-Targeted gRPC Message
## Open Project
Open the _RandomNumberGenerator_ project created in the first tutorial.  It should be located in the _\<Checkout Directory>/IO Plugins/RandomNumberGenerator_ directory.

## Update States
### Handle Message
Until now, _Handle Message_ has been ignored.  This state actually runs asynchronously to the other states so it can handle incoming messages.  The Data Record AD engine forwards any gRPC messages sent with the topic _DataRecordGrpcPluginTopic_.  As shown below the template code already separates the _messageName_ and the _details_:  

![image](https://user-images.githubusercontent.com/15633959/177852440-ddba09ef-49a1-4706-93f7-140116a85b12.png)

Before we implement any of the messages, we need to think through the new behavior we are adding and whether any information should be added to the class private data.
![image](https://user-images.githubusercontent.com/15633959/177856729-dfaa613c-e34d-41a5-ac45-ff1b52fb7045.png)

For record, we will need a Boolean value to store whether the user has sent _recordON_ or _recordOFF_.  For updating the lower and upper boundaries we do not need to make any modifications - we can update the information already in the _Configuration_ cluster.  For reading the latest value, we will need a control to store that value:

![image](https://user-images.githubusercontent.com/15633959/177856928-02252767-1d08-4697-adc0-f6f5b5c5d3ed.png)

#### recordON
For the _recordON_ message, we want to be able to tell the plugin to pass data out to be saved.  Duplicate the _default_ case in the case structure and name it _recordON_. Add a _Bundle by Name_ and wire a constant _TRUE_ to _Record_ as shown below:

![image](https://user-images.githubusercontent.com/15633959/177857116-1a3e04a1-51dd-4910-98b5-22b109089ed7.png)

#### recordOFF
For the _recordOFF_ message, we want to do exactly the opposite of _recordON_.  The simplest way to do this is to duplicate the _recordON_ case, name it _recordOFF_ and modify the constant to be _FALSE_:

![image](https://user-images.githubusercontent.com/15633959/177858013-63538342-1c74-4975-983f-b6b4e87e68d1.png)

#### randomMIN
For _randomMIN_ we want to allow users to update the minimum boundary of the random number being generated.  That means that in addition to the _messageName_ we have _details_ we will need to manage.  _Details_ is a JSON string derived from a cluster.  This cluster can contain any information required for the message.  In our use case it is a double labeled "MIN".  Let's first take a look at how the JSON would be sent so we know how to interpret it:

![image](https://user-images.githubusercontent.com/15633959/177859696-e18d8515-e541-4108-bfc1-e91f0f4f1fd8.png)

Back in _Handle Message_ we can start by duplicating the _Default_ case and naming it _randomMIN_.  We will need to take the incoming JSON for _details_ and convert it back to our expected cluster.  We will take that result and update the Lower Bound Configuration value:

![image](https://user-images.githubusercontent.com/15633959/177860589-af6689f8-f4fb-4bab-b17e-6969b8c8c196.png)

#### randomMAX
The _randomMAX_ message is very similar to _randomMIN_ except we are updating the upper bound by using an incoming "MAX" value.  It is easiest to duplicate the _randomMIN_ case and name it _randomMAX_.  We can update the "MIN" cluster to be "MAX" and update the bundle by name to update teh _Configuration.LowerBound_ value:

![image](https://user-images.githubusercontent.com/15633959/177861055-cdac6238-04af-4bee-87bd-56c0a8edf018.png)

#### getLast
Our final message, _getLast_, should return the last random number that was generated.  Duplicate the _Default_ case and name it _getLast_.  Unbundle and access the _LastValue_ and build it into a cluster before flattening to JSON which is sent out as the _Message Response_:

![image](https://user-images.githubusercontent.com/15633959/177862617-721e0762-b6fa-4d1b-836a-81087cd182cb.png)

### Process
Now we have all of the messages handled but we need to update _Process_ to implement some of the intended behaviors.  Let's start by looking at our current implementation of _Process_:

![image](https://user-images.githubusercontent.com/15633959/177862963-c30f708e-2fe3-454a-b52f-d64064166fe3.png)

We do not need to make any modifications for the _randomMIN_ and _randomMAX_ messages to work as the current code already uses those values.  As we are updating them in the class private data of _Handle Message_, _Process_ will immediately use the new values as they are udpated.

To get the latest value, we need to write the latest generated value to the _LastValue_ stored within the class private data as shown below:

![image](https://user-images.githubusercontent.com/15633959/177863698-73a3bab8-a4b2-4d0f-b58c-450f0277072c.png)

As this IO plugin doesn't actually store the random numbers to a file (that happens in the _RandomNumberLogger_), we will do a workaround to handle _recordON_ and _recordOFF_.  We will wrap _Write ADAS Data_ in a case structure.  If the user has enabled recording by sending _recordON_ we will write the data to the engine.  If they send _recordOFF_ the data will not be written to the engine.  

![image](https://user-images.githubusercontent.com/15633959/177866945-641dd6f9-83f1-4ddc-9fd1-e54e2f684908.png)

Note that this will also prevent the data from being published via _RandomNumberPublisher_ and scaled with our _RandomNumberScalingFactor_.  Ideally the _recordON/recordOFF_ messages would be handled within the IO plugin that writes files to disk.  For simplicity we are implementing different message types within a single plugin.  

Secondly, another option would be to send a single message named _Record_ and send true/false within the details.  Both implementations are valid.

## Build IO Plugin
Expand the Build Specifications in the LabVIEW project. Right-click on the specification and select Build.

## Test IO Plugin 
Open the System Configuration Editor.  The configuration from the last tutorial will work to show our updated functionality.

![image](https://user-images.githubusercontent.com/15633959/177661849-a3115b27-4ae3-457e-8a08-91c0dbe79325.png)

Generate the configuration and launch Data Record AD. You should be able to see the IO Plugin names listed on the main Data Record AD application user interface. You should also see them listed in the array of _Processing Element Statistics_ in the Data Record AD Debug Panel. The _State_ of the IO Plugins should be _Processing_ and no errors should be listed.

We will need to connect to Data Record AD as a client to send the plugin-targeted messages we've defined.
