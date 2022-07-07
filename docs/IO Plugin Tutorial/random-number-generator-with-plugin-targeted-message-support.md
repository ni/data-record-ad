# Overview  
This is part 5 of a five part tutorial. It contains instructions on modifying the original _RandomNumberGenerator_ IO plugin to support plugin-targeted messages.  Four different messages will be supported:

|messageName|details|Description|
|--|--|--|
|recordON|N/A|Instructs plugin to pass through data for recording|
|recordOFF|N/A|Instructs plugin to not pass through data so data does not get saved|
|randomMIN|{"MIN":0}|Updates the Lower Bound or minimum random number generated|
|randomMAX|{"MAX":100}|Updates the Upper Bound or maximum random number generated|

[Return to IO Plugin Tutorial](../IO%20Plugin%20Tutorial.md#io-plugin-tutorial)

# Modify IO Plugin to Support a Plugin-Targeted gRPC Message
## Open Project
Open the _RandomNumberGenerator_ project created in the first tutorial.  It should be located in the _\<Checkout Directory>/IO Plugins/RandomNumberGenerator_ directory.

## Update States
### Handle Message
### Process
## Build IO Plugin
## Test IO Plugin 



