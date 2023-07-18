# skupper service bind

Bind a target to a service

Bind a target to a service

    skupper service bind <service-name> <target-type> <target-name>  --[option]

protocol:: 
The protocol to proxy (tcp, http or http2).
 (string)
publish-not-ready-addresses:: 
If specified, skupper will not wait for pods to be ready
 (bool)
target-port:: 
The port the target is listening on (you can also use colon to map source-port to a target-port).
 (strings)

* [skupper service](skupper_service.adoc)	 - Manage skupper service definitions
