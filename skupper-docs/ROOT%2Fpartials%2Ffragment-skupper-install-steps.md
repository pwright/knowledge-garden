1. Install the `skupper` command-line interface.

   For Linux:
   ```
   $ curl -fL https://github.com/skupperproject/skupper/releases/download/{skupper-version}/skupper-cli-{skupper-version}-linux-amd64.tgz | tar -xzf -
   ```

   For MacOS:
   ```
   $ curl -fL https://github.com/skupperproject/skupper/releases/download/{skupper-version}/skupper-cli-{skupper-version}-mac-amd64.tgz | tar -xzf -
   ```
2. Copy the `skupper` executable to a directory in your $PATH:

   ```
   $ mkdir -p $HOME/bin
   $ export PATH=$PATH:$HOME/bin
   $ mv skupper $HOME/bin
   ```
