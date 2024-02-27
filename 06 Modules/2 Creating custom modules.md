---
parent: Modules
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Creating custom modules

When writing more complex programs, we can create our own modules. This makes it possible to split the program into several files, which is desirable in the case of longer programs. In addition, we can collect frequently used functions into a single module and use them over and over again in various projects.

The simplest module is a Python source file (with extension `.py`) placed in the same directory as the main program. Then we can import it with a command

```python
import filename_without_extension
```
where `filename_without_extension` is the name of the file <span style="text-decoration: underline;">without the extension</span>. For example, if we have a file `mymodule.py` with the following content:

```python
def hello():
print("Hello")
```
then in the main program (in another file that we directly import) we can write:

```python
import mymodule

mymodule.hello()
```

Every Python module (including those created by you) have special variables that do not need to be declared by hand, but they are created by Python. These variables are:

* `__name__`: the name of the module,
* `__file__`: the Python file in which the module is located (this variable is not present in some built-in modules)


## File that can be both a module and a main program

Sometimes it is good to be able to create a file, which can be both a module (that may be imported from other Python file) or a main program run directly. In the former case, the module should only define functions etc. to be used from other code. In the latter case, the program should start doing its operation.

You can check if your file is imported as a module or run directly, by checking the `__name__` variable. For the file run directly it will always be `'__main__'`:

```python
def do_stuff():
    print("I'm alive!")

if __name__ == '__main__':
    do_stuff()
```


## Packages
It is also possible to create a hierarchy of modules. To do this, create a directory with the name of the module (without any extensions) and put the file in this directory with the name `__init__.py` (two underscores at the beginning and at the end of the name). Then the command

```python
import directory_name
```
will load the module from the file `__init__.py`. This directory is called **a package**. We can put other Python source files (with the extension `.py`) in it, which we can import via

```python
import directory_name.file_name_without_extension
```
or in any other way as shown before. We can also increase the number of hierarchy levels by placing a subdirectory in our directory, in which we will again create the file `__init__.py` (this file must always be present, even if it would be empty).

Creating packages is useful when writing more complex programs.


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
