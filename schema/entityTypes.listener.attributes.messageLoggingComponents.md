# entityTypes.listener.attributes.messageLoggingComponents

A comma separated list that indicates which components of the message should be logged. Defaults to 'none' (log nothing). If you want all properties and application properties of the message logged use 'all'. Specific components of the message can be logged by indicating the components via a comma separated list. The components are message-id, user-id, to, subject, reply-to, correlation-id, content-type, content-encoding, absolute-expiry-time, creation-time, group-id, group-sequence, reply-to-group-id, app-properties. The application-data part of the bare message will not be logged. No spaces are allowed

