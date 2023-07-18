# skupper service create

Create a skupper service

Create a skupper service

    skupper service create <name> <port...>  --[option]

aggregate:: 
The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
 (string)
bridge-image:: 
The image to use for a bridge running external to the skupper router
 (string)
container-name:: 
Use a different container name
 (string)
enable-ingress:: 
Determines whether access to the Skupper service is enabled in this site. Valid values are Always (default) or Never.
 (string)
event-channel:: 
If specified, this service will be a channel for multicast events.
 (bool)
generate-tls-secrets:: 
If specified, the service communication will be encrypted using TLS
 (bool)
host-ip:: 
Host IP address used to bind service ports
 (string)
host-port:: 
The host ports to bind with the service (you can also use colon to map service-port to a host-port).
 (strings)
label:: 
Labels to the new service (comma separated list of key and value pairs split by equals (default [])
 (stringToString)
protocol:: 
The mapping in use for this service address (tcp, http, http2) (default "tcp")
 (string)
tls-cert:: 
K8s secret name with custom certificates to encrypt the communication using TLS (valid only for http2 and tcp protocols)
 (string)

platform:: 
The platform type to use [kubernetes, podman]
 (string)

* [skupper service](skupper_service.adoc)	 - Manage skupper service definitions
