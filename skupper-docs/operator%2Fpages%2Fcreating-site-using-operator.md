## Creating a site using the Skupper Operator

1. Create a YAML file defining the ConfigMap of the site you want to create.

   For example, create `skupper-site.yaml` that provisions a site with a console:

   ```yaml

   ```

   **📌 NOTE**\
   The console is a preview feature and may change before becoming fully supported by [skupper.io](https://skupper.io).
   Currently, you must enable the console on the same site as you enable the flow collector. This requirement may change before the console is fully supported by [skupper.io](https://skupper.io).

   You can also create a site without a console:

   ```yaml
   ```
2. Apply the YAML to create a ConfigMap named `skupper-site` in the namespace you want to use:

   ```bash
   $ kubectl apply -f skupper-site.yaml
   ```
3. Verify that the site is created by checking that the Skupper router and service controller pods are running:

   ```bash
   $ kubectl get pods

   NAME                                          READY   STATUS    RESTARTS   AGE
   skupper-router-8c6cc6d76-27562                1/1     Running   0          40s
   skupper-service-controller-57cdbb56c5-vc7s2   1/1     Running   0          34s
   ```

   **📌 NOTE**\
   If you deployed the Operator to a single namespace, an additional site controller pod is also running.
