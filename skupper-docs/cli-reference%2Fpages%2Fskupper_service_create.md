# skupper service create

Create a skupper service

Create a skupper service

    skupper service create <name> <port...>  --[option]

aggregate:: 
The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
 (string)
enable-tls:: 
If specified, the service communication will be encrypted using TLS
 (bool)
event-channel:: 
If specified, this service will be a channel for multicast events.
 (bool)
protocol:: 
The mapping in use for this service address (tcp, http, http2) (default "tcp")
 (string)

* [skupper service](skupper_service.adoc)	 - Manage skupper service definitions
