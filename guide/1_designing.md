---
layout: page
title:  "Chapter 1: Designing a New Approach"
date:   2015-03-24 17:31:20
categories: chapter
---

Chapter 1 Ushahidi v3: designing a new approach
When we decided that we would embark on a complete rewrite of the code, we knew that it would be difficult. We also knew that we would get pulled to making some classic mistakes , including getting lured into over-engineering and over-designing the new architecture


To accelerate process, we commissioned the UX consulting firm SmallSurfaces to interview the community and characterize the key design challenges facing the user base. This study highlighted shortcomings that many community members had experienced and created a daunting wish-list of new features.


The study showed a few things that we already knew. From the start, we designed Ushahidi to put dots on a map. Each dot contained certain data fields about an incident or observation, and the software provided means to alert deployers when certain types of dots happened in specific places.


As happens with a successful open source project, the Ushahidi community took this election monitoring tool and applied it to a wide range of use cases which the developers had never anticipated. As a result, we confronted a truth that we had come to know through all our efforts to add features: our community was ahead of our development team. Some clients had written entire applications on top of the Ushahidi code base, enabling them to perform highly customized data collection. Others wished they had the technical ability to transcend limitations in the existing software.


The study also deepened our understanding of the complexities that our clients confront when collecting and analyzing data from a wide variety of field environments. In rough terms, these issues broke down into a few questions:


•    What is a report? When we wrote Ushahidi, we assumed that a report described an event at a specific place and time. Our clients, however, often had different needs. Some needed to track observations of the state of something over time, like the stock of a particular drug or a sensor reading on the water level of a river. This need to inspect each report’s state as it changed over the course of a deployment is more than semantics: it changed both the fundamental unit of analysis and the primary mechanism for visualization (the map). Ushahidi now had to support multiple methods of collecting, categorizing, clustering, curating, and analyzing observations from people and machines and turning them into a narrative that could be used by both decision makers and other machines. We also needed to rethink how we visualized a stream of observations over both space and time.


•    What is a source? Reports are not always an SMS message submitted by one person from one place. In many cases, Ushahidi teams reach out to trusted sources via social media, email, and voice calls, adding their reports to the system by hand or even via programmatic means (such as the API). Reports might not even be submitted by a human. Some might come from streams of news from the mainstream media. When reports become observations of state of a water level or drug stock over time, a source might well become a sensor or inventory management tool.


•    How do reports relate to each other? Some dynamics cascade over space and time. Floods start in one locality and spread to the next, as do infectious diseases. While Ushahidi 2.0 supported the visual clustering of reports, it had no mechanism to characterize the specific relationships between two or more reports, let alone to describe the change to this relationship over time. Nor did it have a means to relate reports to more than one location.


•    How do you know if a report from a given source is true? Verifying a single report in isolation has always been difficult. More often, deployers have looked at clusters of reports for signs of reinforcing observations. Some deployers even view a single report as far less meaningful than the aggregation of reports over time (e.g. disease outbreaks). Reports are more often in a network, with degrees of probability of being true. Instead of engaging in the quest to create a binary characterization of true/false for any given report, Ushahidi had to enable clients to ascertain ranges of probability around the veracity of a cluster of reports.


These questions triggered deeper design questions:


•    What is the best way to show change over time? When a report is an observation of a level over time, what visualization is best? Ushahidi had started with a map, which generally represents the state of a region at a specific time. While a map can be animated, it is not the best way to visualize a stream of observations over time. What do analysts need to do with the stream of observations feeding into other tools and their data models, let alone the relationship of Ushahidi data to observations collected in other crowdsourcing platforms?


