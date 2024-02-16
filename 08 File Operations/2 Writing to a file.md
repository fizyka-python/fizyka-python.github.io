---
parent: File Operations
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Writing to a file

To write to a file, use the method `write` that takes the string to be written as an argument. It can be called for a file opened for writing (in mode `w` or `a`). This method can be called several times: each subsequent call will add data to the file. For example:

```python
with open('file.txt', 'w') as file:
    file.write("To be or not to be,\n")
    file.write("This is a question!\n")
```
After executing the following commands, the file will have two lines. Please note that you have to insert newlines yourself (of course they don't have to be at the end of the text).

If we have a list or a tuple of text strings, we can write them one by one using a method writelines, e.g.

```python
with open('file.txt', 'w') as file:
    file.writelines(["So long...\n", "And thanks", "for all the fish!\n"])
```
Contrary to the name, the above method does not save successive list items on separate lines, but combines them. Newlines will be inserted where they appear in the text strings.

Another—perhaps easier—method of saving to a text file is to use a function you've already learned: `print`. It may take an optional argument `file` where we can pass a file opened for writing:

```python
with open('file.txt', 'w') as out:
     print(1, 2, 3, file=out)
```
The normal rules for the function `print` apply: consecutive elements are separated by spaces and a newline is printed at the end, unless this is changed with the arguments `sep` and `end`.



<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
