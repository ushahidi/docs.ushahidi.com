---
layout: page
title:  "Developer Guide"
subtitle: "A guide for developing Ushahidi"
date:   2015-04-23 22:53:00
categories: top
weight: 3
---

First, thank you for contributing to the Ushahidi Platform code - thousands of
groups use this platform worldwide, and your work will help benefit all of
them.

Ushahidi Platform is an open source web application. It collects information
from SMS, Twitter (pending), RSS feeds, Email and direct reports to a
platforms website. It helps users process that information, categorize it,
geo-locate it, visualise it and publish it on a map.

Ushahidi Platform V3 is a rebuild from the ground up -- not only the code but
the way in which we think about users interacting with mobile and social data.

The [ushahidi platform stack
](https://github.com/ushahidi/platform/blob/master/LICENSE.md)is:

  * Back-end: [Linux](http://en.wikipedia.org/wiki/Linux), [PHP](https://php.net), [Apache](http://httpd.apache.org/)/[Nginx](http://wiki.nginx.org/Main), [MySQL](http://www.mysql.com) or [PostgreSQL](http://www.postgresql.org)

  * Front-end: [AngularJS](https://angularjs.org), [Javascript](http://en.wikipedia.org/wiki/JavaScript), [Html](http://en.wikipedia.org/wiki/HTML), [CSS](http://en.wikipedia.org/wiki/Cascading_Style_Sheets). Built with [NodeJS](http://nodejs.org) and [Browserify](http://browserify.org/). Using [Leaflet](http://leafletjs.com) for mapping, and a collection of other frontend libraries

Ushahidi Platform will run on any platform that supports PHP, including Linux,
Mac OSX and Windows.

### Get started:

  1. [Installing the Ushahidi Platform](/getting-started/)
  2. [Connecting with other developers](/get-involved.html)
  3. Adding code the the Ushahidi Platform

{% assign pages = (site.pages | where: "categories", "dev-guide" | where: "hideFromMenu", false)  %}

<div class="cards-select">
    {% for p in pages %}
    <div class="selection-card">
        <a href="{{ p.url }}">
            <h3>{{p.title}}</h3>
            <p>
                {{p.subtitle}}
            </p>
        </a>
    </div>
    {% endfor %}
</div><!--end cards select-->