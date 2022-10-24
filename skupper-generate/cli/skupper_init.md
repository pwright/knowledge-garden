## skupper init

Initialise skupper installation

### Synopsis

Setup a router and other supporting objects to provide a functional skupper
installation that can then be connected to other skupper installations

```
skupper init [flags]
```

### Options

```
      --site-name string                        Provide a specific name for this skupper installation
      --ingress string                          Setup Skupper ingress to one of: [route|loadbalancer|nodeport|nginx-ingress-v1|contour-http-proxy|ingress|none]. If not specified route is used when available, otherwise loadbalancer is used.
      --ingress-host string                     Hostname or alias by which the ingress route or proxy can be reached
      --router-mode string                      Skupper router-mode (default "interior")
      --labels strings                          Labels to add to skupper pods
      --router-logging string                   Logging settings for router. 'trace', 'debug', 'info' (default), 'notice', 'warning', and 'error' are valid values.
      --router-debug-mode string                Enable debug mode for router ('asan' or 'gdb' are valid values)
      --routers int                             Number of router replicas to start
      --enable-console                          Enable skupper console (default true)
      --create-network-policy                   Create network policy to restrict access to skupper services exposed through this site to current pods in namespace
      --console-auth string                     Authentication mode for console(s). One of: 'openshift', 'internal', 'unsecured'
      --console-user string                     Skupper console user. Valid only when --console-auth=internal
      --console-password string                 Skupper console user. Valid only when --console-auth=internal
      --console-ingress string                  Determines if/how console is exposed outside cluster. If not specified uses value of --ingress. One of: [route|loadbalancer|nodeport|nginx-ingress-v1|contour-http-proxy|ingress|none].
      --ingress-annotations strings             Annotations to add to skupper ingress
      --annotations strings                     Annotations to add to skupper pods
      --router-service-annotations strings      Annotations to add to skupper router service
      --controller-service-annotation strings   Annotations to add to skupper controller service
      --enable-service-sync                     Participate in cross-site service synchronization (default true)
      --router-cpu string                       CPU request for router pods
      --router-memory string                    Memory request for router pods
      --router-cpu-limit string                 CPU limit for router pods
      --router-memory-limit string              Memory limit for router pods
      --router-node-selector string             Node selector to control placement of router pods
      --router-pod-affinity string              Pod affinity label matches to control placement of router pods
      --router-pod-antiaffinity string          Pod antiaffinity label matches to control placement of router pods
      --router-ingress-host string              Host through which node is accessible when using nodeport as ingress.
      --router-load-balancer-ip string          Load balancer ip that will be used for router service, if supported by cloud provider
      --controller-cpu string                   CPU request for controller pods
      --controller-memory string                Memory request for controller pods
      --controller-cpu-limit string             CPU limit for controller pods
      --controller-memory-limit string          Memory limit for controller pods
      --controller-node-selector string         Node selector to control placement of controller pods
      --controller-pod-affinity string          Pod affinity label matches to control placement of controller pods
      --controller-pod-antiaffinity string      Pod antiaffinity label matches to control placement of controller pods
      --controller-ingress-host string          Host through which node is accessible when using nodeport as ingress.
      --controller-load-balancer-ip string      Load balancer ip that will be used for controller service, if supported by cloud provider
      --config-sync-cpu string                  CPU request for config-sync pods
      --config-sync-memory string               Memory request for config-sync pods
      --config-sync-cpu-limit string            CPU limit for config-sync pods
      --config-sync-memory-limit string         Memory limit for config-sync pods
      --timeout duration                        Configurable timeout for the ingress loadbalancer option. (default 2m0s)
  -h, --help                                    help for init
```

### Options inherited from parent commands

```
  -c, --context string      The kubeconfig context to use
      --kubeconfig string   Path to the kubeconfig file to use
  -n, --namespace string    The Kubernetes namespace to use
```

### SEE ALSO

* [skupper](skupper.md)	 - 

###### Auto generated by spf13/cobra on 6-Oct-2022
