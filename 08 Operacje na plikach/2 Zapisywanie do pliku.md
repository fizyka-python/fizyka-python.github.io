---
parent: Operacje na plikach
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Zapisywanie do pliku

Do zapisywania do pliku służy metoda `write`, która jako argument przyjmuje łańcuch tekstowy do zapisania. Może ona zostać wywołana dla pliku otwartego do zapisu(w trybie `w` lub `a`). Metodę tę można wywoływać wiele razy — każde kolejne wywołanie będzie dodawało dane do pliku. Np:

```python
with open('plik.txt', 'w') as plik:
    plik.write("Ala ma kota.\n")
    plik.write("A kot ma Alę!\n")
```

Po wykonaniu kolejnych poleceń plik będzie miał dwie linijki. Proszę zwrócić uwagę, że konieczne jest samodzielne wstawianie znaków nowej linii (oczywiście nie muszą one być na końcu tekstu).

Jeżeli mamy listę lub krotkę łańcuchów tekstowych, możemy je zapisać po kolei za pomocą metody `writelines`, np.

```python
with open('plik.txt', 'w') as plik:
    plik.writelines(["Ala ma kota.\n", "A kot", " ma Alę!\n"])
```

Wbrew nazwie powyższa metoda nie zapisuje kolejnych elementów listy w osobnych linijkach, ale łączy je. Znaki nowej linii będą wstawiane tam gdzie występują one w łańcuchach tekstowych.

Inną — być może łatwiejszą — metodą zapisania do pliku tekstowego jest użycie poznanej już funkcji `print`. Może ona przyjąć opcjonalny argument `file=plik`, w którym możemy podać plik otwarty do zapisu:

```python
with open('plik.txt', 'w') as plik:
    print(1, 2, 3, file=plik)
```

Stosowane są normalne reguły obowiązujące dla funkcji `print` — kolejne elementy oddzielane są spacjami i na końcu drukowany jest znak nowej linii, chyba że zostanie to zmienione za pomocą argumentów `sep` oraz `end`.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
