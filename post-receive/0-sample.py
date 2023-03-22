#!/usr/bin/env python

# The post-receive hook gets called after a successful push operation, making it a good
# place to perform notifications. For many workflows, this is a better place to trigger
# notifications than post-commit because the changes are available on a public server
# instead of residing only on the user’s local machine. Emailing other developers and
# triggering a continuous integration system are common use cases for post-receive.
#
# The script takes no parameters, but is sent the same information as pre-receive via
# standard input.

import fileinput

for line in fileinput.input():
    print("post-receive:", line)
