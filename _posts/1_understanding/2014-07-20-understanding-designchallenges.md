---
layout: post_guide
chapter: 1
doc_element: 2
title: Design Challenges
date: 2014-07-20
published: true
tags: 
  - guide
editor: jcrowley
layout: post_guide
---

## Why v3: Smallsurfaces and the design challenges of v3

The Ushahidi team took the task of rearchictecting the v2 software to heart. To guide the process, we hired the firm, Small Surfaces to go deeper into the issues that deployers, developers, journalists, and participants had experienced around the deployments of the v2 platform.

Methodology used. Interviews with key audiences...

### Data over time

Reports are not as atomic as they first seem. Need to provide means to develop context around them, show change and evolution of reports over time as team makes sense of complex situations...


### Visualization

Maps are not the only means of visualizing reports, nor are the maps in v2 the only way to use maps...


### Management

Toggling between a reporting and administrative interface was tedious and unnecessary. But permissioning and management of a single interface would require deep rethinking about how users interact with the platform. 


### Code Maintenance

The PHP code was built on Kohana. It had become bloated and hard to add new features.


### Security

Code which is difficult to follow is difficult to secure. Ushahidi received numerous criticisms for security of its code and (by extension) for the data collected from participants.


---
