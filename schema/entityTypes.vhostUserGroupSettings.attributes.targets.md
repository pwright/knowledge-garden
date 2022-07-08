# entityTypes.vhostUserGroupSettings.attributes.targets

A list of target addresses to which users in this group may send messages. To specify multiple addresses, separate the addresses with either a comma or a space. If you do not specify any addresses, users in this group are not allowed to send messages to any addresses. You can use the substitution token `${user}` to specify an address that contains a user's authenticated user name. You can use an asterisk ('*') wildcard to match one or more characters in an address. However, this wildcard is only recognized if it is the last character in the address name. You may specify attributes 'targets' or 'targetPattern' but not both at the same time.

