---
parent: Constants, Variables and Basic Operations
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Other types and logical operations

## None Type

In addition to those mentioned above in Python there is a special constant `None` which means nothing. Its meaning will be discussed later. It is generally used when we want to emphasize that we have no meaningful value at our disposal.

## Logical types and operators

The logical type is called `bool`. There are only two values of this type: `True` and `False`. They usually appear as a result of the operation of logical operators:

* `==` checks if two values are equal (**Note! this is <span style="color:red">double</span> `=`**)
* `!=` checks if two values are different
* `>`, `<`, `>=`, `<=` are operators that compare two elements

Please check the results of the following operations in the console:

```python
1 + 2 == 3

1 - 2 != -1

2 + 2 > 4

2 + 2 >= 4

(3, 2) == (1 + 2, 1 * 2)

(1, 2) > (1, 3)

(1, 2) < (1,)

(1, 2) > (2,)

"Ala" < "Basia"

"a" < "Z"
```


As you can see, it is not only possible to compare numbers, but also tuples and text strings. In the first case, the elements are compared sequentially, starting with the first one. In the second, the comparison is alphabetical, with all uppercase letters being smaller than lowercase. This is due to the ways in which characters are represented in the computer's memory. A detailed discussion of how you can compare text strings without distinguishing between uppercase and lowercase letters is described later in the lecture.

There are also special logical operators for logical values: negation (`not`), conjunction (`and`), alternative (`or`). Please check their operation yourself. For example:

```python
True and False or True

False and not True
```

etc... These operators will be very important when the conditions are discussed.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
