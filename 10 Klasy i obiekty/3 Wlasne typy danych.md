---
parent: Klasy i obiekty
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Własne typy danych

Patrząc na **obiekty** i **klasy**, mogliście zauważyć podobieństwo do **zmiennych** i ich **typów**. W rzeczywistości jest to dokładnie to samo. Definiując klasę, tworzycie nowy typ, a instancja klasy jest po prostu zmienną tego typu. Wbudowane typy Pythona są również klasami. Zauważcie, że używaliście już wcześniej ich metod:

```python
name = "python"
print(name.upper())  # `upper()` jest metodą w klasie `str`
```

Możecie zdefiniować dowolny typ. Rozważmy klasę definiującą ułamek zwykły. Powinna ona mieć dwa atrybuty, *licznik* i *mianownik*. Trzymająć się dobrej praktyki nazywania zmiennych, funkcji, klas i metod po angielsku, oznaczmy je w skrócie `numer` (od *numerator*) i `denom` (od *denominator*):

```python
class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
```

Możliwe jest wykonywanie operacji matematycznych na ułamkach, takich jak dodawanie, odejmowanie, mnożenie i dzielenie. Zdefiniujmy funkcję `mul` (*multiplication* — mnożenie), która pobiera dwa ułamki, mnoży je i zwraca nowy obiekt  `Fraction`, która jest ich iloczynem:

```python
def mul(a, b):
    return Fraction(a.numer * b.numer, a.denom * b.denom)
```

Właściwie ta funkcja jest specyficzna tylko dla ułamków. Tak więc, aby zachować spójność, lepiej jest uczynić ją metodą w ułamku:

```python
class Fraction:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def mul(self, other):
        return Fraction(self.numer * self.numer, self.denom * self.denom)
```

Możemy użyć tej metody w następujący sposób:

```python
x = Fraction(1, 2)
y = Fraction(5, 6)

z = x.mul(y)
```

Ostatnia linia nie wygląda dobrze. W następnym wykładzie pokażę, co można zrobić, aby móc używać normalnych operatorów matematycznych (w stylu `z = x * y`) we własnych klasach.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
