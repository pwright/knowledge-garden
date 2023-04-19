# skupper token create

Create a token.
The 'link create' command uses the token to establish a link from a remote Skupper site.

Create a token.
The 'link create' command uses the token to establish a link from a remote Skupper site.

    skupper token create <output-token-file>  --[option]

expiry:: 
Expiration time for claim (only valid if --token-type=claim) (default 15m0s)
 (duration)
name:: 
Provide a specific identity as which connecting skupper installation will be authenticated (default "skupper")
 (string)
  -p, --password string     A password for the claim (only valid if --token-type=claim). If not specified one will be generated.
  -t, --token-type string   Type of token to create. Valid options are 'claim' or 'cert' (default "claim")
uses:: 
Number of uses for which claim will be valid (only valid if --token-type=claim) (default 1)
 (int)

* [skupper token](skupper_token.adoc)	 - Manage skupper tokens
