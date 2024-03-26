---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  7
---

# Operacje na łańcuchach znaków

Łańcuchy znaków są specjalnymi rodzajami sekwencji przeznaczonymi do przechowywania napisów. W związku z tym posiadają szereg metod, które pozwalają wykonywać przydatne operacje na tych napisach. Ich szczegółowy opis znajduje się w [dokumentacji Pythona](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str). Poniżej przedstawione jest omówienie kilku najbardziej przydatnych operacji i metod dla łańcuchów tekstowych:

## Znajdowanie pod-łańcuchów

W odróżnieniu o innych sekwencji, operatory **`in`** oraz **`not in`** działają nie tylko dla pojedynczych liter, ale dla pod-łańcuchów tekstowych. Np. `'ruz' in 'karuzela'` zwróci wartość `True`.

Jeżeli potrzebna jest znajomość pozycji jakiego fragmentu, metoda `find` znajduje pozycję w jakiej znajduje się dany podciąg, lub `-1`, jeżeli podciąg ten nie występuje w łańcuchu:

```python
'karuzela'.find('ruz')    # 2

'karuzela'.find('ruza')   # -1
```

## Usuwanie białych znaków

Metody `lstrip`, `rsrip` oraz `strip` usuwają białe znaki (spacje, znaki nowej linii, tabulatory) odpowiednio na początku, na końcu oraz na początku i na końcu napisu. Jest to bardzo przydatne, np. gdy chcemy podzielić tekst na fragmenty oddzielone znakami interpunkcyjnymi (po których zazwyczaj znajdują się spacje). Proszę wykonać w konsoli następujące przykłady:

```python
wyrazy = "raz, dwa, trzy"

wyrazy.split(',')                               # ['raz', ' dwa', ' trzy']

[wyraz.strip() for wyraz in wyrazy.split(',')]  # ['raz', 'dwa', 'trzy']
```

Aby zobaczyć jaka jest jest różnica pomiędzy `lstrip`, `rsrip` oraz `strip`, proszę wykonać w konsoli:

```python
tekst = "   AAA   "

tekst.lstrip()

tekst.rstrip()

tekst.strip()
```

## Zamiana wielkości liter

W dowolnym tekście można zmienić wszystkie litery na małe za pomocą metody `lower`, albo na wielkie za pomocą metody `upper`:

```python
tekst = "Alicja w Krainie Czarów"

print(tekst.lower())  # alicja w krainie czarów

print(tekst.upper())  # ALICJA W KRAINIE CZARÓW
```

Jest to szczególnie użyteczne w sytuacji gdy chcemy porównać dwa napisy bez uwzględniania wielkości liter:

```python
'AAA' == 'aaa'                  # False

'AAA'.lower() == 'Aaa'.lower()  # True
```

Bardziej wyrafinowaną metodą do zmiany wielkości liter są:

`capitalize` — zamienia pierwszą literę w całym tekście na wielką, wszystkie pozostałe na małe:

```python
"ala ma kota".capitalize()  # 'Ala ma kota'
```

`title` — zamienia pierwszą literę każdego wyrazu na wielką:

```
"ala ma kota".title()       # 'Ala Ma Kota'
```

## Formatowanie napisów

Python umożliwia konstruowanie napisów z wykorzystaniem wartości przechowywanych w innych zmiennych. Istnieją trzy realizacji tego — za pomocą operatora `%` (jest to metoda przestarzała i nie zaleca się jej stosowania), za pomocą metody `format` oraz za pomocą specjalnych _łańcuchów formatujących_. Ta ostatnia metoda jest najprostsza do zastosowania, jednakże wymaga ona Pythona w wersji przynajmniej 3.6. Ponieważ obecnie dostępna jest już nowsza wersja, ta właśnie metoda zostanie omówiona:

_Łańcuchy formatujące_ to specjalne łańcuchy tekstowe, które tworzy się dodając znak `f` bezpośrednio przed cudzysłowem (pojedynczym lub podwójnym) otwierającym łańcuch (nie wolno pomiędzy nie wstawiać spacji). W takim łańcuchu nawias klamrowy nabiera specjalnego znaczenia — wewnątrz niego można umieścić dowolne wyrażenie Pythona, którego wartość zostanie wstawiona do łańcucha. Na przykład:

