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

