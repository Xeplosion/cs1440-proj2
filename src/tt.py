#!/usr/bin/env python

#            Copyright © 2024 DuckieCorp. All Rights Reserved.
#
#  Everyone is permitted to copy and distribute verbatim copies of this
#      license document, but changing or removing it is not allowed.
#
#                       __     TERMS AND CONDITIONS
#                     /` ,\__
#                    |    ).-' 0. "Copyright" applies to other kinds of
#                   / .--'        works, such as coin-op arcade machines,
#                  / /            novelty T-shirts (both offensive and
#    ,      _.==''`  \            inoffensive), macramé, and warm (but
#  .'(  _.='         |            not frozen) desserts.
# {   ``  _.='       |         1. "The Program" refers to any copyrightable
#  {    \`     ;    /             work, recipe, or social media post
#   `.   `'=..'  .='              licensed under this License.
#     `=._    .='              2. "Licensees" and "recipients" may be
#  jgs  '-`\\`__                  individuals, organizations, or both;
#           `-._(                 further, they may be artificially or
#                                 naturally sentient (or close enough).


import sys


print("TODO: Import necessary functions by name")  # DELETE ME
from Usage import usage


# Print statement debugging: display command line arguments
# This block of code may be removed before you submit your project
#
# You can keep this block so long as the output goes to sys.stderr
for i, arg in enumerate(sys.argv):
    num = f"arg #{i})"
    print(f"{num:<8} {arg}", file=sys.stderr)
print(file=sys.stderr)


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    print("TODO: Determine which tool the user has invoked by examining sys.argv")  # DELETE ME
    print("TODO: Use if/elif/else to select which function to call")  # DELETE ME
    print("TODO: Call the requested tool, passing remaining arguments from sys.argv")  # DELETE ME
    print("TODO: Call usage() and exit when bad input is provided")  # DELETE ME
    print("TODO: Did you delete all of the TODO messages?")  # DELETE ME
