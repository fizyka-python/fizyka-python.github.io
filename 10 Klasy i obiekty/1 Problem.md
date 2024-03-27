---
parent: Klasy i obiekty
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Problem

## Zagrajmy w 21

Wyobraźmy sobie grę w 21. Jej zasady są bardzo proste:

1. Gracz zaczyna z wynikiem 0.
2. Gracz rzuca kostką, aby zwiększyć swój wynik. Liczba na kostce dodaje się do aktualnego wyniku.
3. Po rzucie kośćmi gracz może zakończyć grę z aktualnym wynikiem lub rzucić ponownie.
4. Celem jest zebranie jak największej liczby punktów. Jeśli jednak w dowolnym momencie łączny wynik przekroczy 21 (tj. wyniesie 22 lub więcej), gracz natychmiast przegrywa z wynikiem końcowym 0.

Zagrajcie w tę grę między sobą. Możecie grać na zmianę, zmieniając aktywnego gracza po każdym rzucie, lub najpierw pierwszy gracz rzuca dowolną liczbę razy, a następnie drugi. Można również grać w większą liczbę graczy.

Teraz zaimplementujcie tę grę w Pythonie. Zacznijcie od wersji dla jednego gracza. Musicie śledzić jego aktualny wynik oraz to, czy gracz nadal bierze udział w grze.

Prosta i brzydka implementacja może wyglądać następująco:

```python
import random

final_score = 0
in_game = True

while in_game:
    dice = random.randint(1, 6)
    final_score += dice
    print(f "Rzuciłeś {dice}. Twój aktualny wynik to {final_score}.")
    if final_score > 21:
        final_score = 0
        in_game = False
    else:
        while True:
            answer = input("Czy chcesz kontynuować? [y/n]: ").lower()
            if answer in 'tn':
                break
            print("Musisz odpowiedzieć 't' lub 'n'!")
        if answer == 'n':
            in_game = False

print(f"Twój końcowy wynik to {final_score}!")
```

## Co jest nie tak z tym kodem?

Powyższy kod jest prosty, jednak ma dwa istotne problemy. Jednym z nich jest brak oddzielenia interakcji z użytkownikiem od logiki, tj. śledzenia wyniku, decydowania o tym, kiedy zakończyć itp. Można to jakoś poprawić, organizując części kodu w funkcje:

```python
import random

final_score = 0
in_game = True


def roll():
    global final_score, in_game
    dice = random.randint(1, 6)
    final_score += dice
    score = final_score
    jeśli wynik > 21:
        final_score = 0
        in_game = False
    return dice, score # te zwracane wartości są używane tylko do drukowania wiadomości


def ask():
    while True:
        answer = input("Czy chcesz dalej rzucać? [t/n]: ").lower()
        if answer in 'tn':
            break
        print("Musisz odpowiedzieć 't' lub 'n'!")
    return answer == 't'


while in_game:
    dice, score = roll()
    print(f "Rzuciłeś {kostka}. Twój aktualny wynik to {wynik}.")
    if in_game:
        in_game = ask()

print(f "Twój ostateczny wynik to {final_score}!")
```

Drugi problem... cóż, niech to będzie gra dla dwóch lub trzech osób! Musicie zatem śledzić wyniki z graczy oraz to czy nadal bierze on udział w grze. Zgodzicie się, że nie jest to już takie proste? Jednym z powodów jest użycie zmiennych globalnych, np. w funkcji `roll()`, które są niezbędne do aktualizacji stanu gry pomiędzy jej wywołaniami (nie możemy użyć do tego celu zmiennych lokalnych, ponieważ zostaną one utracone po opuszczeniu funkcji).

 Możecie przechowywać wyniki i stany gry każdego z graczy w listach (jedna dla wyników, druga dla stanów gry, a jeszcze inna dla nazw graczy), jednak nie byłoby to zbyt eleganckie rozwiązanie: będziecie musieli również przekazać numer gracza do funkcji `roll()`. Inną możliwością byłoby przechowywanie danych gracza w słowniku i przekazywanie tego słownika do funkcji `roll()`:

```python
albert = {'name': 'Albert', 'in_game': True, 'final_score': 0}

def roll(player):
    dice = random.randint(1, 6)
    player['final_score'] += dice
    score = player['final_score']
    if score > 21:
        player['final_score'] = 0
        player['in_game'] = False
    return dice, score
```

Wydaje się to lepsze, jednak nadal jest dalekie od elegancji.

**Proszę, nie próbujcie stosować żadnego z tych podejść!** Przeczytajcie uważnie następny rozdział, aby zobaczyć jak rozwiązać opisany tu problem we właściwy sposób.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
