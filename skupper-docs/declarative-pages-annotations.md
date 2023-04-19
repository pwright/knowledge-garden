[id="skupper-annotations"] 
= Configuring services using annotations

After creating and linking sites, you can use Kubernetes annotations to control which services are available on the {service-network}.

[id="exposing-services-annotations"] 
== Exposing simple services on a {service-network} using annotations

This section provides an alternative to the `skupper expose` command, allowing you to annotate existing resources to expose simple services on the {service-network}.

* A site with a service you want to expose

1. Log into the namespace in your cluster that is configured as a site.
2. Create a deployment, some pods, or a service in one of your sites, for example:

   ```
   $ kubectl create deployment hello-world-backend --image quay.io/skupper/hello-world-backend
   ```

   This step is not {skupper-name}-specific, that is, this process is unchanged from standard processes for your cluster.
3. Annotate the kubernetes resource to create a service that can communicate on the {service-network}, for example:

   ```
   $ kubectl annotate deployment backend "skupper.io/address=backend" "skupper.io/port=8080" "skupper.io/proxy=tcp"
   ```

   The annotations include:

   * `skupper.io/proxy` - the protocol you want to use, `tcp`, `http` or `http2`.
   This is the only annotation that is required.
   For example, if you annotate a simple deployment named `backend` with `skupper.io/proxy=tcp`, the service is exposed as `backend` and the `containerPort` value of the deployment is used as the port number.
   * `skupper.io/address` - the name of the service on the {service-network}. 
   * `skupper.io/port` - one or more ports for the service on the {service-network}. 

   <dl><dt><strong>📌 NOTE</strong></dt><dd>

   When exposing services, rather than other resources like deployments, you can use the `skupper.io/target` annotation to avoid modifying the original service.
   For example, if you want to expose the `backend` service:
   ```
   $ kubectl annotate service backend "skupper.io/address=van-backend" "skupper.io/port=8080" "skupper.io/proxy=tcp" "skupper.io/target=backend"
   ```
   This allows you to delete and recreate the `backend` service without having to apply the annotation again.
   </dd></dl>
4. Check that you have exposed the service:

   ```
   $ skupper service status
   Services exposed through Skupper:
   ╰─ backend (tcp port 8080)
      ╰─ Targets:
         ╰─ app=hello-world-backend name=hello-world-backend
   ```

   **📌 NOTE**\
   The related targets for services are only displayed when the target is available on the current cluster.

[id="understanding-annotations"] 
== Understanding Skupper annotations

Annotations allow you to expose services on the {service-network}.
This section provides details on the scope of those annotations

* **skupper.io/address**\
The name of the service on the {service-network}.
Applies to:
  * Deployments
  * StatefulSets
  * DaemonSets
  * Services
* **skupper.io/port**\
The port for the service on the {service-network}.
Applies to:
  * Deployments
  * StatefulSets
  * DaemonSets
* **skupper.io/proxy**\
The protocol you want to use, `tcp`, `http` or `http2`.
Applies to:
  * Deployments
  * StatefulSets
  * DaemonSets
  * Services
* **skupper.io/target**\
The name of the target service you want to expose.
Applies to:
  * Services
* **skupper.io/service-labels**\
A comma separated list of label keys and values for the exposed service.
You can use this annotation to set up labels for monitoring exposed services.
Applies to:
  * Deployments
  * DaemonSets
  * Services
