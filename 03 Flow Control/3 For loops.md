---
parent: Flow Control
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# For loops

Another type of loop in Python is the for loop. It is used when we are able to predict in advance how many times we want to perform this loop, or when we want to repeat it for each element of the sequence. The for loop syntax is as follows:

<pre>
<b>for</b> <i>pointer</i> <b>in</b> <i>sequence_which_we_iterate</i><b>:</b>
    block repeated for each element of the sequence,
    the identifier given as a pointer will
    point at each element of the sequence in every iteration
</pre>

In the above syntax  we give the correct variable name as the pointer. This variable does not have to be previously defined (and if it was, its previous value will be removed). Each time the loop passes, this variable will take the next values ​​in the sequence we iterate through. Of course, the sequence must exist: either be given as a constant or assigned to a variable.

So far, two sequence types have been introduced: string and tuple. The following is an example of a loop in which all the elements of a tuple are summed:

```python
numbers = (1, 2, 3, 5, 7)
sum = 0
for number in numbers:
    sum += number
print("Sum of numbers is", sum)
```

> **Attention!** In Python, many basic operations (such as adding the elements of a set) can be done with one command or function (in this case, it would be enough to write `result = sum(liczby)`). In normal programs, use these abbreviated forms as they are clearer and usually run faster. However, for the purposes of examples and exercises, we will write many of these simple operations by hand — for illustration purposes only.

You can also iterate over elements of a text string:

```python
name = input("What is your name:")
for letter in name:
     print(letter)
```

The above example will ask the user for their first name and then print each letter in a separate line.

## Caesar cipher

Now let's look at a more advanced example. We will implement the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) (although we will limit ourselves to the alphabet used in the English language). First, however, it is necessary to explain how the characters are stored in the computer's memory. Well, every computer is a device that can carry out operations on numbers and only on numbers. Therefore, in order to save any text in the computer's memory, each character must be assigned a numerical value. Which number corresponds to which letter defined by the ASCII and Unicode standards. There are two functions in Python that let you find out which number corresponds to which character and vice versa. The first is a function `ord(character)` whose argument can only be one character (that is, a text string containing exactly one element). It will return the numeric code of this character. The inverse function `chr(code)` will return the character represented by the numeric code given as its argument. Please check in the interactive console:

```python
print(ord('A'))

print(chr(122))
```

The above functions will be used in the encryption program using the Caesar cipher. We will use an alphabetic shift of 13, because the English alphabet has 26 letters, so double encrypted messages will restore it (in other words, the same program can be used to encrypt and decrypt messages — this variant of the Caesar cipher is called ROT-13).

```python
# We read the text to be encrypted
original_text = input("Enter the text to be encrypted: ")
 
# The ciphertext is empty for now; we will add further characters to it
encrypted_text = ''

# In the loop we iterate over each
for character in original_text:

    if 'A' <= character <='Z':  # condition a < x <b is the same as: a < x and x < b
        # We have a capital letter; we calculate its sequence number
        # (so that the letter "A" corresponds to 0)
        code = ord(character) - ord('A')

        # We encrypt the character: add 13 and wrap up to 26 characters (remainder from division)
        new_code = (code + 13) % 26

        # We add a new ciphertext: 
        # first "shift" the new code so that the letter "A" has the correct code, 
        # then convert it to a character and add it to the string with the result
        encrypted_text += chr(new_code + ord('A'))

    elif 'a' <= character <= 'z':  # we do the same for lower case letters
        code = ord(character) - ord('a')   # subtract lower case code "a"
        new_code = (code + 13) % 26
        encrypted_text += chr(new_code + ord('a'))

    else: 
         # Rewrite the remaining characters unchanged
         encrypted_text += character

# Print the results 
print(encrypted_text)
```

Please copy the example below to a new file (e.g. `rot13.py`), and then run. Please carefully analyze its syntax so that you understand each line. As part of the classes, you will write more advanced programs than the above.

If in doubt, please post on the forum.

## Numeric ranges

It is very often necessary to repeat the loop a specific number of times. We can then use the following form:

<pre>
<b>for</b> <i>counter</i> in <b>range</b>(<i>number_of_repetitions</i>)<b>:</b>
     block repeated a given number of times
</pre>

As this loop runs, the counter will go from 0 to the value of *repetitions*–1. Try the following example:

```python
for i in range(10): 
    print(i)
```

Please note that the number 10 has not been printed.

In fact, `range` is a function that generates a sequence of numbers on the fly, and the **for** loop just iterates over that generated sequence. It can be used in three ways: The most basic and most frequently used `range(stop)` will form a sequence from 0 to the preceding value `stop`. We can also provide the function of two arguments `range(start, stop)`. Then the countdown will start from the value given as `start` (if *start* ≥ *stop*, the range will be empty and the loop will not run even once). So *range(stop)* is equivalent of *range(0, stop)*. The third version is `range(start, stop, step)` that adds a step used to change the value each time. In this case, the iteration will end when the next value reaches or exceeds the `stop` value.

So to print the numbers from 1 to 10 we can use:

```python
for i in range(1, 11): 
    print(i)
```

and to do it backwards:

```python
for i in range(10, 0, -1): 
    print(i)
```

## Exercise

Write a program that asks the user for an integer, then calculates and prints its factorial (that is, the product of the numbers from 1 up to and including the given number ). Your work may be based on the above example for calculating the sum of numbers and on the examples of the range function. Please check if you have calculated 5! is equal to 120 and 10! = 3 628 800.

## Breaking and continuing the loop

As with the while loop, the **`break`** and **`continue`** commands and can be used in the for loop. Their operation is the same as in the case described earlier. Here, too, it is possible to use the **`else:`** block, which will be executed only when the loop ends normally (that is, after it has finished iteration over all elements).

```python
trap = int(input("Enter the trap value:"))

for i in range (1, 11):
    if i == trap:
        print("You felt into the trap!") 
        break
    print(i) 
else: 
    print("You successfully avoided the trap.")
```

## Loop nesting

There are no obstacles to place the other inside one loop. It is only important to use different pointer (counter) names in nested loops. For example, to display the names of all fields on a chessboard, we can use the following program:

```python
for row in range(8, 0, -1):                   # numbers from 8 to 1 (inclusive) backwards (row 8 will be on top)
    for column in "ABCDEFGH":
        print(column, row, sep='', end=' ')   # the meaning of sep and end was explained before
    print()                                   # at the end of each row we only print a newline (default end)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
