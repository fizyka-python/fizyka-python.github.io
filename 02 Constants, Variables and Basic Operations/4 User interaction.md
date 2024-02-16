---
parent: Constants, Variables and Basic Operations
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# User interaction

So far we have focused on the back-end part of the code (see [Kitchen and Dining Room](00%20Algorithms/3%20Frontend-backend)). In the simplest cases writing Python commands in a console or a Jupyter Notebook allows to see the result of the last evaluated expression. However, in full programs it does not work so. We need a way to interact with the user of our program. Later, when you have more experience, you may try to create some neat graphical user interface or use web pages for this purpose. However, for now we will stick with the simplest solution: the `print` and `input` functions.

## `print` function

The `print` function is used to print constants and variables to the screen. By default, it prints all values given as its arguments to the screen, separating them with spaces. It finally prints the newline, so that subsequent calls to print will be arguments on subsequent lines.

You can change the character by which the values to be printed are separated: replacing the default space with any text. To do this, after the arguments to be printed, add `sep='new separator'`. Likewise, you can change the characters printed at the end (defaulting to a newline) by adding `end='new end'`. For example:

```python
print(1, 2, 3, sep='...')            # 1...2...3
print(1, 2, 3, end='X')              # 1 2 3X
print(1, 2, 3, sep='...', end='XX')  # 1...2...3XX
```

In the last two cases, no newline will be printed. Another call to print will print the text on the same line.

Remember that a newline or a string given as end will always be printed, even when no argument is given. So, calling `print()` will just jump to a new line.


## Keyboard input

Until now, the values ​​of variables were defined in the program code:

```python
variable1 = 1 
variable2 = 2
```

In real programs, data is usually downloaded from external sources - they can be data entered directly by the user (in a text console, graphical window, through a form on a website, etc.), but they can also be read from a file, sent from an external device ( e.g. measuring equipment), downloaded from the Internet, given as an argument of calling a program launched from the [command line](https://en.wikipedia.org/wiki/Command-line_interface).

A well-written program should be independent of the input method. We will discuss exactly how to achieve this later. Below, we will discuss how to read the data entered by the user directly from the keyboard, but from the very beginning it should be noted that **this stage should be separated from the calculation part, as well as writing the result on the screen using a function `print`**.

The function used to enter data from the keyboard is called `input`. It is used as follows:

```python
entered_value = input ("Question:")
```

The argument of this function (the text in parentheses) is the question that will be displayed to the user. When it is printed, the program will stop and wait for any string to be entered by the user (the string should be terminated by pressing the Enter key). Then, the entered value will be *returned* by the function `input`, i.e. placed somewhere in the memory and made available e.g. for assignment to a variable, for further use (in the above example, the variable named `entered_value` will point to the string entered by the user).

Note that in Python 3, the function input always returns a text string, which is a variable of type `str`. If we need a numeric value, it should be converted to the correct type, as described earlier:

```python
distance = float(input("Enter distance between points [m]:"))
```

In this example, the user will be prompted for a distance, and then the entered value will be immediately passed to the "function" `float` to be converted to a real number. The important point here is that at this moment we have no control over whether users enter the correct value that can be converted to a real number. If this is not the case, the program will be terminated with an error message (please check). A method to deal with this problem will be described later in the course.


## Kitchen and dining room again!

As I wrote earlier (many times by now), it is a good habit to separate the input and display part (the *dining room*) from the computational part (the *kitchen*). Thanks to this, in the future it will be much easier to change our program, e.g. in such a way that it reads data from one file and writes the results to another (this will be discussed later). So a poorly written program is:

```python
inches = 2.54 * float(input("Enter length in centimeters:")) 
print("Length in inches is:", inches)
```

This one looks much better:

```python
# Input 
centimeters = float(input("Enter length in centimeters:")) 

# Calculation part 
inches = 2.54 * centimeters 

# Presentation of the result 
print("Length in inches is:", inches)
```

Please pay attention to write programs this way, **from the very beginning**!


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
