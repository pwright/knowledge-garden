# entityTypes.vhostUserGroupSettings.attributes.sources

A list of source addresses from which users in this group may receive messages. To specify multiple addresses, separate the addresses with either a comma or a space. If you do not specify any addresses, users in this group are not allowed to receive messages from any addresses. You can use the substitution token `${user}` to specify an address that contains a user's authenticated user name. You can use an asterisk ('*') wildcard to match one or more characters in an address. However, this wildcard is only recognized if it is the last character in the address name. You may specify attributes 'sources' or 'sourcePattern' but not both at the same time.

