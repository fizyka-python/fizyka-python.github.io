---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  5
---

# Three remarks about iteration over sequences

## Correctly iterating over sequences

When iterating over a sequence, you may be tempted to use something like:

<div style="text-decoration: line-through;" onmouseover="this.style.textDecoration='none'" onmouseout="this.style.textDecoration='line-through'" markdown="1">

```python
for i in range(len(sequence)):
    element = sequence[i]
    operate on element
```

</div>

This is particularly common for people who have some experience with different programming languages, like C++. **In Python this is wrong!** Instead, you should simply iterate over sequence elements disregarding their indices:

```python
for element in sequence:
    operate on element
```

This is much more elegant and works also with sequences that are not indexed with numbers, like dictionaries or sets.

## Item numbering in a loop

Sometimes there is a need to iterate through the sequence of a set and number them simultaneously. This can be done as follows:

<div style="text-decoration: line-through;" onmouseover="this.style.textDecoration='none'" onmouseout="this.style.textDecoration='line-through'" markdown="1">

```python
number = 0
for element in sequence:
    loop block
    number += 1
```

</div>

However, this is not the best solution. It is much better to use a function `enumerate(sequence)` that will generate successive sequence elements and their numbers in each run of the loop:

```python
for number, element in enumerate(sequence):
    print("Element no", number, "in the sequence is", element)
```

## Iterating over several sequences simultaneously

It is also possible to iterate over several sequences simultaneously using the function `zip(sequence1, sequence2...)`. The number of sequences for simultaneous iteration is arbitrary. The condition is that all these sequences must be of the same length (in fact, it is not really necessary: only as many elements as there are in the shortest sequence will be taken into account). This iteration takes the form:

```python
for element1, element2, element3 in zip(sequence1, sequence2, sequence3):
    loop block
```

For example:

```python
first_names = ["Harry", "Frodo", "James"]
last_names = ["Potter", "Baggins", "Bond"]

for first_name, last_name in zip(first_names, last_names):
    print(first_name, last_name)
```


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
