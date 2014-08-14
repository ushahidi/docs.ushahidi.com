---
layout: post_guide
chapter: 5
doc_element: 8
title: Geocoding
date: {}
published: true
tags: 
  - guide
  - toolkit
editor: shadrock
---

## What is Georeferencing?
The term “georeferencing” broadly means associating something with a location in physical space. In an Ushahidi deployment, reports and their accompanying images, videos, or links to other content can be georeferenced to provide new insights about the content of the reports such as, “are human rights abuses being reported in one part of a city more than another?” This process is sometimes referred to as “geocoding”, which generally means deriving geographic coordinates from other location information, such as an address, or “geotagging”; the process of adding geographical identification metadata to various media. We use the term “georeference” as a general term for the sake of simplicity. 

Georeferencing is an important part of Ushahidi’s functionality and is best considered before launching a deployment to ensure consistent quality of geographic information across reports. In many cases, georeferencing is performed manually by those making a report or by those managing the deployment after the report has been entered. Some deployments may desire a great degree of geographic precision, such as associating a report with a precise building or cross-street, while others may only require less precision such as associating a report with a town, city, or village. In any event, understanding your needs, and communicating those clearly to the users and managers of your deployment is critical to ensuring quality georeferencing. 

##  How georeferencing works using Ushahidi
We find that many first-time users of Ushahidi assume that incoming reports are “automatically” georeferenced by the software. While some parts of this process can be automated, georeferencing often requires the work of a human being at some point during the process: this is especially true when receiving incoming short message service (SMS) reports from dumb-phones or feature phones that do not have a global positioning systems (GPS) unit. Good georeferencing will be largely contingent on your ability to communicate the type of descriptive geographic information you need to accurately geocode reports to those who will be reporting to the deployment. For example, do not say, “include location in your report.” This is too vague and can be interpreted in a wide variety of ways: are you asking for latitude and longitude (which few people will know); or a country name; or an exact address? Rather, do say, “in your report, include the name of the city or village that you are in, followed by any further information such as an address, street name, or specific building or landmark associated with this report.” The more clearly you can communicate your needs the better.

In Ushahidi, users georeference reports via a map interface that allows them to drop a marker by hand or, if connected, use a geocoding service, such as Google or Geonames [1], to search for place names, addresses, etc. Users can often search for an address or place via the geocoding service, which will place their marker in the general vicinity, and then further refine the precise placement of the marker manually. Remember that place names may have different spellings, or different names altogether, in different languages. Test any geocoding services you use before hand to spot any potential problems that can be caused by this. 

If you’re deployment is dependent on those making the reports to georeference them you will need to communicate the level of precision you require: make this part of your communications strategy. You may want to add form fields to the reporting screen that that allows users to describe the level of geographic precision they used while making the report. You can make these subjective terms such as “neighborhood level”, “city level”, etc. or use clearly defined categories. One example of this is the “geographic precision code” used by the International Aid Transparency Initiative (IATI) to clarify the geographic precision of reported development projects [2]. This standard allows analysts using IATI data to sort reports into comparable levels of geographic precision or aggregate reports in a way that they may be geographically comparable by assigning each record a number that corresponds to a specific level of geographic detail.

If your deployment has dedicated managers to assist in geocoding reports be sure to including geographic precision in any training or communications that they receive. Talk with them about the ideal level of geographic precision for reports but understand that their ability to precisely georeference a report will be dependent upon the contents of that report. Reports may only contain a city name even though you are asking for exact locations. Communicating the type of geographic description you need from those making the reports is critical: make this part of your communications plan. Talk to your team about best practices given the contents of reports and agree on a consistent way to georeference. Take time to practice: ask friends to create test reports that you and your team can experiment with.  

For the most precise georeferencing, we recommend using mobile applications, such as the Ushahidi app (available for iOS or Android) to report to a deployment. Users must allow the app to access the mobile’s GPS unit for the greatest accuracy. Once this is done, reports and images will be automatically referenced with latitude and longitude. Even though reports will automatically be georeferenced, GPS units are prone to error. Large vertical objects, such as trees or tall buildings, can deflect or block signals that a mobile’s GPS units needs to take an accurate reading. While different devices will have different levels of error, it is reasonable for you to assume that most mobile devices will provide a GPS reading within 10-20 meters of the actual location at the time of reporting.

## Basemaps

## Social Media

---

## Resources
[1] Further information about the <a href="http://www.geonames.org/about.html">Geonames geocoding database</a> and the <a href="https://developers.google.com/maps/documentation/geocoding/">Google geocoding API</a> can be found using these links. For further information about other geocoding services see <a href="http://en.wikipedia.org/wiki/List_of_geocoding_systems">this Wikipedia page</a>.
[2] The International Aid Transparency Initiative's standard for clarifying the level of geographic precision for reporting of development projects <a href="http://iatistandard.org/codelists/GeographicalPrecision/">can be found here</a>. 