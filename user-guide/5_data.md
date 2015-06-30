---
layout: page
title:  "Chapter 5"
subtitle: "Data & Data Models"
date:   2015-04-23 22:35:00
categories: user-guide
weight: 5
---

> The word DATA derives from the Latin for “to give”; thus, data are really GIVEN FACTS, from which additional facts can be inferred… A given fact in turn corresponds to what logicians call a TRUE PROPOSITION; for example, the statement “Supplier S1 is located in London” might be called a true proposition. It follows that a database is really A COLLECTION OF SUCH TRUE PROPOSITIONS.
>
> C.J. Date, An Introduction to Database Systems

Ushahidi is designed to allow many sources to contribute facts to a central dataset, from which analysts might infer additional facts. For example, many sensors reporting rising water in one village will allow analysts to infer that water is going to rise downstream. Many people reporting fraud at a particular polling site will allow analysts to infer that something is amiss; they may then choose to correlate voting patterns with the allegations of fraud.

For all the power of transparency, data is not itself a force for good or even for change. Data can drive informed decisions, but only when their analysis is more compelling than the narrative already in the head of the decision maker. More often than not, evidence fails to overcome the inertia of history: a manager will default to actions that have usually worked in the past, regardless of any changes or new approaches that new or data or unfamiliar dynamics might suggest (see ALNAP study, Insufficient Evidence). For example, even if sensors say that a flood is particularly bad, a person who knows the place only gets mild flooding may choose to take actions inadequate to the actual scale of the emergency.

Your job in developing the design for your data collection works back from the decision that needs to be made. In general, this work takes two forms: 1) providing data around a signal or trigger for a course of action within an existing system (such as a logistics supply chain); or 2) advocating for changes to behavior (or mindset) based on making some dynamic more legible or transparent (such as election fraud or crisis mapping). The questions for each option differ:

* Are you driving an operational decision in an existing system? If so, what data are needed to drive those decisions? How does data currently flow in the existing system? How would Ushahidi alter the architecture of these data flows? Would Ushahidi be a net positive or would it only help in one particular stream of data? Would it augment the existing flows or replace them? What are the issues around disruption of flows?

* If you are working to change the structure of the system, whose mind are you trying to open? What is the mental model that he or she has of the problem? What actions have worked in the past? What evidence would it take to open his or her mind to a different course of action?

This chapter will help you to move from your answers to these questions to a data model: an architecture for collecting, storing, and querying an assembly of facts from a set of human or automated sensors.

## Knowing Your Data Needs

While it is tempting to start building a custom form for your deployment, there is an art to creating the data model and the management process around its security, collection, curation, analysis, reporting, and archiving. We recommend engaging in a process that defines the minimal viable model for the decision that needs to be made alongside this business process.

Too often, organizations take a kitchen sink approach: they create long custom forms and discover that they end up with inconsistent data entry and incomplete data sets. When data are in such a state, it is often difficult—or even impossible—to infer additional facts from the database. Worse, managers discover these challenges with security, privacy, partners, field sites, or communications network too late, and these issues often defy inexpensive fixes.

Start small. Know what outputs you need to create and how data will flow from their sources to those outputs. Managing these flows will be far easier when a simple data model is built around all the potential opportunities and constraints of the place where you are working.

### 1. Define the spatial and temporal bounds of your data collection efforts

You will collect data over a defined geographic region, time period, or (most commonly) both.

What is the target area for your data collection efforts? Projects that span a larger geographic region often require more planning, time and resources. In many parts of the world, languages vary across the country. When using SMS or IVR and the crowd as your data feeds, it may come into the platform in many different dialects. Organizing a translation team will likely require recruiting staff and/or volunteers with coordinators familiar with these needs for translation and cultural content interpretation.

{ seek example here }

When do you plan on opening and closing your data collection? How does this align with cultural, religious, national, or local events? Are there other surveys slated for the same period, perhaps on a similar topic?

Are you planning on a multi-year project to encourage citizens like tourists and conservationists to report the sighting of vultures in Namibia? The Vultures of Namibia project started nine years ago and covers the entire country of Namibia. This requires planning and outreach to spread the word to report over such a large geographical area. It also requires data collection over a longer period of time.

Another project is the Christmas Lights in Houston project. This project has a smaller target area in one city within the United States over a short time period, from December 7th to 17th.

