---
parent: Flow Control
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# While loops

To be useful any programming language must allow you to repeat a portion of a program more than once. These types of repetitions are called loops. There are two kinds of loops in Python. Below, we will discuss the first of them: the **while** loop. It is used to repeat a given block as long as a certain condition is met. This loop looks like this:

<pre>
<b>while</b> <i>condition</i><b>:</b>
    block of statements executed
    as long as the condition
    is True
</pre>

Please note the colon after the condition and the block indentation — the same rules for defining blocks apply as for the **if** statement. Sample code:

```python
number = 0
while number < 1 or number > 10:
     number = int(input("Enter an integer from 1 to 10:"))
print("Your number is", number)
```

In the above example, the user will be prompted to enter a `number` as long as the value of the variable number to which the value is assigned is either less than 1 or greater than 10.

<u>The condition in the <b>while</b> loop is checked at the very beginning, before the loop is executed for the first time.</u> This means that the loop may not be executed even once if the condition is not met at the very beginning. Please note the first line of the example above `number = 0`. It defines a variable `number` and sets its value to zero, which guarantees that the first time it checks, the **while** loop will be true (0 < 1) i.e. the user will be prompted for a number at least once.

## Breaking the loop

The standard termination of the while loop occurs when the condition has a value False. When set to value True, the entire loop block is executed. This is not always what you want. Therefore, it is possible to interrupt execution of a loop inside its block with an instruction break. Let's see an example of a primitive version of the 21 game:

```python
sum = 0 
given_number = int(input("Enter a number: ")) 
while given_number != 0:
    sum += given_number   # this entry is a shortened version of the assignment sum + = sum + given_number
    if sum > 21:
        print("You have exceeded 21 and you lost! ")
        sum = 0
        break
    given_number = int(input("Enter a number (0 to end): ")) 
print("Your score is", sum)
```

Normal loop break occurs when the user enters the number 0 (the condition will not be fulfilled then `given_number != 0`). However, when the calculated sum exceeds 21, the loop is stopped abnormally using the break command. In both cases, the program will continue from the first command outside the loop block (`print("Your score is", sum)`).

After a completed loop block, it is possible to add a command **`else`** followed by a block, which will only be executed if the loop ended normally (that is, not via a command **`break`**). Using this, you can write the above example in a slightly more elegant way:

```python
sum = 0
given_number = int(input("Enter a number: "))
while given_number != 0:
    sum += given_number
    if sum > 21:
        print("You've exceeded 21 and lost!")
        break
    given_number = int(input("Enter number (0 to finish): ")) 
else:
    print("You won! Your score is", sum)
```

The last line will only be printed when the loop ends with a zero, not by exceeding 21.

## Continuation of the loop

Another statement that is used to control loop execution is **`continue`**. If the Python interpreter hits **`continue`** somewhere in the middle of a loop iteration, it skips all remaining statements and proceeds to the next iteration. Example:

```python
i = -11
while i < 10:
    i += 1
    if i == 0:
        continue
    print(1 / i)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
