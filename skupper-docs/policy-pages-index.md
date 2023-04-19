endif::mod-loc[]
[id="skupper-policy"] 
= Securing a {service-network} using policies

By default, {skupper-name} includes many security features, including using mutual TLS for all {service-network} communication between sites.
By default, applying the {policy-system} to a cluster prevents all {service-network} communication to and from that cluster.
You specify granular policies to allow only the {service-network} communication you require.

**📌 NOTE**\
The {policy-system} is distinct from the `network-policy` option which restricts access to {skupper-name} services to the current namespace as described in {skupperclibooklink}.

Each site in a {service-network} runs a {skupper-router} and has a private, dedicated certificate authority (CA).
Communication between sites is secured with mutual TLS, so the {service-network} is isolated from external access, preventing security risks such as lateral attacks, malware infestations, and data exfiltration.
The {policy-system} adds another layer at a cluster level to help a cluster administrator control access to a {service-network}.

This guide assumes that you understand the following {skupper-name} concepts:

* **site**\
A namespace in which {skupper-name} is installed.
* **token**\
A token is required to establish a link between two sites. 
* **{service-network}**\
After exposing services using {skupper-name}, you have created a {service-network}.

[id="about-skupper-policies"] 
== About the {policy-system}

After a cluster administrator installs the {policy-system} using a Custom Resource Definition (CRD), the cluster administrator needs to configure one or more policies to allow _developers_ create and use services on the {service-network}.

**📌 NOTE**\
In this guide, _developers_ refers to users of a cluster who have access to a namespace, but do not have administrator privileges.

A cluster administrator configures one or more of following items using custom resources (CRs) to enable communication:

* **Allow incoming links**\
Use `allowIncomingLinks` to enable developers create tokens and configure incoming links.
* **Allow outgoing links to specific hosts**\
Use `allowedOutgoingLinksHostnames` to specify hosts that developers can create links to.
* **Allow services**\
Use `allowedServices` to specify which services developers can create or use on the {service-network}.
* **Allow resources to be exposed**\
Use `allowedExposedResources` to specify which resources a developer can expose on the {service-network}.

**📌 NOTE**\
A cluster administrator can apply each policy CR setting to one or more namespaces.

For example, the following policy CR fully allows all {skupper-name} capabilities on all namespaces, except for:

* only allows outgoing links to any domain ending in `.example.com`.
* only allows 'deployment/nginx' resources to be exposed on the {service-network}.

```yaml
apiVersion: skupper.io/v1alpha1
kind: SkupperClusterPolicy
metadata:
  name: cluster-policy-sample-01
spec:
  namespaces:
    - "*"
  allowIncomingLinks: true
  allowedExposedResources:
    - "deployment/nginx"
  allowedOutgoingLinksHostnames: [".*\\.example.com$"]
  allowedServices:
    - "*"
```

<dl><dt><strong>📌 NOTE</strong></dt><dd>

You can apply many policy CRs, and if there are conflicts in the items allowed, the most permissive policy is applied.
For example, if you apply an additional policy CR with the line `allowedOutgoingLinksHostnames: []`, which does not list any hostnames, outgoing links to `*.example.com` are still permitted because that is permitted in the original CR.
</dd></dl>

* **`namespaces`**\
One or more patterns to specify the namespaces that this policy applies to.
Note that you can use [Label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to match the namespaces.
* **`allowIncomingLinks`**\
Specify `true` to allow other sites create links to the specified namespaces.
* **`allowedOutgoingLinksHostnames`**\
Specify one or more patterns to determine which hosts you can create links to from the specified namespaces.
* **`allowedServices`**\
Specify one or more patterns to determine the permitted names of services allowed on the {service-network} from the specified namespaces.
* **`allowedExposedResources`**\
Specify one or more permitted names of resources allowed on the {service-network} from the specified namespaces. 
Note that patterns are not supported. 

<dl><dt><strong>💡 TIP</strong></dt><dd>

Use regular expressions to create pattern matches, for example:

* `.*\\.com$` matches any string ending in `.com`.
A double backslash is required to avoid issues in YAML.
* `^abc$` matches the string `abc`.

</dd></dl>

If you create another CR that allows outgoing links for a specific namespace, a user can create a link from that namespace to join a {service-network}. That is, the logic for multiple policy CRs is `OR`.
An operation is permitted if any single policy CR permits the operation.

[id="installing-crd"] 
== Installing the {policy-system} CRD

Installing the {policy-system} CRD enables a cluster administrator to enforce policies for {service-network}s.

**📌 NOTE**\
If there are existing sites on the cluster, see [installing-crd-existing-sites](#installing-crd-existing-sites) to avoid {service-network} disruption.

* Access to a cluster using a `cluster-admin` account
* The Skupper operator is installed

1. Log in to the cluster using a `cluster-admin` account.
2. Download the CRD:

   ```bash
   $ wget https://raw.githubusercontent.com/skupperproject/skupper/1.0/api/types/crds/skupper_cluster_policy_crd.yaml
   ```
3. Apply the CRD:

   ```bash
   $ kubectl apply -f skupper_cluster_policy_crd.yaml

   customresourcedefinition.apiextensions.k8s.io/skupperclusterpolicies.skupper.io created
   clusterrole.rbac.authorization.k8s.io/skupper-service-controller created
   ```
4. To verify that the {policy-system} is active, use the `skupper status` command and check that the output includes the following line:

   ```bash
   Skupper is enabled for namespace "<namespace>" in interior mode (with policies).
   ```
