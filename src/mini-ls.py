"""
Given Definition (from ../coding_assignment.md)
----------------------------------------------
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
---------------------------------

Logical steps for me to implement:
- [x] 1. Read file(s) - if no file is given, read from current working directory (cwd)
- [x] 2. List the paths within a given in FILE (assuming there is a path per line)
- [x] 3. Gather information required: Owner, Permission, Modified Time
- [x] Add docstrings & test the functionality with multiple files & current working directory (cwd)

TODO: [Enhancement] - putting this here for awareness: Error handling for invalid paths, edge cases & maybe symbolic links
"""

import os
import argparse

from pathlib import Path
from datetime import datetime, timezone


def initiate_argparser():
    """
    - Initiates the argument parser 
    - Defines the arguments (positional, required & optional)
        - Positional: files (default: current directory (cwd; os.getcwd()))
        - Optional: recursive mode (-r)

    - Returns the parsed arguments passed to the script
    """
    parser = argparse.ArgumentParser(
        description="mini-ls: List information about the paths given in FILE.")

    parser.add_argument("-r", "--recursive", action="store_true",
                        help="Run mini-ls recursively on any directory it comes across")

    parser.add_argument("files", nargs="*", default=[os.getcwd()], type=argparse.FileType(
        "r"), help="Files to search (default: standard input)")

    return parser.parse_args()


def output_list_information(path: str, type: str):
    """
    Lists (outputs/prints) information about the paths given in FILE
        - Gather information required: Owner, Permission, Modified Time
        - Uses the Pathlib module to get the Owner, Permission & Modified Time of the given path
        - Converts not-very-readable permissions &  to a more readable format
        - Outputs (prints out) the Owner, Permission & Modified Time of the given path

    - Args:
        -   path: str - The path to process
        -   type: str - The type of the path (file or directory)
    """

    path_obj = Path(path)
    user_owner = path_obj.owner()
    group_owner = path_obj.group()
    permission = path_obj.stat().st_mode
    modified_time = path_obj.stat().st_mtime

    # Readability conversions
    readable_time = datetime.fromtimestamp(modified_time, tz=timezone.utc)
    readable_permissions = oct(permission)[-3:]  # Readable to linux users :)

    print(f"{path} - {type} - Owner: {user_owner}:{group_owner},Permission: {readable_permissions}, Modified Time: {readable_time}")


def process_path(path: str, recursive: bool):
    """
    Process a given path by running "os.scandir()" on it:
        - Loops through a list of all the entries in the directory given by the path
        - Calls "output_list_information()" to output the required data of the the given path
        - If the path is a directory, and '-r' is supplied, this function calls itself recursively
        - TODO: [Enhancement] I've seen some recursive-calling functions within (pathlib) - could be used instead 

    - Args:
        -   path: str - The path to process
        -   recursive: bool - Flag to run mini-ls recursively on any directory it
    """

    for object in os.scandir(path):

        # Check type (file or directory)
        if object.is_file():
            output_list_information(object.path, "file")

        # Recursively call this function to get the Owner, Permission & Modified Time of the sub-directories
        # Once there are no more sub-dirs, recursion will stop
        elif object.is_dir():
            if recursive:
                output_list_information(object.path, "directory")
                process_path(object.path, recursive)

            else:
                output_list_information(object.path, "directory")


def main():
    """
    Handles the main logic of the mini-ls program
        - 1. Reads the arguments by calling initiate_argparser()
        - 2. If the path is the current directory, process the current directories' paths [and optionally sub-directories]
        - 3. If the path is not the current directory, process each line of the passed file's paths 
    NOTE: It is assumed that the file containing the paths has one path per line (standard; more or less and not defined)
    """
    args = initiate_argparser()

    for path in args.files:
        if path == os.getcwd():
            # Get current directories' paths [and optionally sub-directories] in the current directory
            process_path(path, args.recursive)

        else:
            # Get the Owner, Permission & Modified Time of the given path
            paths_file = path
            for line in paths_file:
                path = line.replace("\n", "")
                process_path(path, args.recursive)


if __name__ == "__main__":
    main()
