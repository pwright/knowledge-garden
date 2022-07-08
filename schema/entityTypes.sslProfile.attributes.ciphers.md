# entityTypes.sslProfile.attributes.ciphers

Specifies the enabled ciphers so the SSL Ciphers can be hardened. In other words, use this field to disable weak ciphers. The ciphers are specified in the format understood by the OpenSSL library. For example, ciphers can be set to ALL:!aNULL:!EXPORT56:RC4+RSA:+HIGH:+MEDIUM:+LOW:+SSLv2:+EXP; -- The full list of allowed ciphers can be viewed using the openssl ciphers command

