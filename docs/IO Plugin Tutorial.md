# IO Plugin Tutorial  
The purpose of this tutorial is to walk new IO plugin developers through the creation of three different IO plugins that can be run without hardware.  Once the tutorial is complete, developers will have three separate IO plugins that can be used together with Data Record AD.

![image](https://user-images.githubusercontent.com/15633959/154979199-e8fb5515-37d2-403d-aa80-6da8e54fdd91.png)

The first plugin will generate random numbers.  The second plugin will save the generated numbers to disk as a text file.  The final plugin can be injected between the random number generator and the text file logger and it will allow the user to scale the random numbers.

## Update IO Plugin Project Template
To assist developers with creating IO plugins, a LabVIEW Project Template has been created.  This project template is installed with the Data Record AD Development Suite.

The source code for the project template also exists within this GitHub repository.  It is a good idea to update your project template from GitHub to ensure you are starting with the latest template code.

Navigate to /../IO Plugin Creation Tool.  You'll find the necessary files and a python script that can be used to copy them to the appropriate location.

![image](https://user-images.githubusercontent.com/15633959/154981043-fc8a9235-24d5-463d-92d9-a583ac46eaac.png)

To use the python script, simply open a command prompt and type the script name.  Use _-f_ to force the script to copy.  You must have python installed to use the script.  For more information on installing/using python please visit https://www.python.org/.

![image](https://user-images.githubusercontent.com/15633959/154981599-a488b1dd-7108-46d8-b802-3ac69c51abdc.png)

                    
## Create a Branch

## Create Data Source IO Plugin - Random Number Generator

## Create Data Sink IO Plugin - Text File

## Create Data Processor IO Plugin - Scaling Factor


## Modify Random Number Generator to Support a Plugin-Targeted gRPC Message

