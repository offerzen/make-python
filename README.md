# make-python

This is an example Python app that allows a user to engage with the Root Insurance API via a Slack bot.

The app makes use of the official [Slack Developer Kit for Python](https://github.com/slackapi/python-slackclient) package, specifically the [Real Time Messaging](http://slackapi.github.io/python-slackclient/real_time_messaging.html) WebSocket-based api.

### Getting set up

The example app was developed using Python 3.6 but should work with all versions of Python 3. Changing the code for python 2.7 compatability shouldn't be too much work.

We recommend using an environment manager to set up an isolated python environment for this app. We use [virtualenv](https://virtualenv.pypa.io/en/stable/) but others will also do (`conda`, if you're using an anacondas python installation).

The examples below are for `virtualenv` on a but shouldn't be too different for other operating systems (unless you're using Windows - then you're on your own) and environment managers.

#### Clone the repo
```sh
$ git clone git@github.com:Offerzen/make-python.git
$ cd make-python
```

#### Set up and activate your environment
```sh
$ virtualenv -p /usr/local/bin/python3 make-python
$ source  source make-python/bin/activate
```

#### Install the requirements
```sh
$ pip install -r requirements.txt
```

#### Set up the environment variables
The following environment variables are required by the app:

`SLACK_API_TOKEN`: Your slackbot's API token

`ROOT_APP_ID`: Your Root app's id

`ROOT_APP_SECRET`: Your root app's secret key

#### Run the app
```sh
$ python run.py
```

