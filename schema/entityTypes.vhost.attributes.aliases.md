# entityTypes.vhost.attributes.aliases

Alternate hostnames that share this vhost configuration. Hosts named in this attribute are treated as if this vhost was defined with the alias name in the vhost 'hostname' attribute. This attribute is implemented to help with multitenant configurations where multiple vhosts share a common configuration. The string is a comma- or space-separated list of literal hostnames or hostname patterns. A vhost aliases hostname must be unique across all vhost hostnames and all of their aliases.

