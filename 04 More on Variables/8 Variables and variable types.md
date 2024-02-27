---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  8
---

# Variables and variable types

Lists and dictionaries are variable types. This means that you can add, remove and change their elements. In the topic about variables, it was explained that a variable is a label: several different variables can point to the same object.

Consider the following example:

```python
list1 = [1, 2, 3]
list2 = list1

list2[2] = 10

print(list1)
```

The above code will print `[1, 2, 10]`. This is because `list1` and `list2` are different labels, but point to the same object. To make a copy of a list or dictionary, use the method `copy`:

```python
list1 = [1, 2, 3] 
list2 = list1.copy()

list2 [2] = 10 

print(list1)
```

This time the program will print `[1, 2, 3]` because we have modified a copy of `list1`.

You can use the operator **`is`** to check if two variables point to the same object. Please try to type in the console:

```python
list1 = [1, 2, 3]

list2 = list1

list2 is list1    # True
```

When we create a copy, the operator **`is`** will allow us to check that we are dealing with different objects. In turn, the comparison operator (`==`) will show that these lists are identical:

```python
list1 = [1, 2, 3]

list2 = list1.copy()

list2 is list1    # False

list2 == list1    # True
```

The opposite of the operator **`is`** is **`is not`**.




---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
