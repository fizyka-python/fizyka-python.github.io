---
parent: Flow Control
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Conditions

All previous programs have been executed sequentially, line by line. No line could be skipped.

Consider the following problem: for a given real number, determine its absolute value. If number > 0, the program should print its value, otherwise it should print –number . This behavior cannot be achieved by using a sequential program. The program should conditionally select the next step. The following command used for this purpose is called if:

```python
number = float(input("Enter a number:"))

if number > 0:
    absolute_value = number
else:
    absolute_value = -number

print(absolute_value)
```

This program uses a conditional statement **`if`** . After that, we put a condition `number > 0` after a colon. We then insert a block of statements that will only be executed if the condition is true (i.e. the value of the expression `number > 0` is equal to  `True`). This block can be followed by a word  else, a colon, and another block of instructions that will only be executed if the condition is false (i.e., has the value `False`).

## Blocks in Python

In Python, blocks are marked with indentation i.e. spaces at the beginning of the line. The number of these spaces is arbitrary, but it is important that there are enough of them to make the block visually stand out. Each block  must be identified by a colon (**`:`**) at the end of the  preceding line. Of course, only some commands can start a new block. In the example above, these are the commands if and else. The blocks assigned to them will be executed only if the condition is met (**`if`**) or not met (**`else`**). We finish the block by removing the indentation of the first non-block line.

Blocks can be nested: next levels are marked by increasing the number of spaces at the beginning (e.g. 4, 8, 12 etc.), and each of them is finished by undoing the indentation accordingly. (8, 4, 0). It is possible to remove indentations corresponding to several blocks at once — then we finish them all at once.

The way of marking blocks with indentation is specific to Python. Other programming languages use special characters (usually braces) to mark the beginning and end of a block.

In summary, a conditional statement in Python has the following syntax:

<pre>
<b>if</b> <i>condition</i><b>:</b>
    any number of commands
    executed if the condition is True
<b>else:</b>
    any number of commands
    executed if the condition is False
</pre>

the keyword else along with its corresponding block can be omitted if nothing should be done if the condition is false. For example, we can replace the variable with number with its absolute value as follows:

```python
number = float(input("Enter a number:"))

if number < 0:
    number = -number

print(number)
```

In this example, the variable `number` is assigned the value `-number` only if `number < 0`. On the other hand, the command `print(number)` is executed every time because it is not indented, so it does not belong to the block that is executed only when the tested condition is true.

## Nesting conditions

Each Python statement can be placed in any of the blocks, including a different conditional statement. Thus, we obtain nested conditions. Internal condition blocks are indented with more spaces (e.g., 8 spaces). Let's see an example. Given the coordinates of a point on the plane, print a quarter of it:

```python
x = float(input("Enter x coordinate:"))
y = float(input("Enter y coordinate:"))

if x > 0:
    if y > 0:
        # x is greater than 0, y is greater than 0
        print("Quadrant I")
    else:
        # x is greater than 0, y is less than or equal to 0
        print("Quadrant IV")
else:
    if y > 0:
        # x is less than or equal to 0, y is greater than 0
        print("Quadrant II")
    else:
        # x is less than or equal to 0, y is less than or equal to 0
        print("Quadrant III")
```

If we have more than two options to distinguish using the conditional operator, we can use the statement **`if ... elif ... else`** (**`elif`** is short for *else if*):

<pre>
<b>if</b> <i>condition1</i><b>:</b>
    any number of commands
    executed if condition1 is True
<b>elif</b> <i>condition2</i><b>:</b>
    any number of commands
    executed if the condition1 if False and condition2 is True
<b>elif</b> <i>condition3</i><b>:</b>
    any number of commands
    executed if the condition1 and condition2 are False and condition3 is True
<b>else:</b>
    any number of commands
    executed if all conditions are False
</pre>

Let's show how it works by rewriting the example above:

```python
x = float(input("Enter x coordinate:"))
y = float(input("Enter y coordinate:"))

if x > 0 and y > 0:
    print("Quadrant I")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif y > 0:
    print ("Quadrant II")
else:
    print ("Quadrant III")
```

<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
