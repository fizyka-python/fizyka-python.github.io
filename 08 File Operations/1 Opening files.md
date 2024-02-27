---
parent: File Operations
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Opening files

Virtually every computer program relies on reading and writing files to disk. These can be files containing the current configuration of the program, as well as files containing data processed by the program.

In Python, to open a file one use function `open(filename, mode)`, where *filename* is the name of the file to open, and *mode* is the mode in which the file is opened.

The file name can optionally contain the directory where the file is be located. Standard operating system rules apply:

* Directories and files are separated by a character `\\` (it must be entered twice, because in Python text strings the character `\` stands for a special symbol, e.g. `\n` for a new line) in Windows, or `/` in MacOS and Linux systems.
* If the filename starts with `X:\\/` (Windows, *X* is the drive letter) or `/` (MacOS and Linux) it is treated as a full path. Otherwise, the file is located relative to the current directory.

The file open mode is a text string that can take one of the following values:

* `'r'`: the file is opened for reading,
* `'w'`: the file is opened for writing: the current content of the file is deleted,
* `'a'`: the file is opened for writing: the current content of the file is kept and new data will be added to the end of the file,
* `'r+'`: the file is opened for reading and writing simultaneously.

Additionally, we can add a `b` character to the selected mode. It means opening the file in binary mode, which we will not delve into at this moment.

The function `open` returns a variable of the file type , which is a special type used to interact with an open file (it will be discussed in detail in the next part of the lecture). After reading/writing data is completed, the file should be *closed*. It is necessary especially in the case of writing, because otherwise we have no guarantee that the data will be actually written to the disk (to increase the performance, Python and the operating system use *caching*: the content of the file is stored in the operating memory and only when it is closed, it is actually written to disk). To close the file, use the method `file.close()`. E.g:

<div style="text-decoration: line-through;" onmouseover="this.style.textDecoration='none'" onmouseout="this.style.textDecoration='line-through'" markdown="1">

```python
file = open ('data.txt', 'w')
# Writing data...
file.close ()
```
</div>

The scheme from the example above can be found in many Python tutorials, however, it has two significant drawbacks: first, we must remember to close the file ourselves, and second, if the command sequence is interrupted (e.g. by an exception) before executing the command `file.close()`, the file will not be closed. For this reason, it is recommended that you always open a file using the context that Python creates with the command `with`:

```python
with open('data.txt', 'w') as file:
    pass  # Writing data...
```
The first line of the above example will open the file that will be available under the variable `file` inside the block. Upon exiting a block, the file will be automatically closed: no matter how that block was exited (with a command **`return`**, exception, or normal block termination). For this reason, please remember that we always open files in the following way:

```python
with open(filename, mode) as varname:
    Block of operations on the open file
```

The following parts of the lecture will discuss the operations that can be performed inside the block created in this way, depending on the mode in which the file was opened.


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
