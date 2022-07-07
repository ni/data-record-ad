## High-speed vs Low-speed logging

PEF passes data between PEs using very performant flattening and enqueues/dequeues to the PEF data store via the System Interface API. In generic logging use cases, as in FlexLogger, PEs should be written as small as possible, their sole responsibility to generate data to place onto the System Interface, to be passed through the Logging Gate and consumed by the TDMS plugin. Since the logging interface is clearly defined, data generation PEs can be small and are loosely coupled.

In the Data Record AD use case, not all data types have the same constraints: 

	- Data Record AD will support multiple logging formats in addition to TDMS, such as MD4 
	- For example, a PE pulling CAN frames generally does so at low-enough speeds and bandwidth that there is no issue passing through the System Interface, and the datatype is clearly defined such that it can cleanly be supported by FlexLogger's TDMS PE, or any decoupled logging PE with no performance drawbacks.
	- A high-speed camera, whether IMAQ or FPGA, generates data incredibly quickly, and entire flattened images are much too large to be sent via System Interface at the required speeds. Therefore, it is only feasible to pass Image References across PEs and have the consumer retrieve the image for immediate consumption (publishing to a UI topic or logging).
		○ This can be complex because images can come in a variety of shapes, sizes, bit depths, etc. which can make it difficult or unwieldy for a consumer PE to handle all cases.
		○ Concurrent access to the same image reference across multiple consumers can cause race conditions if the producer is still writing images and reusing references. References need to be released but not before all consumers have used them. This is difficult to genericize. 
		○ Some logging speeds/use cases can only be achieved using incredibly performant schemes like TDMS Advanced Asynchronous Write, which directly operates on EDVRs instead of forcing the user to open the image reference inline.