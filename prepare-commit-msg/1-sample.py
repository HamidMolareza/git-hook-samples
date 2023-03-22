#!/usr/bin/env python

import re
import sys
from subprocess import check_output

# Collect the parameters
_, commit_msg_filepath, commit_type, commit_hash = sys.argv

print(f"File: '{commit_msg_filepath}' - Type: '{commit_type}' - Hash: '{commit_hash}'")

# Figure out which branch we're on
branch = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).decode("utf-8").strip()
print(f"On branch '{branch}'")

# Populate the commit message with the issue #, if there is one
if branch.startswith("issue-"):
    print("Oh hey, it's an issue branch.")
    result = re.match("issue-(.*)", branch)
    issue_number = result.group(1)

    with open(commit_msg_filepath, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(f"ISSUE-{issue_number} {content}")