•    What workflow design best supports analysis of observations over time in a given context? Ushahidi workflows were designed to enable teams to track the movement of a report from unverified to verified and approved for publication. While this process may help move a description of an event from an SMS message to the web map, it is not ideal for tracking which parts of a given observation remain true over time. Some observations may contain elements that are both true and false. A translation or geolocation may be more or less accurate. Sometimes the relevance of a report fades over time, or grows stale. What element should be verified or not? What workflow would enable teams to confront the complex challenges of verifying observations over time and place? How would our workflows capture both state and staleness?
Key Concepts in v3
Software cannot solve all problems. It can, however, catalyze a community of problem solvers to build tools to address those challenges which have a technical solution. Given the number of design challenges facing the Ushahidi team, our developers had to choose how to stage the development of a new version of the platform. We also had to decide how to make this new version more robust, reusable, and resilient against new challenges.


We are not afraid to admit that our decisions are not perfect. We learned a great deal from others who recommended refactoring not only our own code, but also working with code libraries that continued in their own rapid evolution while we were rethinking v3. Constant change to the code brought us back to revered software development principles around maintainable code.


The initial release of v3 does not address all the problems we had hoped. That said, it represents a huge leap forward for the Ushahidi community. We are excited to announce some major revisions to the design of the Ushahidi platform:
Clean Code and SOLID Principles
Building and rebuilding code in Ushahidi v2 tested the limits of our development team. One fix often led to a new bug elsewhere in the code. The PHP framework with which we had build v2—Kohana—was also losing developer support. When we hired one of Kohana’s creators—Woody Gilk—to be our lead software developer, his recommendation was to begin moving from Kohana to design principles from a luminary known as “Uncle Bob.”


In the 1980s, Robert Martin (aka Uncle Bob) had outlined a set of principles for reusable and maintainable software now known by an acronym: SOLID. While technical readers can turn to Appendix (x) for the detailed explanation, the gist of SOLID is this:


Complex software tends to introduce myriad dependencies between systems written for a particular use case and the software libraries that those systems call upon to make their development faster and easier. When a system becomes so deeply coupled, it can become difficult to add new functionality, fix bugs, and extend existing code. Software designed with SOLID principles cuts through these challenges. According to Uncle Bob, software needs to be designed in modules so that any particular element has one and only one responsibility (Single Resposibility Principle). SOLID then provides a set of practices to ensure that developers are building modules which are compatible and maintainable. Developers can substitute these modules for each other and can more easily manage the complexity of their dependencies.


For v3, the Ushahidi team built the code around SOLID principles. While the system is still delivered via the Kohana framework, Kohana is now set up to be phased out of the code.
Rethinking Data Inflows and Outflows
When the team rethought the flow of data into the Ushahidi system and back to other services, we had to develop a means to handle reports that came from a variety of sources (SMS, email, RSS feeds, web services, web forms), in a variety of formats (observations, narratives, surveys, etc) and then provide a mechanism to allow that data to flow back out to other tools, including visualization, GIS, and statistical analysis software. Our solution integrates three concepts:


* Integrated Messaging: Data flowing into the Ushahidi system from observations, reports, email messages, web forms, etc., would be simplified into two data types: structured observations would be posted into the system for visualizations as Posts, and narrative information that describes the context would arrive as Messages. For the special case where Messages also contain an observation, there would exist a means to add those data as a new Post. (Posts and Messages allow for SMS Reports, Social Media, Emails, and Web Reports to flow into common stream)
* Custom Forms: data could be collected by custom forms that reflect the data models used by clients.
* Headless API: the platform would not require the web interface for inputs or outputs, but would instead be built around a headless API, which would allow any client to customize the interface and visualization as they so choose. Ushahidi would provide one or more such interfaces, but the application would no longer be limited to the default configuration.
Unified Interface
Much of the work around a deployment is done by volunteers within the administrative interface. They often toggled between a map, a spreadsheet, and a queue of tasks. No more.


