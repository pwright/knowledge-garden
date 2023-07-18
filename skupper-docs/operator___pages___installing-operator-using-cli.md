## Installing the Operator using the CLI

The steps in this section show how to use the `kubectl` command-line interface (CLI) to install and deploy the latest version of the {SkupperOperatorName} in a given {kubernetes-flavor} cluster.

* The Operator Lifecycle Manager is installed in the cluster.
For more information, see the [QuickStart](https://olm.operatorframework.io/docs/getting-started/).

1. Download the Skupper Operator example files, for example:

   ```
   $ wget https://github.com/skupperproject/skupper-operator/archive/refs/heads/main.zip
   ```
2. Create a `my-namespace` namespace.
NOTE: If you want to use a different namespace, you need to edit the referenced YAML files.
   1. Create a new namespace:

      ```bash
      $ kubectl create namespace my-namespace
      ```
   2. Switch context to the namespace:

      ```bash
      $ kubectl config set-context --current --namespace=my-namespace
      ```
3. Create a CatalogSource in the `openshift-marketplace` namespace:

   ```bash
   $ kubectl apply -f examples/k8s/00-cs.yaml
   ```
4. Verify the skupper-operator catalog pod is running before continuing:

   ```bash
   $ kubectl -n olm get pods | grep skupper-operator
   ```
5. Create an OperatorGroup in the `my-namespace` namespace:

   ```bash
   $ kubectl apply -f examples/k8s/10-og.yaml
   ```
6. Create a Subscription  in the `my-namespace` namespace:

   ```bash
   $ kubectl apply -f examples/k8s/20-sub.yaml
   ```
7. Verify that the Operator is running:

   ```bash
   $ kubectl get pods -n my-namespace

   NAME                                     READY   STATUS    RESTARTS   AGE
   skupper-site-controller-d7b57964-gxms6   1/1     Running   0          1m
   ```

   If the output does not report the pod is running, use the following command to determine the issue that prevented it from running:

   ```
   $ kubectl describe pod -l name=skupper-operator
   ```
