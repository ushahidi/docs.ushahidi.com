---
layout: page
title:  "Getting Started"
subtitle: "Getting Ushahidi installed"
date:   2015-04-23 22:53:00
categories: top
weight: 1
---

Ushahidi Platform can be installed on several operating systems. We have different instructions depending on what type of user you are:

### Just trying it out?

* [Installing on Heroku](/getting-started/installing-on-heroku.html)
* [Install with Vagrant + a NodeJS dev server](/getting-started/installing-with-vagrant.html)

### Installing in production

* [Install on Linux](/getting-started/installing-on-linux.html)
* Not recommended: Windows or Mac

### Getting set up for development

* [Install with Vagrant + a NodeJS dev server](/getting-started/installing-with-vagrant.html)

### After install

* ...

{% assign pages = (site.pages | sort: "weight" | where: "categories", "getting-started" | where: "hideFromMenu", false)  %}