### 2. Survey the Environment and know your data capacity

Managers of successful deployments recommend surveying the way that data currently flows from remote sites to your analytical team. When possible, go to a remote site and explore the challenges that local staff have around the simple act of sending an SMS, tweet, or email. What days of the week do they have power and Internet? How reliable are these connections? Are there backups, such as a generator or satellite internet connection? Are the cell towers always on? What is cellular coverage like? Do their cell phones have keyboards that support the local language? Do their computers have backup drives or uninterruptable power supplies (UPSs) so that someone can shutdown gracefully before losing data? Is the only way to get data to Ushahidi by driving a computer with the data from a disconnected remote site to another place which has an Internet connection? Who drives the motorbike or van between sites, how often, and at what cost?

### 3. Define Security and Privacy Guidelines

The context for your work will define what kind of security protocols your staff will need to build around the data flows, as well as the privacy concerns that you will need to manage around the way that you release any data.

Are your data going to describe dynamics that challenge the political, social, cultural, or religious status quo? Will your sources be taking a risk by submitting the data? Are the pathways by which the data will flow secure? Is there a relationship between the national telecommunications provider and internal security services, gangs, or other groups which may be able to exact retribution on your sources?

Once the data is on the Ushahidi server, what level of security will be necessary to protect the data? Would individual reports or the aggregated data be targets for cyberattacks or cybertheft? What are the potential consequences of an unplanned release of your data on your sources, your organization, or the local context?

{extend}

Considering the risks and privacy issues is a responsibility of you and your team during a Ushahidi or Crowdmap Project. This starts from designing your project goals and objectives and we will help provide some tips here on how to integrate safe practices into planning your data model and data collection. Consider the following.

As your team determines what types of data to collect and how consider the following:

For example your project is planning to collect information using SMS short code. The plan is to collect the names and locations of reporters for a corruption project. Ask members of your partner groups how they feel about sharing this information.

Consider the following questions.

* Will this endanger their lives during a conflict?
* Will this cause their family and community scrutiny from government official if they report corruption about their homes?
* How do people and communities feel about being reported by others in their community? Is this acceptable?
* How might they change the data model or collection to ensure privacy of information and acceptability to their members involved?

Reporting, collecting and sharing data using the Ushahidi software or crowdmap software is a responsibility not only to your partners but also to the communities and the crowd.

### Defining your Outputs

Your data will rarely be given to a decision maker in their raw form. More often, you will be presenting some kind of analysis that makes one or more assertions based on the data. Your terms of reference may specify a particular kind of report that you need to communicate, or you may be using the data as an input into an advocacy campaign. You may use visualizations to convey this point; you may just use charts or a purely text-based narrative. In each case, you have an output in mind (even if its design remains inchoate).

Defining this output is a critical aspect of building your data model. If you do not collect what you need, you will not be able to make assertions based on evidence. If you collect too much, you may be overloaded not only in information, but the management of a campaign with unnecessary complexity and (potentially) cost overruns.

### Decision Makers Needs

Who is making a decision based on the data? Are you changing the minds of a population facing an epidemic of violence? Are you driving a donor to make an investment in your organization? Are you engaging in continuous monitoring of a parallel project so that you have better data for your M&E team?

Regardless of who you are trying to reach, ask these questions:

* Where do these decision makers sense uncertainty?
* What data would reduce that uncertainty?
* What is the minimum amount of data necessary to drive a decision?

### Information Overload

With data, organizations often think ‘more is more.’ More data means more time devoted to cleansing it (data munging), correlating it (statistical analysis), and building a story (reporting)—all of which contribute the perception of being overloaded with information. When you lack the resources to ensure that a large campaign is collecting complete and accurate data across a large region, time span, or both, much of the data collected is irrelevant, incomplete, inaccurate, and/or questionable veracity. Ask yourself these questions:

* What is your organization’s capacity to ensure that your data collection process is accurate and complete?
* How much capability can you mobilize to check the veracity of your posts and/or messages?
* What analytical capacity does your organization have to work with large, sometimes messy datasets? Who will perform the work and what experience do they have with preparing SMS social media data for analysis?

### Analysis and Visualizations

