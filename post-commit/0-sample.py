#!/usr/bin/env python

# The post-commit hook is called immediately after the commit-msg hook.
# It can’t change the outcome of the git commit operation, so it’s used primarily for
# notification purposes.
#
# The script takes no parameters and its exit status does not affect the commit in any
# way. For most post-commit scripts, you’ll want access to the commit that was just
# created. You can use git rev-parse HEAD to get the new commit’s SHA1 hash, or
# you can use git log -1 HEAD to get all of its information.
#
# For example, if you want to email your boss every time you commit a snapshot
# (probably not the best idea for most workflows), you could add the following
# post-commit hook.

# It’s possible to use post-commit to trigger a local continuous integration system,
# but most of the time you’ll want to be doing this in the post-receive hook. This runs
# on the server instead of the user’s local machine, and it also runs every time any
# developer pushes their code. This makes it a much more appropriate place to perform
# your continuous integration.


import sys
import smtplib
from email.mime.text import MIMEText
# from subprocess import check_output

# # Get the git log --stat entry of the new commit
# log = check_output(['git', 'log', '-1', '--stat', 'HEAD']).decode("utf-8")
#
# # Create a plaintext email message
# message = MIMEText("Look, I'm actually doing some work:\n\n%s" % log)
#
# message['Subject'] = 'Git post-commit hook notification'
# message['From'] = 'mary@example.com'
# message['To'] = 'boss@example.com'
#
# # Send the message
# SMTP_SERVER = 'smtp.example.com'
# SMTP_PORT = 587
#
# session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# session.ehlo()
# session.starttls()
# session.ehlo()
# session.login(message['From'], 'secretPassword')
#
# session.sendmail(message['From'], message['To'], message.as_string())
# session.quit()
