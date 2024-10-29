"""
Given Definition (from ./coding_assignment.md)
----------------------------------------------
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
----------------------------------------------

Logical steps for me to implement:
- [x] 1. Read file(s) - if no file is given, read from stdin
- [x] 2. Validate the regex pattern, if invalid, exit gracefully
- [x] 2.1 Search for pattern in each line
- [x] 3. Print line & number if pattern is found
- [x] 3.1 If quiet mode is enabled, only print the line
- [x] 4. If no file is given, read from stdin
- [x] Add docstrings & test the functionality with multiple files & stdin and diffrent [invalid] regex 
"""

import re
import sys
import argparse
import logging


logger = logging.getLogger(__name__)


def initiate_argparser():
    """
    - Initiates the argument parser & 
    - Defines the arguments (positional, required & optional)
        - Positional: files (default: stdin)
        - Required: pattern (-e)
        - Optional: quiet mode (-q)

    - Returns the parsed arguments
    """
    parser = argparse.ArgumentParser(
        description="mini-grep: Search for PATTERN in each FILE.")

    parser.add_argument("-q", "--quiet", action="store_true",
                        help="Only output lines, omit matching line numbers")

    parser.add_argument("-e", "--pattern", required=True, type=str,
                        help="(REQUIED) The regex pattern to search for")

    parser.add_argument("files", nargs="*", default=[sys.stdin], type=argparse.FileType(
        "r"), help="Files to search (default: standard input)")

    return parser.parse_args()


def main():
    """
    Main function to run the mini-grep program
    - Reads the arguments by calling initiate_argparser()
    - Compiles the pattern with 're' module
    - Iterates through each line in the file(s) (or stdin if no files are given)
    - Checks for the '-q' flag and prints the line accordingly
    """

    args = initiate_argparser()

    try:
        pattern = re.compile(args.pattern)
        logger.info(f"Pattern compiled successfully: {args.pattern}")
    except Exception as e:
        logger.exception(f"Invalid regex pattern: {args.pattern}")
        sys.exit(1)

    for file in args.files:
        for i, line in enumerate(file, 1):

            if pattern.search(line):
                if args.quiet:
                    print(line, end='')
                else:
                    print(f"{i}:{line}", end='')


if __name__ == "__main__":
    main()
