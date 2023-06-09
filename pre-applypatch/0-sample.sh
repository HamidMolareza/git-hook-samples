#!/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.

. git-sh-setup
pre_commit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$pre_commit" && exec "$pre_commit" ${1+"$@"}
:
