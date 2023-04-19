# skupper gateway expose

Expose a process to the service network (ensure gateway and cluster service)

Expose a process to the service network (ensure gateway and cluster service)

    skupper gateway expose <address> <host> <port...>  --[option]

aggregate:: 
The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
 (string)
event-channel:: 
If specified, this service will be a channel for multicast events.
 (bool)
protocol:: 
The protocol to gateway (tcp, http or http2). (default "tcp")
 (string)
type:: 
The gateway type one of: 'service', 'docker', 'podman' (default "service")
 (string)

* [skupper gateway](skupper_gateway.adoc)	 - Manage skupper gateway definitions
