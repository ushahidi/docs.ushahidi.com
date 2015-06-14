---
layout: page
title:  "Chapter 3"
subtitle: "Installing the Platform"
date:   2015-04-23 21:28:00
categories: chapter
weight: 3
---

## Tech Environment
Deploying Ushahidi on your own server requires some careful thought. The technology requirements are straightforward:

### Server

1.    Unix/Linux
2.    MacOSX
3.    Windows

Server can be in the cloud or in your own hosting environment. You can even run Ushahidi v3 on your laptop.

1.    PHP version 5.4.0 or greater
2.    MySQL database version 5.5 or greater (PostgreSQL support planned)
3.    An HTTP server, we develop Ushahidi using Apache 2.2+ and nginx
4.    Unicode support in the operating system (UTF-8 charset, PCRE, iconv extension, etc)

### Database

Ushahidi is currently built on MySQL. With version 3, however, your can use other databases, provided you build the interface. (explain).

### Cloud v Rack Servers

Ushahidi can be deployed on a physical server in your custody (or even a laptop in the field). It can also be deployed on a cloud-based server. There are pros and cons for each setup:
Matrix: Cloud v Rack


### Tech expertise (ToR)

To deploy your instance and maintain it, you will need to have a tech team on call or on staff. Keeping a stack of tools running—from the telco SMS system to your data exports—is not something for a novice to attempt, particularly when sensitive data is pasing through the system.

When to have the following positions:

1.    Security Officer
2.    System Admin
3.    Developer
4.    UX Designer
5.    Data Scientist
6.    Data Visualization Specialist

## Unix/Linux
The manual installation process on UNIX/Linux, as defined by the Ushahidi Wiki. The first choice you will need to make is whether you will run the web server in a virtual machine (such as Vagrant) or directly on the local server. If you are going to use Vagrant:

1.    Install Vagrant (and its dependency, Virtual Box) following the instructions on the Vagrant website and Virtual Box web site.
2.    Check the settings in the Vagrantfile
3.    Start the virtual machine (VM) from your console: % vagrant up

[ explain what vagrant does ]

### 1. Clone the code from Git

First, get a copy of the Ushahidi v3 source code. Go the directory in which you will be installing v3 and clone the source code which lives in the Ushahidi Github repository:

```
% git clone https://github.com/ushahidi/platform.git
```

### 2. Prepare the Web Server

Prepare the database
To create a database, first login to MySQL as root.

```
% mysql -u root -p
```

Using the -p is only required when your MySQL configuration requires it. You may need to use the -h option to specify localhost or 127.0.0.1 if you are unable to connect.

Next, create a new user and database for Ushahidi. The username and database can be anything; we will use ushahidi for both in this example:

```
CREATE DATABASE ushahidi;
GRANT ALL ON ushahidi.* to ushahidi@localhost IDENTIFIED BY 'set-a-strong-password-here';
quit;
```

[ strong password link ]

#### Configure the database.php file
Now copy the database.php config file into environments/development/ and edit it. Make sure that the database, username, and password match the database you just created.

```
% cp application/config/database.php application/config/environments/development/database.php
% $EDITOR application/config/environments/development/database.php
```


#### Configure the .htaccess file

You should also rename template.htaccess in httpdocs to .htaccess (for Apache) to enable rewriting of all non-existent files to index.php. If you do not want to, or are unable to, enable rewriting, then customize the initialization settings by also copying the init.php config file into environments/development/ and editing it, setting index_file to “index.php”.

Typically, Ushahidi is run under a separate virtual host / domain name. Be sure to make platform/httpdocs/ the DocumentRoot (for Apache) or root (for nginx) setting in your virtual host
.

If you are running Ushahidi via http://localhost/ then the base_url will be http://localhost/platform/httpdocs/

You may need to set the RewriteBase statement to match the directory in which the Ushahidi instance is running

#### Set base directory

```
RewriteBase /ushahidi3/httpdocs/
```

#### Set Permissions for writeable directories
Enable writing to the logs, cache, and upload directories:

```
% chmod 0777 application/logs application/cache application/media/uploads
```

If you are running in shared or production environment, it is better to use chown to set the owner of the directories to the user that runs the web server runs as, rather than making them globally writable.

[ note: we are recommending 777 permission here. we may want to be have the example show run as the web server user instead with lesser permissions ]

### 3. Install Dependencies
You can now check if you have everything ready with the install checklist: http://hostname:port/httpdocs/index.php?install=1

