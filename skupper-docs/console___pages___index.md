
sid:: skupper-console 
# Using the Skupper console

By default, when you create a {skupper-name} site, you also enable the Skupper console.
The Skupper console URL is displayed whenever you check site status using `skupper status`.

sid:: accessing-console 
## Accessing the Skupper console

By default, the Skupper console is available whenever you create a {service-network} router and is protected by credentials available in the `skupper-console-users` secret.

1. Determine the Skupper console URL using the `skupper` CLI, for example:

   ```
   $ skupper status
   Skupper is enabled for namespace "west" in interior mode. It is not connected to any other sites. It has no exposed services.
   The site console url is:  https://skupper-west.apps-crc.testing
   ```
2. Browse to the Skupper console URL. 
The credential prompt depends on how the site was created using `skupper init`:

   * using the `--console-auth unsecured` option, you are not prompted for credentials.
   * using the `--console-auth openshift` option, you are prompted to enter OpenShift cluster credentials.
   * using the default or `--console-user <user>  --console-password <password>` options, you are prompted to enter those credentials.
3. If you created the site using default settings, that is `skupper init`, a random password is generated for the `admin` user.
To retrieve the password the `admin` user:

   ```
   $ kubectl get secret skupper-console-users -o jsonpath={.data.admin} | base64 -d
   JNZWzMHtyg
   ```

sid:: linking-sites-using-skupper-console 
## Linking sites using the Skupper console

The Skupper console allows you create and use claim type tokens as described in {SkupperCliBookLink}.

* Two sites, each with Skupper console enabled
* Google Chrome browser

**📌 NOTE**\
Your browser may prompt you to allow using the clipboard. You must accept that prompt for this procedure.

1. Log into the console for the first site.
2. Navigate to **Site** in left hand menu.
3. Click **Link a remote site** to display the steps for linking.
4. Click **Copy a token to the clipboard**.
5. Log into the console for the second site.
6. Navigate to **Site** in left hand menu.
7. Click **Use a token** to accept the token from the first site.
8. Verify that the sites are linked by Checking that both sites are listed in the **Network details** section of the **Site** page.

sid:: exploring-console 
## Exploring the Skupper console

The Skupper console provides an overview of the following:

* Services - services that are exposed on the {service-network}, both local and remote.
* Sites - {skupper-name} installations on the current {service-network}.
* Deployments - deployments relating to exposed services.

The Skupper console also provides useful networking information about the {service-network}, for example, traffic levels between sites.

![{img-loc}skupper-console]({img-loc}skupper-console.png)

1. Perform the {SkupperOpenShiftBookLink} tutorial.
2. Navigate to the Skupper console.
3. Click the **Network** menu item.
Both the **east** and **west** sites should be displayed in circles.
4. Drag the **west** circle to be on the left of the **east** circle.
5. Click the **Table** tab to display the sites as text items.
This view allows you drill down into details relating to the selected site.
6. Click the **Deployments** menu item.
This view shows you any deployments that are exposed as services on the {service-network}.
In this case, the console displays the **hello-world-backend (east)** deployment.
7. Click the **Services** menu item to display details for all services exposed on the {service-network}.

   **📌 NOTE**\
   Although two services are involved in the tutorial, only one service, `hello-world-backend` is exposed on the {service-network}.
8. Click the **Site** menu.
This page shows:
   * The number of sites in the {service-network}.
   * The services that are exposed on the {service-network}.
   * The gateways that are defined in the {service-network}.
   * The traffic for the current site.
