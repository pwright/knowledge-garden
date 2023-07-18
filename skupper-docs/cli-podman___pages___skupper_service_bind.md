# skupper service bind

Bind a target to a service

Bind a target to a service

    skupper service bind <service-name> <target-type> <target-name>  --[option]

target-port:: 
The port the target is listening on (you can also use colon to map source-port to a target-port).
 (strings)
tls-trust:: 
K8s secret name with the CA to expose the service over TLS (valid only for http2 and tcp protocols)
 (string)

platform:: 
The platform type to use [kubernetes, podman]
 (string)

* [skupper service](skupper_service.adoc)	 - Manage skupper service definitions
