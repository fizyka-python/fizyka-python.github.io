---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Operations on sequences

So far, we have introduced two types that are sequences (containing ordered data): tuple (`tuple`) and string (`str`). You can iterate over each element with a for loop. Below is a description of other useful operations that we can perform on each sequence (not only on the two above, but also on the others, which will be introduced soon).
Sequence length

The first operation that may be useful is to know the sequence length. This is done by a function `len(sequence)` that returns the number of elements in the sequence given as its argument (i.e. in parentheses). E.g:

```python
data = (1, 2, 3, 10)
print(len(data))

length = len("To be of not to be?")
print("Sentence has", length, "letters.")
```

As an exercise, I propose to modify the Password task from the previous topic (without sending it) and add an additional security test for the password you entered: it must be at least 8 letters long.

> **Warning!**
> When using a for loop, do not iterate over the element indexes as follows `for i in range(len(sequence)):`. Instead, you should use simple syntax `for element in sequence:`. If you need element numbers, or you want to iterate over several sequences simultaneously, the appropriate methods are described separately.

## Does the sequence contain an element?

Another useful operation is checking if a given element is present in the sequence. The operator is for this **`in`**, or **`not in`**. E.g:

```python
if 'a' in 'Alice':
    print("The word 'Alice' contains the letter 'a'")
else
    print("No 'a' in 'Alice'")

if 4 not in (2, 3, 5, 7, 11, 13, 17, 19): 
    print("Four is not a prime less than 20")
```

## Access to individual sequence elements

Since sequences are an ordered collection of elements, it is necessary to be able to access the element with a specific number. For this, in Python, square brackets are used immediately after the sequence, or (more commonly) the name of the variable representing it:

```python
data = ('A', 'B', 'C') 
print(data[0])   # prints the first element of the tuple ('A')
print(data[2])   # prints the third element of the tuple ('C')

word = "Kalambur" 
for i in (1, 3, 6):
    # print second, fourth and seventh letters
    print(word[i])
```

Inside the square brackets there must be an integer (or a variable that represents such a number) called the index. It indicates the element number in the sequence, with the first element numbered 0. This is somewhat counterintuitive and is due to the fact that in most older programming languages this convention has been used historically. Please note that this behavior is consistent with the function of the previously discussed function `range`:  **Python always counts from 0!**

In Python it is also possible to use negative numbers as indices. Then the countdown starts from the end. So `sequence[-1]` means the last element of the sequence, `sequence[-2]` the penultimate one, etc. Example:

```python
name = input("Enter your name:")

if name[-1] == 'a':   # in Polish, female names end with "a"
     print("You are a woman") 
else: 
    print("You are a man ")
```

As a simple exercise, please modify the example above so that each Kuba is treated like a man ☺.


## Range slices

You can use square brackets to dereference not only individual sequence elements, but also slices of them. Such slices have the following form `sequence[start:stop:step]`, where `start` is the index of the first element entering the slice, `stop` the index of the first element that does not enter the slice, and the `step` is the step with which subsequent elements are taken (please note that there is some similarity to the arguments of the `range` the function). Each of the `start`, `stop` and `step` numbers can be omitted.

The operation of the slices is best illustrated by an example. Please rewrite them in the interactive console and try to understand exactly how the successive elements of each slice are counted.

```python
digits = tuple(range(10))  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

digits[2:7]                # (2, 3, 4, 5, 6)
digits[2:7:2]              # (2, 4, 6)
digits[:5]                 # (0, 1, 2, 3, 4)
digits[5:]                 # (5, 6, 7, 8, 9)
digits[::3]                # (0, 3, 6, 9)
digits[7:2:-1]             # (7, 6, 5, 4, 3)
digits[-1:3:-2]            # (9, 7, 5)
digits[6::-2]              # (6, 4, 2, 0)
digits[::-1]               # ( 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
digits[:-4:-1]             # (9, 8, 7)
```

**Important!** Please note that the element with the stop index is no longer part of the slice.

Example for text strings:

```python
text = input("Enter text:")
print("Your text backwards is:", text[::-1])
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
