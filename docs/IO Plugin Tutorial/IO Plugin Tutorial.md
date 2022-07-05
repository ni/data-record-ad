# IO Plugin Tutorial  
The purpose of this tutorial is to walk new IO plugin developers through the creation of three different IO plugins that can be run without hardware.  Once the tutorial is complete, developers will have three separate IO plugins that can be used together with Data Record AD.

<img src="https://user-images.githubusercontent.com/15633959/154979199-e8fb5515-37d2-403d-aa80-6da8e54fdd91.png" width="300">

The first plugin will generate random numbers.  The second plugin will save the generated numbers to disk as a text file.  The third plugin can be injected between the random number generator and the text file logger and it will allow the user to scale the random numbers.

As developers move through the tutorial they should note that less detailed instructions are provided for the second and third plugins - this is intentional.  If there are questions, the instructions for the first tutorial should be referenced.

Additional instructions are provided for an additional plugin that utilizes the DatastreamGrpc library to publish the generated data.  Instructions are also included to modify the _Random Number Generator_ IO plugin to accept plugin-targeted gRPC messages.

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
Instructions for creating the Random Number Generator IO plugin can be found [here](./1%20-%20Random%20Number%20Generator.md#io-plugin-tutorial).

## Create Data Sink IO Plugin - Text File
Instructions for creating the Random Number Logger IO plugin can be found [here]().

## Create Data Processor IO Plugin - Scaling Factor
Instructions for creating the Random Number Scaling Factor IO plugin can be found [here]().

## Create Data Publisher IO Plugin - gRPC 
Instructions for creating the Random Number Publisher IO plugin can be found [here]().

## Modify IO Plugin to Support a Plugin-Targeted gRPC Message
Instructions for modifying the Random Number Generator IO plugin to support plugin-targeted gRPC messages can be found [here]().

## Additional Developer Features
### Custom Data
See [this README](./CustomData#custom-data-types) to learn more about Custom Data and how it is used within the IO plugins.

### Icons
If no icons are specified, the default plugin icon is used:
  
![image](https://user-images.githubusercontent.com/15633959/176736748-6c0fc8fe-0d2c-44e1-9dd0-cf43d901ef09.png)

Users can also specify custom icons such as this:

![image](https://user-images.githubusercontent.com/15633959/176736857-363df4f0-60f5-48d4-bf20-fadfa5c1f82d.png)

To use a custom icon, create a 40x40 pixel image and save it as PluginIcon.png.  Colors and transparency are supported.  The file needs to reside within the deployed plugin directory:
 
 _C:\Users\Public\Documents\National Instruments\ADAS\Plugins\IOPlugins\\<PluginName>\PluginIcon.png_
  
 [Return to Table of Contents](./IO%20Plugin%20Tutorial.md#table-of-contents) 
