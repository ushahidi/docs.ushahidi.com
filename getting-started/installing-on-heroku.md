---
layout: page
title:  "Installing on Heroku"
subtitle: ""
categories: getting-started
weight: 1
---

Deploying on Heroku is good way to test out the platform quickly. Its also a viable option for running a production deployment (though this could be expensive depending on your traffic needs).

1. First deploy the API with the [latest release](https://heroku.com/deploy?template=https://github.com/ushahidi/platform/tree/release) or the [latest development code](https://heroku.com/deploy?template=https://github.com/ushahidi/platform/tree/master)
  * If you haven't used heroku before, you'll be asked to sign up:
  * Pick an *App name* for your deployment (or let heroku pick one for you)
	<img src="https://www.dropbox.com/s/hukiitu167o49je/Screenshot%202015-08-10%2011.58.48.png?dl=1" />
  * then hit **Deploy for free**
  * .. and wait <img src="https://www.dropbox.com/s/55bsfgs3ltdl0ce/Screenshot%202015-08-10%2012.03.19.png?dl=1" />
  * Confirm you're deployment went ok by clicking "View". You should see a block of JSON something like: <img src="https://www.dropbox.com/s/clfm4tk5ebsusel/Screenshot%202015-08-10%2012.04.01.png?dl=1" />
  * Take not of the URL of the created app (ie: https://afternoon-castle-5024.herokuapp.com/)
2. **Deploy the client** with the [latest release](https://heroku.com/deploy?template=https://github.com/ushahidi/platform-client/tree/release) or the [latest development code](https://heroku.com/deploy?template=https://github.com/ushahidi/platform-client/tree/master).<br />Make sure you use the same version as you did for the API.
  * Again, Pick an *App name* for your deployment
  * Set *Backend URL* to the URL of the API app you just created (ie: https://afternoon-castle-5024.herokuapp.com/)
  <img src="https://www.dropbox.com/s/str18yzvur7xj06/Screenshot%202015-08-10%2012.09.15.png?dl=1" />
    **Important: make sure you don't include the trailing slash **
  * Leave other config as-is
  * hit **Deploy for free**
  * .. and wait (the client takes much longer to deploy)
  * Click **View** and check out you're new deployment
3. Log in to your new deployment
  * By default there is a single user<br />
  	username: admin<br />
  	password: admin

### Follow up: configuring scheduled jobs for fetching/sending messages