```python
wzrost = float(input("Podaj swój wzrost [cm]: ")) / 100   # przeliczamy podany wzrost na metry
masa = float(input("Podaj swoją wagę [kg]: "))

bmi = masa / wzrost**2    # https://pl.wikipedia.org/wiki/Wskaźnik_masy_ciała

komunikat = f"Wzrost: {100 * wzrost}cm, waga: {masa}kg, BMI: {bmi}"

print(komunikat)
```

Proszę uruchomić powyższy przykład i zobaczyć jaki komunikat zostanie wyświetlony. Następnie proszę spróbować usunąć znak `f` sprzed cudzysłowu i zobaczyć różnicę.

W powyższym przykładzie wyświetlony komunikat będzie miał postać:

```python
Wzrost: 172.0cm, waga: 64.0kg, BMI: 21.63331530557058

```

Proszę zwrócić uwagę, że wartość BMI wydrukowana jest w sposób nieczytelny — ze zbyt dużą ilością cyfr. Można temu zaradzić. Wewnątrz klamry, w której znajduje się wyrażenie Pythona możemy (po wyrażeniu) dodać znak **`:`** a następnie informację, w jaki sposób wartość tego wyrażenia ma zostać sformatowana. Proszę zmienić linijkę tworzącą łańcuch z komunikatem na następującą

```python
komunikat = f"Wzrost: {100 * wzrost}cm, waga: {masa}kg, BMI: {bmi:.2f}"
```

Występujące po dwukropku `.2f` oznacza, że wartość wyrażenia (w tym przypadku zmiennej `bmi`) ma być przedstawiona jako liczba rzeczywista ( `f` od _float_) z dwoma miejscami po przecinku ( `.2`). Poniżej znajduje się zestawienie kilku przydatnych opisów formatu, które mogą występować po dwukropku ( _X_ i _Y_ w tabeli powinny zostać zastąpione liczbami całkowitymi):

| Format  | Opis                                                                                                                                        |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `.Yf`   | liczba rzeczywista z _`Y`_ cyframi po kropce dziesiętnej (wartość musi być typu `float`)                                                    |
| `Xf`    | liczba rzeczywista zawierająca co najmniej _`X`_ znaków, w razie potrzeby spacje zostaną dodane na początku (wartość musi być typu `float`) |
| `X.Yf`  | liczba zajmująca co najmniej _`X`_ znaków z _`Y`_ miejscami po kropce dziesiętnej (wartość musi być typu `float`)                           |
| `0Xf`   | liczba rzeczywista obejmująca co najmniej _`X`_ znaków, w razie potrzeby na początku zostaną dodane zera (wartość musi być typu `float`)    |
| `0X.Yf` | jak `X.Yf`, ale puste miejsca zostaną wypełnione zerami                                                                                     |
| `+XXf`  | gdzie _`XX`_ jest jedną z _`X`_, _`X.Y`_, _`0X`_, _`0X.Y`_ - znak będzie zawsze dodany (+ dla liczb nieujemnych)                            |
| `e`     | liczba rzeczywista w notacji wykładniczej (`1.4e+2`) (wartość musi być typu `float`)                                                        |
| `XXXe`  | dla liczb w notacji wykładniczej, możliwe jest wymuszenie liczby cyfr lub cyfr po kropce w mantysie, jak powyżej                            |
| `Xd`    | liczba całkowita obejmująca co najmniej _`X`_ znaków, w razie potrzeby spacje zostaną dodane na początku (wartość musi być typu `int`)      |
| `0Xd`   | liczba całkowita obejmująca co najmniej _`X`_ znaków, w razie potrzeby na początku zostaną dodane zera (wartość musi być typu `int`)        |
| `x`     | liczba całkowita w zapisie szesnastkowym (wartość musi być typu `int`)                                                                      |
| `o`     | liczba całkowita w zapisie ósemkowym (wartość musi być typu `int`)                                                                          |
| `b`     | liczba całkowita w zapisie binarnym (wartość musi być typu `int`)                                                                           |
| `<XXs`  | dowolne wyrównane do lewej wyrażenie obejmujące co najmniej _`XX`_ znaków                                                                   |
| `>XXs`  | dowolne wyrównane do prawej wyrażenie obejmujące co najmniej _`XX`_ znaków                                                                  |
| `^XXs`  | dowolne wyśrodkowane wyrażenie obejmujące co najmniej _`XX`_ znaków                                                                         |

