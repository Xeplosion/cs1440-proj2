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


def cut(args, usage_callback):
    """remove sections from each line of files"""
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="cut")
        return

    # Parse flags
    fields_to_extract = [0]
    if '-f' in args:
        try:
            f_index = args.index('-f')
            fields = args[f_index + 1]
            fields_to_extract = [int(f) - 1 for f in fields.split(',')]
            del args[f_index:f_index + 1]
        except (ValueError, IndexError):
            usage_callback(error="Error: invalid field specification", tool="cut")
            return

    print(f"FIELDS: {fields_to_extract}")
    # Sort files for processing
    processed_files = []
    for filename in args:
        processed_file = []
        with open(filename, 'r') as file:
            for line in file:
                processed_file.append(line.strip()) # Strip newline

        processed_files.append(processed_file)

    # Iterate through the arrays and extract desired fields
    line = 0
    while True:
        out = []
        exhausted = 0

        for file in processed_files:
            if line < len(file):
                fields = file[line].split(',')
                for field_num in fields_to_extract:
                    if field_num < len(fields):
                        out.append(fields[field_num])
                    else:
                        out.append('')
            else:
                exhausted += 1  # Count exhausted files

        if exhausted == len(processed_files):
            break  # Exit if all files are exhausted

        if out:
            print(','.join(out))
        else:
            print('')

        line += 1


def paste(args, usage_callback):
    """merge lines of files"""
    # Check for valid number of arguments
    if len(args) < 1:
        usage_callback(error="Error: too few arguments", tool="paste")
        return

    # Sort the file lines into arrays
    processed_files = []
    for filename in args:
        with open(filename, 'r') as file:
            processed_files.append([line.strip() for line in file.readlines()])

    # Iterate through the arrays creating appropriate output
    line = 0
    while True:
        out = []
        exhausted = 0
        for file in processed_files:
            if line < len(file):
                out.append(file[line])
            else:
                exhausted += 1

        if exhausted == len(processed_files):
            break  # Exit if all files are exhausted

        print(','.join(out))
        line += 1
