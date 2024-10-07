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


def cat(args, usage_callback):
    """concatenate files and print on the standard output"""
    # Check for valid number of arguments
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="cat")
        return

    # Concatenate the files
    for filename in args:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')tac


def tac(args, usage_callback):
    """concatenate and print files in reverse"""
    # Check for valid number of arguments
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="tac")
        return

    # Concatenate the files
    for filename in args:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in reversed(lines):
                print(line, end='')


def nl(args, usage_callback):
    """number lines of files"""
    # Check for valid number of arguments
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="nl")
        return

    # Concatenate the files
    line_number = 1
    for filename in args:
        with open(filename, 'r') as file:
            for line in file:
                # If the line is not blank
                if line.strip():
                    print(f"{line_number} {line}", end='')
                    line_number += 1
                    continue

                print(line, end='')
