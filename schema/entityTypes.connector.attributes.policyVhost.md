# entityTypes.connector.attributes.policyVhost

'A connector may optionally define a policy to restrict the remote container to access only specific resources. This attribute defines the name of the policy vhost for this connector. Within the vhost the connector will use the vhost policy settings from user group ''$connector''. If the vhost policy is absent or if the user group ''$connector'' within that policy is absent then the connector will fail to start.  In policy specified via connector attribute ''policyVhost'' the following vhostUserGroupSettings attributes are unused:  ''users'', ''remoteHosts'', ''maxFrameSize'', ''maxSessionWindow'', ''maxSessions''.'

