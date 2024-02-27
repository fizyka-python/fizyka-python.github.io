---
parent: Functions
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Functions with arbitrary arguments

## Defining functions with arbitrary arguments

In Python, it is possible to create functions with any number of arguments, not specified in advance. For this purpose, when defining the function, we give a special argument `*args` (an asterisk `*` at the beginning is the important part: the name can be anything, but it is customary to use _args_ and I recommend sticking to this convention):

```python
def function1(*args): 
    print(args)
```
When calling this function, any number of positional arguments can be given. Inside the function, the argument `args` will be a **tuple** containing all the given arguments. For example:

```python
function1(1, 2, 3)     # (1, 2, 3)
```
Similarly, a function can accept any number of arguments given by name. For this purpose, when defining it, we give a special argument `**kwargs` (double asterisk `**` is the important thing and the name _kwargs_ is just a convention):

```python
def function2(**kwargs):
    print(kwargs)
```
When calling this function, you can pass any number of arguments with any name. Inside the function, the argument `kwargs` will be a **dictionary** containing all the arguments given. For example:

```python
function2(a=1, b=2, c=3)     # {'a': 1, 'b': 2, 'c': 3}
```
Most often, both types of arguments are used simultaneously:

```python
def function3(*args, **kwargs): 
    print(args, kwargs)
```
Then the function can be called with any positional arguments and arguments given by name: they will be assigned to the tuple `args` and the dictionary `kwargs`, respectively. For example:

```python
function3 (1, 2, a=3, b=4)     # (1, 2) {'a': 3, 'b': 4}
```
Special arguments `*args` and `**kwargs` can be combined with normal arguments. Then `args` and  `kwargs` will contain only the values ​​not given in the argument list:

```python
def function4(x, y, *args, **kwargs):
    print (x, y, args, kwargs)
```
Call examples:

```python
function4(1, 2, a=3, b=4)     # 1 2 () {'a': 3, 'b': 4}

function4(1, y=2, a=3, b=4)   # 1 2 () {'a': 3, 'b': 4}

function4(1, 2, 3, a=4)       # 1 2 (3,) {'a': 4}
```
An interesting case is to put normal arguments  after `**args`. Then these parameters can only be passed by name. It is reasonable to use some default values for such arguments. For example:

```python
def function5(*args, x=None, y=None, **kwargs):
    print (x, y, args, kwargs)
```
Call examples:

```python
function4(1, 2, a=3, b=4)             # None None (1, 2) {'a': 3, 'b': 4}

function4(1, 2, x=3, y=4, a=5, b=6)   # 3 4 (1, 2) {'a': 5, 'b': 6}

function4(1, 2, 3, y=4)               # None 4 (1, 2, 3) {}
```
An example of a function that uses this is  `print`. Its definition is as follows:

```python
def print(*args, sep='', end='\n', file=sys.stdout, flush=False):
    """print all items from the tuple args
    sep, end, file and flush are arguments passed by names only
    (so far the meaning of sep and end have been explained).
    """
```

## Calling functions with any arguments

Similarly like in function definition, you may use `*` and `**` symbols when calling them. See the following example:
```python
def function(a, b, c):
    print(a, b, c)

data = [1, 2, 3]
function(*data)
```
This is equivalent to calling this function as
```python
function(1, 2, 3)
```

In general, when calling a function as `function(*sequence)`, the sequence is expanded and its elements are passed as positional parameters. Similarly, `function(**dictionary)` is equivalent to passing the dictionary elements as named parameters. So the function from the example above can be called as
```python
params = {'a': 1, 'b': 2, 'c':  3}
function(**params)
```
The keys of the dictionary passes to a function with `**` **must be strings**. In other case, `TypeError` will be raised.

The above method of calling function can be used regardless of its definition: it will work for both classical functions and the functions with arbitrary arguments described above.

A typical use case is printing all elements of a sequence:
```python
data = [1, 2, 3, 4]
print(*data, sep=', ')
```
or even
```python
print(*"abcd", sep='-')
```
The last example will print “`a-b-c-d`”.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
