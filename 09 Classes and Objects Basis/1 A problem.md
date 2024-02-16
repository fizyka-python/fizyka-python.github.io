---
parent: "Classes and Objects: Basis"
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# A Problem

## Let's play 21

Imagine a game of 21. Its rules are very simple:

1. A player starts with score 0.
2. He/she rolls a dice to increase the score. The number on the dice adds to the current score.
3. After rolling the dice, the player may decide to end the game with the current score or roll again.
4. The goal is to collect as high score as possible. However, if in any moment the total score exceeds 21 (i.e. becomes 22 or higher), the player immediately loses with the final score 0.

Play this game with your friend. You can play in turns, changing active player after each roll, or first the first player rolls as many times as wishes, then the other one. You may also play with a larger number of players.

Now implement this game in Python. Start with a version for a single player. You need to keep track of the player's current score. It is also beneficial to track whether a player is still in a game.

A simple and ugly program may look like this:

```python
import random

final_score = 0
in_game = True

while in_game:
    dice = random.randint(1, 6)
    final_score += dice
    print(f"You roll {dice}. Your current score is {final_score}.")
    if final_score > 21:
        final_score = 0
        in_game = False
    else:
        while True:
            answer = input("Do you want to keep rolling? [y/n]: ").lower()
            if answer in 'yn':
                break
            print("You must answer 'y' or 'n'!")
        if answer == 'n':
            in_game = False

print(f"Your final score is {final_score}!")
```

## What is wrong with this code?

The above code is simple. However, it has two significant problems. One is the lack of separation of the user interaction and logic i.e. keeping track of your score, deciding when to finish etc. (remember [Kitchen and Dining Room](../00%20Algorithms/3%20Frontend-backend)). You may somehow improve it by organizing parts of your code into functions:

```python
import random

final_score = 0
in_game = True


def roll():
    global final_score, in_game
    dice = random.randint(1, 6)
    final_score += dice
    score = final_score
    if score > 21:
        final_score = 0
        in_game = False
    return dice, score  # this return values are used only for printing messages


def ask():
    while True:
        answer = input("Do you want to keep rolling? [y/n]: ").lower()
        if answer in 'yn':
            break
        print("You must answer 'y' or 'n'!")
    return answer == 'y'


while in_game:
    dice, score = roll()
    print(f"You roll {dice}. Your current score is {score}.")
    if in_game:
        in_game = ask()

print(f"Your final score is {final_score}!")
```

The other problem... well make it a game for two or three! You need to track the score of each player and whether a particular player is still in a game. Seems not easy, doesn't it? One reason is using global variables e.g. in the `roll()` function, which are necessary to update the game state between its calls (we cannot use local variables for this purpose, as they will be lost once we leave the function).

 You may keep a score and playing state of each player in lists (one for scores, second for playing states, and yet another for player names), however, it would not be very elegant solution: you will also have to pass the player number to the `roll()` function. Another possibility would be to store player data in a dictionary and pass it to the roll function:

```python
alfred = {'name': 'Alfred', 'in_game': True, 'final_score': 0}

def roll(player):
    dice = random.randint(1, 6)
    player['final_score'] += dice
    score = player['final_score']
    if score > 21:
        player['final_score'] = 0
        player['in_game'] = False
    return dice, score
```

This seems better, however, it is still far from elegant.

**Please don't try any of these approaches!** Read the next chapter, to see how to solve the problem the right way.

<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
