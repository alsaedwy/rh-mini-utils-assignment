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
- [ ] 1. Read file(s) - if no file is given, read from current directory
- [ ] 2. List information about the paths given in FILE
- [ ] 3. Gather information required: Owner, Permission, Modified Time
- [ ] 4. If no file is given, list information about the current directory

"""

import os
import argparse
import logging
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger(__name__)


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


def list_information(path: str, type: str ):
    """
    - List information about the paths given in FILE
    - Gather information required: Owner, Permission, Modified Time
    """
    
    path_obj = Path(path)
    user_owner =  path_obj.owner()
    group_owner =  path_obj.group()
    permission=  path_obj.stat().st_mode
    modified_time=  path_obj.stat().st_mtime

    readable_time = datetime.fromtimestamp(modified_time, tz=timezone.utc) 
    
    readable_permissions = oct(permission)[-3:] # (Readable for linux users)    

    print(f"{path} - {type} - Owner: {user_owner}, Permission: {permission}, Modified Time: {modified_time}")


    
def process_path(path: str, recursive: bool):
    """
    - Process the given path to get the Owner, Permission & Modified Time
    """

    for object in os.scandir(path):

        # Check type (file or directory)
        if object.is_file():
            list_information(object.path, "file")

        # Recursively call this function to get the Owner, Permission & Modified Time of the sub-directories
        # Once there are no more sub-dirs, recursion will stop
        elif object.is_dir():
            if recursive:
                list_information(object.path, "directory")
                process_path(object.path, recursive)
                # print(object.path)

            else:
                list_information(object.path, "directory")



def main():
    """
    
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


        # if os.path.isfile(file):
            # print(file)


if __name__ == "__main__":
    main()
