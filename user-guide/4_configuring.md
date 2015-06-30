---
layout: page
title:  "Chapter 4"
subtitle: "Configuring the Platform"
date:   2015-04-23 22:27:00
categories: user-guide
weight: 4
---

This chapter provides you with a first look at the system that you have just installed. For those who have used v2 for several years, the initial load of v3 might be disorienting. The administrative interface is gone, and the new Views interface requires a little getting used to. Whenever one makes a cumbersome but familiar process easier, some will ask for the old way back. Trust us: after a year of working in the new interface on the development server, it is much easier to have everything in one place.

## Accessing the new installation

Depending on how you configured the baseurl (see installation), go to the index.php page for the installation.

* Mac
* Linux
* Win

This is now the only url you need to remember; the index.php file is the controller within the new architecture; all pages are accessed via the index.php file, including any static pages (we may want to explain how to set up aliases for various static pages, especially for migrations). See the developer’s annex for a deeper explanation.

## First Look

The installation will open to the initial map view with several default reports. You can see that there are tabs across the top: Map, List, Graph and Timeline. These views give you different ways to view posts in your deployment.

In the menu you can also see: Saved Searches and Collections. Each of these will show you a pre defined group of posts. Saved searches - as one expects - show posts based on some collection of filters or search tersm; Collections show a manually curated set of posts. Will dig into both of these features later on in the guide

### First Steps

First things to do in v3

### Site Settings

#### Site Name

#### Site Owner Name

### Managing Users

An intro to users in Ushahidi. Roles and permissions. Views and exports limited by permissions, etc.

#### Roles and Permissions in v3

How roles and permissions work within the v3 platform.

### Post Type settings

What is a post type?

#### Adding a new post type

#### Post type permissions

#### Adding steps

#### Adding custom fields

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

#### Deleting Users

### View Settings

#### Map

#### List

etc
