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


def wc(files, usage_callback):
    """print newline, word, and byte counts for each file"""
    if len(files) < 1:
        usage_callback(error="Error: too few arguments", tool="wc")
        return

    total_lines = 0
    total_words = 0
    total_chars = 0

    for filename in files:
        with open(filename, 'r') as file:
            lines = file.readlines()

            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)

            # Update totals
            total_lines += num_lines
            total_words += num_words
            total_chars += num_chars

            # Print individual file counts
            print(f"{num_lines}\t{num_words}\t{num_chars}\t{filename}")

    # Print total
    print(f"{total_lines}\t{total_words}\t{total_chars}\t total")

