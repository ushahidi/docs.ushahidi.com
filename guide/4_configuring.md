---
layout: page
title:  "Chapter 4: Configuring the Platform"
date:   2015-04-23 22:27:00
categories: chapter
---

This chapter provides you with a first look at the system that you have just installed. For those who have used v2 for several years, the initial load of v3 might be disorienting. The administrative interface is gone, and the new Views interface requires a little getting used to. Whenever one makes a cumbersome but familiar process easier, some will ask for the old way back. Trust us: after a year of working in the new interface on the development server, it is much easier to have everything in one place.

## Accessing the new installation

Depending on how you configured the baseurl (see installation), go to the index.php page for the installation.

* Mac
* Linux
* Win

This is now the only url you need to remember; the index.php file is the controller within the new architecture; all pages are accessed via the index.php file, including any static pages (we may want to explain how to set up aliases for various static pages, especially for migrations). See the developer’s annex for a deeper explanation.

## Activating Features

The first screen that appears will ask the administrator to activate several features in the v3 platform with simple checkboxes.

(screenshot)

* Media Uploads
* Sets UI
* API Explorer
* Data Provider Configuration
* Post Export
* Form Wizard

For now, accept these features and click submit. We will explain how to reconfigure them to meet your needs later in this chapter.

## First Look

The installation will open to the initial map view with several default reports. You can see that there are two tabs across the top: Views and Sets. The Views show you all data; Sets show you filtered visualizations of data.

Click on Views. A submenu will appear with Full, Map, Lists, and Media.

corresponding to four different ways to view these sample reports. Click on each tab.

* Map
* List

### First Steps

First things to do in v3

### Site Settings

#### Site Name

#### Site Owner Name

##### Features

Media Uploads
Sets UI
API Explorer
Data Provider Configuration
Post Export
Form Wizard

### Managing Users

An intro to users in Ushahidi. Roles and permissions. Views and exports limited by permissions, etc.

#### Roles and Permissions in v3

How roles and permissions work within the v3 platform.

#### Managing Users Interface

Each user has the following attributes:

* Email
* Real Name
* Username
* Password (sha1 encrypted)

Users may have one or more roles, such as an admin or participant.

Users might also be Contacts who are sending messages via social media or email (or via an API?).

#### Roles: Admin, Member, Guest

#### Setting up admin, setting up initial team

#### Editing a User

#### Changing Roles

####Deleting Users

### Map Settings

#### Default Location

#### Cluster Reports

#### Map Base Layer

#### Default Zoom Level
