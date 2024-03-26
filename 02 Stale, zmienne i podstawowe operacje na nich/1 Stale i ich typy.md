---
parent: Stałe, zmienne i podstawowe operacje na nich
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Stałe i ich typy

## Stałe

Stałe wartości, takie jak cyfry, litery i ciągi znaków (stringi), nazywane są „stałymi”, ponieważ ich wartość się nie zmienia. W Pythonie stałe mogą być następujących typów:

### Typy liczbowe

* liczby całkowite: `1`, `100`;
* liczby całkowite w zapisane systemach niedziesiątkowych, zaczynające się prefiksem `0b` (zapis dwójkowy), `0x` (zapis szestnastkowy), `0o` (zapis ósemkowy): `0b101` (5), `0x1a` (26), `0o12` (10);
* liczby rzeczywiste (część dziesiętna oddzielona jest kropką — brak cyfr przed lub po kropce oznacza 0): `2.27`, `3.14`, `-1.2`, `1.0`, `2.` (2.0), `.5` (0.5);
* liczby rzeczywiste zapisane w notacji wykładniczej (o podstawie 10) <em style="color: #0000ff;">mantysa</em>e<em style="color: #ff00ff;">wykładnik</em>, oznaczające <em style="color: #0000ff;">mantysa</em> × 10<sup><em style="color: #ff00ff;">wykładnik</em></sup>: `-5e3` (-5000), `2.5e-2` (0.025);
* liczby zespolone, w których obie składowe zapisujemy jak liczby rzeczywiste, a część urojoną oznaczmy dopisując na końcu znak `j`: `1.5-0.2j`, `-2+1e-1j` (-2+0.1j);

### Typy tekstowe

Ciągi znaków umieszczone pomiędzy jednym z następujących zestawów cudzysłowów:

* pojedynczy cudzysłów: `'...'`,
* podwójny cudzysłów: `"..."`,
* pojedynczy lub podwójny cudzysłów powtórzony trzykrotnie: `'''...'''`, lub `"""..."""`.

W ostatnim przypadku tekst może rozciągać się na kilka linijek. W dwóch pierwszych jest to niedozwolone, jednakże znaki nowej linii można wstawiać używając symbolu specjalnego \\n.

Do oznaczenia łańcuchów tekstowych można wykorzystać dowolny zestaw powyższych symboli, ale bardzo ważne jest aby każdy łańcuch zaczynał się tak samo jak kończył. Poprawne przykłady to (kolor czerwony oznacza początkowy i końcowy cudzysłów):

```python
"Ala ma kota"  
  
'Nazwa tego rozdziału to "Stałe"'  
  
"""Pierwsza linijka  
Druga linijka"""  
  
"To też są\ndwie linijki"
```

### Krotki

Krotki (ang. _tuples_) są uporządkowanym stałym zbiorem wartości. Kolejne wartości oddziela się od siebie przecinkami, zaś całość powinna być zawarta w nawiasach. Więcej o zastosowaniu krotek znajduje się dalej. Przykładowe krotki to:

```python

(1, 2, 5)  
  
(2.5, 3, 1j, 'tekst')  # elementy krotek nie muszą być tego samego typu  
  
("tekst", (1, 2))      # krotki mogą zawierać inne krotki (i inne typy, o których jeszcze nie wspomnieliśmy)  
  
(1,)                   # krotka jednoelementowa musi mieć dodatkowy przecinek (aby odróżnić ją od liczby w nawiasie)  
  
()                     # pusta krotka
```

Więcej o zastosowaniu krotek i sposobach wydobycia ich poszczególnych elementów będzie dalej w tym wykładzie.

## Operacje na wartościach

Na obsługiwanych przez Pythona wartościach można wykonywać działania za pomocą operatorów matematycznych. Podstawowymi operatorami są `+`, `\-`, `*` (mnożenie), `/` (dzielenie), `**` (potęgowanie), `//` (dzielenie całkowite), `%` (reszta z dzielenia). Python potrafi wykonywać działania zgodnie z obowiązującymi regułami matematycznymi (dozwolone jest stosowanie nawiasów okrągłych). Aby się z nimi zapoznać, proszę uruchomić notatnik Jupytera i wpisać w nim w oddzielnych komórkach następujące wyrażenia (nie jest konieczne stosowanie funkcji print — Jupyter samoczynnie wypisze wynik obliczonego wyrażenia):

