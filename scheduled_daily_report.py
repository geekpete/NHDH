from NHDH.modules.daily import Daily
from NHDH.modules.trails import Trails
from NHDH.modules.py_email import *
from NHDH.modules.cache import cache
from datetime import datetime
from dateutil import parser
from StringIO import *
from flask import Blueprint, request, redirect, url_for,  \
     render_template, flash, send_from_directory, send_file, Flask
from math import isnan
import os,sys,locale,yaml
from NHDH.modules.fetch import *
from NHDH import app

#app configuration items
app = Flask(__name__)
app.secret_key = 'sdakjk353453453456346346346346326346460103939999kjkjkjdksjkajlkjaskljdkljklsdj'
app.config['UPLOAD_FOLDER'] = os.path.abspath('NHDH/csv')
app.config['CONFIG_FILE'] = os.path.abspath('NHDH/conf/config.yml')
app.config['ALLOWED_EXTENSIONS'] = set(['zip'])
app.config['CSV_FOLDER'] = os.path.abspath('NHDH/csv/')

configStr = open(app.config['CONFIG_FILE'], 'r')
app.config['CONFIG'] = yaml.load(configStr)

#try:
    # fetch latest data
ff = Fetch()
ff.fetch(scheduler=True)
#except:
#    print >> sys.stderr, "ERROR: failed to download file from S3 bucket"
#    sys.exit(1)
sys.exit(0)

# Determine the current date's filename to run the report on
dt = datetime.now()
datefilename = dt.strftime("%Y-%m")
billingCsv = str(app.config['CONFIG']['s3']['account_number'])+"-aws-billing-detailed-line-items-with-resources-and-tags-"+datefilename+".csv"

daily = Daily()
mdf = daily.month_by_day(filename)
html = render_template('dailymail.html',
                           mdf=mdf)
dt = datetime.now()
show = dt.strftime("%A %d %B %Y")
try:
    py_email('Daily Report '+ show, html)
    print 'Successfully sent daily mail.'
except smtplib.SMTPException, emsg:
    #return ' SMTPException : '+str(emsg)
    print ' SMTPException : '+str(emsg)

