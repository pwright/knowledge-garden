# skupper expose

Expose a set of pods through a Skupper address

Expose a set of pods through a Skupper address

    skupper expose [host hostOrIP]  --[option]

address:: 
The Skupper address to expose
 (string)
aggregate:: 
The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
 (string)
container-name:: 
Use a different container name
 (string)
enable-ingress-from-target-site:: 
Determines whether access to the Skupper service is enabled in the site the target was exposed through. Always (default) or Never are valid values.
 (string)
event-channel:: 
If specified, this service will be a channel for multicast events.
 (bool)
generate-tls-secrets:: 
If specified, the service will be exposed over TLS (valid only for http2 and tcp protocols)
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
port:: 
The ports to expose on
 (ints)
protocol:: 
The protocol to proxy (tcp, http, or http2) (default "tcp")
 (string)
target-port:: 
The ports to target on pods
 (strings)

platform:: 
The platform type to use [kubernetes, podman]
 (string)

* [skupper](skupper.adoc)	 -
