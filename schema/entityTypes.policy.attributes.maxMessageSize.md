# entityTypes.policy.attributes.maxMessageSize

The maximum size in bytes of AMQP message transfers allowed for this router as messages enter the router network. This limit is applied to transfers over user connections and to transfers to interior routers from edge routers. This limit is not applied to interior-to-interior router connections. This limit may be overridden by vhost or by vhost user group settings. A value of zero disables this limit. Administrators are advised not set interior router maximum message sizes so low that edge router management requests or responses are blocked. Administrators are also advised to set edge router maximum message sizes lower than the attached interior router maximum message size.