`.Yf`liczba rzeczywista z _Y_ miejsc po kropce dziesiętnej (wartość wyrażenia musi typu `float`) `Xf`liczba zajmująca przynajmniej _X_ znaków, w razie potrzeby na początku zostaną dodane spacje(wartość wyrażenia musi typu `float`) `X.Yf`liczba zajmująca przynajmniej _X_ znaków z _Y_ miejsc po kropce dziesiętnej (wartość wyrażenia musi typu `float`) `0Xf`liczba zajmująca przynajmniej _X_ znaków, w razie potrzeby na początku zostaną dodane zera(wartość wyrażenia musi typu `float`) `0X.Yf`jak `X.Yf`, ale puste miejsca wypełniane są zerami`+XXf`gdzie _XX_ to jedno z powyższych oznaczeń `X`, `X.Y`, `0X`, `0X.Y` — zawsze będzie dodany znak (w przypadku liczb nieujemnych `+`)**`e`**liczba rzeczywista zapisana w postaci wykładniczej ( `1.4e+2`)(wartość wyrażenia musi typu `float`) `XXXe`dla liczb w postaci wykładniczej można wymusić ilość miejsc po przecinku (w mantysie), minimalną szerokość napisu i znak tak jak powyżej`Xd`liczba całkowita zajmująca przynajmniej _X_ znaków, w wypełnieniem spacjami(wartość wyrażenia musi typu `int`) `0Xd`liczba całkowita zajmująca przynajmniej _X_ znaków, w wypełnieniem zerami(wartość wyrażenia musi typu `int`) **`x`**liczba całkowita zapisana w systemie szesnastkowym (wartość wyrażenia musi typu `int`) **`o`**liczba całkowita zapisana w systemie ósemkowym (wartość wyrażenia musi typu `int`) **`b`**liczba całkowita zapisana w systemie dwójkowym (wartość wyrażenia musi typu `int`) `<XXs`dowolne wyrażenie wyrównane do lewej o całkowitej szerokości minimum _XX_ znaków`>XXs`dowolne wyrażenie wyrównane do prawej o całkowitej szerokości minimum _XX_ znaków`^XXs`dowolne wyrażenie wyrównane do środka o całkowitej szerokości minimum _XX_ znaków

Jako przykład spróbujmy wydrukować tabelę z kolejnymi rekordami świata w biegu na 100m:

```python
# Tworzymy listę słowników z danymi
rekordy = [
     { 'data': '16.08.2009', 'zawodnik': 'Usain Bolt', 'czas': 9.58 },
     { 'data': '20.09.2009', 'zawodnik': 'Tyson Gay', 'czas': 9.69 },
     { 'data': '23.09.2012', 'zawodnik': 'Yohan Blake', 'czas': 9.69 },
     { 'data': '2.09.2008', 'zawodnik': 'Asafa Powell', 'czas': 9.74 }
]

szer = 42          # szerokość całej tabeli
print("-" * szer)  # drukujemy poziomą linię
print("|  Czas  |     Zawodnik     |    Data    |")
print("-" * szer)
for rekord in rekordy:
    print(f"| {rekord['czas']:6.3f} | {rekord['zawodnik']:^16s} | {rekord['data']:>10s} |")
print("-" * szer)
```

**Jak wstawić do łańcucha formatującego nawias klamrowy „{}”?**

Aby wstawić do łańcucha formatującego nawias klamrowy, który ma być potraktowany jako część tekstu, a nie początek wyrażenia, należy go powtórzyć:

{% raw %}
```python
f"To jest nawias klamrowy {{2 + 2}}, a to wyrażenie w nawiasie klamrowym {{{2 + 2}}}"
```
{% endraw %}

W powyższym tekście wyrażenie zaznaczone na czerwono zostanie obliczone, zaś powtórzone nawiasy klamrowe pojawią się tylko raz.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
