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


def grep(args, usage_callback):
    """print lines that match patterns"""
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="grep")
    search = args[0]
    del args[0]

    # Parse flags
    v = False
    if '-v' in args:
        v_index = args.index('-v')
        del args[v_index]

    if len(args) > 1:
        for filename in args:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if search in line:
                        print(f"{filename}: {line}", end='')

        return
    elif len(args) == 1:
        with open(args[0]) as file:
            lines = file.readlines()
            for line in lines:
                if search in line:
                    print(line, end='')
    else:
        usage_callback(error="Error: please provide a pattern and at least one filename", tool="grep")


