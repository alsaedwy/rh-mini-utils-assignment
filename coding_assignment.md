Linux mini-utils
================

The goal of this exercise is to test your understanding of Linux
systems by reimplementing (minimal versions of) common utilities.

Pick 2 of the following 3 utilities and provide a simple
implementation:

1. "mini-grep"
--------------

Usage:

    ./mini-grep [-q] -e PATTERN [FILE...]

`mini-grep` goes through every argument in FILE and prints the whole
line in which PATTERN is found. By default `mini-grep` also outputs
the line number of each printed line.

- PATTERN has to be a valid regex
- FILE can be zero or more arguments. If zero args are given,
  `mini-grep` will parse entries from the standard input.
- If given, the `-q` options only outputs lines but omits the matching
  line numbers.



2. "mini-ls"
------------

Usage

    ./mini-ls [-r] [FILE...]

`mini-ls` lists information about the paths given in FILE. The
information required are: Owner, Permission, Modified Time.

- FILE can be zero or more arguments. If zero args are given,
  `mini-ls` will list information about the current directory.
- If given, the `-r` option will make `mini-ls` run recursively on any
  directory it comes across.


3. "mini-df"
------------

Usage:

    ./mini-df [-h] [PATH...]

`mini-df` outputs displays the amount of space available on the file
system containing each file name argument.

The information required is: Total Space, Free Space. The result
should be in Bytes.

- PATH can be zero or more arguments. IF zero args are given, the
  space available on all currently mounted file systems is shown.

- If given `-h` will output the result in human-readable
  format. (print sizes in powers of 1024 (e.g. 1023M)

