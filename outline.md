---
layout: page
title: Outline
permalink: /outline.html

---

# Ushahidi Guide Outline
By John Crowley and Jennifer Chan

# 0 Introduction

## &sect; Ushahidi as Testimony.

From the 2008 Elections to citizen engagement. In Swahili, 'ushahidi' means testimony. During the 2008 Kenyan elections... Ushahidi was first designed as a platform to enable citizens of Kenya to tell their stories, to give testimony. Tell Ushahidi story...

## &sect; What is Ushahidi?

Today, Ushahidi might best be described as an organization that builds tools to empower communities. The original tool, Ushahidi SMS platform, has grown. Release v3 is a rethinking of the original idea. Simplified code. Simplified interface. Could even function as a headless API. Start to continued simplification and renewed engagement. How does it relate to other tools, how is it unique? Interface for digital data collection, relation to tech environment?

## &sect; Why use Ushahidi and for what purpose?

What do you need to think about first? Ushahidi is more than a tool; it is a set of practices that have emerged around how best to use citizen reports to collect data and analyze it for a particular end. These ends now include evidence gathering for human rights, citizen journalism, health mapping, etc...

# 1 Understanding v3

## &sect; Case: deploying v2 and finding challenges.


Custom development to meet needs. Security questions.

## &sect; Why v3: Smallsurfaces and the design challenges of v3

### Data Collection

### Aggregation

### Context

### Visualization

### Management

### Code Maintenance

### Security

## &sect; Key Concepts in v3


Software cannot solve all problems. It can, however, catalyze a community of problem solvers to build tools to address challenges.

### Clean Code


SOLID, Clean Code framework based on Uncle Bob. Kohana is still there, but not the core. Ushahidi delivered by Kohana, but not based on Kohana.

### Security and Permissions


Role-based views, security around code.

### Simplified Installation

### Customized Design
Custom forms, interface

### Integrated Messaging: Posts and Messages


Posts and Messages allow for SMS Reports, Social Media, Emails, and Web Reports to flow into common stream

### Unified Interface

#### Workspace Toolbar

#### Views

### Workflows

---

# 2 Strategy

## &sect; Before you install and configure Ushahidi, take time to think about your strategy and design your campaign.

### Practical Considerations

### Questions to ask yourself

## &sect; Objectives and Goals

### What are trying to do?

### What data will enable you to get to your goals?

## &sect; Deployment Types

### Human Rights Evidence Gathering

### Crisis Reporting

### Citizen Journalism

### Election Monitoring

### Health Mapping

### Poverty Mapping

### Sensor Tracking

## &sect; Staffing

### Staffing Plan

### Roles

### Hiring

### Training

## &sect; Crowdsourcing

### Building a Campaign: If you build it, they might come:

### Types of Crowdsourcing

## &sect; Partners

### Technology

### Programs

## &sect; Scheduling

### Time Commitment

### Timelines

## &sect; Resources

### Costs

## &sect; Ushahidi Product Matrix

### Crowdmap, Ushahidi v3, Red Carpet, Custom

---

# 3 Installation

## &sect; Tech Environment

### Cloud v Rack Servers

### Tech expertise (ToR)

## &sect; Unix/Linux

### Dependencies

### Install Process

## &sect; MacOSX

### Dependencies

### Install Process

## &sect; Windows

### Dependencies

### Install Process

## &sect; Migrating from v2

### Planning your  migration

### Backing Up

### Migration Script

### Checking the data

### Customization and Migration: what will not work?

## &sect; Migrating from Crowdmap

---

# 4 Configuration

## &sect; First Look at the Site

### Setting up initial admin user and password

### Introduction to Workspace

### Introduction to Views

### Introduction to Posts and Messages

## &sect; First Steps: Localization, Site Settings, Users, and

### Localization

#### Language

#### Time Zone

## &sect; Modifying Site Settings

### Site Name

### Site Owner Name

## Features

### Media Uploads

### Sets UI

### API Explorer

### Data Provider Configuration

### Post Export

### Form Wizard

## &sect; Managing Users
An intro to users in Ushahidi. Roles and permissions. Views and exports limited by permissions, etc.

### Roles and Permissions in v3

### Managing Users Interface
Roles: Admin, Member, Guest

### Setting up admin, setting up initial team

