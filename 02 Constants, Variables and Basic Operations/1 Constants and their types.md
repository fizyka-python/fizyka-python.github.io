---
parent: Constants, Variables and Basic Operations
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Constants and their types

## Constants

Constant values such as numbers, letters, and strings (strings) are called "constants" because their value does not change. In Python, constants can be of the following types:

### Numeric types

* integer numbers: `1`, `100`;
* integers in non-decimal notation systems beginning with the prefix `0b` (binary notation), `0x` (hexadecimal notation), `0o` (octal notation): `0b101` (5), `0x1a` (26), `0o12` (10);
* real numbers (the decimal part is separated by a dot and no digits before or after the dot means 0): `2.27`, `3.14`, `-1.2`, `1.0`, `2.` (2.0), `.5` (0.5);
* real numbers written in exponential (base 10) notation <em style="color: #0000ff;">mantissa</em>e<em style="color: #ff00ff;">exponent</em>, oznaczające <em style="color: #0000ff;">mantissa</em> × 10<sup><em style="color: #ff00ff;">exponent</em></sup>: `-5e3` (-5000), `2.5e-2` (0.025);
* complex numbers in which we write both components as real numbers, and denote the imaginary part by adding `j` at the end: `1.5-0.2j`, `-2+1e-1j` (-2+0.1j);

### Text types

Strings between one of the following sets of quotation marks:

* single quotation marks: `'...'`,
* double quotation marks: `"..."`,
* single or double quotation marks repeated three times: `'''...'''`, or `"""..."""`.

In the latter case, the text may span several lines. In the first two it is not allowed, however newlines can be inserted using the special symbol `\n`.

You can use any set of the above symbols to denote text strings, but it is very important that each string begins as it ends. The valid examples are (red indicates the beginning and ending quotation marks):

```python
"Ala ma kota"

'This chapter is named "Constants"'

"""First line
Second line"""

"Here are\ntwo lines too"
```

### Tuples

Tuples are an ordered set of values constant. Successive values ​​are separated by commas, and the whole tuples should be enclosed in parentheses. More about using tuples will follows in this course later. Examples of tuples are:

```python
(1, 2, 5)

(2.5, 3, 1j, 'tekst')  # tuples' elements don't have to be of the same type 

("tekst", (1, 2))      # tuples can contain other tuples (and other types, with which we haven't mentioned yet)

(1,)                   # a one-element tuple must have an extra comma (to distinguish it from the number in parentheses)

()                     # empty tuple
```

More on the use of tuples and how to extract their individual elements will be presented later in this lecture.

## Operations on values

You can act on the values supported by Python using mathematical operators. The basic operators are `+`, `-`, `*` (multiplication), `/` (division), `**` (power), `//` (integer division), `%` (division remainder). Python can perform operations according to the applicable mathematical rules (the use of parentheses is allowed). To read them, start the Spyder program and enter the following expressions in the interactive console (it is not necessary to use the `print` function - the interactive shell will automatically print the result of the calculated expression):

```python
1 + 2

2 + 2 * 2

(2 * (1 + 1))**2

2.5 * 2

7.5 / 3

5 / 2

4 / 2

8 // 3

8 % 3

2**10

8**(1/3)

(-1)**0.5

'1' + '2'

(1, 2) + (3,)   # notice comma in (3,)

3 * "a"

(1, 2) * 2
```

I also suggest trying this interactive Python shell yourself as a calculator.

A few of the above examples should be discussed in detail. The division operator (`/`) on real or integer numbers will always return the real result (even if the result is an integer). In turn, the integer division operator (`//`) will remove the fractional part - for this reason, it has limited use in engineering and scientific applications.

The exponentiation operator (`**`) can also raise to a non-integer power. Therefore `(-1)**0.5` is treated as the principal root of `-1`, i.e. the imaginary number `1j`. It is shown as `(0 + 1j)`, or something like `(6.123233995736766e-17+1j)`. Do not be afraid of this: according to the previously described exponential notation, the real part of this number is in the order of 10<sup>-17</sup>, which is practically 0. Floating point computer calculations are not 100% accurate, hence the result (accuracy of calculations is a separate issue on which you need to pay attention to when writing calculation programs, but at this stage we will not deal with it).

It is a good practice to write spaces around the mathematical operators, as it significantly increases the readability of the code (of course, this is not a formal requirement, but omitting spaces frequently makes it very difficult to analyze the program, especially when it is written by someone else).

Python can also work on non-numeric types as long as they make sense. Adding text strings or tuples together combines them, and multiplication by a whole number repeats their contents a given number of times.

For actions that don't make sense, Python will throw an error. Please try the following in the console and read and understand the error message each time:

```python
1 / 0

1 + "2"

2.5 * (1, 2)

"Alala" - "la"

50.0 ** 1000000
```

The last operation is mathematically and logically correct, however, it results in too large number that cannot be correctly stored in the computer's memory as a real number.

## Converting types

All the constants of a specific type described above (as well as other types, not yet shown) have names. For the types already described, they are as follows:

* integer numbers: `int`
* real numbers: `float`
* complex numbers: `complex`
* text strings: `str`
* tuples: `tuple`


For any value you can check its type using the type function, for example:

```python
type(2)

type(2.5)

type(2j)

type("2")

type(1 + 2)

type(1 + 2.0)
```

As you can see above, Python is able to convert numeric types by itself so that the result of a given action makes sense. However, it is possible to force type conversions manually by directly using their names as functions. This is especially useful when you want to convert a string to a number. For example:

```python
float("2.5")
```

Please see what is the difference between:

```python
"1" + "2"
```

and

```python
int("1") + int("2")
```

and

```python
str(1) + str(2)
```

If the conversion doesn't make sense, Python will throw an error. Please try

```python
int(10+2j)

float("dwa")

float("two and half")

int("one")

int("4O")         # can you notice a problem here?
```

The exception is the conversion of a real number to an integer. The expression

```
int(2.7)
```

will simply discard the fractional part.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