The biggest change in v3 is the unification of the administrative interface with Views of the data. There is now a single interface. Instead of all the toggling, volunteers can now work directly on the data in Views, with permissions on what any particular person can see being set by role-based Permissions. A Workspace Toolbar enables access to the messaging systems, configuration, and backend services—all without the clunky text-based administrative interface in the way. While the guide will go into a full description of each part of the interface, this introduction gives a sample of what is to come:
Views
During the development process, our development looked for a way to enable our clients to develop whatever visualization they might need, while supporting a few common default views that can be replaced or customized. In the process of building a unified interface for administrative tasks and visualizations of the data, we settled on building an interface that would ship with the default installation: a tabbed interface between a map and several types of lists of reports. Of course, these Views would only show the reports that each user was allowed to view.


For instance, while a visitor to the site may see only verified reports that have been published to the general public, volunteers might see all the posts from submitted from SMS, a media working group might see the messages from Twitter, and administrators may see everything.


With this simple change, the cumbersome administrative interface became superfluous. So we were able to factor it out of the code, simplifying life for the deploying team.
Workspace Toolbar
That said, we still needed to provide a way for authorized users to access key administrative functions and system settings. To enable authorized users to get to all the functions that the former administrative interface permitted, we created a collapsible workspace toolbar on the right of the screen. This bar has places links to all Posts, Messages, and curation functions in one place. The Workspace toolbar can also be extended to allow for custom modules, plugins, or other tools developed by the deployer.
Security and Permissions
Controlling who has access to system functions and data is a critical aspect of every crowdsourcing platform. Ushahidi v3 is arranged around a role-based security model that conveys permissions to each class of user. These permissions can be customized. The code is also written in a way that allows for clients to more easily extend certain software classes to meet their needs.


(Privacy of data…)
Simplified Installation
Installing Ushahidi v2 was difficult—often so difficult that clients chose to use the more limited Crowdmap than to run their own Ushahidi instance. While Ushahidi v3 is not yet “one-click” install, we have greatly simplified the installation process and are building the platform on a number of libraries which have package managers which enable easy updating.
Customized Design
Most clients who deploy Ushahidi require that the interface reflect the branding of their organization. Almost all deployments have custom forms that enable our clients to collect fields specific to the unique needs of their data collection campaigns.
Ushahidi v3 is far more customizable than v2.


The interface provided by v3 is only one implementation of completely customizable user experience. Clients now have a headless API on top of which they can build whatever interface the need. v3 also offers a form builder, so that a data team can build not just one form, but as many form as are needed for any particular deployment or instance.
History of Posts and Messages
In the process of turning an initial report from the field into a verified, published report, many people may touch the data. Someone may translate it, another may geolocate it, and a third may verify it against other data. Sometimes, additional information needs to get associated with the report, such as an image, document, or other set of messages.


To facilitate the aggregation and review of this network of data around the data, we built a history for every Post and Message. Your team can now add its commentary, ancillary documents to each Post and Message.
Filters and Sets
Even with histories, managing reports with categories can be a challenge. While it is easy to tag each report, finding all the reports with a particular status in the workflow or shared trait can be a challenge which requires custom database calls.


To support Views, we now provide a mechanism to create sets of messages, controlled by filters. These sets are dynamic lists of Posts and Messages that match a certain set of criteria (e.g., all Messages from Twitter that include the hashtag #fraud). These criteria are the Filters; the resulting list of Posts and Messages are the Sets.
Workflows
The management of reports through its lifecycle requires managemennt of the state of the report, especially when multiple teams are involved in moving reports from unverified, untranslated states to verified, geolocated reports. Workflows support this management.


More than 90% of the work in an Ushahidi deployments happens behind the scenes. Unsurprisingly, most of our development efforts went to supporting this (often invisible) processes.
Definitions
Types of Contributors
Collectors, reporters, contacts.


•    Collectors: The public side of Ushahidi enables hundreds or thousands of individuals to report on what they see to a shared place. Some Ushahidi instances use smaller “bounded” crowds, which may be staff of the organization deploying the platform.


•    Curators: behind successful Ushahidi projects are a smaller crowd of data curators: staff or volunteers who make sense of the data received from collectors. These individuals tend be highly trained and sometimes specialize in specific techniques, such as translation, geolocation, or verification.