"""Just a quicky script to annoy Dean right now (2015-04-28).

"""
import sys
import os
import time
import random


def touch(filename):
    """Touch a file."""
    with open(filename, 'a'):
        os.utime(filename, None)


def remove(filename):
    """Delete with no error if file doesn't exist."""
    try:
        os.remove(filename)
    except OSError:
        pass

directory = os.path.abspath(sys.argv[1])
template = 'hi-dean-%s.fun~'
delay = 7

# The fun never ends.
FILENAME_LIST = []


def fun():
    print "You're about to have some fun with %s" % template
    while True:

        basename = template % random.randint(10000000, 99999999)
        filename = os.path.join(directory, basename)
        FILENAME_LIST.append(filename)
        print "Fun! %s" % filename

        touch(filename)

        time.sleep(delay)

        # Don't worry if they delete the file, let the fun continue.
        remove(filename)

try:
    fun()
except KeyboardInterrupt:
    for filename in FILENAME_LIST:
        remove(filename)
