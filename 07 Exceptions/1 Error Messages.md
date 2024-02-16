---
parent: Exceptions
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Error messages

Each of you has certainly encountered error messages. For example, issuing the command in the console:

```python
print(float("two"))
```

It will produce the message:

```
Traceback (most recent call last):

  File "<ipython-input-1-ed629b1feb04>", line 1, in <module>
    print(float("two"))

ValueError: could not convert string to float: 'two'
```

In Python, errors are called **exceptions**. Their appearance means that a non-standard situation has occurred. Its appearance may result from an error in the program: then the message shows the exact place where the problem appeared and the entire sequence of function calls that led to it. Please take a look at the following program (when rewriting it, please skip the line numbers that are given for information only):

```python
1 def replace_number(value):
2 return float(value)
3
4 print(replace_number('2'))
5   print(replace_number('two'))
```

Its launch will result in the following message:

```
Traceback (most recent call last):

  File "temp.py", line 5, in <module>
    print (replace_number("two"))

  File "temp.py", line 2, in replace_number
    return float(value)

ValueError: could not convert string to float: 'two'
```

Python printed the so-called **traceback**, which is the function call stack. It should be read from the bottom: an error has occurred `ValueError`, i.e. a value error. We read in the error message that Python is not able to convert the text string `'two'` to a real number. Above, we find information that this error occurred in the second line of the file `temp.py` in the function `replace_number` (this line is rewritten below). In turn, this function was called on the fifth line in the main code of the module (without any function). Note that calling the function  `replace_number` on line four did not produce an error.

## Exception types
In Python, exceptions can be of different types that correspond to different types of errors or abnormal situations. The following is a list of the most common types of exceptions:

**`AttributeError`**: Raised when attribute reference or assignment fails (when the object does not support attribute references or assignments at all TypeError).

**`IOError`**: Dispatched when an error occurs in the I/O of a print statement, built-in function, `open()` or file object methods. For example, these errors can be caused by "file not found" or "out of disk space" problems.

**`ImportError`**: Raised when an import statement fails because the module is not found, or when the `from ... import statement` cannot find the specified name in the module.

**`IndexError`**: Called when an index out of scope is used to access an element of a sequence (however, mind that slices are automatically adjusted to the size of the sequence; if the index is not an integer `TypeError` is raised).

**`KeyError`**: Raised when the key used to access the mapping element (dictionary) is not present.

**`KeyboardInterrupt`**: Called when the interrupt key is used (usually `Ctrl-C` or `Ctrl-Delete`). Checking for this is done regularly when the program is called. Using the abort key (key combination) while the function is waiting for input in the `input()` function also raises this exception.

**`MemoryError`**: Raised when the memory is exhausted. The value assigned to the exception is a string indicating what (internal) operation has exhausted memory.

**`NameError`**: Raised when local or global name is not found. The value associated with the exception is an error message that contains a name that was not found.

**`SyntaxError`**: Raised when the parser encounters a syntax error.

**`TypeError`**: Raised when an inline operation is performed on an object of the wrong type. The assigned value of the exception is a string that describes the details of the type mismatch.

**`UnboundLocalError`**: Raised when reference is made to a local variable of a function or method and no value has been assigned to that variable.

**`ValueError`**: Raised when some operation was requested with an argument of the right type, but with an incorrect value.

**`ZeroDivisionError`**: Raised when the second operand of the division operation or the division remainder (modulo) is zero. The value assigned to the exception is a string that describes the types of operands and operations.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
