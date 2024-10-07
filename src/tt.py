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
from Usage import usage
from Concatenate import cat, tac, nl
from CutPaste import cut, paste
from Grep import grep
from Partial import head, tail
from Sorting import sort
from WordCount import wc


if len(sys.argv) < 2:
    usage()
    sys.exit(1)
else:
    tool_name = sys.argv[1]
    options = sys.argv[2:]

    print(options)

    if tool_name == "cat":
        cat(options, usage)
    elif tool_name == "tac":
        tac(options, usage)
    elif tool_name == "nl":
        nl(options, usage)
    elif tool_name == "cut":
        cut(options, usage)
    elif tool_name == "paste":
        paste(options, usage)
    elif tool_name == "wc":
        paste(options, usage)
    elif tool_name == "grep":
        grep(options, usage)
    elif tool_name == "head":
        head(options, usage)
    elif tool_name == "tail":
        tail(options, usage)
    elif tool_name == "sort":
        sort(options, usage)
    else:
        usage(error=f"Error: {tool_name} is not a valid subcommand")

    sys.exit(0)
