#!/usr/bin/env python

# The commit-msg hook is much like the prepare-commit-msg hook, but it’s called after
# the user enters a commit message. This is an appropriate place to warn developers
# that their message doesn’t adhere to your team’s standards.
# The only argument passed to this hook is the name of the file that contains the
# message. If it doesn’t like the message that the user entered, it can alter this
# file in-place (just like with prepare-commit-msg) or it can abort the commit
# entirely by exiting with a non-zero status.

# For example, the following script checks to make sure that the user didn’t delete the
# ISSUE-[#] string that was automatically generated by the prepare-commit-msg hook in
# the previous section.

# While this script is called every time the user creates a commit, you should avoid
# doing much outside of checking the commit message. If you need to notify other
# services that a snapshot was committed, you should use the post-commit hook instead.
# https://www.atlassian.com/git/tutorials/git-hooks

import re
import sys
from subprocess import check_output

# Collect the parameters
commit_msg_filepath = sys.argv[1]

# Figure out which branch we're on
branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).decode("utf-8").strip()
print(f"commit-msg: On branch '{branch}'")

# Check the commit message if we're on an issue branch
if branch.startswith('issue-'):
    print("commit-msg: Oh hey, it's an issue branch.")
    result = re.match('issue-(.*)', branch)
    issue_number = result.group(1)
    required_message = "ISSUE-%s" % issue_number

    with open(commit_msg_filepath, 'r') as f:
        content = f.read()
        if not content.startswith(required_message):
            print(f"commit-msg: ERROR! The commit message must start with '{required_message}'")
            sys.exit(1)
