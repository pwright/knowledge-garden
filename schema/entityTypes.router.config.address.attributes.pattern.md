# entityTypes.router.config.address.attributes.pattern

'A wildcarded pattern for address matching. Incoming addresses are matched against this pattern. Matching addresses use the configured settings. The pattern consists of one or more tokens separated by a forward slash ''/''. A token can be one of the following: a * character, a # character, or a sequence of characters that do not include /, *, or #.  The * token matches any single token.  The # token matches zero or more tokens. * has higher precedence than #, and exact match has the highest precedence. Cannot be used with a prefix attribute.'

