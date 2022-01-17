#!/usr/bin/env python
import sys

stop_words = {
 '.',
 ',',
 ':',
 'a',
 'the',
 'an',
 'and'
}

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if not word in stop_words:
        	print '%s\t%s' % (word, "1")
