# Terms

## adr/0001-architectural-decision-records.md

## adr/0002-avoid-router-restarts.md

## cli/skupper.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_completion.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_debug.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_debug_dump.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_debug_events.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_debug_service.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_delete.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_expose.md
* [[address]]
      --address string                  The Skupper address to expose
* [[enable-tls]]
      --enable-tls                      If specified, the service will be exposed over TLS (valid only for http2 protocol)
* [[headless]]
      --headless                        Expose through a headless service (valid only for a statefulset target)
* [[port]]
      --port ints                       The ports to expose on
* [[protocol]]
      --protocol string                 The protocol to proxy (tcp, http, or http2) (default "tcp")
* [[proxy-cpu]]
      --proxy-cpu string                CPU request for router pods
* [[proxy-cpu-limit]]
      --proxy-cpu-limit string          CPU limit for router pods
* [[proxy-memory]]
      --proxy-memory string             Memory request for router pods
* [[proxy-memory-limit]]
      --proxy-memory-limit string       Memory limit for router pods
* [[proxy-node-selector]]
      --proxy-node-selector string      Node selector to control placement of router pods
* [[proxy-pod-affinity]]
      --proxy-pod-affinity string       Pod affinity label matches to control placement of router pods
* [[proxy-pod-antiaffinity]]
      --proxy-pod-antiaffinity string   Pod antiaffinity label matches to control placement of router pods
* [[publish-not-ready-addresses]]
      --publish-not-ready-addresses     If specified, skupper will not wait for pods to be ready
* [[target-port]]
      --target-port strings             The ports to target on pods
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_bind.md
* [[aggregate]]
      --aggregate string   The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
* [[event-channel]]
      --event-channel      If specified, this service will be a channel for multicast events.
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_delete.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_export-config.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_expose.md
* [[aggregate]]
      --aggregate string   The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
* [[event-channel]]
      --event-channel      If specified, this service will be a channel for multicast events.
* [[protocol]]
      --protocol string    The protocol to gateway (tcp, http or http2). (default "tcp")
* [[type]]
      --type string        The gateway type one of: 'service', 'docker', 'podman' (default "service")
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_forward.md
* [[aggregate]]
      --aggregate string   The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
* [[event-channel]]
      --event-channel      If specified, this service will be a channel for multicast events.
* [[loopback]]
      --loopback           Forward from loopback only
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_generate-bundle.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_init.md
* [[config]]
      --config string   The gateway config file to use for initialization
* [[type]]
      --type string     The gateway type one of: 'service', 'docker', 'podman' (default "service")
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_status.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_unbind.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_unexpose.md
* [[delete-last]]
      --delete-last   Delete the gateway if no services remain (default true)
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_gateway_unforward.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_init.md
* [[site-name]]
      --site-name string                        Provide a specific name for this skupper installation
* [[ingress]]
      --ingress string                          Setup Skupper ingress to one of: [route|loadbalancer|nodeport|nginx-ingress-v1|contour-http-proxy|ingress|none]. If not specified route is used when available, otherwise loadbalancer is used.
* [[ingress-host]]
      --ingress-host string                     Hostname or alias by which the ingress route or proxy can be reached
* [[router-mode]]
      --router-mode string                      Skupper router-mode (default "interior")
* [[labels]]
      --labels strings                          Labels to add to skupper pods
* [[router-logging]]
      --router-logging string                   Logging settings for router. 'trace', 'debug', 'info' (default), 'notice', 'warning', and 'error' are valid values.
* [[router-debug-mode]]
      --router-debug-mode string                Enable debug mode for router ('asan' or 'gdb' are valid values)
* [[routers]]
      --routers int                             Number of router replicas to start
* [[enable-console]]
      --enable-console                          Enable skupper console (default true)
* [[create-network-policy]]
      --create-network-policy                   Create network policy to restrict access to skupper services exposed through this site to current pods in namespace
* [[console-auth]]
      --console-auth string                     Authentication mode for console(s). One of: 'openshift', 'internal', 'unsecured'
* [[console-user]]
      --console-user string                     Skupper console user. Valid only when --console-auth=internal
* [[console-password]]
      --console-password string                 Skupper console user. Valid only when --console-auth=internal
* [[console-ingress]]
      --console-ingress string                  Determines if/how console is exposed outside cluster. If not specified uses value of --ingress. One of: [route|loadbalancer|nodeport|nginx-ingress-v1|contour-http-proxy|ingress|none].
* [[ingress-annotations]]
      --ingress-annotations strings             Annotations to add to skupper ingress
* [[annotations]]
      --annotations strings                     Annotations to add to skupper pods
* [[router-service-annotations]]
      --router-service-annotations strings      Annotations to add to skupper router service
* [[controller-service-annotation]]
      --controller-service-annotation strings   Annotations to add to skupper controller service
