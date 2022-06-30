# IO Plugin Creation Tool

The IO Plugin Creation Tool is used to generate new IO plugins for Data Record AD. It works by copying the template plugin to your target directory, and using VI Scripting to change placeholder names, metadata, icons, etc. in the newly created plugin. The acronym "PE" is used throughout to designate a "Processing Element," which is a plugin within the Processing Element Framework, the background engine used in Data Record AD. "PE" and "IO plugin" are interchangeable terms for the purposes of Data Record AD.

## Install and Use

Run `installPluginCreationWizard.py`.

Run the resulting NIPKG to install all necessary files to their necessary locations. Once install is complete, the LabVIEW Create Project screen will have a tab for "ADAS" with an option for "ADAS IO Plugin Template." Follow the prompts in the template to create a new plugin.

## PE Template

The template PE LVPROJ is located in `data-record-ad\IO Plugin Creation Tool\PE Template`.

Each IO plugin consists of several required components that are stubbed out in the template. Plugins are class-based, and the classes inherit from parents defined in PEF's PluginSDK.lvlibp.

### Controller

The PE Controller is a component which defines the plugin's interface to the engine. The plugin's ID and output streams are defined here, and the latter may need to be modified by the developer after creation. There are also serialization and deserialization mechanisms to expose the plugin to the System Configuration Utility.

### PE 

The core functionality of the plugin. The user will need to implement each of the States to match their plugin's need. See the IO Plugin Developer Guide for additional details. There are additional overrides not exposed in the template that a user may want to override to extend functionality. The purpose of the template is to guide the plugin developer into making the most optimal decisions with regards to where to implement specific functionality in their new plugin, without being overly burdensome or needlessly prescriptive.

### Tests

The tests folder of the template includes a simple Caraya test to validate whether the plugin's configuration is successfully loadable. This should always pass. The plugin developer must write further unit or integration tests to validate any of their functionality. 

## LabVIEW Project Wizard

The source code for the LabVIEW Project Wizard is located in `data-record-ad\IO Plugin Creation Tool\IO PE Creation Wizard`.

The wizard consists of the Metadata Object (MDO) and Spec Pages for integration with LabVIEW's Create Project Window. The scripting code mostly occurs in PostCopyScripting.vi to perform all of the renames on the copied template.

## Contributing

Pull Requests to the PE Template are always welcome to reduce development burden on plugin developers. Prefer clear documentation over sample code inside the template to reduce prescriptiveness and template complexity.
