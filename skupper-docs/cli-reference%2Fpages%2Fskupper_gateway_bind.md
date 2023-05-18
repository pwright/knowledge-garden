# skupper gateway bind

Bind a process to the service network

Bind a process to the service network

    skupper gateway bind <address> <host> <port...>  --[option]

aggregate:: 
The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
 (string)
event-channel:: 
If specified, this service will be a channel for multicast events.
 (bool)

* [skupper gateway](skupper_gateway.adoc)	 - Manage skupper gateway definitions
