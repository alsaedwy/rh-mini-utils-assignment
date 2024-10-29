# Minit Utils Assignmnent
Solution for "mini-utils" take-home assignment. I have chosen to implement:
- `mini-grep` 
- `mini-ls` - still WIP if you're reading this, delivery in few hours. :)

Languages used is Python as confirmed. 

Directory structure:
```bash
.
├── LICENSE
├── README.md
├── bin
├── coding_assignment.md
├── mini-grep
├── src
│   └── mini-grep.py
└── tests
    └── data-to-grep.log
```




# Description
- argparse -> standard
- All linted using PEP8 -> Black


> pathlib implements path operations using PurePath and Path objects, and so it’s said to be object-oriented. On the other hand, the os and os.path modules supply functions that work with low-level str and bytes objects, which is a more procedural approach. Some users consider the object-oriented style to be more readable.

## Some complex regex examples
```bash
 "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
```

```bash
"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
```



# References
- [YouTube - Argparse Basics](https://www.youtube.com/watch?v=FbEJN8FsJ9U)
- [Official Python docs - Argparse Tutorial](https://docs.python.org/3/howto/argparse.html)
- [Argparse Reference](https://docs.python.org/3/library/argparse.html)
- [re — Regular expression operations](https://docs.python.org/3/library/re.html)

- https://docs.python.org/3/whatsnew/3.5.html#pep-471-os-scandir-function-a-better-and-faster-directory-iterator


- https://docs.python.org/3/library/pathlib.html#comparison-to-the-os-and-os-path-modules


https://stackoverflow.com/questions/61004092/how-to-interpret-os-stat-st-mode-value