---
parent: Operacje na plikach
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Odczytywanie z pliku

Czytanie  pliku odbywać się może na kilka sposobów. Najprostsze jest użycie metody `read`, która wczyta zawartość całego pliku do zmiennej typu `str` (w przypadku otwarcia pliku w trybie binarnym będzie to typ `bytes`). Np.

```python
with open("plik.txt", "r") as plik:
    tekst = plik.read()
    print("Zawartość pliku:")
    print(tekst)
```

Jeżeli chcemy odczytywać po kolei poszczególne linie, możemy potraktować plik jako sekwencję i iterować po nim za pomocą pętli **for**:

```python
with open("plik.txt", "r") as plik:
    for linia in plik:
        print("Linijka:", linia.rstrip())
```

Należy zwrócić uwagę na dwie kwestie:

1. Wczytana linia zawiera znak końca linii (o ile występuje — w ostatniej linii w pliku może go nie być). Jeżeli chcemy uzyskać linię bez tego znaku, należy go usunąć. Przydatna do tego może być metoda `rstrip` dla łańcuchów tekstowych, która usuwa białe znaki na końcu tekstu (spacje, tabulatory i znaki nowej linii).

2. Raz otwarty plik możemy iterować jednokrotnie. Po odczytaniu linii, Python przechodzi do następnej i ponowna iteracja nie spowoduje powrotu do wcześniej odczytanej zawartości. Aby odczytać plik ponownie, należy albo go ponownie otworzyć, albo wczytać zawartość linii do listy:


   ```python
   with open("plik.txt", "r") as plik:
       linie = [linia.rstrip() for linia in plik]
   ```


   Lista `linie` będzie przechowywana w pamięci i będzie możliwość wielokrotnej iteracji po niej oraz jej modyfikowania. Istnieje możliwość powrotu do wybranego miejsca w pliku za pomocą metody `seek`, ale w najprostszych zastosowaniach nie jest to potrzebne.

Poniższy przykład drukuje plik wraz z numerami wierszy:

```python
with open("plik.txt", "r") as plik:
    for nr, linia in enumerate(plik):
        print(f"{nr+1:3d}: {linia.rstrip()}")
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
