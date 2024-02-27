---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Lists

There is a data type very similar to tuples in Python. These are  lists (`list`). Unlike tuples, which are constants, lists are structures that can change: you can add new elements to them, delete or change them.

Lists with specific items are created similar to tuples, however, instead of parentheses, square brackets are used:

```python
list = ["first", 2, 2.5, 3-1j]
```

As with tuples, the list items don't have to be of the same type. All the previous operations shown for tuples, such as iterating over them in a **for** loop, indexing elements, slices, and so on, work exactly the same for lists.

However, the list items can be changed. Please enter the following commands in the interactive console

```python
list = [1, 2, 3] 

list[0] = 10

print(list)     # [ 10 , 2, 3]
```

If I did such an assignment for a tuple, it would cause a `TypeError`.

List items can also be removed with a command **`del`**. E.g:

```python
list = ['A', 'B', 'C', 'D'] 

del list[1]     # delete the second element

print(list)     # ['A', 'C', 'D']
```

It is also possible to insert and add items to the list. They are used to this  method  with names `insert` and `append`. These methods are specific operations related to a variable of a given type. They are similar to a function, but affect only one specific object. They are called as follows `object.method(arguments...)`, where object is usually a variable name, and the method name is separated from the object by a period. Adding an item to the list will look like this:

```python
list = ['A', 'B', 'C']

list.append('D')
```

The method append puts the element given as its argument to the end of the list. So in the example above, the list would be `['A', 'B', 'C', 'D']`. In contrast, the method `insert` takes two arguments: the place where the element should be inserted (i.e. the index of the inserted element) and its value:

```python
list = ['A', 'B', 'C'] 

list.insert(1, 'X')

print(list)     # ['A', 'X', 'B', 'C']
```

Below is an example of creating a names list. Please run it and analyze it:

```python
names = []     # this creates an empty list 

# The following loop will run infinitely 
# it can only be ended with break
while True:
    name = input("Enter name or write a dot to end:")
    if name == '.':
        break
    names.append(name) 

print(names)
```

## Converting lists and other types

You can convert lists to tuples and vice versa without any restrictions. This way, you can work around the restriction not allowing tuples to be modified:

```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
my_list[0] = 10 
my_tuple = tuple(my_list)
print(my_tuple)
```

However, keep in mind that tuples are more efficient and run faster, so avoid this conversion unless absolutely necessary.

Similarly, you can convert strings into lists, but not the other way around: check what the following command will do `str(['a', 'b', 'c'])`. However, there are two very useful methods defined for strings: `split` and `join`. The method `split` is used to split a text string into words, and join to concatenate list items. Please try to split the text yourself in the interactive console:

```python
text = "one two three"

list = text.split()

print(list)     # ['one', 'two', 'three']
```

There is also an alternate way of calling the method `split` that allows you to split text not into words (that is, at spaces and newlines), but selected strings. For example, let's see how to split a text containing words separated by a comma followed by a space:

```python
text = "one, two, three"

list = text.split(', ')

print(list)     # ['one', 'two', 'three']
```

The method `join` (which works on text strings) is used to concatenate the elements of a list (or a tuple) given as its arguments. The hyphen is the text that this method works on. This is best illustrated by an example:

```python
list = ['Kacper', 'Melchior', 'Balthazar'] 

hyphen = "+"

text = hyphen.join(list)

print(text)     # "Kacper+Melchior+Baltazar
```

The methods also work directly for text values:

```python
list = ['Kacper', 'Melchior', 'Balthazar'] 

text = "+".join(list)

print(text)     # "Kacper+Melchior+Baltazar
```

### Elegant list creation

The method `append` is used to add items to the list. If it can be avoided, it is better not to use it to build entire lists, repeating it inside a for loop. Python offers an elegant method of creating lists called **list comprehension**. Above is an example of creating a list by listing its elements separated by a comma and placed in square brackets `[...]`. Instead of listing the items manually, you can use a for loop  with the following syntax:

```python
list = [expression for counter in sequence]
```

This expression comes before the **`for`** command and there is no colon anywhere. This expression can use a loop counter to compute successive values to insert into the list. It is best to illustrate this with an example. Suppose we want to create a list containing squares of numbers in the range 1-10:

```python
squares = [i**2 for i in range(1, 11)]

print(squares)
```

Please note that this is very similar to the natural language: "let the list of squares consist of the values i² for i in the range 1 to 10".

In a more advanced version, we can add an additional condition that the loop counter must satisfy in order for the corresponding expression to be included in the list:

```python
list = [expression for counter in sequence if condition]
```

For example, if we do not want to include the squares of 3 and 7 in our list of squares, we can write:

```python
squares = [i**2 for i in range(1, 11) if i not in (3, 7)]
```

## Exercise

Please write the shortest possible program, which will create a list containing the lengths of individual words in the sentence "To be or not to be" (for the sake of simplicity, punctuation marks have been omitted).





---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
