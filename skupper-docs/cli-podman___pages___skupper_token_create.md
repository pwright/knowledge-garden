# skupper token create

Create a token.
The 'link create' command uses the token to establish a link from a remote Skupper site.

Create a token.
The 'link create' command uses the token to establish a link from a remote Skupper site.

    skupper token create <output-token-file>  --[option]

ingress-host:: 
Hostname or alias by which the ingress route or proxy can be reached
 (string)
name:: 
Provide a specific identity as which connecting skupper installation will be authenticated (default "skupper")
 (string)

platform:: 
The platform type to use [kubernetes, podman]
 (string)

* [skupper token](skupper_token.adoc)	 - Manage skupper tokens
