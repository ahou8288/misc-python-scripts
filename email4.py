#!/usr/bin/python

import smtplib

message = """From: From Person <from@fromdomain.com>
To: To Person <a.houghton@exemail.com.au>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print "Successfully sent email"
