# NHDH a Stats Reducer for AWS CSV
The purpose of this program is to reduce the large number of line items in a detailed billing file to a daily/monthly summary.

#### What it does
 - Downloads direct from your billing bucket
 - Displays a monthly summary including daily total, % daily difference, running total
 - Emails the monthly summary to a list of recipients
 - processes uploaded billing zip files
 - provides a summary csv for download
 - basic js graphing
 - flask caching - for those large reports
 - added support for UnBlendedCost or Cost report formats - its a kludge but it works

#### What we are currently working on
 - a better ui - to replace the crappy one monk-ee knocked up
 - administrative panel
 - json gui

## Quickstart
 - You will need to fill out the configuration data in the config.yml.sample and save it as config.yml
 - s3
 - account_number   : '' #your Amazon Account number
 - billing_bucket   : '' #the name of your billing bucket
 - name             : '' #the name of your administrative account user - currently not used
 - aws_access_key   : '' #user access key
 - aws_secret_key   : '' #user secret key
 - smtp
 - name             : '' # name of account user - ses specific - currently not used
 - user             : '' # user account for smtp auth
 - password         : '' # user password for smtp auth
 - server           : '' # smtp server without port
 - sender_address   : 'me@mysite.com' #smtp from address
 - port             : '587' # we always engage tls
 - recipients: # this is an array of accounts
 - address     : 'test@test.com'
 - general:
 - format           : 'standard' # we have noticed that there are different formats for the bills
 - filter: ''
 - debug            : 'True' # bugginess to be reported
 - cache:
 - timeout: '600'#the length of time you want your pages cached
 - scheduler:
 - hourly_interval: '4' #the interval at which the scheduler runs
 - logfile: 'nhdh.log' # a log file mainly for scheduler actions

 - on the AWS side you will need to ensure that the S3 billing bucket has a policy to allow access to it and that programmatic access to billing is enabled.

 - resolve all dependencies

 - you can change the port in the runserver.py

#### Dependencies
 - Flask==0.10.1
 - Jinja2==2.7.1
 - Werkzeug==0.9.4
 - wsgiref==0.1.2
 - boto==2.19.0
 - numpy==1.8.0
 - pandas==0.12.0
 - PyYAML==3.10
 - Flask-Cache==0.12
 - APScheduler==2.1.1

### Debian/Ubuntu

(Only debian/ubuntu instructions for now until I test it all out on RHEL)

Ensure you can build the required python libs by installing python development libraries:

`sudo apt-get install python-dev`

Install the required python libraries:

`sudo pip install -r requirements`

### NHDH has been changed to a flask blueprint.

Run it up:

`python runserver.py`

Test by going to:
<http://localhost:5000/> or <http://yourservername:5000/>

To run the scheduler:

Run:

`./scheduler.py`

### RHEL

TODO... TOOHARD

### Windows

* You'll need Microsoft Visual Studio if you want to compile the pandas and numpy python libraries yourself.
* You can download precompiled versions of pandas and numpy from pypi site
* pip for windows is easy too <https://sites.google.com/site/pydatalog/python/pip-for-windows>

### Screenshots
Screenshot of home view:

![ScreenShot](https://raw.github.com/monk-ee/NHDH/master/screenshots/home_screen.png)

Screenshot of daily summary view:

![ScreenShot](https://raw.github.com/monk-ee/NHDH/master/screenshots/daily_screen.png)

Screenshot of daily graph view:

![ScreenShot](https://raw.github.com/monk-ee/NHDH/master/screenshots/daily_graph.png)

Screenshot of email body:

![ScreenShot](https://raw.github.com/monk-ee/NHDH/master/screenshots/email_shot.png)

### Contributors
 - @monkee_magic - hidden code development - poor html and css
 - @geekpetedotcom - hidden code and quality control
 - @linkthief - the stuff that everyone sees
 - @dizzy_thinks - mad refactoring skills
