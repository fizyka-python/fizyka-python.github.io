import random


class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.in_game = True

    def roll(self):
        dice = random.randint(1, 6)
        self.score += dice
        score = self.score  # `score` oraz `self.score` to ZUPEŁNIE RÓŻNE ZMIENNE
        if score > 21:
            self.score = 0
            self.in_game = False
        return dice, score


def ask(player):
    # Ta funkcja jest częścią wejścia-wyjścia,
    # więc nie powinna być w klasie `Player`
    while True:
        answer = input(f"{player.name}, czy chcesz kontynuować? [t/n]: ").lower()
        if answer in 'tn':
            break
        print("You must answer 't' or 'n'!")
    return answer == 't'


player1 = Player(input("Wprowadź imię pierwszego gracza: "))
player2 = Player(input("Wprowadź imię drugiego gracza: "))

while player1.in_game or player2.in_game:
    for player in (player1, player2):
        if player.in_game:
            dice, score = player.roll()
            print(f"\n{player.name} rzuca {dice}. Całkowity wynik wynosi {score}.")
        # Sprawdzamy warunek ponownie, ponieważ mógł on ulec zmianie w `player.roll()`
        if player.in_game:
            player.in_game = ask(player)

print()
print(f"{player1.name} — wynik ostateczny: {player1.score}!")
print(f"{player2.name} — wynik ostateczny: {player2.score}!")

print()
if player1.score > player2.score:
    print(f"Zwycięża {player1.name}!")
elif player2.score > player1.score:
    print(f"Zwycięża {player2.name}!")
else:
    print("Remis!")
