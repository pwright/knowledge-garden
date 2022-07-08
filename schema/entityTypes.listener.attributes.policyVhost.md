# entityTypes.listener.attributes.policyVhost

A listener may optionally define a virtual host to index to a specific policy to restrict the remote container to access only specific resources. This attribute defines the name of the policy vhost for this listener.  If multi-tenancy is enabled for the listener, this vhost will override the peer-supplied vhost for the purposes of identifying the desired policy settings for the connections.

