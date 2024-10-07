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


def head(args, usage_callback):
    """output the first part of files"""
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="head")
    # Parse flags
    n = 10
    if '-n' in args:
        try:
            n_index = args.index('-n')
            n = int(args[n_index + 1])
            args = args[:n_index] + args[n_index + 2:]  # Isolate the filepath arguments
            del args[n_index:n_index + 1]
        except (ValueError, IndexError):
            usage_callback(error="Error: number of lines is required", tool="head")
            return

    # Concatenate the files
    multiple = False
    if len(args) > 1:
        multiple = True

    for filename in args:
        if multiple:
            print(f"==> {filename} <==")

        with open(filename, 'r') as file:
            line_count = 1
            for line in file:
                if line_count > n:
                    break

                print(line, end='')
                line_count += 1

        print(' ')


def tail(args, usage_callback):
    """output the last part of files"""
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="head")
    # Parse flags
    n = 10
    if '-n' in args:
        try:
            n_index = args.index('-n')
            n = int(args[n_index + 1])
            args = args[:n_index] + args[n_index + 2:]  # Isolate the filepath arguments
            del args[n_index:n_index + 1]
        except (ValueError, IndexError):
            usage_callback(error="Error: invalid field specification", tool="head")
            return

    # Concatenate the files
    multiple = False
    if len(args) > 1:
        multiple = True

    for filename in args:
        if multiple:
            print(f"==> {filename} <==")

        with open(filename, 'r') as file:
            line_count = 1
            lines = file.readlines()
            for line in lines[-n:]:
                if line_count > n:
                    break

                print(line, end='')
                line_count += 1

        print('')
