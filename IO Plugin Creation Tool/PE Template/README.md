# IO Plugin README Template Instructions [Remove When Done]
This is the template for the README file for newly created IO plugins.  Please update the sections below.  If the section is marked _[REQUIRED]_ please update the information.  If it is marked _[OPTIONAL]_ and not applicable to your plugin, please remove the section.  Tags (_[REQUIRED]/[OPTIONAL]_) should be removed once updates are complete.

# [REQUIRED] IO Plugin Name <-- Update with actual name
Brief description of IO plugin.

Author(s): List of developers who worked on the IO plugin. 

# [REQUIRED] Usage/Configuration

## [OPTIONAL] Dependencies
List any additional dependencies.  This could be dependencies on external libraries, APIs or even other IO plugins.

## [OPTIONAL] Custom Data
If the plugin uses any custom data types, please list the type(s) here.  

## [REQUIRED] Parameters
This is a table of the configuration parameters for the IO plugin.  Additional tables can be used to list options for clusters, enums, text rings, etc. 
| Parameter | Description | Default |
| -- | -- | -- |
| File Path | File path to store data to disk, includes file name and extension | C:\Data\Test.tdms |
| Compress Data | Boolean to determine whether data is compressed | TRUE |
| File Description | Cluster containing file details, see table below | N/A |

[OPTIONAL] Additional table

**File Description** | Details for File Description cluster
|Parameter| Description | Default |
| -- | -- | -- |
| Comment | String, File comment | " " |
| Time Source | String, Description of timing source used when gathering data | GPS |
| Source | Source classification, e.g. ECU, see options below | U8 |

[OPTIONAL] Additional table

**Source** | All available options for source types
| Name | Value | Description |
|--|--|--|
| Other | 0 | Source type does not fit into given categories or is unknown |
| ECU | 1 | Source is an ECU |
| BUS | 2 | Source is a bus (e.g. for bus monitoring) |
| I/O Device | 3 | Source is an I/O device (e.g. analog I/O) |
| Software Tool | 4 | Source is a software tool (e.g. for tool generated signals/events) |
| User | 5 | Source is a user interaction/input (e.g. for user generated events) |

## [OPTIONAL] Supported _DataRecordGrpcPluginTopic_ Messages
List and describe behavior for any plugin targeted gRPC messages.  These messages are managed in the _Handle Message_ VI.