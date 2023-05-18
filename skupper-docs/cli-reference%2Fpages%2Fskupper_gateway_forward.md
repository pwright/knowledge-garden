# skupper gateway forward

Forward an address to the service network

Forward an address to the service network

    skupper gateway forward <address> <port...>  --[option]

aggregate:: 
The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
 (string)
event-channel:: 
If specified, this service will be a channel for multicast events.
 (bool)
loopback:: 
Forward from loopback only
 (bool)

* [skupper gateway](skupper_gateway.adoc)	 - Manage skupper gateway definitions
