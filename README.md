# UAAccess website

[visit the site](https://uaaccess.org/)

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

The site and it's associated HTML can now be found under the output directory (src/output/). You can make modifications to any of the content in the "src" directory, and run `nikola build` as many times as needed to render it again.

To run the website on the local network and open it up in the default browser:

```
$ nikola serve -b
```

## Going live

This repository is made up of two important branches to be aware of:

* main: Contains the code for the site that hasn't yet been rendered.
* deploy: Contains only the HTML. This is the branch that is actually served by GitHub pages.

If you have made modifications to the sites files, posts, pages, etc.

* Checkout the main branch: `git checkout main`
* Run `nikola github_deploy`