#### Composer

Composer is a tool to help manage PHP libraries. For installation, see https://getcomposer.org/doc/00-intro.md.

#### NPM

Node Packaged Modules is a NodeJS package manager. Bower (below) requires it. A good introduction to NPM can be found on Isaac Schlueter’s site. Download NPM here.

#### Bower

Bower is a tool to manage the assets of a web site. It can be downloaded here.

#### UI Dependencies
We use Composer to manage server side dependencies, and Bower to manage our client-side JS and CSS dependencies. Once you have installed both tools, you can run the update script with:

```
% bin/update
```

Whenever the repository is updated using git pull, run the update script to ensure that your installation stays updated!

If you are updating a production deployment, you will want to avoid installing developer dependencies (testing tools, etc) by using the “deploy” option:

```
% bin/update deploy
```

#### Icon
To install Bower, you will need to have NPM installed. How NPM is installed depends on your operating system, see Introduction to NPM for more information.

If you are going to modify the CSS, you will also need to install the UI dependencies.

### Configuration
Base config files are in application/config/.

You can add per-environment config overrides in application/config/environments/. The environment is switched based on the KOHANA_ENV environment variable.

Routes are configured in application/routes/default.php. Additional routes can be added in per-environment routing files ie. application/routes/development.php

## Mac OSX

There are 3 main ways to install Ushahidi 3.x on Mac OS:

* Using Vagrant virtual machine
* Using Homebrew to install mysql and run Ushahidi natively
* Use Mamp

Vagrant is generally recommended for Ushahidi 3.x because it allows you to isolate your environment, and you don't have to manage a *AMP (Apache-Mysql-Php) stack on your Mac.   Homebrew is recommended over Vagrant if you're going to develop other websites locally on your Mac. Mamp is last on the list of recommendations.

### Configuring Apache, PHP, and MySQL Using Homebrew

#### Install Homebrew

The first thing you will need to do is install Homebrew. Open up your terminal and run this:

Do not run any of these commands with sudo! Repeat: *DO NOT USE sudo!*

```
% ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

Pay attention to all the instructions, run the brew doctor command as required, and be sure to configure your PATH afterwards (you might not need to do this).

#### Install MySQL with Homebrew

OSX does not come with MySQL installed by default, so we will need to install it using Homebrew:

```
% brew install mysql
```

Follow all of the instructions that are output by this process, including the parts about securing your database. Once installed you might want to use LaunchRocket.prefPane to manage MySQL and other services you install with Homebrew.

#### Install PHP with Homebrew

Next you will need to install PHP. Because OSX comes with PHP preinstalled, and Homebrew does not duplicate preinstalled packages, you will need to "tap" a new repository first:

```
% brew tap josegonzalez/homebrew-php
% brew install php54 php54-http php54-mcrypt
```

Again, follow all of the instructions that are output by this process. Once successful, you will also want to install composer:

```
% brew install composer
```

Installing composer this way is optional, but will ensure that your local version of Composer stays updated when you run brew upgrade.

You should also edit /usr/local/etc/php/5.4/php.ini and set date.timezone to your local timezone. Check the list of supported timezones and choose the one most appropriate.

#### Enable the Built-in Apache Server

Mac OSX comes with Apache installed by default, but disabled. The easiest way to enable it it is to use WebSharing.prefPane. If you want to start Apache manually, you can use:

```
sudo apachectl start
```

To add a new virtual host, you will need to edit the Apache configuration in /etc/apache2. You might want to use either osx-vhost manager (free) or VirtualHostX (paid) to help manage virtual hosts.

#### Finished

Once these steps are completed, have you have properly updated your PATH to include /usr/local/bin, you can follow the rest of the install process. Double check that everything is installed properly with:

```
% php --version
% mysql --version
```

You should end up with PHP 5.4.x and MySQL 5.6.x (or higher).

#### Now Install and Run Ushahidi

Go to Installing Ushahidi 3.x and follow the instructions there, starting with downloading the Ushahidi code.

### Installing Ushahidi 3.x on OSX with MAMP Pro

#### Install Git
If git is not installed on your machine or the version you have installed by default requires XCode, download and install this version:

http://git-scm.com/download/mac

#### Setting up MAMP Pro

* GENERAL - no need to change anything here:

* HOSTS
	* Create a new host by clicking the [+] at bottom left
	* Give your server a name - in our case (ushahidi.dev)
	* Create a folder to hold the site by clicking the folder icon - in our case /Applications/MAMP/ushahidi

 At this point we don't need to modify anything else

#### Create a Database

* Click on the phpMyAdmin link at the bottom of the MySQL screen above
* Click on the Databases tab within phpMyAdmin
* Create an ushahidi database


#### Downloading and installing Ushahidi

* Open the 'Terminal' app by going to Applications > Utilities > Terminal
* Change to our document root folder
cd /Applications/MAMP/ushahidi

* Remove the default MAMP Pro files from this directory
rm MAMP-PRO-Logo.png
rm index.php

* Clone the Ushahidi Platform repository from Github
git clone --recursive https://github.com/ushahidi/platform ./

* Follow the rest of the instructions listed here with the exception of using the database.php file listed below:

```
<?php defined('SYSPATH') or die('No direct access allowed.');
/**
 * Database Config
 *
 * @author     Ushahidi Team <team@ushahidi.com>
 * @package    Ushahidi\Application\Config
 * @copyright  2013 Ushahidi
 * @license    https://www.gnu.org/licenses/agpl-3.0.html GNU Affero General Public License Version 3 (AGPL3)
 */
