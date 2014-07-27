---
layout: guide
title: Guide
permalink: /guide.html

---

The homepage for the Guide. [Links to the outline](outline.html).

<ul class="posts">
{% for post in site.tags.guide limit: 20 %}
  <div class="post_info">
    <li>
         <a href="{{ post.url }}">{{ post.title }}</a>
         <span>({{ post.date | date:"%Y-%m-%d" }})</span>
    </li>
    </div>
  {% endfor %}
</ul>