Although Ushahidi was originally built to put dots on a map, the v3 platform removes the assumption that you are building a geospatial analysis. You can now choose the way that you visualize your data: charts, graphs, and/or maps. This freedom also gives you more responsibility to plan what data you will need for your visualization.

* Do you need temporal series?
* What kind of sampling method will you analysts be using and what do they need?
* Are there ways your form needs to be structured to allow for the survey techniques that your analytic team needs?

### Data Collection Methods

Whether you are collecting data from Twitter feeds, a digital data collection tool, or SMS messages from short code, it needs to be collected, managed and processed to fit the goals and objective of your project.

#### Primary or Secondary Sources

Data collection can come directly from your sources (from the crowd or your project partners) or imported from an existing database into the platform. With the new capabilities of the v3 platform, data could come from both simultaneously. You will need to develop an approach to managing both your primary sources (from direct observation or from sources that report on behalf of others), as well as your secondary sources (datasets and data pulled in via API from social media).

Here are some questions to consider:

1.    Will those sending information to the platform be directly observing or will they be reporting on behalf of another person or group?
2.    If the data or report sent to the platform is observed and includes urgent or sensitive information, how will you determine how accurate the data is for decision and action?


For example the WaterTracker project collected community-level data of direct observations of broken water sources. Community members in Afghanistan reported their observations using short code and IVR (Interactive Voice Response) technology that was linked to their Ushahidi platform.

The Anti-Eviction Mapping Crowdmap Project aims to “highlight struggles of increasing inequality across the Bay Area and create a community around those wishing to remember neighborhood stories and character”. The project uses both primary and secondary data. There are original radio transcripts from evicted persons as well as news stories about those evicted from their homes.

### Tips and Resources
Data Collection Do's and Don'ts . Don't just collect it because you can. Have a purpose. Anticipate the people side of data and your Ushahidi platform. How will you manage and re-organize your data. What can you do to ease this process as you collect the data? What is necessary to do post colleciton? Does your pre-existing data or collected data need fusion or merging? Who might do this on your team?

## Posts & Messages
Ushahidi offers a method to handling your various data sources: posts and messages. Posts hold information from your primary sources where you are able to structure the data within your data model(s). Messages are from your secondary sources (Twitter and other social media). Messages also provide a private backchannel for emails from a bounded list of trusted sources.

The big difference is this: Posts are where you get to control the structure of the data. Messages are where your source controls the structure of the data.

### Posts

#### SMS Posts
#### Web Posts
#### Messages

##### Email Messages
##### Social Media Messages (Twitter)

#### Posts and Messages Configuration

##### Email

Server settings: POP|IMAP, etc.

##### FrontlineSMS

Key, FrontlineCloud API URL

##### Nexmo

From, secret, api key, api secret

##### SYSync

Android App, Android App Settings/Secret

##### Twilio

From Phone, Account SID, Auth Token, SMS Auto Response

### Building a Data Model


#### Data Model from Deployment Types

Human Rights Evidence Gathering
Crisis Reporting
Citizen Journalism
Election Monitoring
Health Mapping
Poverty Mapping
Sensor Tracking

### Custom Forms

Toolkit will give overview of thinking about forms, manual will examine what can and cannot be done with individual field types. This page will be in two parts:

1.    How to think about forms
2.    How to build forms.
3.    What forms will and won't allow you to do with filtering and sets
4.    Forms and Mapping and visualizations

May split into multiple files
Matching data collection needs to post structure

#### Managing Forms
Field Types
Text
Text Area
Number (Decimal)
Number (Integer)
Select
Radio
Checkbox
Checkboxes
Date
DateTime
Location
Creating a Form
Editing a Form
Deleting Forms

### Categories & Tags

Planning categorization of posts and messages
Categories
Tags
________________________________________

## Resources

Categorization: Sometimes Less is More Ushahidi allows users to create and visualize categories to help organize and analyze data. But sometimes category lists get out of control, slowing report processing and compromising accuracy, or at least consistency. What I learned about the way the U.S. Armed Forces use categorization and maps at the Esri User Conference in San Diego provided an interesting lesson – when it comes to categorization, sometimes less is more. http://blog.ushahidi.com/2011/08/16/categorization-sometimes-less-is-more/


## What is Georeferencing?

