---
parent: Moduły
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Korzystanie z modułów Pythona

Python standardowo zapewnia bardzo szeroki wachlarz funkcji i obiektów pozwalających na proste wykonywanie różnych zaawansowanych operacji. Czyni to pisanie programów w Pythonie znacznie łatwiejszym niż w innych popularnych językach programowania, takich jak C++. Najbardziej powszechne i często używane funkcje (np. `print`, `input`, `len`, czy `range`) dostępne są zawsze i bezpośrednio — są to tak zwane funkcje _wbudowane_. Jednakże zdecydowana większość zgrupowana jest w _paczkach_ i _modułach_, które muszą zostać _zaimportowane_ wtedy gdy są potrzebne.

Aby zaimportować moduł należy wydać komendę:

```python
import nazwa_modułu
```

Przykładem może być moduł [`random`](https://docs.python.org/3/library/random.html#module-random), który udostępnia funkcje służące go generowania liczb pseudo-losowych. Importujemy go poleceniem

```python
import random
```

Komenda ta nie powoduje, że wszystkie funkcje i obiekty zdefiniowane w tym module staną się bezpośrednio dostępne. Aby się do nich dostać trzeba użyć notacji `nazwa_modułu.funkcja(...)`. Np. aby wygenerować liczbą losową z zakresu \[ _a_, _b_\] możemy użyć funkcji `uniform` z modułu `random`:

```python
liczba_losowa = random.uniform(-1, 1)
```

Pełną listę wbudowanych modułów oraz funkcji Pythona można znaleźć w [dokumentacji](https://docs.python.org/3/library/index.html). W szczególności warto przejrzeć opisy modułów [`sys`](https://docs.python.org/3/library/sys.html) oraz [`os`](https://docs.python.org/3/library/os.html), który zawierają zbiór podstawowych funkcji i obiektów do korzystania z narzędzi systemu operacyjnego. Np. można sprawdzić aktualną wersję Pythona za pomocą:

```python
import sys

print(sys.version)
```

W tym przypadku `sys.version` nie jest funkcją, ale po prostu łańcuchem znaków. Niemniej jest to obiekt zdefiniowany wewnątrz modułu.

Moduły mogą zawierać wewnątrz inne modułu zagnieżdżone w sposób hierarchiczny — dowolny moduł może zawierać moduły podrzędne (moduły nadrzędne nazywane wtedy są _paczkami_). Aby zaimportować wybrany moduł podrzędny należy użyć komendy `import moduł_nadrzędny.moduł_podrzędny`. Poziomów zagnieżdżenia może być dowolnie wiele — w takim przypadku należy je wpisać wszystkie oddzielając kolejne poziomy kropką. Użyteczne funkcje i obiekty mogą znajdować się zarówno w module nadrzędnym jak i w modułach podrzędnych. Moduły podrzędne stosowane są po to aby zgrupować zbiór funkcji. Na przykład moduł [`os`](https://docs.python.org/3/library/os.html) zawiera funkcje pozwalające wykonywać różne operacje na plikach na dysku, zaś moduł [`os.path`](https://docs.python.org/3/library/os.path.html#module-os.path) — zbiera funkcje pozwalające na manipulację ścieżką do pliku:

```python
import os.path

print(os.path.join('katalog', 'plik.txt'))
```

## Uproszczone wczytywanie modułów

Fakt, że komenda **`import`** definiuje tylko nazwę modułu pozwala zachować porządek w kodzie programu. W szczególności nie ma problemu, by w w kilku modułach znajdowały się funkcje o takich samych nazwach — ponieważ ich użycie wymaga podania nazwy modułu przed kropką, nie będzie pomiędzy nimi kolizji. Czasami jednak — szczególnie w przypadku modułów zagnieżdżonych — może to być uciążliwe (np. kiedy konieczne jest częste pisanie `modulA.modulB.modulC.funkcja1()`, `modulA.modulB.modulC.funkcja2()` itd.). Istnieją dwie metody aby sobie z tym poradzić. Pierwsza polega na zaimportowaniu dowolnego modułu (także zagnieżdżonego) pod własną nazwą. Służy do tego słowo kluczowe **`as`**:

```python
import modulA.modulB.modulC as mc
```

Wtedy zamiast `modulA.modulB.modulC.funkcja1()` możemy napisać po prostu `mc.funkcja1()`, co jest znacznie krótsze. Np.

```python
import os.path as p

print(p.join('katalog', 'plik.txt'))
```

Należy pamiętać by nazwy, które nadajemy importowanym modułom, były coś mówiące — nawet gdy jest to jedno- lub dwuliterowy skrót (w powyższym przykładzie użyto pierwszej litery nazwy modułu podrzędnego `path`).

Druga metoda pozwala na bezpośrednie wczytywanie wybranych funkcji i innych obiektów z modułu i dostęp do nich bez poprzedzania ich nazwą modułu. W tym celu stosujemy następującą składnię:

```python
from nazwa_modułu import funkcja
```

`nazwa_modułu` może mieć postać `moduł_nadrzędny.moduł_podrzędny`, tak jak we wcześniej opisanych przypadkach ilość importowanych funkcji może być dowolna — gdy jest więcej niż jedna, powinny one być oddzielone przecinkiem. Zaimportowane w ten sposób funkcje możemy używać bezpośrednio. Na przykład:

```python
from numpy import pi, sin, cos

print(sin(pi/2))
```

co jest równoważne z:

```python
import numpy

print(numpy.sin(numpy.pi/2))
```

Należy jednak pamiętać, że stosując to podejście ryzykujemy, że zaimportowana funkcja zastąpi funkcję wbudowaną. Ponadto w kodzie programu nie widzimy jasno, z jakiego modułu ona pochodzi. Proszę zatem tę metodę wykorzystywać z rozwagą.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