return array
(
    'default' => array
    (
        'type'       => 'MySQLi',
        'connection' => array(
            'hostname'   => 'localhost',
            'database'   => 'ushahidi',
            'username'   => 'root',
            'password'   => 'root',
            'socket'     => '/Applications/MAMP/tmp/mysql/mysql.sock',
            'persistent' => FALSE,
        ),
        'table_prefix' => '',
        'charset'      => 'utf8',
        'caching'      => TRUE,
        'profiling'    => TRUE,
    )
);
```

Your new site will be accessible at http://ushahidi.dev:8888/

## Windows

1. Clone the code from Git

First, get a copy of the Ushahidi v3 source code. Go the directory in which you will be installing v3 and clone the source code which lives in the Ushahidi Github repository:

```
% git clone https://github.com/ushahidi/platform.git
```

2. Prepare the Web Server

* Prepare the database *
To create a database, first login to MySQL as root.

```
% mysql -u root -p
```

Using the -p is only required when your MySQL configuration requires it. You may need to use the -h option to specify localhost or 127.0.0.1 if you are unable to connect.

Next, create a new user and database for Ushahidi. The username and database can be anything; we will use ushahidi for both in this example:

```
CREATE DATABASE ushahidi;
GRANT ALL ON ushahidi.* to ushahidi@localhost IDENTIFIED BY 'set-a-strong-password-here';
quit;
```

[ strong password link ]

### Configure the database.php file

Assuming that you have cloned Lamu into folder c:\wamp\www\Lamu
Use localhost/phpmyadmin to create a database.  I've called mine lamutest.  Your database.php should look something like this:

```
return array
(
 'default' => array
 (
 'type' => 'MySQLi',
 'connection' => array(
 'hostname' => 'localhost',
 'database' => 'lamutest',
 'username' => 'root',
 'password' => 'mypassword',
 'persistent' => FALSE,
 ),
 'table_prefix' => '',
 'charset' => 'utf8',
 'caching' => TRUE,
 'profiling' => TRUE,
 )
);
```

Where 'database' is the database name that you chose; 'username' is the user that you set up in phpmyadmin (look at the 'users' tab: my user is root@127.0.0.1) and 'password' is the password that you set up for that phpmyadmin user.

### Base_url
Like with Ushahidi v2.x, your baseurl is going to be slightly different to everyone else's.
In init.php, for Ushahidi v3 installed at c:\wamp\www\Lamu, it's

```
 'base_url'    => '/lamu/httpdocs',
```

In .htaccess, it's

```
RewriteBase /lamu/httpdocs/
```

### Minion
Minion won't work if you can't run php (you can test this by trying "php -v" in your terminal window).  To make this happen in wamp,  find your system path (on windows 7, that's control panel > system and security > system, then advanced system settings, (lhs list) and add a link to your php to it: for my Wamp install, that means adding the text

```
";C:\wamp\bin\php\php5.3.13"
```

to my path; you might want to look in

```
C;\wamp\bin\php
```

to see what the right address for you is (e.g. you might have a different version of php).

In your terminal window, go to your top-level directory (in this case, c:/wamp/www/Lamu) and run minion with this command:

```
php minion --task=migrations:run --up
```

Go to http://localhost/lamu/httpdocs/

## Migrating from v2
TBD


