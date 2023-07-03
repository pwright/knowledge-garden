sid:: skupper-declarative 
# Configuring {skupper-name} sites using YAML

Using YAML files to configure {skupper-name} allows you to use source control to track and manage {skupper-name} network changes.

sid:: installing-using-yaml 
## Installing {skupper-name} using YAML

Installing {skupper-name} using YAML provides a declarative method to install {skupper-name}.
You can store your YAML files in source control to track and manage {skupper-name} network changes.

* Access to a Kubernetes cluster

1. Log into your cluster.
If you are deploying {skupper-name} to be available for all namespaces, verify you have `cluster-admin` privileges.
2. Deploy the site controller:
   * To install {skupper-name} into the current namespace deploy the site controller using the following YAML:

     ```
     kubectl apply -f deploy-watch-current-ns.yaml
     ```
     where the contents of `deploy-watch-current-ns.yaml` is specified in the [watch-current-reference](#watch-current-reference) appendix.
   * To install {skupper-name} for all namespaces:

     1. Create a namespace named `skupper-site-controller`.
     2. Deploy the site controller using the following YAML:

        ```
        kubectl apply -f deploy-watch-all-ns.yaml
        ```
        where the contents of `deploy-watch-all-ns.yaml` is specified in the [watch-all-reference](#watch-all-reference) appendix.
3. Verify the installation.

   ```
   $ oc get pods
   NAME                                       READY   STATUS    RESTARTS   AGE
   skupper-site-controller-84694bdbb5-n8slb   1/1     Running   0          75s
   ```

sid:: creating-using-yaml 
## Creating a {skupper-name} site using YAML

Using YAML files to create {skupper-name} sites allows you to use source control to track and manage {skupper-name} network changes.

* {skupper-name} is installed in the cluster or namespace you want to target.
* You are logged into the cluster.

1. Create a YAML file to define the site, for example, `my-site.yaml`:

   ```
   apiVersion: v1
   data:
     cluster-local: "false"
     console: "true"
     flow-collector: "true"
     console-authentication: internal
     console-password: "password"
     console-user: "barney"
     name: my-site
     router-console: "true"
     service-controller: "true"
     service-sync: "true"
   kind: ConfigMap
   metadata:
     name: skupper-site
   ```
2. Apply the YAML file to your cluster:

   ```
   kubectl apply -f ~/my-site.yml
   ```

See the [site-config-reference](#site-config-reference) section for more reference.

sid:: linking-sites-using-yaml 
## Linking sites using YAML

While it is not possible to declaratively link sites, you can create a token using YAML.

* {skupper-name} is installed on the clusters you want to link.
* You are logged into the cluster.

1. Log into the cluster you want to link to and change context to the namespace where {skupper-name} is installed.
This site must have `ingress` enabled.
2. Create a YAML file named `token-request.yml` to request a token:

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     labels:
       skupper.io/type: connection-token-request
     name: secret-name
   ```
3. Apply the YAML to the namespace to create a secret.

   ```
   $ kubectl apply -f token-request.yml
   ```
4. Create the token YAML from the secret.

   ```
   $ kubectl get secret -o yaml secret-name | yq 'del(.metadata.namespace)' > ~/token.yaml
   ```
5. Log into the cluster you want to link from and change context to the namespace where {skupper-name} is installed.
6. Apply the token YAML.

   ```
   $ kubectl apply -f token.yml
   ```
7. Verify the link, allowing some time for the process to complete.

   ```
   $ skupper link status --wait 60
   ```

sid:: site-config-reference 
## Site ConfigMap YAML reference

Using YAML files to configure {skupper-name} requires that you understand all the fields so that you provision the site you require.

The following YAML defines a {skupper-name} site:

```
apiVersion: v1
data:
  cluster-local: "false" //<.>
  console: "true" //<.>
  flow-collector: "true" //<.>
  console-authentication: internal //<.>
  console-user: "username" //<.>
  console-password: "password" //<.>
  edge: "false" //<.>
  name: my-site //<.>
  router-console: "true" //<.>
  service-controller: "true" //<.>
  service-sync: "true" //<.>
kind: ConfigMap
metadata:
  name: skupper-site //<.>
```

1. Only accept connections from within the local cluster, defaults to `false`.
2. Enables the skupper console, defaults to `false`.
NOTE: You must enable `console` and `flow-collector` for the console to function.
3. Enables the flow collector, defaults to `false`.
4. Specifies the skupper console authentication method. The options are `openshift`, `internal`, `unsecured`.
5. Username for the `internal` authentication option.
6. Password for the `internal` authentication option.
7. Specifies whether an edge site is created, defaults to `false`.
8. Specifies the site name.
9. Enables the router console, defaults to `false`.
10. Specifies whether the service controller runs, defaults to `true`.
11. Specifies whether the services are synchronized across the {service-network}, defaults to `true`.

sid:: watch-current-reference 
## YAML for watching current namespace

The following example deploys {skupper-name} to watch the current namespace.

```
```

sid:: watch-all-reference 
## YAML for watching all namespaces

The following example deploys {skupper-name} to watch all namespaces.

```
```
