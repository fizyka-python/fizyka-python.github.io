---
parent: "Classes and Objects: Basis"
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Classes and objects

The problem described in the previous chapter can be summarized as follows: how to combine together all the variables describing each player's state and how to operate on them. Python has neat solution for this using a concept of classes and objects. Classes are general concepts of an entity, its state and what it can do (in our case this will be **a** player), while objects are specific instances of these concepts (**the** players: *Alfred*, *Beatrice*, *Charlie*).

It is best illustrated in example. In Python you define a class using **`class`** keyword:

```python
class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.in_game = True

    def roll(self):
        dice = random.randint(1, 6)
        self.score += dice
        score = self.score  # `score` and `self.score` are DIFFERENT THINGS
        if score > 21:
            self.score = 0
            in_game = False
        return dice, score
```

What you see above is a declaration of a class named `Player` (usually class names should start with a CapitalLetter), are two functions defined **inside a class** (in an indented block). Such functions in a class are called *methods*: I will use this term from now on. Methods in a class take one additional argument called `self`, which must be always the first argument. This argument represents a particular instance (object) we are operating on. We can use it to set and read object *attributes*, using `self.attribute_name` notation. Contrary to the local variables, the attributes are shared between the calls of the methods and may also be accessed from outside. On the other hand, unlike global variables, they can be different for different objects (i.e. we track e.g. `score` separately for *Alfred* and separately for *Beatrice*).

I guess, you understand the role of the `roll` method. `__init__` is the special method name, used for initialization of objects (it will be called automatically). Here, we set the player's name to the value provided as argument `name` (this a different thing than the attribute `self.name`) and initialize the score (`self.score`) and playing status (`self.in_game`).

To create particular instances of a class, we call it like a function:

```python
player1 = Player("Alfred")
player2 = Player("Beatrice")
```

In the parenthesis we put the arguments that must be passed to the `__init__` method, **skipping the first argument `self`**.

Other methods are called using notation, you have already seen: `object.method(arguments_without_self)`:

```python
player1.roll()
player2.roll()
```

For creating objects and calling methods, all the normal rules of passing arguments by name or using default arguments are the same as for normal functions. The only difference you must remember is to skip the first `self` argument. This argument is passed automatically and contains the object before the dot (or a newly created one in case of `__init__`).

You use the dot-notation, you may access not only methods, but also object attributes:

```python
print(player1.score)
```

## Two-player game

Using classes and objects it is now very easy to write a two-player game:

```python
import random


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.in_game = True

    def roll(self):
        dice = random.randint(1, 6)
        self.score += dice
        score = self.score  # `score` and `self.score` are DIFFERENT THINGS
        if score > 21:
            self.score = 0
            self.in_game = False
        return dice, score


def ask(player):
    # This function is part of the input-output,
    # so it should not be in the `Player` class
    while True:
        answer = input(f"{player.name}, do you want to keep rolling? [y/n]: ").lower()
        if answer in 'yn':
            break
        print("You must answer 'y' or 'n'!")
    return answer == 'y'


player1 = Player(input("Enter first player's name: "))
player2 = Player(input("Enter second player's name: "))

while player1.in_game or player2.in_game:
    for player in (player1, player2):
        if player.in_game:
            dice, score = player.roll()
            print(f"{player.name} roll {dice} and has total score {score}.")
        # We check the condition again, as it might have changed in `player.roll()`
        if player.in_game:
            player.in_game = ask(player)

print(f"{player1.name}'s final score is {player1.score}!")
print(f"{player2.name}'s final score is {player2.score}!")
```

You may download the game code [from here](game21.py). Can you write this game to allow any number of players?

## Conclusions

This tutorial went through creating classes, instantiating objects, initializing attributes with the constructor method, and working with more than one object of the same class.

Object-oriented programming is an important concept to understand because it makes code recycling more straightforward, as objects created for one program can be used in another. Object-oriented programs also make for better program design since complex programs are difficult to write and require careful planning, and this in turn makes it less work to maintain the program over time.


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
