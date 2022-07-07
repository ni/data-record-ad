# IO Plugin Project Template
LabVIEW has in-product templates and sample projects, which provide recommended starting points designed to ensure the quality and scalability of a system.  All of the templates and sample projects are open-source and include extensive documentation designed to clearly indicate how the code works and the best practices for adding or modifying functionality. In addition to demonstrating recommended architectures, these projects also illustrate best practices for documenting and organizing code.

To assist developers with creating IO plugins, the _ADAS IO Plugin Template_ has been created.  This project template is installed with the Data Record AD Development Suite.  The source code for the project template also exists within this GitHub repository.  

## Update IO Plugin Project Template
It is a good idea to update your project template from GitHub to ensure you are starting with the latest template code.

Navigate to _/../IO Plugin Creation Tool_.  You'll find the necessary files and a python script that can be used to copy them to the appropriate location.

![image](https://user-images.githubusercontent.com/15633959/154981043-fc8a9235-24d5-463d-92d9-a583ac46eaac.png)

To use the python script, simply open a command prompt and type the script name.  Use _-f_ to force the script to copy.  You must have python installed to use the script.  For more information on installing/using python please visit https://www.python.org/.

<img src="https://user-images.githubusercontent.com/15633959/154981599-a488b1dd-7108-46d8-b802-3ac69c51abdc.png" width="1000">

## Create a Branch
Before creating any plugins, if you want to work within the Data Record AD repository, it is necessary to create a branch to work in.  If this is your first time creating a branch, you may find [this tutorial](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-and-deleting-branches-within-your-repository) helpful.

## Create Project
Launch LabVIEW and select _Create Project_:

<img src="https://user-images.githubusercontent.com/15633959/154990689-c1e1e95a-d72f-4759-8514-5ed28a276732.png" width="600">
  
Select _ADAS IO Plugin Template_ from the list.
  
<img src="https://user-images.githubusercontent.com/15633959/154991045-051586f8-3c22-4972-b5e4-563f09f9e91a.png" width="600">

Complete the information for the template as provided.  The _IO Plugin Name_ should be representative of its purpose.  The _IO Plugin Directory_ should be _\<Checkout Directory>/IO Plugins/\<IO Plugin Name>_.  It is also a good idea to update the icon to be more representative of the plugin purpose.  When you are finished updating the information, select _Finish_.

<img src="https://user-images.githubusercontent.com/15633959/154993224-3c26ad00-a073-49da-a570-4de32a146a9a.png" width="800">

LabVIEW will now generate your project from the template code.  A progress bar will appear showing the current status:
  
<img src="https://user-images.githubusercontent.com/15633959/155002416-24d5c8bd-df32-4a47-87fe-ec3d194d197a.png" width="800">

When the project is completely generated, a Windows Explorer window will open at the location specicified within the project template:  
<img src="https://user-images.githubusercontent.com/15633959/155002647-97bed789-8c7e-424b-91ac-835cc45d9695.png" width="600">
