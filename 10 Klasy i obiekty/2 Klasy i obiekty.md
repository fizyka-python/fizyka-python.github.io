---
parent: Klasy i obiekty
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Klasy i obiekty

Problem opisany w poprzednim rozdziale można podsumować w następujący sposób: jak połączyć wszystkie zmienne opisujące stan każdego gracza i jak na nich operować. Python ma na to zgrabne rozwiązanie wykorzystujące koncepcję klas i obiektów. Klasy są ogólnymi koncepcjami bytu, jego stanu i tego, co może zrobić (w naszym przypadku będzie to **gracz**), podczas gdy obiekty są konkretnymi instancjami tych koncepcji (**gracze**: *Albert*, *Beata*, *Czesław*).

Najlepiej zilustrować to na przykładzie. W Pythonie definiujemy klasę używając słowa kluczowego **`class`**:

```python
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
            in_game = False
        return dice, score
```

To, co widzicie powyżej, to deklaracja klasy o nazwie `Player` (zazwyczaj nazwy klas powinny zaczynać się od wielkiej litery). Zawiera ona dwie funkcje zdefiniowane **wewnątrz klasy** (we wciętym bloku). Takie funkcje w klasie nazywane są *metodami* — od teraz będę używał tego terminu. Metody w klasie przyjmują jeden dodatkowy argument zwany `self`, który musi być zawsze pierwszym argumentem. Argument ten reprezentuje konkretną instancję (obiekt), na której operujemy. Możemy go używać do ustawiania i odczytywania *atrybutów* obiektu, używając notacji `self.attribute_name`. W przeciwieństwie do zmiennych lokalnych, atrybuty są współdzielone między wywołaniami metod i mogą być również dostępne z zewnątrz. Z drugiej strony, w przeciwieństwie do zmiennych globalnych, mogą one być różne dla różnych obiektów (tj. śledzimy np. wynik gracza w atrybucie `score` osobno dla *Alberta* i osobno dla *Beaty*).

W klasie jest też zdefiniowana metoda o nazwie `__init__`. Jest to specjalna nazwa metody, używana do inicjalizacji obiektów — będzie ona wywoływana automatycznie. Ustawiamy w niej nazwę gracza na wartość podaną jako argument `name` (jest to coś innego niż atrybut `self.name`) i inicjalizujemy wynik (`self.score`) oraz status gry (`self.in_game`).

Aby utworzyć konkretne instancje klasy, wywołujemy ją jak funkcję:

```python
player1 = Player("Albert")
player2 = Player("Beata")
```

W nawiasie umieszczamy argumenty, które muszą zostać przekazane do metody `__init__`, **pomijając pierwszy argument `self`**.

Inne metody są wywoływane przy użyciu notacji, z którą już się spotkaliście: `object.method(arguments_without_self)`:

```python
player1.roll()
player2.roll()
```

Przy tworzeniu obiektów i wywoływaniu metod, wszystkie normalne zasady przekazywania argumentów przez nazwę lub używania domyślnych argumentów są takie same jak w przypadku zwykłych funkcji. Jedyną różnicą, o której należy pamiętać, jest pominięcie pierwszego argumentu `self`. Argument ten jest przekazywany automatycznie i zawiera obiekt przed kropką (lub nowo utworzony w przypadku `__init__`).

Używając adnotacji z kropką, można uzyskać dostęp nie tylko do metod, ale także do atrybutów obiektu:

```python
print(player1.score)
```

## Gra dla dwóch graczy

Używając klas i obiektów można teraz bardzo łatwo napisać grę dla dwóch graczy:

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
        score = self.score
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
```

Możecie pobrać kod gry [stąd](game21.py). Czy potraficie zmodyfikować ją tak, aby umożliwić dowolną liczbę graczy?

## Wnioski

W tym wykładzie omówiono tworzenie klas, tworzenie instancji obiektów, inicjowanie atrybutów za pomocą metody konstruktora i pracę z więcej niż jednym obiektem tej samej klasy.

Programowanie obiektowe jest bardzo ważnym konceptem, ponieważ umożliwia łatwy recycling (ponowne wykorzystanie) kodu. Wynika to stąd, że obiekty utworzone w jednym programie mogą być używane w innym. Programy zorientowane obiektowo umożliwiają również lepsze projektowanie aplikacji, gdyż wymagają starannego planowania, a to z kolei sprawia, że utrzymanie kodu w czasie jego cyklu życia jest mniej pracochłonne.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
