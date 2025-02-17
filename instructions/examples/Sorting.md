# Sorting Files

### Important: do not create your own sorting routine!

The purpose of this project is to practice *text processing* and *command-line interfaces*. Because you have already studied sorting algorithms in CS 1400, **you have earned the right to use Python's built-in sorting function** instead of writing your own.

**TL;DR: if you think you need to write a bubble-sort or insertion sort, you're doing it wrong**


## sort

For each input file named on the command line, `sort` prints the contents sorted in *lexical* order:

    $ python src/tt.py sort data/colors8
    Antique White
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Light Salmon
    Midnight Blue
    Royal Blue
    Snow


Lexical order is defined by ASCII.  You can think of lexical ordering being essentially the same as alphabetical order, but extended to cover digits and punctuation symbols.  Additionally, ASCII lexical order treats upper-case letters separately from lower-case letters (upper-case letters come before their lower-case counterparts).

Lexical order is determined by ASCII values. (This isn't required for this project, but the ASCII value of a character can be revealed in Python by the `ord()` function, like so: `print(ord('a')` prints `97`). Lexical order is similar to alphabetical order but includes digits, white space, and punctuation symbols. In ASCII lexical order, upper-case letters are treated differently from lower-case letters, with upper-case letters coming before their lower-case counterparts.


The "complexity" file includes several blank lines. Pay attention to how the blank lines appear at the top of the sorted output:

    $ python src/tt.py sort data/complexity



                    one way is to make it so simple
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
         "There are two ways of constructing a software design:
        -- Tony Hoare


When multiple files are given on the command line, lines from all files are mixed together into one sorted output:

    $ python src/tt.py sort data/colors8 data/names10
    Alexa
    Angela
    Antique White
    Bailey
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Frank
    Hazel
    Isabel
    Jerry
    Kai
    Karen
    Light Salmon
    Midnight Blue
    Mikayla
    Royal Blue
    Snow


    $ python src/tt.py sort data/complexity data/debugging





                      how will you ever debug it?"
                    one way is to make it so simple
                as writing a program in the first place.
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
            "Everyone knows that debugging is twice as hard
         "There are two ways of constructing a software design:
        -- Brian Kernighan
        -- Tony Hoare
        So if you're as clever as you can be when you write it,


Because lines from all files are all mixed together, it does not matter which order the filenames are presented to the program.  These two examples are different commands that produce the same output as the previous two examples:

    $ python src/tt.py sort data/names10 data/colors8
    Alexa
    Angela
    Antique White
    Bailey
    Dark Goldenrod
    DarkSea Green
    Dodger Blue
    Favorite Color
    Frank
    Hazel
    Isabel
    Jerry
    Kai
    Karen
    Light Salmon
    Midnight Blue
    Mikayla
    Royal Blue
    Snow


    $ python src/tt.py sort data/debugging data/complexity





                      how will you ever debug it?"
                    one way is to make it so simple
                as writing a program in the first place.
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
            "Everyone knows that debugging is twice as hard
         "There are two ways of constructing a software design:
        -- Brian Kernighan
        -- Tony Hoare
        So if you're as clever as you can be when you write it,


The results are surprising if you forget that `sort` *lexically* sorts strings and does not consider its input to be numeric:

    $ python src/tt.py sort data/random20
    1
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    2
    20
    3
    4
    5
    6
    7
    8
    9


To Python, digits sort before letters:

    $ python src/tt.py sort data/ages8
    17
    22
    23
    24
    26
    29
    36
    39
    Age


Reverse-sorted data can be obtained by first sorting in order with the `sort`
tool, then reversing the result with `tac`:

    $ python src/tt.py sort data/colors8 > sortedColors8
    $ python src/tt.py tac sortedColors8
    Snow
    Royal Blue
    Midnight Blue
    Light Salmon
    Favorite Color
    Dodger Blue
    DarkSea Green
    Dark Goldenrod
    Antique White


Don't forget to clean up after yourself:

    $ rm sortedColors8


### Help!  My Program's Output Disagrees With The Shell's Built-In `sort` Program!

The `sort` command in your shell may follow different rules than Python's built-in sorting routines, depending on what (human) language it thinks you speak.  When your program's output disagrees with that of the shell's `sort` command, running this `export` command will force the built-in `sort` program to follow the same sorting rules as Python:

    $ export LC_COLLATE=c


You need to re-run this `export` command each time you close and re-open the terminal.

As an example, on my computer the `sort` command prints this output when given the file `data/complexity` (pay attention to the first non-blank line):

    $ sort data/complexity



               and the other is to make it so complicated
                    one way is to make it so simple
                that there are no obvious deficiencies."
               that there are obviously no deficiencies,
         "There are two ways of constructing a software design:
        -- Tony Hoare


Exporting `LC_COLLATE=c` makes it behave the same as Python (again, notice the
top non-blank line):

    $ export LC_COLLATE=c
    $ sort data/complexity



                    one way is to make it so simple
                that there are no obvious deficiencies."
               and the other is to make it so complicated
               that there are obviously no deficiencies,
         "There are two ways of constructing a software design:
        -- Tony Hoare


### Handling Errors

The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py sort data/let3 DOES_NOT_EXIST data/complexity
    Traceback (most recent call last):
      File "/home/fadein/proj2/src/tt.py", line 32, in <module>
        sort(sys.argv[2:])
      File "/home/fadein/proj2/src/Sorting.py", line 16, in sort
        f = open(fil)
            ^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


Raise an error when too few arguments are given.  At minimum one input file is required.

    $ python src/tt.py sort
    Error: Too few arguments

        tt.py sort FILENAME...
            Output lines of text file in sorted order
