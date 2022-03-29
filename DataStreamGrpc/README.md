# Datastream Grpc

## Introduction

The Datastream Grpc defines a [grpc](https://grpc.io/) service that allows remote data passing via publishing and subscribing "topics".
TopicData consists of a topicName plus a messageData bytestream.

The data can be raw binary data or text, there is no restriction.

[`datastream.proto`](source/datastream.proto) is the grpc proto file for our service.  The proto file defines the data structure of the topic data as well as
supported operations (known as Remote Procedure Calls, or rpc).

Using the grpc `protoc.exe` tool, APIs in [various popular programming languages](https://grpc.io/docs/languages/) can be generated that implements the service as defined by the `datastream.proto` file.

While G code generation is not supported by the grpc tool.  We have created a G implementation of the datastream service.  Refer to [`dataStreamGrpcLabview`](../dataStreamGrpcLabview) for more details.

## Service Workflow

The client of the service needs to add itself as a "subscriber" to the service via the `AddSubscriber` rpc call.

A "subscriber token" is returned to the client as a result of `AddSubscriber`.  The token uniquely identifies the client.  Most subsquent rpc calls will require this token.  Not passing a valid token will result in the server returning an error to the client.

Next the client can subscribe for a specific topic name with the `SubscribeTopic` rpc call.  Once the topic name is subscribed, the client can either get the latest message data of the topic via the `ReadLatestTopicMessage` rpc call, or set up a streaming request via the `StartReadingTopicMessages` call to get notified whenever there is new topic message data that is published.

A client can subscribe multiple topics and use one streaming request to get notified of any new topic message data from any topic name the client has subscribed.

## Talking to the Data Record AD Application 

For messages targeting the Data Record AD application, the TopicData should be formatted as follows:

`topicName` is set to `DataRecordGrpcApplicationTopic`
`messageData` is a JSON string consisting of:
```
{
"messageName":"",
"details":"{}"
}
```

`details` is generally not required for application-targeted messages, except for Reconfigure. Supported application-targeted messages are:
The contents `details` are further JSON, which may not be needed for all messages. 

| **messageName**  | **details**  | **Behavior**  |
| -- | -- | -- |
| Help | n/a | Return a list of all supported messages. |
| Ping | n/a | Return "Service running." if able. |
| Shutdown | n/a | Shut down the Data Record AD application. |
| Reconfigure | {"Config Path":"", "Engine History Length":0}  | Shutdown the currently configured session and restart Data Record AD with the requested configuration file.  |
| Query PEF | n/a | Return the latest message from the Data Record AD Processing Engine. |
| Get Active Configuration | n/a  | Return a list of currently running plugins. |
