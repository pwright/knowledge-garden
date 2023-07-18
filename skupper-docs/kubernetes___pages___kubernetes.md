
:sectnums:
sid:: k8s-tutorial 
# Creating a {service-network} with Kubernetes

This tutorial demonstrates how to connect a frontend service on a {kubernetes-flavor} cluster with a backend service on a {kubernetes-flavor} cluster using the `skupper` command-line interface (CLI).

See {SkupperOverviewBookLink} for an introduction to {skupper-name}.

* Access to namespaces in two {kubernetes-flavor} clusters, `cluster-admin` access is not required.
* One of the {kubernetes-flavor} clusters must be addressable from the other cluster.
* `kubectl` CLI. Many commands can be performed on OpenShift using `oc`, however this tutorial shows the `kubectl` options.

This tutorial shows how to connect the following namespaces:

* `west` - runs the frontend service and is typically a public cluster.
* `east` - runs the backend service.

sid:: configuring-consoles 
## Configuring terminal sessions

This procedure describes how to configure your terminal sessions to use configurations to avoid problems as you configure {skupper-name} on different clusters.

The following table shows how you might set up your terminal sessions.

**Terminal sessions**

| west terminal session | east terminal session |
| --- | --- |
```bash
 $ kubectl get pods
```
|  |  |
```bash
 $ kubectl get pods

```

1. Start a terminal session to work on the `west` namespace and set the `KUBECONFIG` environment variable:

   ```bash
   $ export KUBECONFIG=$HOME/.kube/config-west
   ```

   This session is referred to later as the _west_ terminal session.
2. Start a terminal session to work on the `east` namespace and set the `KUBECONFIG` environment variable:

   ```bash
   $ export KUBECONFIG=$HOME/.kube/config-east
   ```

   This session is referred to later as the _east_ terminal session.
3. In each terminal session, log into the {kubernetes-flavor} cluster.

sid:: installing-skupper 
## Installing the {service-network} router in both clusters

1. In the west terminal session:
   1. Create the `west` namespace:

      ```bash
      $ kubectl create namespace west
      $ kubectl config set-context --current --namespace west
      ```
   2. Create the {service-network} router:

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
2. In the east terminal session:
   1. Create the `east` namespace:

      ```bash
      $ kubectl create namespace east
      $ kubectl config set-context --current --namespace east
      ```
   2. Create the {service-network} router:

      ```bash
      $ skupper init
      ```
   3. Check the site status:

      ```bash
      $ skupper status
      ```
      The output should be similar to the following:
      ```
      Skupper enabled for namespace 'east'. It is not connected to any other sites.
      ```

sid:: connecting-namespaces 
## Connecting namespaces to create a {service-network}

With the {service-network} routers installed, you can connect them together securely and allow service sharing across the {service-network}.

1. In the west terminal session, create a connection token to allow connection to the west namespace:

   ```bash
   $ skupper token create $HOME/secret.yaml
   ```

   This command creates the `secret.yaml` file in your home directory, which you can use to create the secure connection.
2. In the east terminal session, use the token to create a connection to the west namespace:

   ```bash
   $ skupper link create $HOME/secret.yaml
   ```
3. Check the site status from the west terminal session:

   ```bash
   $ skupper status
   ```
   The output should be similar to the following:
   ```
   Skupper is enabled for namespace "west" in interior mode. It is connected to 1 other site. It has no exposed services.
   The site console url is:  https://<skupper-url>
   The credentials for internal console-auth mode are held in secret: 'skupper-console-users'
   ```

sid:: frontend 
## Creating the frontend service

The frontend service is a simple Python application that displays a message from the backend application.

Perform all tasks in the west terminal session:

1. Deploy the frontend service:

   ```bash
   $ kubectl create deployment hello-world-frontend --image quay.io/skupper/hello-world-frontend
   ```
2. Expose the frontend deployment as a cluster service:

   ```bash
   $ kubectl expose deployment hello-world-frontend --port 8080 --type LoadBalancer
   ```
3. Check the frontend route:
   1. Get the route details:

      ```bash
      $  kubectl get service/frontend
      ```

      The output should be similar to the following:

      ```
      NAME                   HOST/PORT                                   
      NAME       TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)          AGE
      frontend   LoadBalancer   10.103.232.28   <external-ip>   8080:30407/TCP   15s
      ```
   2. Navigate to the `<frontend-ip>:8080` URL in your browser, you see a message similar to the following because the frontend cannot communicate with the backend yet:

      ```
      Trouble! HTTPConnectionPool(host='hello-world-backend', port=8080): Max retries exceeded with url: /api/hello (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7fbfcdf0d1d0>: Failed to establish a new connection: [Errno -2] Name or service not known'))
      ```

      To resolve this situation, you must create the backend service and make it available on the {service-network}.

sid:: backend 
## Creating the backend service and making it available on the {service-network}

The backend service runs in the `east` namespace and is not available on the {service-network} by default.
You use the `skupper` command to expose the service to all namespaces on the {service-network}.
The backend app is a simple Python application that passes a message to the frontend application.

1. Deploy the backend service in the east terminal session:

   ```bash
   $ kubectl create deployment hello-world-backend --image quay.io/skupper/hello-world-backend
   ```
2. Expose the backend service on the {service-network} from the east terminal session:

   ```bash
   $ skupper expose deployment hello-world-backend --port 8080 --protocol tcp
   ```
3. Check the site status from the west terminal session:

   ```bash
   $ skupper status
   ```
   The output should be similar to the following:
   ```
   Skupper is enabled for namespace "west" in interior mode. It is connected to 1 other site. It has 1 exposed service.
   ```
   The service is exposed from the `east` namespace.
4. Check the frontend route in the west terminal session:
   1. Get the route details:

      ```bash
      $  oc get routes
      ```

      The output should be similar to the following:

      ```
      NAME                   HOST/PORT                                   
      hello-world-frontend   <frontend-url>       
      ```
   2. Navigate to the `<frontend-url>` value in your browser, you see a message similar to the following:

      ```
      Hi, <name>. I am Mathematical Machine (backend-77f8f45fc8-mnrdp).
      ```

      If you click **Say hello** again, a different backend process responds showing how {skupper-name} balances the requests.

This shows how the frontend calls the backend service over the {service-network} from a different {kubernetes-flavor} cluster.

* {SkupperConsoleBookLink}
* {SkupperCliBookLink}

sid:: tearing-down 
## Tearing down the {service-network}

This procedure describes how to remove the {service-network} you created.

1. Delete the `west` namespace from the west terminal session:

   ```bash
   $ kubectl delete namespace west
   ```
2. Delete the `east` namespace from the east terminal session:

   ```bash
   $ kubectl delete namespace east
   ```
