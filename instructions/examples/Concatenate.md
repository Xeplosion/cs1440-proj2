# Forward And Reverse Concatenation (`cat`, `tac`, and `nl`)


## cat
Concatenate two files into one output

    $ python src/tt.py cat data/let3 data/num2
    a
    b
    c
    1
    2


Ordinarily, `cat` is used by Unix hackers to print a file to the screen

    $ python src/tt.py cat data/complexity
         "There are two ways of constructing a software design:

                    one way is to make it so simple
               that there are obviously no deficiencies,

               and the other is to make it so complicated
                that there are no obvious deficiencies."

        -- Tony Hoare



`cat` accepts any number of filename arguments >= 1.  In this example hundreds of lines of text are clipped out of the middle:

    $ python src/tt.py cat data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
    Age
    22
    36
    24
    ... Skipped hundreds of lines...
    reconfigurations
    activates
    autobiographies
    adverbs


### Handling Errors
The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

$ python src/tt.py cat data/let3 DOES_NOT_EXIST data/debugging
    a
    b
    c
    Traceback (most recent call last):
      File "/home/fadein/cs1440-falor-erik-proj2/src/tt.py", line 27, in <module>
        cat(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-proj2/src/Concatenate.py", line 14, in cat
        f = open(fil, 'r')
            ^^^^^^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'

Your program must use `usage()` to raise an error when too few arguments are given; at least one input file is required.

    $ python src/tt.py cat
    Error: Too few arguments

    tt.py cat|tac|nl [-ba] FILENAME...
        Concatenate and print files in order, in reverse, or with line numbers
        -ba  Include blank lines (only for the nl tool)


## tac
`tac` works just like `cat`, only backwards.  That is, the lines of each file are printed in reverse order.  The files themselves *are* still processed in the order given on the command line:

    $ python src/tt.py tac data/let3 data/num2
    c
    b
    a
    2
    1


    $ python src/tt.py tac data/complexity
        -- Tony Hoare

                that there are no obvious deficiencies."
               and the other is to make it so complicated

               that there are obviously no deficiencies,
                    one way is to make it so simple

         "There are two ways of constructing a software design:


Like `cat`, `tac` also accepts any number of filename arguments >= 1.  In this example hundreds of lines of text are clipped out of the middle.

    $ python src/tt.py tac data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
    17
    29
    23
    26
    ... Skipped hundreds of lines...
    cranky
    implicitly
    insomniac
    social


### Handling Errors
The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py tac data/let3 DOES_NOT_EXIST data/debugging
    c
    b
    a
    Traceback (most recent call last):
      File "/home/fadein/cs1440-falor-erik-proj2/src/tt.py", line 29, in <module>
        tac(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-proj2/src/Concatenate.py", line 30, in tac
        f = open(fil)
            ^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


Your program must use `usage()` to raise an error when too few arguments are given; at least one input file is required.

    $ python src/tt.py tac
    Error: Too few arguments

    tt.py cat|tac FILENAME...
        Concatenate and print files in order or in reverse


## nl
Number lines of files

`nl` is like `cat`, but with line numbers added on the left side of the output.  Line numbers begin at `1` and increase for every non-blank line.  The count does not restart when a new file is encountered.

    $ python sln/tt.py nl data/let3 data/num2
         1  a
         2  b
         3  c
         4  1
         5  2


By default, only non-blank lines are numbered.  Blank lines are printed without a number and the count does not increase:

    $ python src/tt.py nl data/complexity data/debugging
         1       "There are two ways of constructing a software design:

         2                  one way is to make it so simple
         3             that there are obviously no deficiencies,

         4             and the other is to make it so complicated
         5              that there are no obvious deficiencies."

         6      -- Tony Hoare
         7          "Everyone knows that debugging is twice as hard
         8              as writing a program in the first place.

         9      So if you're as clever as you can be when you write it,
        10                    how will you ever debug it?"

        11      -- Brian Kernighan


Blank lines are counted when the `-ba` option is given:

    $ python src/tt.py nl -ba data/complexity data/debugging
         1       "There are two ways of constructing a software design:
         2  
         3                  one way is to make it so simple
         4             that there are obviously no deficiencies,
         5  
         6             and the other is to make it so complicated
         7              that there are no obvious deficiencies."
         8  
         9      -- Tony Hoare
        10          "Everyone knows that debugging is twice as hard
        11              as writing a program in the first place.
        12  
        13      So if you're as clever as you can be when you write it,
        14                    how will you ever debug it?"
        15  
        16      -- Brian Kernighan


`nl` accepts any number of filename arguments >= 1.  In this example hundreds of lines of text are clipped out of the middle:

    $ python src/tt.py nl data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
         1  Age
         2  22
         3  36
         4  24
    ... Skipped hundreds of lines...
       300  reconfigurations
       301  activates
       302  autobiographies
       303  adverbs


Notice how the final line count differs when blank lines are included:

    $ python src/tt.py nl -ba data/ages8 data/colors8 data/complexity data/debugging data/dup5 data/let3 data/names10 data/names8 data/num10 data/num2 data/random20 data/verbs8 data/wordcount data/words200
         1  Age
         2  22
         3  36
         4  24
    ... Skipped hundreds of lines...
       307  reconfigurations
       308  activates
       309  autobiographies
       310  adverbs


### Handling Errors
The program aborts as soon as a non-existent, invalid or inaccessible file is encountered.  You do not need to pre-screen the arguments before you begin processing; just let `open()` raise an exception.

    $ python src/tt.py nl data/let3 DOES_NOT_EXIST data/debugging
         1  a
         2  b
         3  c
    Traceback (most recent call last):
      File "/home/fadein/cs1440-falor-erik-proj2/src/tt.py", line 31, in <module>
        nl(sys.argv[2:])
      File "/home/fadein/cs1440-falor-erik-proj2/src/Concatenate.py", line 53, in nl
        f = open(fil)
            ^^^^^^^^^
    FileNotFoundError: [Errno 2] No such file or directory: 'DOES_NOT_EXIST'


Your program must use `usage()` to raise an error when too few arguments are given; at least one input file is required.

    $ python src/tt.py nl
    Error: Too few arguments

    tt.py cat|tac|nl [-ba] FILENAME...
        Concatenate and print files in order, in reverse, or with line numbers
        -ba  Include blank lines (only for the nl tool)
