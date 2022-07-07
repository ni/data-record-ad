# Design and Style
  
## Recommendations
	- PEs should be as small as possible but no smaller
	- Rather than targeting single responsibility per PE, consider single use case
	- Multiple PEs that only differ in slight ways are superior to one PE that has a very complex set of configuration parameters
	- PEs should have behavior that is easily testable, even if those tests require real hardware
	- PEs with highly specific logging requirements should handle logging within the PE
	- PEs using reference data (such as IMAQ Image References) should pre-allocate a reasonably-sized ring buffer and reuse reference locations


## Interop with the System Configuration Utility

Since Data Record AD does not support editing configurations live, the Configurator must expose all the parameters required to launch the plugin and have it work. As such, as few parameters as possible should be exposed to the customer, especially if some parameters can be derived from / depend on other parameters. At the time of this writing, any illegal configurations or configurations that will fail at runtime cannot be caught by the configurator, and this significantly slows down the development process, and can be difficult to debug. 

Avoid magic strings, doubles, and heavily nested clusters. If possible, give your parameters descriptive names to influence what the customer is supposed to do. Avoid arrays when possible as this is difficult to navigate for a user.