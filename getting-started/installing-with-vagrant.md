---
layout: page
title:  "Installing with vagrant"
subtitle: ""
categories: getting-started
weight: 0
---

* [Installing the API](#installing-the-api)
    * [Getting the api code](#getting-the-api-code)
    * [Preparing the Server](#preparing-the-server)
* [Installing the client](#installing-the-client)
    * [Getting the client code](#getting-the-client-code)
    * [Dependencies](#client-dependencies)
    * [Install, build and run a local dev server](#install,-build-and-run-a-local-dev-server)
* [Logging in the first time](#logging-in-the-first-time)

## Installing the API

### Getting the API code

First, you will need a copy of the source code, which lives in our Github
repository:

```
git clone https://github.com/ushahidi/platform.git
```

**Note**: if you're getting set up for development, you might want to [fork the repository](developer-guide/adding-code.html) first.

Once you have the code, the next step is to prepare a web server.

### Prerequisites

* [Vagrant](http://www.vagrantup.com/)
* Ruby

> If you already use Vagrant, check the settings in the [Vagrantfile](http://docs.vagrantup.com/v2/vagrantfile/index.html) and make sure the IP address won't conflict with your existing VMs.

### Preparing the Server

Before we run vagrant we need to get some puppet modules. We do this with librarian puppet:

```
gem install puppet librarian-puppet
librarian-puppet install
```

Then you can bring up the vagrant server and provision it:

```
vagrant up && vagrant provision
```

This should set up a server, and install all the dependencies too.

Go to [192.168.33.110](http://192.168.33.110) to check the API is up and running. You should see some JSON with an API version, endpoints and user info.

> The vagrant set up uses a 64 bit VM so you may need to enable 64 bit virtualization on your host machine.

## Installing the client

### Getting the client code

First, you will need a copy of the source code, which lives in our Github
repository:

```
git clone https://github.com/ushahidi/platform-client.git
```

> The latest install instructions for the client are always in the [README](https://github.com/ushahidi
/platform-client/blob/master/README.md). If you have any trouble check those instructions first.

### Client dependencies

First you'll need nodejs or io.js installed,
npm takes care of the rest of our dependencies.

* nodejs v0.10 or v0.12 or io.js v1.2

### Install, build and run a local dev server

1. Clone the repo

    ```
    git clone https://github.com/ushahidi/platform-client.git
    ```

    **Note**: if you're getting set up for development, you might want to [fork the repository](developer-guide/adding-code.html) first.


2. Navigate to project root

    ```
    cd platform-client
    ```
3. Install Build Requirements

    ```
    npm install -g gulp
    ```
4. Install Packages

    ```
    npm install
    ```

    *This will install both NPM and Bower dependencies! No separate `bower install` command is required.*

6. Set up build options. Create a `.env` file, you'll need to point `BACKEND_URL` at an instance of the [platform api](https://github.com/ushahidi/platform) (If you followed the vagrant instructions above that'll be: http://192.168.33.110)

    ```
    NODE_SERVER=true
    BACKEND_URL=http://192.168.33.110
    ```

7. Run gulp

    ```
    gulp
    ```
8. You should now have a local development server running on http://localhost:8080


## Logging in the first time

The default install creates a user **admin** with password **admin**. Once
logged in this user can create further user accounts or give others admin
permissions too.