* [[enable-service-sync]]
      --enable-service-sync                     Participate in cross-site service synchronization (default true)
* [[router-cpu]]
      --router-cpu string                       CPU request for router pods
* [[router-memory]]
      --router-memory string                    Memory request for router pods
* [[router-cpu-limit]]
      --router-cpu-limit string                 CPU limit for router pods
* [[router-memory-limit]]
      --router-memory-limit string              Memory limit for router pods
* [[router-node-selector]]
      --router-node-selector string             Node selector to control placement of router pods
* [[router-pod-affinity]]
      --router-pod-affinity string              Pod affinity label matches to control placement of router pods
* [[router-pod-antiaffinity]]
      --router-pod-antiaffinity string          Pod antiaffinity label matches to control placement of router pods
* [[router-ingress-host]]
      --router-ingress-host string              Host through which node is accessible when using nodeport as ingress.
* [[router-load-balancer-ip]]
      --router-load-balancer-ip string          Load balancer ip that will be used for router service, if supported by cloud provider
* [[controller-cpu]]
      --controller-cpu string                   CPU request for controller pods
* [[controller-memory]]
      --controller-memory string                Memory request for controller pods
* [[controller-cpu-limit]]
      --controller-cpu-limit string             CPU limit for controller pods
* [[controller-memory-limit]]
      --controller-memory-limit string          Memory limit for controller pods
* [[controller-node-selector]]
      --controller-node-selector string         Node selector to control placement of controller pods
* [[controller-pod-affinity]]
      --controller-pod-affinity string          Pod affinity label matches to control placement of controller pods
* [[controller-pod-antiaffinity]]
      --controller-pod-antiaffinity string      Pod antiaffinity label matches to control placement of controller pods
* [[controller-ingress-host]]
      --controller-ingress-host string          Host through which node is accessible when using nodeport as ingress.
* [[controller-load-balancer-ip]]
      --controller-load-balancer-ip string      Load balancer ip that will be used for controller service, if supported by cloud provider
* [[config-sync-cpu]]
      --config-sync-cpu string                  CPU request for config-sync pods
* [[config-sync-memory]]
      --config-sync-memory string               Memory request for config-sync pods
* [[config-sync-cpu-limit]]
      --config-sync-cpu-limit string            CPU limit for config-sync pods
* [[config-sync-memory-limit]]
      --config-sync-memory-limit string         Memory limit for config-sync pods
* [[timeout]]
      --timeout duration                        Configurable timeout for the ingress loadbalancer option. (default 2m0s)
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_link.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_link_create.md
* [[cost]]
      --cost int32    Specify a cost for this link. (default 1)
* [[name]]
      --name string   Provide a specific name for the link (used when deleting it)
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_link_delete.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_link_status.md
* [[timeout]]
      --timeout duration   Configurable timeout for retrieving information about remote links (default 2m0s)
* [[verbose]]
      --verbose            Show detailed information about a link
* [[wait]]
      --wait int           The number of seconds to wait for links to become active
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_network.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_network_status.md
* [[timeout]]
      --timeout duration   Configurable timeout for retrieving remote information (default 2m0s)
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_revoke-access.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service_bind.md
* [[protocol]]
      --protocol string               The protocol to proxy (tcp, http or http2).
* [[publish-not-ready-addresses]]
      --publish-not-ready-addresses   If specified, skupper will not wait for pods to be ready
* [[target-port]]
      --target-port strings           The port the target is listening on (you can also use colon to map source-port to a target-port).
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service_create.md
* [[aggregate]]
      --aggregate string   The aggregation strategy to use. One of 'json' or 'multipart'. If specified requests to this service will be sent to all registered implementations and the responses aggregated.
* [[enable-tls]]
      --enable-tls         If specified, the service communication will be encrypted using TLS
* [[event-channel]]
      --event-channel      If specified, this service will be a channel for multicast events.
* [[protocol]]
      --protocol string    The mapping in use for this service address (tcp, http, http2) (default "tcp")
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service_delete.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service_label.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service_status.md
* [[show-labels]]
      --show-labels   show service labels
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_service_unbind.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_status.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_token.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_token_create.md
* [[expiry]]
      --expiry duration     Expiration time for claim (only valid if --token-type=claim) (default 15m0s)
* [[name]]
      --name string         Provide a specific identity as which connecting skupper installation will be authenticated (default "skupper")
* [[uses]]
      --uses int            Number of uses for which claim will be valid (only valid if --token-type=claim) (default 1)
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_unexpose.md
* [[address]]
      --address string   Skupper address the target was exposed as
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_update.md
* [[force-restart]]
      --force-restart   Restart skupper daemons even if image tag is not updated
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use

## cli/skupper_version.md
* [[kubeconfig]]
      --kubeconfig string   Path to the kubeconfig file to use