```python
1 + 2  
  
2 + 2 * 2  
  
(2 * (1 + 1))**2  
  
2.5 * 2  
  
7.5 / 3  
  
5 / 2  
  
4 / 2  
  
8 // 3  
  
8 % 3  
  
2**10  
  
8**(1/3)  
  
(-1)**0.5  
  
'1' + '2'  
  
(1, 2) + (3,)   # proszę zwrócić uwagę na przecinek w (3,)  
  
3 * "a"  
  
(1, 2) * 2
```

Proponuję także samodzielnie popróbować wykorzystanie tej interaktywnej powłoki Pythona jako kalkulatora.

Kilka powyższych przykładów wymaga szczegółowego omówienia. Operator dzielenia (`/`) zastosowany dla liczb rzeczywistych lub całkowitych zawsze zwróci wynik rzeczywisty (nawet jeśli wynikiem jest liczba całkowita). Z kolei operator dzielenia całkowitego (`//`) usunie część ułamkową — z tego powodu w zastosowaniach inżynierskich i naukowych ma on ograniczone zastosowanie.

Operator potęgowania (`**`) potrafi podnosić także do potęgi niecałkowitej. W związku z tym `(-1)**0.5` zostało potraktowane jako pierwiastek główny z –1, czyli jednostka urojona. Została ona wypisana jako `(0+1j)`, lub coś w stylu `(6.123233995736766e-17+1j)`. Nie należy się tym przerażać — zgodnie z opisaną wcześniej notacją wykładniczą, część rzeczywista tej liczby jest rzędu 10<sup>-17</sup>, czyli praktycznie 0. Zmiennoprzecinkowe obliczenia komputerowe nie są 100% dokładne, stąd taki a nie inny wynik (dokładność obliczeń jest osobnym zagadnieniem, na które trzeba zwracać uwagę pisząc programy obliczeniowe, jednak na obecnym etapie nie będziemy się nim zajmować).

Dobrym zwyczajem jest pisanie znaków spacji dookoła operatorów matematycznych, gdyż znacznie zwiększa to czytelność kodu (oczywiście nie jest to wymóg formalny, ale nagminne pomijanie spacji powoduje, że bardzo ciężko analizuje się program, szczególnie gdy jest on napisany przez kogoś innego).

Python potrafi wykonywać działania także na typach nieliczbowych o ile mają one sens. Dodawanie do siebie łańcuchów tekstowych lub krotek powoduje ich połączenie, zaś pomnożenie przez liczbę całkowitą — powtórzenie ich zawartości daną ilość razy.

W przypadku działań, które nie mają sensu, Python zgłosi błąd. Proszę spróbować wykonać w konsoli następujące działania i za każdym razem przeczytać i postarać się zrozumieć komunikat błędu:

```python
1 / 0  
  
1 + "2"  
  
2.5 * (1, 2)  
  
"Alala" - "la"  
  
50.0 ** 1000000
```

Ostatnie działanie jest matematycznie i logicznie poprawne, jednakże jego wynikiem jest zbyt duża liczba, której nie da się poprawnie zapisać w pamięci komputera jako liczby rzeczywistej.

## Konwersja typów

Wszystkie opisane powyżej stałe konkretnego typu (a także inne, nieprzedstawione jeszcze typy) mają swoje nazwy. Dla opisanych już typów są one następujące:

* liczby całkowite: `int`
* liczby rzeczywiste: `float`
* liczby zespolone: `complex`
* łańcuchy tekstowe: `str`
* krotki: `tuple`

Dla dowolnej wartości można sprawdzić jej typ za pomocą funkcji `type`, np:

```python
type(2)  
  
type(2.5)  
  
type(2j)  
  
type("2")  
  
type(1 + 2)  
  
type(1 + 2.0)
```

Jak to można było zaobserwować powyżej, Python potrafi samodzielnie konwertować typy liczbowe tak, aby wynik danego działania miał sens. Jednakże możliwe jest ręczne wymuszenie konwersji typów, poprzez bezpośrednie użycie ich nazw jako funkcji. Jest to szczególnie użyteczne gdy chcemy zamienić łańcuch znaków na liczbę. Np.:

```python
float("2.5")
```

Proszę zobaczyć jaka jest różnica pomiędzy:

```python
"1" + "2"
```
oraz

```python
int("1") + int("2")
```
a także

```python
str(1) + str(2)
```

Jeżeli konwersja nie ma sensu, Python zgłosi błąd. Proszę spróbować

```python
int(10+2j)  
  
float("dwa")  
  
float("two and half")  
  
int("one")  
  
int("4O")         # czy ktoś jest w stanie zauważyć jaki tu występuje problem?
```

Wyjątkiem jest konwersja liczby rzeczywistej na całkowitą. Wyrażenie

```python
int(2.7)
```

spowoduje jedynie odrzucenie części ułamkowej.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
