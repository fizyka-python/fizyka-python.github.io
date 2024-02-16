---
parent: File Operations
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Reading from a file

Reading a file can be done in several ways. The easiest way is to use a method `read` that will read the contents of the entire file into a variable of type `str` (in case of opening the file in binary it will be of type `bytes`). For example

```python
with open("file.txt", "r") as file:
    text = file.read()
    print("File contents:")
    print(text)
```
If we want to read individual lines sequentially, we can treat the file as a sequence and iterate through it with a **for** loop :

```python
with open("file.txt", "r") as file:
    for line in file:
         print ("Line:", line.rstrip())
```
There are two points to note:

1. The read line contains a line break (if present, the last line in the file may not contain it). If you want to get a line without this character, remove it. For this purpose you can use a method `rstrip` for text strings that removes white space at the end of text (spaces, tabs, and newlines).

2. Once opened, the file can be iterated over only once. After reading a line, Python moves on to the next one and iterating again will not return to the content that was previously read. To read a file again, either open it again or read the contents of a line into the list:

   ```python
   with open ("file.txt", "r") as file:
       lines = [line.rstrip() for line in file]

   ```



The list `lines` will be stored in memory and it will be possible to iterate through it and modify it many times. It is possible to return to a specific place in the file with a method `seek`, but in the simplest cases it is not needed.

The following example prints a file with line numbers:

```python
with open("file.txt", "r") as file:
    for no, line in enumerate(file):
         print(f"{no+1:3d}: {line.rstrip()}")
```


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
