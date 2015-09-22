---
layout: page
title:  "Installing on linux"
subtitle: ""
categories: install
weight: 0
---

* [Installing the API](#installing-the-api)
    * [Getting the api code](#getting-the-api-code)
    * [System Requirements](#system-requirements)
    * [Set up the database](#set-up-the-database)
    * [Set up URL rewrites](#set-up-url-rewrites)
    * [Enable writing logs, cache and uploads dirs](#enable-writing-to-the-logs,-cache,-and-upload-directories)
    * [Installing dependencies](#installing-dependencies)
* [Installing the client](#installing-the-client)
    * [Getting the client code](#getting-the-client-code)
    * [Building the client](#building-the-client)
    * [Configure nginx or apache](#configure-nginx-or-apache)
* [Logging in the first time](#logging-in-the-first-time)

## Installing the API

### Getting the API code

First, you will need a copy of the source code, which lives in our Github
repository:

```
git clone https://github.com/ushahidi/platform.git
```

Once you have the code, the next step is to prepare a web server.

### System Requirements

To install the platform on your computer/server, the target system must meet
the following requirements:

  * [PHP](http://php.net) version 5.4.0 or greater
    * The following php extensions enabled: curl, gd, imap, json, mcrypt, mysqlnd (optional)
  * [Composer](http://getcomposer.org)
  * [MySQL](http://mysql.com) database version 5.5 or greater (PostgreSQL support planned)
  * [Apache](http://apache.org) 2.2+ or [nginx](http://nginx.org)

### Set up the database

To create a database, first login to MySQL as root.

```
mysql -u root -p
```

> Using the `-p` is only required when your MySQL configuration requires it.
>
> You may need to use the `-h` option to specify `localhost` or `127.0.0.1`
> if you are unable to connect.

Next, create a new user and database for Ushahidi. The username and database
can be anything; we will use `ushahidi` for both in this example:

```
CREATE DATABASE ushahidi_db;
GRANT ALL ON ushahidi_db.* to ushahidi_user@localhost IDENTIFIED BY 'ushahidi-db-password';
quit;
```

Now create a `.env` config file in the base of repository. Make sure that the database, username, and password match the database you just created.

```
DB_HOST=localhost
DB_NAME=ushahidi_db
DB_TYPE=MySQLi
DB_USER=ushahidi_user
DB_PASS=ushahidi-db-password
```

### Set up URL rewrites

Rename `httpdocs/template.htaccess` to `httpdocs/.htaccess` (for Apache)
to enable rewriting of all non-existent files to `index.php`.

> If you are unable to enable rewriting, then you'll need to customize the init settings.
>
> - Copy the `application/config/init.php` file into `application/config/environments/development/` (create this directory if it doesn't exist).
> - Edit init.php and set `index_file` to `"index.php"` to include index.php in your URLs

#### A note on urls, docroots and base_url

Typically, Ushahidi is run under a separate virtual host / domain name. Be
sure to make `platform/httpdocs/` the `DocumentRoot` (for Apache) or `root`
(for nginx) setting in your virtual host.

If you are running Ushahidi via http://localhost/ then the `base_url` will be
http://localhost/platform/httpdocs/

### Enable writing to the logs, cache, and upload directories

The webserver will need write access to logs, cache and upload directories.
To do this run:

```
% chmod 0777 application/logs application/cache application/media/uploads
```

OR

```
% chown www-data 0777 application/logs application/cache application/media/uploads
```

Its generally better to use `chown` to set the owner of the directories to the user the web
server runs as, rather than making them globally writable.

### Installing dependencies

We use [Composer](https://getcomposer.org/) to manage server side dependencies.
Once you have installed composer, you can run the update script with:

```
bin/update
```

_Whenever the repository is updated using `git pull`, run the update script to
ensure that your installation stays updated!_

If you are updating a production deployment, you will want to avoid installing
developer dependencies (testing tools, etc) by using the "deploy" option:

```
bin/update --production
```

### Extra: Customizing configuration

Base config files are in `application/config/`.

You can add per-environment config overrides in `application/config/environments/`.
The environment is switched based on the `KOHANA_ENV` environment variable.

## Installing the client

### Getting the client code

First, you will need a copy of the source code, which lives in our Github
repository:

    % git clone https://github.com/ushahidi/platform-client.git

### Client dependencies

First you'll need nodejs or io.js installed,
npm takes care of the rest of our dependencies.

* nodejs v0.10 or v0.12 or io.js v1.2
  * We recommend using NodeJS builds from [NodeSource](https://github.com/nodesource/distributions) or using [NVM](https://github.com/creationix/nvm)
* Build tools for building native addons from npm:
  * Debian users install the `build-essential` package
  * Fedora users install `gcc-c++` and `make`
* nginx or apache2

### Building the client

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

6. Set up build options. Create a `.env` file, you'll need to point `BACKEND_URL` at an instance of the [platform api](https://github.com/ushahidi/platform)

    ```
    BACKEND_URL=http://myapi.server/
    ```

7. Run gulp

    ```
    gulp build
    ```

You should now have a client build in server/www.

### Configure nginx or apache

**Nginx**:

1. Copy the virtual host config from server/nginx-site.conf into your nginx conf dir (/etc/nginx or /etc/nginx/sites-enabled)
2. Edit the config:
  - Set `server_name` to whatever domain you plan to use
  - Replace `root /var/www` with the path to server/www ie. `platform-client/server/www`
3. Include the config in your nginx.conf (usually located in /etc/nginx.conf) by adding the following
  ```
  include /etc/nginx/ushahidi-site.conf
  ```
4. Restart nginx
5. Load the new vhost in a browser

**Apache2**:

1. Copy server/rewrite.htaccess to server/www/.htaccess
2. Create a new apache vhost and point the docroot at `server/www`
3. Restart apache
4. Load the new vhost in a browser

## Logging in the first time

The default install creates a user **admin** with password **admin**. Once
logged in this user can create further user accounts or give others admin
permissions too.
