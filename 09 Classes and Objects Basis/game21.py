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
            print(f"\n{player.name} rolls {dice} and has total score {score}.")
        # We check the condition again, as it might have changed in `player.roll()`
        if player.in_game:
            player.in_game = ask(player)

print()
print(f"{player1.name}'s final score is {player1.score}!")
print(f"{player2.name}'s final score is {player2.score}!")

print()
if player1.score > player2.score:
    print(f"The winner is {player1.name}!")
elif player2.score > player1.score:
    print(f"The winner is {player2.name}!")
else:
    print("There is a tie!")
