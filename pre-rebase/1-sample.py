#!/usr/bin/env python

# The pre-rebase hook is called before git rebase changes anything, making it a good
# place to make sure something terrible isn’t about to happen.

# This hook takes 2 parameters: the upstream branch that the series was forked from,
# and the branch being rebased. The second parameter is empty when rebasing the
# current branch. To abort the rebase, exit with a non-zero status.
# For example, if you want to completely disallow rebasing in your repository,
# you could use the following pre-rebase script:

import sys

_, base_branch, rebased_branch = sys.argv
print(f"base branch: {base_branch}\nrebased branch:{rebased_branch}")

# Disallow all rebasing
print("Rebasing is dangerous. Don't do it.")
sys.exit(1)
