#!/usr/bin/env python

"""Print words for which certain differentiating properties exist.  This may
help in finding which rule letter should be modified because it has the least
undesired side-effects.
"""

for line in open("de_DE-1901.dic"):
    if line and not line.startswith("\t") and not line[0] in "0123456789":
        word, sep, rules = line.strip().rpartition("/")
        if sep == "/":
            if "P" in rules and not "E" in rules and word.endswith("ß"):
                print(word)
