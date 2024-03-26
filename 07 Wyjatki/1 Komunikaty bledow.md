---
parent: Wyjątki
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Komunikaty błędów

Każdy z Was z pewnością spotkał z komunikatami błędów. Na przykład, wydanie w konsoli komendy:

```python
print(float("dwa"))
```

Spowoduje komunikat:

```
Traceback (most recent call last):

  File "<ipython-input-1-ed629b1feb04>", line 1, in <module>
    print(float("dwa"))

ValueError: could not convert string to float: 'dwa'
```

W Pythonie błędy noszą nazwę **wyjątków**. Ich pojawienie się oznacza, że zaistniała sytuacja niestandardowa. Jej pojawienie się może wynikać z błędu w programie — wtedy komunikat pokazuje dokładne miejsce, w którym pojawił się problem oraz cały ciąg wywołań funkcji, które do niego doprowadziły. Proszę przyjrzeć się następującemu programowi (przepisując go, proszę pominąć numery linii, które podane są tylko informacyjnie):

```python
1  def zamien_na_liczbe(wartosc):
2      return float(wartosc)
3
4  print(zamien_na_liczbe('2'))
5  print(zamien_na_liczbe('dwa'))
```

Jego uruchomienie spowoduje komunikat:

```
Traceback (most recent call last):

  File "temp.py", line 5, in <module>
    print(zamien_na_liczbe("dwa"))

  File "temp.py", line 2, in zamien_na_liczbe
    return float(wartosc)

ValueError: could not convert string to float: 'dwa'
```

Python wydrukował tzw. _zrzut stosu_ ( _traceback_), czyli stos wywołań funkcji. Należy go czytać od dołu: pojawił się błąd `ValueError`, czyli błąd wartości. W komunikacie błędu czytamy, że Python nie jest w stanie przekonwertować łańcucha tekstowego `'dwa'` do liczby rzeczywistej. Powyżej znajdziemy informację, że błąd ten wystąpił w drugiej linii pliku `temp.py` w funkcji `zamien_na_liczbe` (dla ułatwienia, linia ta jest poniżej przepisana). Z kolei funkcja ta była wywołana w piątej linii w głównym kodzie modułu (bez żadnej funkcji). Proszę zwrócić uwagę, że wywołanie funkcji `zamien_na_liczbe` w linii czwartej nie spowodowało błędu.

## Typy wyjątków

W Pythonie wyjątki mogą być różnych typów, które odpowiadają różnym rodzajom błędów bądź sytuacji nietypowych. Poniżej znajduje się spis najczęściej spotykanych typów wyjątków:

**`AttributeError`:** Wywoływany w przypadku, gdy nie powiedzie się odwołanie lub przypisanie do atrybutu (gdy obiekt w ogóle nie obsługuje odwołań lub przypisań do atrybutów wywoływany jest `TypeError`).

**`IOError`:** Wywoływany w przypadku wystąpienia błędu operacji wejścia/wyjścia instrukcji print, funkcji wbudowanej `open()` czy też metod obiektów plikowych. Przyczyną wystąpienia tych błędów może być na przykład „nie odnaleziono pliku” lub „brak miejsca na dysku”.

**`ImportError`:** Wywoływany w przypadku wystąpienia błędu instrukcji import spowodowanego nieodnalezieniem modułu lub w przypadku instrukcji from ... import kiedy system nie może odnaleźć w module wyspecyfikowanej nazwy.

**`IndexError`:** Wywoływany w przypadku użycia indeksu spoza zasięgu dla uzyskania dostępu do elementu sekwencji (indeksy operacji wycinania są dopasowywane automatycznie do rozmiaru sekwencji; jeśli indeks nie jest liczbą całkowitą wywoływany jest `TypeError`).

**`KeyError`:** Wywoływany w przypadku nie wystąpienia klucza użytego dla uzyskania dostępu do elementu odwzorowania (słownika).

**`KeyboardInterrupt`:** Wywoływany w przypadku użycia klawisza przerwania operacji (zwykle `Ctrl-C` lub `Ctrl-Delete`). Sprawdzanie wystąpienia takiej sytuacji jest dokonywane regularnie podczas wywołania programu. Użycie klawisza (kombinacji klawiszy) przerwania operacji podczas oczekiwania funkcji `input()` na dane wejściowe również wywołuje ten wyjątek.

**`MemoryError`:** Wywoływany w przypadku wyczerpania się pamięci operacji z możliwością uratowania sytuacji (poprzez usunięcie obiektów). Wartość przypisaną wyjątku stanowi napis określający jaka operacja (wewnętrzna) wyczerpała pamięć.

**`NameError`:** Wywoływany w przypadku nieodnalezienia lokalnej lub globalnej nazwy. Wartość przypisaną wyjątku stanowi komunikat o błędzie zawierający nazwę, która nie została odnaleziona.

**`SyntaxError`:** Wywoływany w sytuacji, gdy parser napotka błąd składniowy.

**`TypeError`:** Wywoływany w sytuacji wykonania operacji wbudowanej na obiektu niewłaściwego typu. Wartość przypisaną wyjątku stanowi napis opisujący szczegóły dotyczące niedopasowania typów.

**`UnboundLocalError`:** Wywoływany w przypadku odwołania do lokalnej zmiennej funkcji lub metody, kiedy nie została tej zmiennej przypisana żadna wartość.

**`ValueError`:** Wywoływany w przypadku wywołania operacji z argumentem właściwego typu, lecz o nieprawidłowej wartości a sytuacja ta nie daje się zasygnalizować bardziej szczegółowym wyjątkiem jak np. `IndexError`.

**`ZeroDivisionError`:** Wywoływany w przypadku, gdy drugi argument operacji dzielenia lub reszty z dzielenia (modulo) jest równy zero. Wartość przypisana wyjątku jest napisem opisującym typy operandów i operacji.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
