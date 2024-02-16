---
parent: Functions
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Defining and calling functions

A function is a separate piece of code that can be used multiple times in different places in the program. So far, the use of functions, such as print, len, range, etc. has been shown several times. You did not have to write it yourself, because it was already done by the creators of Python. It was enough to know how they work. Most functions require external information - numbers, texts, other objects - and they are given as arguments to the function. Most also return some result, which, for example, can be assigned to a variable or used directly in an expression.

A function is a separate piece of code that can be used multiple times in different places in the program. So far, the use of functions, such as print, len, range, etc. has been shown several times. You did not have to write it yourself, because it was already done by the creators of Python. It was enough to know how they work. Most functions require external information - numbers, texts, other objects - and they are given as arguments to the function. Most also return some result, which, for example, can be assigned to a variable or used directly in an expression.

## Defining a function
In every modern programming language it is possible to define functions independently. Without them, teamwork on even an average program would be almost impossible. New functions should be created whenever we are able to extract a code fragment that performs a certain, defined operation for certain data (and possibly returns a result). Also, when writing a program, you see the need to use an identical piece of code several times, you should put it in a separate function - thanks to this, the code only needs to be written once and you can easily use it multiple times.

We define functions using the **`def`** keyword:

```python
def function_name (argument1, argument2 ...):
block containing commands
performed in a function
```

The name of the function and the names of the arguments must follow exactly the same rules as the names of the variables. For example, below is the definition of a function that prints a string in a frame:

```python
def print_int_frame (text):
    line = "+-" + "-" * len(text) + "-+"
    print(line)
    print("|", text, "|")
    print(line)
```

Once a function has been defined, it is called with its name followed by parentheses containing arguments:

```python
print_int_frame("Hello!")

print_int_frame("How are you?")

```
**Note!** Even if the function takes no arguments, calling it requires giving the parentheses, even if nothing is in them:

```python
def greet ():
print ("How are you?")

greet()
```

## Returning a value

Functions can also return values ​​as the result of their operation. The **`return`** keyword is used for this, which can only appear inside a function. After this keyword, we put the value to be returned. For example

```python
def sum(number1, number2):
    return number1 + number2
```

When calling such a function, the result returned by it can be used in any way, e.g. by assigning it to a variable or using it directly in an expression (it has already been demonstrated many times, e.g. using the `len` or `range` functions). In the case of the above function, it could be:

```python
number1 = float(input("Enter the first number:"))
number2 = float(input("Enter the second number:"))

print("The sum of these numbers is:", sum(number1, number2))
```

Within a function, the **`return`** command can be anywhere, including a conditional block or inside a loop. In any case, it will cause the function to exit immediately: the execution of the loop will be interrupted and the commands below will not be executed. For example:

```python
def quotient(dividend, divisor):
    if divisor == 0:
        return
    quotient = dividend / divisor
    return quotient
```

The **`return`** command itself, with no return value given, will return `None`. The same happens when the function ends without the **`return`** command (as in the first example, the `print_in_frame` function). So, in Python, each function returns its result: defaulting to `None`.

The function can also return several results simultaneously. To do this, all results should be given after the return command, separated by a comma. For example

```python
def sum_and_difference(number1, number2):
    sum = number1 + number2
    difference = number1 - number2
    return sum, difference
```

When calling such a function, its result can be assigned to two variables, separated by a comma:

```python
sum21, difference21 = sum_and_difference (2, 1)
```

You can also assign the results of such a function to one variable or use it directly in an expression. In this case, it will be treated as a tuple containing a given number of elements:

```python
result = sum_and_difference(5, 3)  # result = (8, 2)
print(type(result))                # tuple
```

The type function used in the above example returns the type of the value given as its argument.

## Local and global variables

Variables defined outside of functions (as in all the previous lessons) are *global variables*. They are available throughout the program from the moment of their definition (value assignment). In some of the examples above, variables were also defined inside a function. These are local variables and they are shown <u>exclusively</u> inside the function, and after leaving they are destroyed. Function arguments are also treated as local variables (with values defined at the time the function was called).

If there are variables with the same names inside and outside the function, the values assigned to the local variable will not change the global variable:

If there are variables with the same names inside and outside the function, the values assigned to the local variable will not change the global variable:

```python
def function (): 
    variable = 2
    print ("Local variable:", variable )     # 2

variable = 1
function()
print ("Global variable:", variable )       # 1
```

The two variables in the example above have the same name. However, they are completely independent of each other. There is no access to the global variable inside the function because it is "obscured" by a local variable with the same name. If we do not assign any value to the variable inside the function, then we can read and use the value of the global variable:

```python
def function():
    print ("Global variable:", variable ) # 1

variable = 1
function()
```

