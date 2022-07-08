# entityTypes.connector.attributes.maxFrameSize

The maximum frame size in octets that will be used in the connection-open negotiation with a connected peer.  The frame size is the largest contiguous set of uninterrupted data that can be sent for a message delivery over the connection. Interleaving of messages on different links is done at frame granularity. Policy settings will not overwrite this value. Defaults to 16384.

