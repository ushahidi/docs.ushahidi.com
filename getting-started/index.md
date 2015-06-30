---
layout: page
title:  "Getting Started"
subtitle: "Getting Ushahidi installed"
date:   2015-04-23 22:53:00
categories: top
weight: 1
---

{% assign pages = (site.pages | where: "categories", "getting-started" | where: "hideFromMenu", false)  %}

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