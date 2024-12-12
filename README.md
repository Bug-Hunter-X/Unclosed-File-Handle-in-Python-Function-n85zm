# Unclosed File Handle in Python Function

This repository demonstrates a common error in Python: forgetting to close a file handle after it's been opened.  This can lead to resource leaks and, in some cases, errors if other parts of the program attempt to access the same file.

The `bug.py` file contains a function that opens a file but does not close it. The `bugSolution.py` shows the correct way to handle file I/O using `with` statement to guarantee closure.