---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Słowniki


Normalne listy (tablice) są zwykle zbiorem ponumerowanych elementów, więc aby odwołać się do dowolnego elementu listy, należy podać jego numer. Ale numery identyfikacyjne nie zawsze są wygodne. Na przykład numery lotów identyfikowane są przez kod alfa-numeryczny. Podobnie numery autobusów w Łodzi mogą zawierać litery.

Struktura danych, która pozwala na użycie dowolnego typu indeksu (zwanego kluczem) zamiast liczby, nazywana jest _słownikiem_. W Pythonie odpowiednia struktura danych nosi nazwę `dict`. Podobnie jak lista jest to struktura zmienna — po utworzeniu słownika można go zmieniać. Podobnie jak krotki tworzyło się za pomocą nawiasów okrągłych, listy za pomocą nawiasów kwadratowych, słowniki tworzy się za pomocą nawiasów klamrowych:

```python
słownik = { klucz1: wartość1, klucz2: wartość2, klucz2: wartość2 }
```

Rozważmy prosty przykład. Stwórzmy słownik, w którym klucz to nazwa państwa, a wartość — nazwa stolicy tego kraju:

```python
stolice = {      # po otwarciu nawiasu można przechodzić do nowej linii
    'Polska': 'Warszawa',
    'Niemcy': 'Berlin',
    'USA': 'Waszyngton
}
```

Zatem każdy element słownika składa się z dwóch obiektów: _klucza_ i _wartości_ . W naszym przykładzie klucz jest nazwą państwa, a wartość jest nazwą stolicy. Klucz identyfikuje element słownika, wartość to dane odpowiadające danemu kluczowi. Wartości kluczy są unikalne, tzn. Nie może być dwóch identycznych kluczy w słowniku.

Książka telefoniczna to kolejny przykład struktury danych słownika. W takim przypadku kluczem jest nazwa, a wartością numer telefonu. Zarówno dla słownika, jak i książki telefonicznej łatwo jest znaleźć element dla danego klucza (np. jeśli rekordy są przechowywane w kolejności alfabetycznej), ale jeśli klucz jest nieznany, a znamy tylko wartość, wyszukiwanie elementu o podanej wartości może wymagać przejrzenia całego słownika.

Dostęp do elementów słownika odbywa się za pomocą nawiasów kwadratowych. W odróżnieniu od krotek i list, wewnątrz nawiasów podaje się wartość klucza, np.:

```python
print(stolice['Polska'])
```

Próba pobrania w ten sposób wartości dla klucza, którego w słowniku nie ma, spowoduje błąd **KeyError**.

Tak jak to napisano powyżej, słownik można zmieniać. Dodawania nowych elementów i zmiana istniejących jest bardzo prosta:

```python
stolice['Francja'] = 'Paryż'
```

Jeżeli klucza „Francja” wcześniej w słowniku nie było, to zostanie on dodany i przypisana mu zostanie wartość „Paryż”. Jeżeli istniał on już wcześniej, to po prostu zostanie mu przypisana nowa wartość.

Usuwanie elementów ze słownika możliwe jest za pomocą komendy `del`:

```python
del stolice['USA']
```

W języku Python kluczem może być dowolny niezmienialny typ danych: liczby całkowite i liczby rzeczywiste, łańcuchy, krotki. Nie mogą być nimi listy ani inne słowniki. Wartością elementu słownika może być dowolny typ danych.

Oprócz stosowania nawiasów kwadratowych dostęp do elementów słownika możliwy jest za pomocą metody `get`: `A.get(klucz)`. Jeżeli dany klucz znajduje się w słowniku, to zostanie zwrócony odpowiadający mu element. W przeciwnym razie zostanie zwrócona wartość `None`. Metoda ta ma też wersję z dwoma argumentami `A.get(klucz, wartość_domyślna)`, która — w przypadku braku podanego klucza w słowniku, zwraca podaną wartość domyślną. W obu przypadkach, metoda ta — w odróżnieniu od pobierania elementu s pomocą nawiasów kwadratowych, nie wygeneruje wyjątku (błędu).

Aby sprawdzić, czy w słowniku znajduje się dany klucz, używane są operacje `in` i `not in` , tak jak w przypadku sekwencji.

```python
litery = {'ab' : 'ba',  'aa' : 'aa', 'bb' : 'bb', 'ba' :  'ab' }

klucz = 'ac'
if klucz in litery:
    del litery[klucz]
```

## Jeszcze o tworzeniu słowników

Podobnie jak jest możliwe eleganckie tworzenie list za pomocą _list comprehension_, tak możliwe jest tworzenie słowników w następujący sposób:

```python
słownik = {wyrażenie_dla_klucza: wyrażenie_dla_wartości for licznik in sekwencja}
```

Na przykład:

```python
wyrazy = "Ala ma kota".split()    # ['Ala', 'ma', 'kota']

dlugosci_wyrazow = {wyraz: len(wyraz) for wyraz in wyrazy}
```

Stworzy to słownik `{'Ala': 3, 'ma': 2, 'kota': 4}`.

### Iteracja po słownikach

Pomimo, że słowniki nie są sekwencjami, można po nich iterować za pomocą pętli **for**:

```python
for klucz in słownik:
    blok pętli
```

Pętla taka zostanie wykonana dla każdego klucza w słowniku. W odróżnieniu od sekwencji, kolejność iteracji jest nieokreślona (czyli pętla zostanie wykonana dla każdego klucza, ale nie możemy przewidzieć w jakiej kolejności). Na przykład:

```python
dlugosci_wyrazow = {'Ala': 3, 'ma': 2, 'kota': 4}

for wyraz in dlugosci_wyrazow:
    print("Wyraz", wyraz, "ma", dlugosci_wyrazow[wyraz], "liter")
```

Jeżeli chcemy iterować wyłącznie po wartościach słownika, możemy użyć metody `słownik.values()`:

```python
stolice = {'Wielka Brytania': 'Londyn',  'Niemcy': 'Berlin',  'USA': 'Waszyngton}

for miasto in stolice.values():
   print("Nie ma takiego miasta jak", miasto)
```

Możliwa jest też jednoczesna iteracja po kluczach i wartościach za pomocą metody `słownik.items()`:

```python
for panstwo, miasto in stolice.items():
   print("Stolicą", panstwo, "jest", miasto)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
