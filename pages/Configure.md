- The easiest way to configure a site is to install the `skupper` [CLI](https://skupper.netlify.app/skupper/latest/cli/index.html).
  collapsed:: true
	- You can also use [yaml](https://skupper.netlify.app/skupper/latest/declarative/index.html).
	- You can also use the [operator](https://skupper.netlify.app/skupper/latest/operator/index.html).
- Typically, you only configure a site when initialising skupper, for example: `skupper init --ingress none`
  collapsed:: true
  creates a skupper site that you cannot link to from other sites.
	- If you want a specific ingress type, you can specify that:
	  `skupper init --ingress nodeport`
	- See