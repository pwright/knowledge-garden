# Exploring a {service-network}

{skupper-name} includes a command to allow you report all the sites and the services available on a {service-network}.

* A {service-network} with more than one site

1. Set your Kubernetes context to a namespace on the {service-network}.
2. Use the following command to report the status of the {service-network}:

   ```bash
   $ skupper network status
   ```

   For example:

   ```
   Sites:
   ├─ [local] 4dba248 - west  ①
   │  URL: 10.96.146.236 ②
   │  name: west ③
   │  namespace: west
   │  version: 0.8.6 ④
   │  ╰─ Services:
   │     ╰─ name: hello-world-backend ⑤
   │        address: hello-world-backend: 8080 ⑥
   │        protocol: tcp ⑦
   ╰─ [remote] bca99d1 - east <8> 
      URL: 
      name: east
      namespace: east
      sites linked to: 4dba248-west ⑨
      version: 0.8.6
      ╰─ Services:
         ╰─ name: hello-world-backend
            address: hello-world-backend: 8080
            protocol: tcp
            ╰─ Targets:
               ╰─ name: hello-world-backend-7dfb45b98d-mhskw ⑩
   ```

   1. The unique identifier of the site associated with the current context, that is, the `west` namespace
   2. The URL of the {service-network} router.
   This is required for other sites to connect to this site and is different from the console URL. 
   If you require the URL of the console, use the `skupper status` command to display that URL.
   3. The site name.
   By default, skupper uses the name of the current namespace.
   If you want to specify a site name, use `skupper init  --site-name <site-name>`.
   4. The version of {skupper-name} running the site.
   The site version can be different from the current `skupper` CLI version.
   To update a site to the version of the CLI, use `skupper update`.
   5. The name of a service exposed on the {service-network}.
   6. The address of a service exposed on the {service-network}.
   7. The protocol of a service exposed on the {service-network}.
   8. The unique identifier of a remote site on the {service-network}.
   9. The sites that the remote site is linked to.
   10. The name of the local Kubernetes object that is exposed on the {service-network}.
   In this example, this is the `hello-world-backend` pod.

   <dl><dt><strong>📌 NOTE</strong></dt><dd>

   The URL for the east site has no value because that site was initialized without ingress using the following command:
   ```
   $ skupper init --ingress none
   ```
   </dd></dl>
