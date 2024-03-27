---
parent: Klasy i obiekty
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Metody specjalne

## Operacje arytmetyczne

Wróćmy do naszej klasy [`Fraction`](../10%20Klasy%20i%20obiekty/3%20Wlasne%20typy%20danych):

```python
class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def mul(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)
```

Takie sformułowanie pozwala nam mnożyć dwa ułamki w brzydki sposób `c = a.mul(b)`. Byłoby to o wiele bardziej przejrzyste, gdybyśmy mogli napisać `c = a * b`. Dobra wiadomość jest taka, że możemy. Zmieńmy nazwę metody `mul` na `__mul__` (dwa podkreślenia na początku i końcu, jak w `__init__`):

```python
class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)
```

Pozwala nam to na zapisanie:

```python
x = Fraction(1, 2)
y = Fraction(5, 6)

z = x * y
```

Metody z dwoma podkreśleniami na początku i końcu to [*metody specjalne*](https://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie/Metody_specjalne) lub [*magiczne*](https://printpython.pl/python/magiczne-metody-czyli-szczypta-magii-w-pythonie/). Generalnie nigdy nie wywołuje się ich bezpośrednio. Na przykład, nigdy nie wywołujecie jawnie metody `__init__`. Jest ona uruchamiana automatycznie podczas tworzenia instancji. `__mul__` jest kolejną taką metodą i jest wywoływana, gdy dwa obiekty są mnożone.

Istnieje wiele takich metod. Listę wszystkich z nich można znaleźć w [dokumentacji](https://docs.python.org/3/reference/datamodel.html#special-method-names). Oto najbardziej podstawowe z nich używane w arytmetyce:

| Chcecie...         | Więc piszecie... | A funkcja specjalna to... |
| ------------------ | ---------------- | ------------------------- |
| dodawać            | `x + y`          | `x.__add__(y)`            |
| odejmować          | `x - y`          | `x.__sub__(y)`            |
| mnożyć             | `x * y`          | `x.__mul__(y)`            |
| dzielić            | `x / y`          | `x.__truediv__(y)`        |
| resztę z dzielenia | `x % y`          | `x.__mod__(y)`            |
| podnieść do potęgi | `x ** y`         | `x.__pow__(y)`            |

Proszę zaimplementować metody `__add__`, `__sub__` i `__truediv__` dla klasy `Fraction`.


## Ładne drukowanie obiektów

Inne metody specjalne pozwalają na dostęp do „elementów” naszej klasy za pomocą nawiasów kwadratowych (jak w przypadku list lub słowników) ([`__getitem__`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__) oraz [`__setitem__`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__)), uzyskanie „długości” naszej niestandardowej sekwencji ([`__len__`](https://docs.python.org/3/reference/datamodel.html#object.__len__)) itp.

Ważną specjalną metodą, o której powinniście zawsze pamiętać jest `__str__`. Rozważmy następujący kod:

```python
class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

frac = Fraction(1, 2)

print(frac)
```

Wynik jego działania będzie wyglądał mniej więcej tak:

```
<__main__.Fraction object at 0x7f61ad175b80>
```

Nie wygląda to zbyt czytelnie. Na szczęście można poprawić sytuację, używając metody `__str__`, aby przekonwertować klasę na ciąg znaków, który można wydrukować:

```python
class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        # Ta metoda musi ZWRÓCIĆ ciąg znaków. Nie próbujcie niczego drukować!!!
        return f"{self.numer}/{self.denom}"

frac = Fraction(1, 2)

print("Naszym ułamkiem jest:", frac)
```

Tym razem wynik wygląda znacznie lepiej:

```
Naszym ułamkiem jest: 1/2
```

## Porównanie obiektów

Inne bardzo przydatne metody specjalne to porównania. Ułamki mogą być równe (jeśli oba liczniki i mianowniki są równe) lub jeden może być większy od drugiego. Funkcje specjalne wykonujące porównania powinny zawsze zwracać `True` lub `False`. Ich nazwy są następujące:

| Porównanie | Metoda specjalna    |
| ---------- | ------------------- |
| `x < y`    | `x.__lt__(self, y)` |
| `x <= y`   | `x.__le__(self, y)` |
| `x == y`   | `x.__eq__(self, y)` |
| `x != y`   | `x.__ne__(self, y)` |
| `x > y`    | `x.__gt__(self, y)` |
| `x >= y`   | `x.__ge__(self, y)` |



> **Uwaga: skracanie ułamka**
>
> Podczas wykonywania operacji arytmetycznych na ułamkach może powstać ułamek redukowalny, np. 2/3 × 3/5 = 6/15. Oczywiście ułamek ten jest równy 2/5.
>
> Aby Wasza klasa zachowywała się elegancko i aby porównania działały, powinniście zawsze redukować ułamek, dzieląc zarówno licznik, jak i mianownik przez ich [największy wspólny dzielnik](https://pl.wikipedia.org/wiki/Najwi%C4%99kszy_wsp%C3%B3lny_dzielnik), który można znaleźć za pomocą funkcji `gcd` w module `math`. Zastanówcie się, w której metodzie powinniście to zrobić? Jeśli zrobicie to w każdej metodzie specjalnej odpowiedzialnej za operacje matematyczne, będziecie musieli ten sam kod powtórzyć kilka razy. Co więcej, jeśli ktoś utworzy instancję Waszej klasy np. jako `Fraction(4, 6)`, ułamek nie zostanie skrócony. Jeżeli jednak dokonacie skrócenia w konstruktorze, obejmie to wszystkie przypadki użycia:
>
> ```python
> from math import gcd
>
> class Fraction:
>     def __init__(self, numer, denom):
>         r = gcd(numer, denom)
>         self.numer = numer // r      # do dzielenia liczb całkowitych używamy // 
>         self.denom = denom // r
>
>     def __str__(self):
>         return f"{self.numer}/{self.denom}"
>
>     def __mul__(self, other):
>         return Fraction(self.numer * other.numer, self.denom * other.denom)
> ```
>
> W konstruktorze można wykonać więcej czynności porządkujących nasz ułamek, takich jak sprawdzenie, czy mianownik nie jest równy 0 (i zgłoszenie `ValueError` w takim przypadku), upewnienie się, że mianownik jest zawsze dodatni (a znak licznika jest odpowiednio dostosowany) itp.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
