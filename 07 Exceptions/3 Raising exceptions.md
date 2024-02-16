---
parent: Exceptions
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Raising exceptions

It may happen that we want to report an exception ourselves. For example, consider an integer input function:

```python
def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print ("Invalid number. Returning 0.")
        return 0
```
Suppose we require this number to be in the range 1-10. It is reasonable that an exception is thrown when this condition is not met ValueError. We can *raise* such an exception (generate it) using the command **`raise`**:

```python
raise ExceptionType(message)
```
The exception type is one of the standard types described earlier, and the *message* is an optional message that will appear when the exception is not handled. It is possible to create your own types of exceptions (just like creating your own types of variables in general), but this is an object-oriented issue and will be discussed later. At this moment I suggest choosing the most appropriate type from among standard exceptions.

Using this, the function above could look like this:

```python
def input_int(prompt, min=1, max=10):
    try:
        number = int(input(prompt))
        if number < min or number > max:
            raise ValueError("Number out of range")
    except ValueError:
        print("Invalid number. I return 0. ")
        return 0
    else:
        return number
```
There is no obligation for the exception thrown to be handled in the same function. Please rewrite and run the following program:

```python
def ten_minus(number):
    if number < 0 or number > 10:
        raise ValueError("Number out of range")
    return 10 - number

print(ten_minus(2))
print(ten_minus(12))   # this will abort the program, because the exception is not cought
```


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
