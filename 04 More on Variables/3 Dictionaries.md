---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Dictionaries

Normal lists (arrays) are usually a collection of numbered elements, so to refer to any list element you must enter its number. But identifying elements by numbers aren't always convenient. For example, flight numbers are identified by an alpha-numeric code. Similarly, bus numbers in Łódź may contain letters.

A data structure that allows any type of index (called a key) to be used instead of a number is called a dictionary. In Python, the corresponding data structure is called `dict`. Like a list, it is a variable structure: after you create a dictionary, you can change it. Just like tuples are made with parentheses, lists with square brackets, dictionaries are made with curly braces:

```python
dictionary = { key1: value1, key2: value2, key3: value3 }
```

Consider a simple example. Let's create a dictionary where the key is the name of the country, and the value the name of the capital of that country:

```python
capitals = {       # after opening the parenthesis, you can go to a new line
     'Poland': 'Warsaw',
     'Germany': 'Berlin',
     'USA': 'Washington 
}
```

Thus, each dictionary element consists of two objects: a key and a value. In our example, the key is the name of the country and the value is the name of the capital. A key identifies an element of a dictionary, value is the data corresponding to the given key. The key values ​​must be unique, i.e. there cannot be two identical keys in the dictionary.

The phone book is another example of the dictionary data structure. In this case the name is the key and the value is the phone number. For both a dictionary and a phone book, it is easy to find an item for a given key (e.g., if the records are stored in alphabetical order), but if the key is unknown and only the value is known, searching for an item with the given value may require you to browse the entire dictionary.

Access to the dictionary elements is done using square brackets. The key value is given inside the parentheses, e.g.:

```python
print(capitals['Poland']
```

Attempting to retrieve a value for a key that is not in the dictionary in this way will result in a `KeyError`.

As stated above, the dictionary can be changed. Adding new items and changing existing ones is very simple:

```python
capitals['France'] = 'Paris'
```

If the key "France" was not previously in the dictionary, it will be added and assigned the value "Paris". If it already existed, it will simply be assigned a new value.

Removing items from the dictionary is possible with the command **`del`**:

```python
del capitals['USA']
```

In Python, the key can be any immutable data type: integers and real numbers, strings, tuples. It cannot be lists or other dictionaries. The value of a dictionary item can be any data type.

In addition to the use of square brackets to access the dictionary elements it is possible using the method `get`: `dictionary.get(key)`. If the given key is in the dictionary, the corresponding element will be returned. Otherwise, the method will return None. This method also has a version with two arguments `dictionary.get(key, default_value)`, which — if the given key is missing from the dictionary — returns the given default value. In both cases, this method (unlike retrieving the item using square brackets), will not generate an exception (error).

To check if a key is in the dictionary, you can use operators **`in`** and **`not in`**, similarly to sequences.

```python
letters = {'ab': 'ba', 'aa': 'aa', 'bb': 'bb', 'ba': 'ab'} 

key = 'ac' 
if key in letters: 
    del letters[key]
```

## More about creating dictionaries

Just as it is possible to create lists elegantly with list comprehensions, it is possible to construct dictionaries as follows:

```python
dictionary = { expression_for_key: expression_for_value for item in sequence }
```

E.g:

```python
words = "Ala has a cat".split()     # ['Ala', 'has', 'a', 'cat']

word_lengths = {word: len(word) for word in words}
```

This will create a dictionary `{'Ala': 3, 'has': 3, 'a': 1, 'cat': 3}`.

## Iteration through dictionaries

Although dictionaries are not sequences, you can iterate over them with a **for** loop:

<pre>
<b>for</b> <i>key</i> <b>in</b> <i>dictionary</i><b>:</b>
    loop block
</pre>

This loop will be performed for each  key in the dictionary. Unlike sequences, the iteration order is undefined (i.e. the loop will be executed for each key, but we cannot predict in what order). E.g:

```python
word_lengths = {'Ala': 3, 'has': 3, 'a': 1, 'cat': 3} 

for word in word_lengths: 
    print("Word", word, "has", word_lengths[word], "letters")
```

If we want to iterate over dictionary values only, we can use the method `dictionary.values()`:

```python
capitals = { 'United Kingdom': 'London', 'Germany', 'Berlin', 'USA' 'Washington} 

for city in capitals.values(): 
   print("There is no such city as", city, "in Poland")
```

It is also possible to iterate through keys and values simultaneously using the method `dictionary.items()`:

```python
for country, city in capitals.items(): 
   print("Capital of", country, "is", city)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