**Attention!** For a variable to be treated as a local variable, it is enough that it is assigned a value anywhere inside the function. The following code won't work:

```python
def function ():
    print ("Global variable:", variable ) # ERROR - local variable is not defined yet
    variable = 2

variable = 1
function()
```

It is possible to force the variables inside the function to be treated as global by a command `global` followed by a list of global variable names. Assigning values to them inside this function changes the global variable:

```python
def function():
    global variable
    variable = 2
    print ("Global variable:", variable ) # 2

variable = 1
function()
print ("Global variable:", variable ) # 2
```

**<u>An important rule!</u>**

Each extractable code fragment should be placed in a separate function. Also, make sure that functions that perform calculations  do not print anything on the screen or change any global variables (generally avoid using a keyword `global`). When writing a function, we are often unable to predict how many times it will be performed. These can be thousands of times - in which case any message inside the function will be printed thousands of times. In general, parts of the program responsible for calculations and for interaction with the user (e.g. through functions `print` and `input`) should be clearly separated from each other. Thanks to this, in the future it will be possible and relatively simple to change the way of communication with the user, e.g. to a windowed version or via a website. <span style="background-color: #ffff99;">Under no circumstances you may use `input` in functions which purpose is different than directly reading from the keyboard All necessary data must be given as arguments to the function and the result returned with **`return`**.</span>


## Calling a function
The function  is always called by giving its name followed by parentheses. The arguments of the function are placed inside these parentheses. Their number must be the same as the number of arguments given when defining the function (except for default arguments and functions with a variable number of arguments, which are described below).

There are two ways to pass arguments to a function: by position and by name. To explain this, suppose we have a defined function:

```python
def function(a, b, c, d, e):
   function block
```

It takes 5 arguments. In the basic method of calling a function, we give 5 values ​​in parentheses, separated from each other by commas:

```python
function(1, 2, 3, 4, 5)
```

Then the first argument (`a`) will be 1 for a given call, the second (`b`) will be 2, etc. When calling a function, its arguments can also be passed by name by giving `argument_name=value` (with a single `=` character as in the variable assignment command):

```python
function(a=1, c=3, b=2, e=5, d=4)
```

In this case, the order in which we gave the arguments does not matter. The argument `a` will be 1, `b`:  2, `c`: 3, `d`: 4, and `e`: 5. It is also possible to combine both of the above methods. Then we first pass any number of arguments by position, then arguments by name (no need to follow the order or arguments passed by name):

```python
function(1, 2, d=4, c=3, e=5)
```

In this case, the values ​​1 and 2 will be assigned to the arguments `a` and `b` (as they appear in the definition as the first and second arguments), and the remaining arguments are passed by name (that is `c`: 3,  `d`: 4, and `e`: 5).

**Note!** Once we start supplying arguments using their names, we must not  revert to positional specification on the same call. This will cause a syntax error.

### Default arguments
It often happens that some arguments of a function have sensible defaults. Then, when defining the function, we can give these default values ​​using the sign `=`:

```python
def function(a, b, c, d=0, e=None):
   function block
```

The important thing is that all arguments with default values must be at the end of the argument list . This means that if a default value is given for any argument, each subsequent argument must also  have a default value.

When calling a function defined in this way, we can omit these arguments. Then, when invoked, their default values will be adopted:

```python
function(1, 2, 3)
```

In the above call, the value of the argument `d` will be 0, and the argument  `e`: `None`. Calling:

```python
function(1, 2, 3, 4)
```
In this call, the argument `d` will be set to 4 and `e` will remain at its default value.

When using default arguments, it is very useful to pass arguments by name. Let's see the following example of a call:

```python
function(1, 2, 3, e=5)
```
In this case, the argument `d` will keep its default value, and the argument `e` will take the value given in the function call (5). Python often uses functions with a very large number of arguments, most of which have default values. When calling such a function, you can easily change only the arguments you need.

**Attention!** Default argument values ​​are evaluated when the function is defined, not when it is invoked. For this reason, you should not use mutable types (lists and dictionaries) as default arguments. Instead of

```python
def function(numbers=[1, 2, 3]): 
    function body
```
you should write

```python
def function(numbers=None): 
    if numbers is None: 
        numbers = [1, 2, 3]
    function body
```
## Recurrence
A function can call itself to solve a problem. We call such a function a **recursive function**. Example calculating the factorial:

```python
def factorial(n):
     if n == 1:
         return 1
     elif n > 1:
         return n * factorial (n-1) 
     else:
         return None
```
For a recursive function to work properly, each subsequent call must be made for a different value of the argument controlling the the recurrence (in the example above it is `factorial(n-1)`). It must also be guaranteed to stop subsequent function calls when the value of this argument reaches a given value (in the example it will be for *n* equal to 1).


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
