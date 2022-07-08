# entityTypes.vhostUserGroupSettings.attributes.allowAnonymousSender

'Whether this connection is allowed to create sending links if the sender does not provide a target address. By prohibiting anonymous senders, the router only needs to verify once, when the link is created, that the sender is permitted to send messages to the target address. The router does not need to verify each message that is sent on the link. A value of ''true'' means that users may send messages to any address. Allowing anonymous senders can also decrease performance: if the sender does not specify a target address, then the router must parse each message to determine how to route it.'

