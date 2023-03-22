#!/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.

. git-sh-setup
pre_commit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$pre_commit" && exec "$pre_commit" ${1+"$@"}
:
