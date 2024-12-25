# UAAccess website

UAAccess website, currently configured to run on GitHub pages.

We are using [Nikola](https://getnikola.com/) in the interests of quick setup and rapid deployment.

## Building

Assuming you have a Python installation with version 3.12 or later.

```
$ git clone https://github.com/uaaccess/uaaccess.git
$ pip install nikola
$ cd src
$ nikola build
```

To run the website on the local network and open it up in a browser:

```
$ nikola serve -b
```
