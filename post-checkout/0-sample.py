#!/usr/bin/env python

# The post-checkout hook works a lot like the post-commit hook, but it’s called
# whenever you successfully check out a reference with git checkout. This is nice
# for clearing out your working directory of generated files that would otherwise
# cause confusion.
#
# This hook accepts three parameters, and its exit status has no affect on the git
# checkout command.
#
# 1. The ref of the previous HEAD
# 2. The ref of the new HEAD
# 3. A flag telling you if it was a branch checkout or a file checkout. The flag will be 1 and 0, respectively.

# A common problem with Python developers occurs when generated .pyc files stick
# around after switching branches. The interpreter sometimes uses these .pyc
# instead of the .py source file. To avoid any confusion, you can delete all .pyc
# files every time you check out a new branch using the following post-checkout script.

# You can also use the post-checkout hook to alter your working directory based on
# which branch you have checked out. For example, you might use a plugins branch to
# store all of your plugins outside of the core codebase. If these plugins require a
# lot of binaries that other branches do not, you can selectively build them only when
# you’re on the plugins branch.


import os
import sys

# Collect the parameters
previous_head = sys.argv[1]
new_head = sys.argv[2]
is_branch_checkout = sys.argv[3]

if is_branch_checkout == "0":
    print("post-checkout: This is a file checkout. Nothing to do.")
    sys.exit(0)

print("post-checkout: Deleting all '.pyc' files in working directory")
for root, dirs, files in os.walk('.'):
    for filename in files:
        ext = os.path.splitext(filename)[1]
        if ext == '.pyc':
            os.unlink(os.path.join(root, filename))