### Editing a User

### Changing Roles

### Deleting Users

## &sect; Map Settings

### Default Location

### Cluster Reports

### Map Base Layer

### Default Zoom Level

## &sect; Customizing the UI

### See Appendix C

## &sect; Security

### See Appendix B

---

# 5 Data Collection Design

## &sect; Data Model and Data Collection Methodology

### Building your data collection around your data model and outputs

## &sect; Data Collection Methods

### Limits of Data

### Privacy

### Security of Contributors

## &sect; Defining your Ouputs

### Maps

### Visualizations

### Decision Makers Needs

### Information Overload

## &sect; Data Models for Deployment Types

### Human Rights Evidence Gathering

### Crisis Reporting

### Citizen Journalism

### Election Monitoring

### Health Mapping

### Poverty Mapping

### Sensor Tracking

## &sect; Posts and Messages in Ushahidi

### Posts

#### SMS Posts

#### Web Posts

### Messages

#### Email Messages

#### Social Media Messages (Twitter)

## &sect; Messages Configuration

### Email
Server settings: POP|IMAP, etc.

### FrontlineSMS
Key, FrontlineCloud API URL

### Nexmo
From, secret, api key, api secret

### SMSSYNC
Android App, Android App Settings/Secret

### Twilio
From Phone, Account SID, Auth Token, SMS Auto Response

## Creating your Data Model

### Matching data collection needs to post structure

### Managing Forms

#### Field Types

##### Text

##### Text Area

##### Number (Decimal)

##### Number (Integer)

##### Select

##### Radio

##### Checkbox

##### Checkboxes

##### Date

##### DateTime

##### Location

#### Creating a Form

#### Editing a Form

#### Deleting Forms

### Categories and Tags

#### Planning categorization of posts and messages

#### Categories

#### Tags

### Spatial Resolution: what do you need?

---

# 6 Deployment

## Preparation

### Technology Preparation

### Staffing Preparation

## Training

### Teaching Ushahidi to your staff

### Instructing the crowd

## Simulating your Deployment

## Running the Campaign

### Collecting Data from Crowd

### Getting the word out

#### Advertising

#### Word of Mouth

#### Grassroots Organizing

#### Bounded Crowdsourcing

### Creating a Feedback Loop

#### Monitoring: are you reaching your goals? Linked to objectives/goals? not tech, but programmatical goals?

---

# 7 Curation

## Unified Interface

### Monitoring Posts, Messages, Verification, Workflow State

### Administration and User Views are united, but permissions enable what can be seen by which users and the public

## Views

### Full

### Maps

### List

### Media

## Curating Posts and Messages

### Deduplication

### Geolocation

### Clustering

### Verification

### Translation

## Managing Posts and Messages with Sets

### Sets

### Filters

## Managing Individual Posts

### Details

#### Title

#### Description

#### Tags & Categories

#### Location

### Permissions and Status

#### Status: Public, Draft, Pending

#### View Permissions: Public, Private, Custom

#### Edit Permissions: Users who can edit

### Media

#### Adding Media

#### Primary Media Post

### Links

#### Adding Links: URL and Title

### Set

#### TBD

### Edit History

#### How History works

#### Undo

## Delegating Curation Tasks with Workflows

### TBD

## Protection

### Protecting Contributors

### Protecting Privacy

---

# 8 Analysis

## Views and Maps: Telling a Story

### Building a Map Visualization

### Building Charts and Graphs

## Exporting your Data for Analysis

### CSV Exports to Spreadsheets

### qGIS

## Ushahidi as an API: Connecting to Third-Party Applications

### What is an API?

### Ushahidi v3 API

### Calling the API from Third-Party Applications

### Resources and Documentation

---

# 9 Closing

## Closing out the campaign or monitoring program.

## Data Archive

### Protecting contributors

### Handing off data

## Shutting down the v3 server

---

# 10 Developing on Ushahidi

## Kohana and Ushahidi: A Story

### Uncle Bob’s Clean Code and SOLID

### BDD and TDD

### Architecture of v3

## Code Tour

## API Explorer

## Extending Ushahidi v3

---

# Appendix A: Mapping

## Mapping 101 from Shadrock

# Appendix B: Security

## TBD

# Appendix C: Customizing the Interface

## TBD

