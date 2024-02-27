---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Sets

The last standard Python type that allows you to hold other elements is a `set`. Unlike a list, the elements in the set are not ordered (they do not have assigned indexes nor keys, as in a dictionary).

The sets are created as follows:

```python
the_set = {element1, element2, element3...}
```

The braces are the same as creating a dictionary, except that the colon is not used.

All elements of the set must be immutable (that is, they cannot be lists and tuples). In addition, the set cannot contain two identical items. Please check on the interactive console

```python
{1, 2, 3, 1} == {1, 2, 3}
```

The above expression will be `True` as both sets are identical.

The number of elements in a set can be checked (just like for any other sequence or dictionary), by the function `len`. Similarly, you can iterate over them using a **for** loop (however, the iteration order will be undefined). For example:

```python
primes = {2, 3, 5, 7, 11}
for num in primes:
    print(num)
```

You can also check whether a given element belongs to a set or not using operators **`in`** and **`not in`**.

The `add` (`the_set.add(new_element)`) method is used to add new elements to the set. For example:

```python
A = {1, 2, 3}
print(1 in A, 4 not in A)
A.add(4)
print(4 in A)
```

There are two methods for removing items from a collection: `discard` and `remove`. Their behavior changes only if the deleted item is not in the collection. In this case, the method `discard` does nothing and the method `remove` raises a `KeyError` exception.

Since the elements of the set have neither indexes nor keys, direct access to individual elements is not possible. If necessary, you can convert such a file into a list (`my_list = list(my_set)`).

## Operations on sets

You can perform mathematical operations on sets:

| Python syntax                                  | Meaning                                                                                   |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `A | b` or `A.union(B)`                        | Returns a set that contains elements from both `A` and `B`                                |
| `A |= B` or `A.update(B)`                      | Adds all elements present in `B` to `A`                                                   |
| `A & B` or `A.intersection(B)`                 | Returns a set containing only elements present in both `A` and `B`                        |
| `A &= B` or `A.intersection_update(B)`         | Removes all elements from `A` that are not present in `B`                                 |
| `A - B` or `A.difference(B)`                   | Returns difference of `A` i `B` (elements present in `A` but not in `B`)                  |
| `A -= B` or `A.difference_update(B)`           | Removes all elements present in `B` from `A`                                              |
| `A ^ B` or `A.symmetric_difference(B)`         | Returns symmetric difference of `A` i `B` (elements belonging to `A` or `B` but not both) |
| `A ^= B` or `A.symmetric_difference_update(B)` | Stores symmetric difference of `A` and `B` in `A`                                         |
| `A <= B` or `A.issubset(B)`                    | Returns `True` if `A` is a subset of `B`                                                  |
| `A >= B` or `A.issuperset(B)`                  | Returns `True` if `B` is a subset of `A`                                                  |
| `A < B`                                        | Equivalent of `A <= B` and `A != B`                                                       |
| `A > B`                                        | Equivalent of `A >= B` and `A != B`                                                       |

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
