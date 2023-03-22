#!/usr/bin/env python

# The pre-receive hook is executed every time somebody uses git push to push commits
# to the repository. It should always reside in the remote repository that is the
# destination of the push, not in the originating repository.
#
# The hook runs before any references are updated, so it’s a good place to enforce any
# kind of development policy that you want. If you don’t like who is doing the pushing,
# how the commit message is formatted, or the changes contained in the commit, you can
# simply reject it. While you can’t stop developers from making malformed commits,
# you can prevent these commits from entering the official codebase by rejecting them
# with pre-receive.
#
# The script takes no parameters, but each ref that is being pushed is passed to
# the script on a separate line on standard input in the following format:
#
# <old-value> <new-value> <ref-name>

# https://www.atlassian.com/git/tutorials/git-hooks

import sys
import fileinput

# Read in each ref that the user is trying to update
for line in fileinput.input():
    print(f"pre-receive: Trying to push ref: {line}")

# Abort the push
# sys.exit(1)