The term “georeferencing” broadly means associating something with a location in physical space. In an Ushahidi deployment, reports and their accompanying images, videos, or links to other content can be georeferenced to provide new insights about the content of the reports such as, “are human rights abuses being reported in one part of a city more than another?” This process is sometimes referred to as “geocoding”, which generally means deriving geographic coordinates from other location information, such as an address, or “geotagging”; the process of adding geographical identification metadata to various media. We use the term “georeference” as a general term for the sake of simplicity.

Georeferencing is an important part of Ushahidi’s functionality and is best considered before launching a deployment to ensure consistent quality of geographic information across reports. In many cases, georeferencing is performed manually by those making a report or by those managing the deployment after the report has been entered. Some deployments may desire a great degree of geographic precision, such as associating a report with a precise building or cross-street, while others may only require less precision such as associating a report with a town, city, or village. In any event, understanding your needs, and communicating those clearly to the users and managers of your deployment is critical to ensuring quality georeferencing.

### How georeferencing works using Ushahidi

We find that many first-time users of Ushahidi assume that incoming reports are “automatically” georeferenced by the software. While some parts of this process can be automated, georeferencing often requires the work of a human being at some point during the process: this is especially true when receiving incoming short message service (SMS) reports from dumb-phones or feature phones that do not have a global positioning systems (GPS) unit. Good georeferencing will be largely contingent on your ability to communicate the type of descriptive geographic information you need to accurately geocode reports to those who will be reporting to the deployment. For example, do not say, “include location in your report.” This is too vague and can be interpreted in a wide variety of ways: are you asking for latitude and longitude (which few people will know); or a country name; or an exact address? Rather, do say, “in your report, include the name of the city or village that you are in, followed by any further information such as an address, street name, or specific building or landmark associated with this report.” The more clearly you can communicate your needs the better.

In Ushahidi, users georeference reports via a map interface that allows them to drop a marker by hand or, if connected, use a geocoding service, such as Google or Geonames [1], to search for place names, addresses, etc. Users can often search for an address or place via the geocoding service, which will place their marker in the general vicinity, and then further refine the precise placement of the marker manually. Remember that place names may have different spellings, or different names altogether, in different languages. Test any geocoding services you use before hand to spot any potential problems that can be caused by this.

If you’re deployment is dependent on those making the reports to georeference them you will need to communicate the level of precision you require: make this part of your communications strategy. You may want to add form fields to the reporting screen that that allows users to describe the level of geographic precision they used while making the report. You can make these subjective terms such as “neighborhood level”, “city level”, etc. or use clearly defined categories. One example of this is the “geographic precision code” used by the International Aid Transparency Initiative (IATI) to clarify the geographic precision of reported development projects [2]. This standard allows analysts using IATI data to sort reports into comparable levels of geographic precision or aggregate reports in a way that they may be geographically comparable by assigning each record a number that corresponds to a specific level of geographic detail.

If your deployment has dedicated managers to assist in geocoding reports be sure to including geographic precision in any training or communications that they receive. Talk with them about the ideal level of geographic precision for reports but understand that their ability to precisely georeference a report will be dependent upon the contents of that report. Reports may only contain a city name even though you are asking for exact locations. Communicating the type of geographic description you need from those making the reports is critical: make this part of your communications plan. Talk to your team about best practices given the contents of reports and agree on a consistent way to georeference. Take time to practice: ask friends to create test reports that you and your team can experiment with.

For the most precise georeferencing, we recommend using mobile applications, such as the Ushahidi app (available for iOS or Android) to report to a deployment. Users must allow the app to access the mobile’s GPS unit for the greatest accuracy. Once this is done, reports and images will be automatically referenced with latitude and longitude. Even though reports will automatically be georeferenced, GPS units are prone to error. Large vertical objects, such as trees or tall buildings, can deflect or block signals that a mobile’s GPS units needs to take an accurate reading. While different devices will have different levels of error, it is reasonable for you to assume that most mobile devices will provide a GPS reading within 10-20 meters of the actual location at the time of reporting.

### Basemaps

### Social Media

### Resources

[1] Further information about the Geonames geocoding database and the Google geocoding API can be found using these links. For further information about other geocoding services see this Wikipedia page. [2] The International Aid Transparency Initiative’s standard for clarifying the level of geographic precision for reporting of development projects can be found here.


