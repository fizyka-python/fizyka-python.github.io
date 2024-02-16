---
parent: More on Variables
grand_parent: Technologie Informatyczne II
nav_order:  7
---

# String operations

Strings are special kinds of sequences designed to hold strings. Therefore, they have a number of methods that allow you to perform useful operations on these strings. Their detailed description can be found in the Python documentation. Below is an overview of some of the most useful operations and methods for text strings:

## Finding sub-strings

Unlike other sequences, the **`in`** and **`not in`** operators work not only for individual letters but for sub-strings of text. For example, `'rous' in 'carousel'` will return `True`.

If you need to know the position of some substring, the method find finds the position in which the given substring begins or -1 if the substring is not present in the string:

```python
'carousel'.find('rous')    # 2

'carousel'.find('ruza')    # -1
```

## Whitespace removal

The `lstrip`, `rsrip` and `strip` methods remove whitespaces (spaces, newlines, tabs) at the beginning, end, and both beginning and end of the string, respectively. This is very useful, for example, when you want to break the text into sections separated by punctuation marks (usually followed by spaces). Please try the following in the console:

```python
words = "one, two, three"

words.split(',')                                # ['one', ' two', ' three']

[word.strip() for word in words.split(',')]     # ['one', 'two', 'three']
```

To see the difference between  lstrip,  rsrip and  strip, please do in console:

```python
text = "   AAA   "    # mind the spaces at the beginning and end

text.lstrip()

text.rstrip()

text.strip()
```

## Case-swapping

In any text, you can change all letters to lowercase using the method `lower`, or to uppercase using the method `upper`:

```python
text = "Alice in Wonderland"

print (text.lower())   # Alice in Wonderland

print (text.upper())   # ALICE IN WONDERLAND
```

This is especially useful when you want to compare two strings in a case-insensitive manner:

```python
'AAA' == 'aaa'                   # False

'AAA'.lower() == 'Aaa'.lower()   # True
```

A more sophisticated method for changing the case of letters are:

`capitalize`: convert the first letter in the entire text to uppercase, all other letters to lowercase:

```python
"ala has a cat".capitalize()   # 'Ala has a cat'
```

`title`: converts the first letter of each word to capital:

```python
"ala has a cat".title()        # 'Ala Has A Cat'
```

## String formatting

Python allows you to construct strings using values stored in other variables. There are three ways of doing this: with a `%` operator (this is a deprecated method and not recommended), with a `format` method, and with special *format strings*. The latter method is the easiest to use, however it <u>requires Python version 3.6 or higher</u>. As this method is the newest one available, it will be discussed here:

*Format strings* are special text strings that are created by adding a character `f` immediately before the double or single quotation marks that open the string (no spaces between them). In such a string, the brace has a special meaning: inside it you can put any Python expression, the value of which will be inserted into the string. E.g:

```python
height = float(input("Enter your height [cm]:")) / 100    # we convert the given height into meters
mass = float(input("Enter your weight [kg]:")) 

bmi = weight / height ** 2     # https://en.wikipedia.org/wiki/Body_mass_index

message = f"Height: {100 * height} cm, weight: {mass} kg, BMI: {bmi}."

print(message)
```

Please run the above example and see what message will be displayed. Then try to remove the `f` prefix mark and see the difference.

In the example above, the message displayed will be:

```
Height: 172.0cm, weight: 64.0kg, BMI: 21.63331530557058.
```

Please note that the BMI value is printed with too many digits. This can be remedied. Inside the brace where the Python expression is located, we can (after the expression) add a : sign and then information how the value of this expression is to be formatted. Please change the string string with the message to the following:

```python
message = f "Height: {100 * height} cm, weight: {mass} kg, BMI: {bmi:.2f}"
```

`.2f` after the colon it means that the value of the expression (in this case the variable `bmi`) is to be presented as a real number (`f` from *float*) with two decimal places (`.2`). Below is a list of some useful format descriptors that can appear after a colon (*X* and *Y* in the table should be replaced with integers):

| Format  | Description                                                                                                                                 |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `.Yf`   | a real number with *`Y`* digits after the decimal dot (the value must be of type `float`)                                                   |
| `Xf`    | a real number spanning at least *`X`* characters, if necessary, spaces will be added at the beginning (the value must be of type `float`)   |
| `X.Yf`  | number taking up at least *`X`* characters with *`Y`* places after the decimal dot (the value must be of type `float`)                      |
| `0Xf`   | a real number spanning at least *`X`* characters, if necessary, zeros will be added at the beginning (the value must be of type `float`)    |
| `0X.Yf` | like `X.Yf`, but empty spaces will be filled with zeros                                                                                     |
| `+XXf`  | where *`XX`* is one of *`X`*, *`X.Y`*, *`0X`*, *`0X.Y`* — a sign will always be added (+ for non-negative numbers)                          |
| `e`     | real number in exponential notation (`1.4e+2`) (the value must be of type `float`)                                                          |
| `XXXe`  | for numbers in exponential notations, it is possible to force the number of digits or digits after the dot in mantissa, as above            |
| `Xd`    | an integer number spanning at least *`X`* characters, if necessary, spaces will be added at the beginning (the value must be of type `int`) |
| `0Xd`   | an integer number spanning at least *`X`* characters, if necessary, zeros will be added at the beginning (the value must be of type `int`)  |
| `x`     | integer number in hexadecimal notation (the value must be of type `int`)                                                                    |
| `o`     | integer number in octal notation (the value must be of type `int`)                                                                          |
| `b`     | integer number in binary notation (the value must be of type `int`)                                                                         |
| `<XXs`  | any left-aligned expression spanning at least *`XX`* characters                                                                             |
| `>XXs`  | any right-aligned expression spanning at least *`XX`* characters                                                                            |
| `^XXs`  | any centered expression spanning at least *`XX`* characters                                                                                 |

As an example, let's try to print a table with the 100-meter runs world records:

```python
# Create a list of dictionaries with data
records = [
     {'date': '16.08.2009', 'champion':' Usain Bolt', 'time': 9.58},
     {'date': '20.09.2009', 'champion' : 'Tyson Gay', 'time': 9.69},
     {'date': '23.09.2012', 'champion': 'Yohan Blake', 'time': 9.69},
     {'date': '2.09.2008', 'champion': 'Asafa Powell', 'time': 9.74}
]

width = 42            # width of the whole table
print("-" * width)   # print a horizontal line
print("|  Time  |     Champion     |    Date    |") 
print("-" * width) 
for record in records: 
    print (f"| {record['time']:6.3f} | {record ['champion']:^16s} | {record ['date']:>10s} |")
print ("-" * width)
```

## How do I put the brace "{}" in the format string?

In a format string, to insert a brace that you want to be treated as part of the text rather than the beginning of the expression, repeat it:

 {% raw %}
```python
f"This is a brace {{2 + 2}} and this is a brace expression {{{2 + 2}}}"
```
 {% endraw %}

In the above text, the expression marked in blue will be evaluated and the repeated braces will appear only once.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
