# entityTypes.listener.attributes.initialHandshakeTimeoutSeconds

The timeout, in seconds, for the initial handshake for connections coming in through listeners.  If the time interval expires before the peer sends the AMQP OPEN frame, the connection shall be closed.  A value of zero (the default) disables this timeout.

