---
parent: Constants, Variables and Basic Operations
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Variables

Writing any program would be impossible if the calculated values could not be saved. For this purpose we use **variables**.

A variable is the name (label) of the memory location that contains the specified value. It is created using the instruction `=` (single character, unlike the logical comparison operator described earlier):

```python
a = 5
b = 10
c = a + b
```

What will be the value of the variable `c`? This can be checked either by typing a command `print(c)` that will work both in the interactive console and program code written in the editor, or (only in the interactive console) by simply typing the variable name:

```python
>>> c
```

(`>>>` is just an illustration of what the console is printing: do not enter it)  
Of course, in any case we will get 15.

The above code works exactly as follows:

1. It places the number 5 somewhere in memory and labels it `a`.
2. It places the number 10 somewhere in memory and labels it `b`.
3. Calculates the sum of the value indicated by labels `a` and `b`, places the result somewhere in memory, and labels it `c`.

The very important thing is that a single `=` character is an instruction that is a direct command for the computer. It must always be on a separate line and only the variable name can be on the left side. On the right side, there is an expression, i.e. something that has or evaluates to a specific value (of any type). As with math operators, it is good practice to write spaces around the `=` symbol (as in all the examples in this lecture). This significantly increases the readability of the code.

The same label can be used multiple times. Let's look at the following code:

```python
a = 2
a = a + 1
```

The last line is not a mathematically incorrect operation, but a valid and frequently used reassignment. The action on the right will be performed first (that is, the computed value pointed to by the variable `a` and stored somewhere in memory), and then the variable `a` will be set to point to this new value. The previous value (2) will be considered unnecessary and removed from the memory.

In general, Python keeps objects in memory as long as there is even one variable pointing to them. We will consider the following example:

```python
text1 = "Use the Force, Luke!"
text2 = text1
```

In this case, the text `"Use the Force, Luke!"` Will only be stored once, but two variables will point to it. If we remove the variable `text1`:

```python
del tekst1    # del variable_name removes the variable completely
```

the Obi-Wan's original sentence will still be stored in the computer's memory and can be accessed as a variable `text2`. Only when we remove or change this variable:

```python
text2 = 123  # Python does not require the new value to be of the same type
```

this sentence will be removed from the memory (as there is no longer a variable pointing to it) and the space it occupies can be used again.

## Example

Let us calculate how long it will take for the body to fall freely from a 30 m high skyscraper. Since in uniformly accelerated motion the distance traveled (in this case the height of the building _h_) is expressed by  _h_ = _g_ _t_<sup>2</sup> / 2, where _g_ is the gravitational acceleration, a simple transformation allows to compute the drop time _t_ = (2 _h_ / _g_)<sup>1/2</sup>. Let's write this in Python:

```python
g = 9.81                # gravitational acceleration [m/s²]
h = 30                  # building height [m]
t = (2 * h / g)**0.5    # calculated fall time [s]

print("Time of falling from height", h, "m is", t, "s.")
```

In the last line, we used the `print` function to print the answer as a full sentence.


## Naming Variables

In Python, variable names can be almost anything. However, they must meet the following conditions:

* variable names must consist of letters (upper and lower case), numbers, and the underscore _;
* the first character cannot be a digit;
* the variable name cannot be the same as one of the reserved keywords (**`and`**, **`as`**, **`assert`**, **`async`**, **`await`**, **`break`**, **`class`**, **`continue`**, **`def`**, **`del`**, **`elif`**, **`else`**, **`except`**, **`False`**, **`finally`**, **`for`**, **`from`**, **`global`**, **`if`**, **`import`**, **`in`**, **`is`**, **`lambda`**, **`nonlocal`**, **`None`**, **`not`**, **`or`**, **`pass`**, **`raise`**, **`return`**, **`True`**, **`try`**, **`while`**, **`with`**, **`yield`**).

Valid variable names are therefore: `a`, `b`, `number1`, `first_result`, `_temporary_data`, `ты_крутой` (in Python 3 non-Latin letters may be used in variable names, however this is not recommended).

Incorrect names are `12monkeys`, `temporary-data`, `something_important!`, `lambda`. In the first case, the variable name starts with a digit, in the next two it contains an illegal character. The last case is a reserved keyword.

In addition to formal requirements, it is important that the names of the variables are clear and understandable. Very often we are forced to analyze programs written by someone else. We also forget programs written by ourselves after a few weeks and we must be able to read their code with understanding. Please take a look at the following code snippet and answer what it does:

```python
z1q3z5ocdval = 35.0 
z1q3z5afdval = 12.50
z1q3p5afdval = z1q3z5ocdval * z1q3z5afdval
print(z1q3p5afdval)
```

Is the code presented below more readable?

```python
x = 3.14 
y = 100 
z = x * y 
print(z)
```

At first, it would seem so: the variables are short and easy to distinguish. However, their meaning is still not clear — the above code would make sense if `x`, `y`, and `z` were coordinates in three-dimensional space (but then `z = x * y` would not make any physical sense).

What does the following code do?

```python
work_hours = 35.0 
pay_rate = 12.50 
salary = work_hours * pay_rate
print(salary)
```

In this case, everything is clear. Similarly, in the example shown earlier, they are used single-variable `h`, `g`, `t`. Their meaning is clear, as they are generally accepted symbols of physical multiplicities. Please note, however, that in the commentary they were additionally described and the unit was given (in physical science this is crucial)!

> ### Attention!
>
> **In Python, variable names are case-sensitive**. Therefore, the variables named `number`, `Number` and `NUMBER` are three different and independent variables. This can be used to increase the readability of the program, however, it is good practice to use only lowercase letters for variable names (however, it is not a necessary requirement).

### Non-Latin characters

In Python 3 it is possible to include letters of non-Latin alphabets in character names. Hence, this is an absolutely valid code:

```python
印 = print

數 = 10
印("這是一個數: ", 數)

θ = 90
印("這是一個角度: ", θ)

def 算到(一個數):
    ξ = 1
    while ξ <= 一個數:
        印(ξ)
        ξ = ξ + 1

算到(10)
```

You may decide yourself whether it is a good idea to use local characters in your code...

## Multiple assignment

In Python, it is possible for a single assignment statement to change the value of multiple variables:

```python
a, b = 0, 1
```

which is equivalent to writing:

```python
a = 0 
b = 1
```

Multiple assignment is useful when you need to exchange the values of two variables. In older programming languages without support for multiple assignment, this requires the use of an auxiliary variable. In Python, you can simply write:

```python
a, b = b, a
```

There should be a comma-separated list of variable names to the left of the character `=`. The right side can be any expressions separated by commas. The number of elements on the left and on the right must be identical.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
