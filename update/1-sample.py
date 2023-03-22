#!/usr/bin/env python

# The update hook is called after pre-receive, and it works much the same way.
# It’s still called before anything is actually updated, but it’s called separately
# for each ref that was pushed. That means if the user tries to push 4 branches, update
# is executed 4 times. Unlike pre-receive, this hook doesn’t need to read from standard
# input. Instead, it accepts the following 3 arguments:
#
# 1. The name of the ref being updated
# 2. The old object name stored in the ref
# 3. The new object name stored in the ref
#
# This is the same information passed to pre-receive, but since update is invoked
# separately for each ref, you can reject some refs while allowing others.

import sys

branch = sys.argv[1]
old_commit = sys.argv[2]
new_commit = sys.argv[3]

print(f"Moving '{branch}' from {old_commit} to {new_commit}")

# Abort pushing only this branch
# sys.exit(1)
