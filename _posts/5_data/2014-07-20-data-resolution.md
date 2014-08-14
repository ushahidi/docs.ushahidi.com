---
layout: post_guide
doc_element: 5
title: Spatial Resolution
date: {}
published: true
tags: 
  - guide
editor: shadrock
---

### Spatial Resolution: what do you need?
Reports and accompanying content can be georeferenced in Ushahidi to paint a better picture of what is happening where. However, a report’s level of geographic precision can vary greatly across different Ushahidi deployments or even across reports within a single deployment. By striving for a consistent level of precision, you will provide a more accurate picture of what is happening; your data will be more useful for analysis; and your deployment will gain credibility from your attention to detail. The most important question to ask yourself is, “how precise do I need to be?”

We find it easiest to understand geographic precision as analogous to the level of “zoom” found on most web maps. A brief experiment will help you understand this: open any web map that allows you to drop a marker. Pan over the general area in which you are located, while staying zoomed out so that individual buildings or roads are not easy to pick out. Drop a marker at your approximate location. At this “zoom” or “scale” the marker probably does a pretty good job of communicating where you are. It may show that you are in a particular village, city, or region. Now, zoom in as close as possible to that marker: is it precisely where you are? Is it miles or kilometers away? Is it city blocks away? Is it in the middle of a lake or distant mountain range? Leave this marker where it is and now find your location as precisely as you can by panning around and zooming in and out until you can find building you are in or that is nearest to you. Drop another marker but this time make it as precise as possible. Now zoom slowly out. At first the two markers may seem very far apart. As you zoom out, however, the markers will come closer together: and possibly converge altogether. **Georeferencing reports at different zoom levels changes their geographic precision: reports made at different levels of zoom are not as comparable geographically as reports made at the same level.** 

If your deployment requires very precise geographic information, such as the location of services that need to be repaired in a small city, all reports should be georeferenced as precisely as possible. If, on the other hand, your deployment is comparing the number of newspapers printed in cities across the country, or globe, then reports can be georeferenced while being “zoomed out” as long as the report falls generally within the boundaries of a city. 

Ultimately, the level of geographic precision you need is up to you and dependent on what you are reporting on and trying to convey. However, you should strive for consistency since the act of dropping a marker in an Ushahidi deployment automatically generates an exact latitude and longitude for the location of the marker on the surface of the Earth. Your computer does not know the difference between precisely georeferencing a report to an exact building or generally indicating a city. Analysts who acquire your data via download, API endpoints, or otherwise will likely assume – based on the presence of latitude and longitude coordinates – that all markers are meant to be exact locations. If they are not exact, or are not meant to be exact, the reports you have collected may give misleading or completely erroneous results when being analyzed. 
