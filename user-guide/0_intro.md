---
layout: page
title:  "Introduction"
subtitle: "Ushahidi as Testimony"
date:   2015-03-24 17:31:20
categories: chapter
weight: 0
---

> “People become the stories they hear and the stories they tell.”
>
> —    Elie Wiesel, Nobel Laureate for Peace

Ushahidi was born from calamity. When the 2008 Kenyan elections descended into social conflict, a few of us who came together around an idea. As activists and technologists, we asked: what if we created a platform that would allow Kenyans to report incidents of violence in their neighborhoods? What if this tool harnessed a common technology—the cell phone—so that any anyone could submit a report via text message/SMS? What if we made it possible for everyone to see these reports and develop a consciousness about what was happened to our country?

While the idea was simple, the process of building software and business process raised deeper questions. What would a minimal report look like? How would volunteers then verify each report and approve it for public release? What would be the best way to post all the verified data for the world to see? And who would staff that project?

Rather than seeking to solve every potential problem, we built a simple and admittedly imperfect solution. Over a few days, our team agreed on minimal functionality, sketched out the workflows, and developed a stack of software code that allowed anyone with a cell phone to turn a report into a dot on a map. We called this new tool ushahidi: the word for testimony in Swahili. Then we launched it for Kenyans to use.

Over the weeks after the election, the Ushahidi platform collected thousands of reports. Volunteers took thousands of small observations and built the outlines of a larger story, making it possible for the public to see a growing narrative of violence on the Web. From the contributions of many voices, Kenyans had formed a collective understanding about their shared experience of social strife.

The first version of the Ushahidi platform had been born, and with it, a movement to harness the power of the crowd.

## Giving Testimony to the World
The Ushahidi model resonated with other activists and journalists around the world. In 2009, the Pajhwok Afghan News hired Small World News to train its journalists in the use of citizen-generated reports to monitor the second election under Afghanistan’s constitution. This effort harnessed SMS reports collected via Ushahidi as well as social media reports from other sources, including Twitter. “Alive in Afghanistan” applied it to election monitoring in 2009 and 2010.

The lessons learned from this work fed directly into an effort to apply Ushahidi to the humanitarian operation after the 12 January 2010 earthquake in Haiti. Ushahidi@Tufts monitored 35K reports after the Haiti earthquake for the needs of the affected communities.

[ others TBD, to expand ]

A problem emerged from all these deployments: giving voice to the general public almost always requires recruiting and managing a smaller crowd—a team of trained volunteers who verify reports and often translate, geolocate, and categorize them for analysis, visualization, and reporting. We built most of the software to enable this invisible team.

As a result, the common perception of Ushahidi is that the platform is an SMS framework that aggregates messages from many cell phones, when its true magic happens on the back end. It is here that volunteers can collate messages from SMS/text messages from multiple services, Twitter, news feeds, and emails. It is here that those volunteers make sense of the information flows, turn them into maps, and make them available for the public.

## A Great and Growing Responsibility
While there is great power in giving voice to citizens in countries where collective action drives change, there is also great responsibility around the management of crowd-submitted data, much of which is invisible to the general public. The Ushahidi SMS platform must be seen not just as a method for collecting reports from many contributors, but also (and primarily) a tool for a smaller community of committed individuals to categorize, verify, and analyze the assembled data.

As Ushahidi grew from a quick hack to a platform for general use, the developers and community of deployers had to build new features to support use cases of a growing range of organizations. We needed to confront security holes, enable easier integration of mainstream news and tweets from trusted sources, and turn all the dots on a map into a narrative that decision makers could apply to their needs.

We added software at an increasing pace. We added alerts to trigger messages when certain events happened, workflows to enable teams to track the state of any report through the verification process, and integration with social media.

All the while, code piled on code. One class overloaded another. One security patch opened vulnerabilities in another vector. Eventually, no amount of security audits or refactoring could turn an architecture that had been designed around ‘putting dots on a map’ into a the sophisticated analysis tool that the Ushahidi community needed.

We knew that the game of software whackamole had to come to an end. Our team needed to make some difficult choices. What we did turned out to be harder than we ever imagined. We rewrote Ushahidi from scratch. That story requires a bit of telling…