---
parent: Modules
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Using Python modules

Standard Python provides a very wide range of functions and objects that allow you to easily perform various advanced operations. This makes writing Python programs much easier than using other popular programming languages ​​such as C++. The most common and frequently used functions (e.g. `print`, `input`, `len`, and `range`) are always available. They are so-called _built-in_ functions. However, the vast majority are grouped in _packages_ and _modules_ that must be _imported_ when needed.

To import a module, you should issue the command:

```python
import module_name
```
An example would be a module `random` that provides functions for generating pseudo-random numbers. We import it with the command

```python
import random
```
This command does not make all functions and objects defined in this module directly available. To get to them you have to use notation `module_name.function(...)`. For example, to generate a random number in the range [_a_, _b_] we can use the function `uniform` from the module `random`:

```python
random_number = random.uniform(-1, 1)
```
A complete list of built-in Python modules and functions can be found in the [documentation](https://docs.python.org/3/library/index.html). In particular, it is worth reviewing the module descriptions [sys](https://docs.python.org/3/library/sys.html) and [os](https://docs.python.org/3/library/os.html) which contain a set of basic functions and objects for using the operating system tools. For example, you can check the current version of Python with:

```python
import sys

print(sys.version)
```
In this case, `sys.version` is not a function, but just a string. However, it is an object defined inside a module.

Modules may contain other modules nested in a hierarchical manner: any module may contain sub-modules (master modules are then called _packages_). To import the selected sub-module, use the command `import package.submodule`. There can be any number of nesting levels: in such case, enter all of them, separating subsequent levels with a dot. Useful functions and objects can be found both in the top module and in submodules. Submodules are used to group a set of functions. For example, a module [os](https://docs.python.org/3/library/os.html) contains functions that allow you to perform various operations on files on the disk, and a module [os.path](https://docs.python.org/3/library/os.path.html) provides functions that allow you to manipulate filesystem paths:

```python
import os.path

print(os.path.join('directory', 'file.txt'))
```
## Simplified module loading
The fact that the command `import` only defines the name of the module keeps the program code in order. In particular, there is no problem with functions with the same names in several modules. As their use requires the name of the module before the dot, there will be no collisions between them. However, sometimes—especially with nested modules—this can be cumbersome (e.g. when you have to frequently type `moduleA.moduleB.moduleC.function1()`, `moduleA.moduleB.moduleC.function2()` etc.) There are two methods to deal with this. The first one is to import any module (also nested) with its own name, using the keyword `as`:

```python
import moduleA.moduleB.moduleC as mc
```
Then instead of `moduleA.moduleB.moduleC.function1()` we can just write `mc.function1()`, which is much shorter. For example

```python
import os.path as p

print(p.join('directory', 'file.txt'))
```
Remember that the names we give the imported modules should be meaningful: even if it is a one- or two-letter abbreviation (in the example above, the first letter of the submodule name `path` was used).

The second method allows you to directly load selected functions and other objects from the module and access them without prefixing them with the module name. For this, we use the following syntax:

```python
from module_name import function
```
`module_name` can have the form _`package.submodule`_, as in the previously described cases. You can import more than one function from a single module in such a way. If there is more than one, they should be separated by a comma. Functions imported in this way can be used directly. E.g:

```python
from numpy import pi, sin, cos

print(sin(pi / 2))
```
which is equivalent to:

```python
import numpy

print(numpy.sin(numpy.pi / 2))
```
Note, however, that in using this approach, we run the risk that the imported function will replace the built-in function. Moreover, in the program code we do not clearly see which module it comes from. Therefore, please use this method with caution.


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
