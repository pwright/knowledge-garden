endif::mod-loc[]
:sectnums:

[id="gateway-tutorial"] 
= Creating a {service-network} with Kubernetes and accessing a backend service using a gateway

This tutorial describes how to connect a local backend service on a local machine with a frontend service running on a {kubernetes-flavor} cluster. 

In this tutorial, the services are the same as used in {SkupperOpenShiftBookLink}, however you run the backend service locally and expose the service on the service network using the `skupper` command-line interface (CLI).

* Access to a projects in a {kubernetes-flavor} cluster, `cluster-admin` access is not required.
* Python on your local machine.

This tutorial shows how to connect the following:

* `west` - a namespace in an accessible cluster running the frontend service.
* `hello-world-backend` - a Python service running on a local machine.

**📌 NOTE**\
Although this tutorial demonstrates exposing a Python service on the {service-network}, a more typical use case would involve a database service, for example, MySQL.

[id="introduction-to-skupper"] 
== Introduction to {skupper-name} {product-version}

A {service-network} enables communication between services running in different network locations. 
It allows geographically distributed services to connect as if they were all running in the same site.

![Overview of a service network]({image-prefix}overview-gateway.png)

For example, you can deploy your frontend in a public {kubernetes-flavor} cluster and deploy your backend on a local network, then connect them into a {service-network}.

You deploy and manage a {service-network}, including a gateway, using the `skupper` CLI.

* {SkupperOverviewBookLink}

[id="creating-backend"] 
== Creating a backend service

This procedure describes how to create a backend service on your local machine that is accessed from the {service-network}.

* Python

1. Clone the [skupper-example-hello-world](https://github.com/skupperproject/skupper-example-hello-world) repo.
2. Change to the service directory.

   ```bash
   $ cd skupper-example-hello-world/backend/
   ```
3. Install the required libraries.

   ```bash
   $ pip install --user flask starlette uvicorn

   ```
4. Run the backend service

   ```bash
   $ python ./main.py
   ```
   The output is similar to the following:

   ```bash
   INFO:     Started server process [107836]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
   ```
5. Test the service by navigating to the following URL.

   ```bash
   http://localhost:8080/api/hello
   ```

   The output is similar to the following:

   ```bash
   Hello from workstation (1)
   ```
   This indicates that the backend service is running and available.

[id="configuring-consoles"] 
== Logging into cluster

* The kubectl CLI is installed.

1. Start a terminal session to work on the `west` namespace and set the `KUBECONFIG` environment variable:

   ```bash
   $ export KUBECONFIG=$HOME/.kube/config-west
   ```

   This session is referred to later as the _west_ terminal session.
2. Log into the {kubernetes-flavor} cluster.

[id="installing-skupper"] 
== Creating a skupper site

1. Create the `west` namespace:

   ```bash
   $ kubectl create namespace west
   $ kubectl config set-context --current --namespace west
   ```
2. Create the {service-network} site:

   ```bash
   $ skupper init
   ```
3. Check the site status:

   ```bash
   $ skupper status
   ```
   The output should be similar to the following:
   ```
   Skupper enabled for namespace 'west'. It is not connected to any other sites.
   ```

[id="frontend"] 
== Creating the frontend service

The frontend service is a simple Python application that displays a message from the backend application.

Perform all tasks in the west terminal session:

1. Deploy the frontend service:

   ```bash
   $ kubectl create deployment hello-world-frontend --image quay.io/skupper/hello-world-frontend
   ```
2. Expose the frontend deployment:

   ```bash
   $ kubectl expose deployment hello-world-frontend --port 8080 --type LoadBalancer
   ```
3. Find the external IP address for the frontend:

   ```bash
   $ kubectl get service/frontend
   ```
4. Check the frontend route:
   1. Get the route details:

      ```bash
      $  oc get routes
      ```

      The output should be similar to the following:

      ```
      NAME                   HOST/PORT                                   
      hello-world-frontend   <frontend-url>       
      ```
   2. Navigate to the `<frontend-url>` value in your browser, you see a message similar to the following because the frontend cannot communicate with the backend yet:

      ```
      Trouble! HTTPConnectionPool(host='hello-world-backend', port=8080): Max retries exceeded with url: /api/hello (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fbfcdf0d1d0>: Failed to establish a new connection: [Errno -2] Name or service not known'))
      ```

      To resolve this situation, you must make the backend service available on the {service-network} using a gateway.

[id="gateway"] 
== Creating and using a Skupper gateway

This procedure describes how to create a gateway and make a backend service available on the {service-network}.

* Skupper router is installed on local machine

1. Create a gateway:

   ```bash
   $ skupper gateway init --type podman
   ```
2. Create a {skupper-name} service:

   ```bash
   $ skupper service create hello-world-backend 8080
   ```
3. Bind the local backend service to the {skupper-name} service:

   ```bash
   $ skupper gateway bind hello-world-backend <backend-ip-address> 8080
   ```
   where the &lt;backend-ip-address is the address you noted in [creating-backend](#creating-backend)
4. Check the gateway status:

   ```bash
   $ skupper gateway status
   ```

   The output should be similar to following:

   ```bash
   Gateway Definitions:
   ╰─ <machine>-<user> type: podman version: 1.17.1
    ╰─ Bindings:
       ╰─ hello-world-backend:8080 tcp hello-world-backend:8080 <backend-ip-address> 8080

   ```

[id="check"] 
== Checking service access from the frontend

1. Get the URL details:

   ```bash
   $ kubectl get service hello-world-frontend -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
   ```

   Use the output IP address to construct the &lt;frontend-url>:
   ```
   <cluster-ip-address>:8080/
   ```
2. Navigate to the `<frontend-url>` value in your browser and click **Say hello**. 
You see a message similar to the following:

   ```
   Hi, <name>. I am Mathematical Machine (backend-77f8f45fc8-mnrdp).
   ```

   If you click **Say hello** again, a different backend process responds showing how {skupper-name} balances the requests.

This shows how the frontend calls the backend over the {service-network} from an {kubernetes-flavor} cluster.

* {SkupperConsoleBookLink}
* {SkupperCliBookLink}

[id="tearing-down"] 
== Tearing down the {service-network}

This procedure describes how to remove the {service-network} you created.

1. Delete the gateway:

   ```bash
   $  skupper gateway delete 
   ```
2. Delete the `west` namespace from the west terminal session:

   ```bash
   $  kubectl delete namespace west
   ```
