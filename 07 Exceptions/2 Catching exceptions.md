---
parent: Exceptions
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Catching exceptions

Not all exceptional situations can be avoided during writing the program. For example, consider the following function:

```python
def input_float(prompt):
    return float(input(prompt))
```
The purpose of this function is to read the actual number from the keyboard. However, we don't know what the user will enter. If it gives a string that cannot be converted to a real number, the program will be aborted. This is not correct behavior. In this situation, the correct program should inform the user that the entered text is incorrect and, for example, ask him to enter it again.

In order to be able to program the program behavior in exceptional situations, the following structure is used:

```python
try:
     a block of commands that can cause an exception
except ExceptionType:
     a block of commands performed on exceptions
except DifferentExceptionType:
     a block of commands executed in the case of another type of exception
```
If **`try`** is used, there must be at least one **`except`** block.

Using this, a function that asks user to input a number could look like this:

```python
def input_float(prompt):
    try:
        return float(input(prompt)
    except ValueError:
         print ("Invalid number. I return 0.")
         return 0.
```
This function calls the function `input` that asks for a string. Then that string is converted to type `float`. The conversion result is returned as the function result. If any of these steps fails, an exception will be thrown. If it is an exception of the type `ValueError` (in this case it may appear due to a failed conversion), it will be *caught* and an appropriate message will be printed and the function will return the value 0.

Exceptions do not have to be caught in the same function as they appeared. Consider the following program:

```python
def input_float(prompt):
    return float(input(prompt))

def ask_number():
    return input_float("Enter a number:")

try:
    number = ask_number()
    result = 10 + number
except ValueError:
     result = 0.

print (number)
```
If an incorrect value is entered, the function `input_float` will be aborted immediately. The function `ask_number` will also be interrupted. However, the entire program will not fail, since the exception is caught in the main code that calls the function `ask_number`.

The  **`try... except`** construct may additionally have an **`else`** block  that is called when no exception occurs. E.g:

```python
try:
    number = ask_number()
    result = 10 + number
 except ValueError:
     result = 0.
 else:
    print("Thank you")
```
The *Thank you* message  will only be printed if the correct real number has been entered.

Only exceptions of the given type are caught by the **`except`** command . Other exceptions are ignored by it and will either cause the program to stop or be caught elsewhere. Consider the following code:

```python
def input_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
         print ("Invalid number. Returning 0.")
        return 0.

try:
    number = input_float("Enter a number:")
except KeyboardInterrupt:
    number = -1
```
If the `ValueError` exception occurs  in the function `input_float`, it prints a message and returns the value 0. However, pressing `Ctrl + C` or `Ctrl + Delete` will generate an exception `KeyboardInterrupt` that will break the function. However, it will be caught at the point where this function was called, and the variable `number` will be set to –1.

## Better to ask for forgiveness than permission

In Python, exceptions are normal and should be used. Let's look at a function that returns the inverse of the number given as its argument:

```python
def inverse(x):
    return 1 / x
```

Suppose we want to protect ourselves in case the given argument is 0 and we want to return the value 0 in this case (which of course is mathematically incorrect, but may be useful in some situations). We can do this in two ways:

```python
def inverse (x):
    if x == 0:
        return 0
    else :
        return 1 / x
```
or

```python
def inverse (x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 0
```

In the first case, "we ask for permission", i.e. we use a condition to check whether the operation can be performed. In the second, we "beg for forgiveness", that is, we simply perform the operation, and in case of problems, we solve them. Generally the second way is better. In case of more complex programs, it results in more readable code and it is easier to add handling of other exceptions, which we are not able to predict at the time of writing the original version of the program. In addition, we are not able to check everything in advance, and even if it is possible, it may be unreliable: this applies in particular to file operations, which will be discussed in the next lecture. For example, if we first check if a given file exists and then open it, there is a non-zero probability that within microseconds between checking the existence of the file and opening it, it will be deleted (the probability is not so small if, for example, the computer's disk is damaged). In such a situation, we will receive permission to perform the operation (the condition will confirm the existence of the file), but the operation itself will fail. By using exception catching, we protect ourselves against such a situation. Another reason why "begging for forgiveness" is better is the performance of the program: when checking the condition first, we need to perform some operations that are likely to be repeated afterwards. When we use exceptions, we only perform a given operation once. The difference may be a few microseconds but it becomes noticeable when a given function is repeated several dozen million times (which is not unusual in larger programs for data analysis or scientific calculations).

## How to clean up a mess?

The instruction **`try`** has one more, optional clause, which is used to define actions to perform the necessary cleanups in all respects. E.g:

```python
try:
    number = float('two')   # this will cause an exception ValueError
finally:
    print('Goodbye, world!')
```
The clause **`finally`** is executed whether or not an exception occurs. The code in this block is also executed when the try block is "exited" with the `break` or `return` statements.

The **`try`** statement must have at least one **`except`**  block or one **`finally`** block.


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
