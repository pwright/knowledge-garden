# skupper init

Initialise skupper installation

Setup a router and other supporting objects to provide a functional skupper installation that can then be connected to other skupper installations

    skupper init  --[option]

site-name:: 
Provide a specific name for this skupper installation
 (string)
ingress:: 
Setup Skupper ingress to one of: [external|none].
 (string)
router-mode:: 
Skupper router-mode (default "interior")
 (string)
labels:: 
Labels to add to skupper pods
 (strings)
router-logging:: 
Logging settings for router. 'trace', 'debug', 'info' (default), 'notice', 'warning', and 'error' are valid values.
 (string)
router-debug-mode:: 
Enable debug mode for router ('asan' or 'gdb' are valid values)
 (string)
ingress-host:: 
Hostname or alias by which the ingress route or proxy can be reached.
 (strings)
                                   Tokens can only be generated for addresses provided through ingress-hosts,
                                   so it can be used multiple times.
ingress-bind-ip:: 
IP addresses in the host machines that will be bound to the inter-router and edge ports.
 (strings)
bind-port:: 
ingress host binding port used for incoming links from sites using interior mode (default 55671)
 (int)
bind-port-edge:: 
ingress host binding port used for incoming links from sites using edge mode (default 45671)
 (int)
container-network:: 
container network name to be used (default "skupper")
 (string)
podman-endpoint:: 
local podman endpoint to use
 (string)

platform:: 
The platform type to use [kubernetes, podman]
 (string)

* [skupper](skupper.adoc)	 -
