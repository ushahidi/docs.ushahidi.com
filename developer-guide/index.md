---
layout: page
title:  "Developer Guide"
subtitle: "A guide for developing Ushahidi"
date:   2015-04-23 22:53:00
categories: top
weight: 3
---

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