---
layout: page
title:  "Installing Ushahidi"
subtitle: ""
date:   2015-04-23 22:53:00
categories: top
weight: 1
---

Ushahidi Platform can be installed on several operating systems. We have different instructions depending on what type of user you are:

### Just trying it out?

* [Installing on Heroku](/install/installing-on-heroku.html)
* [Install with Vagrant + a NodeJS dev server](/install/installing-with-vagrant.html)

### Installing in production

* [Install on Linux](/install/installing-on-linux.html)
* Not recommended: Windows or Mac

### Getting set up for development

* [Install with Vagrant + a NodeJS dev server](/install/installing-with-vagrant.html)

### After install

* Video tutorials coming soon

{% assign pages = (site.pages | sort: "weight" | where: "categories", "install" | where: "hideFromMenu", false)  %}
