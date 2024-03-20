---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Listy

W Pythonie istnieje typ danych bardzo podobny do krotek. Są to **listy** ( `list`). W odróżnieniu od krotek, które są stałymi, listy są strukturami, które mogą ulegać zmianie — można do nich dodawać nowe elementy, usuwać, zmieniać.

Listy z określonymi elementami tworzy się podobnie jak krotki, jednakże zamiast nawiasów okrągłych stosuje się nawiasy kwadratowe:

```python
lista = ["pierwszy", 2, 2.5, 3-1j]
```

Tak jak w przypadku krotek elementy list nie muszą być tego samego typu. Wszystkie dotychczasowe operacje przedstawione dla krotek, takie jak iterowanie po nich w pętli **for**, indeksowanie elementów, wycinki itd. działają dokładnie w taki sam sposób dla list.

Elementy list można jednak zmieniać. Proszę wpisać następujące komendy w konsoli interaktywnej

```python
lista = [1, 2, 3]

lista[0] = 10

print(lista)    # [10, 2, 3]
```

Gdyby takie przypisanie zrobić dla krotki, spowodowałoby to błąd **TypeError**.

Elementy list można też usuwać za pomocą komendy **`del`**. Na przykład:

```python
lista = ['A', 'B', 'C', 'D']

del lista[1]    # usuwamy drugi element

print(lista)    # ['A', 'C', 'D']
```

Możliwe też jest wstawianie i dodawanie elementów do listy. Służą do tego _metody_ o nazwach `insert` i `append`. _Metody_ to są specyficzne operacje związane ze zmienną danego typu — podobne do funkcji, ale działające na jeden konkretny obiekt. Wywołuje je się w następujący sposób `obiekt.metoda(argumenty...)`, gdzie _obiekt_ to zazwyczaj nazwa zmiennej, nazwę metody od obiektu oddziela znak kropki. Dodanie elementu do listy będzie wyglądało następująco:

```python
lista = ['A', 'B', 'C']

lista.append('D')
```

Metoda `append` dostawia element podany jako jej argument na koniec listy. Zatem w powyższym przykładzie lista będzie miała postać `['A', 'B', 'C', 'D']`. Z kolei metoda `insert` przyjmuje dwa argumenty — miejsce, w które należy wstawić element (czyli indeks, jaki będzie miał wstawiony element) oraz jego wartość:

```python
lista = ['A', 'B', 'C']

lista.insert(1, 'X')

print(lista)    # ['A', 'X', 'B', 'C']
```

Poniżej znajduje się przykład tworzenia listy imion. Proszę go uruchomić i przeanalizować:

```python
imiona = []    # w ten sposób tworzy się pustą listę

# Poniższa pętla będzie się wykonywała w nieskończoność
# może ona być zakończona tylko przez break
while True:
    imie = input("Podaj imię albo napisz wstaw kropkę by zakończyć: ")
    if imie == '.':
        break
    imiona.append(imie)

print(imiona)
```

## Konwersja list i innych typów

Bez żadnych ograniczeń można konwertować listy na krotki i na odwrót. Można dzięki temu obejść ograniczenie niepozwalające na modyfikowanie krotek:

```python
krotka = (1, 2, 3)
lista = list(krotka)
lista[0] = 10
krotka = tuple(lista)
print(krotka)
```

Należy jednak pamiętać, że krotki są wydajniejsze i działają szybciej, więc należy unikać takiej konwersji o ile nie jest ona absolutnie niezbędna.

Podobnie można konwertować łańcuchy znaków na listy (ale już nie na odwrót: proszę sprawdzić jaki efekt da polecenie `str(['a', 'b', 'c'])`. Istnieją jednak dwie bardzo przydatne metody zdefiniowane dla łańcuchów tekstowych: `split` i `join`. Metoda `split` służy do dzielenia łańcucha tekstowego na słowa, zaś `join` na łączenie elementów listy. Proszę spróbować samodzielnie podzielić tekst w interaktywnej konsoli:

```python
tekst = "raz dwa trzy"

lista = tekst.split()

print(lista)    # ['raz', 'dwa', 'trzy']
```

Istnieje też alternatywne wywołanie metody `split`, które pozwala podzielić tekst nie na wyrazy (czyli w miejscach spacji i nowych linii), ale wybranych ciągów znaków. Zobaczmy np. jak podzielić tekst zawierający wyrazy oddzielone od siebie przecinkiem:

```python
tekst = "raz,dwa,trzy"

lista = tekst.split(',')

print(lista)    # ['raz', 'dwa', 'trzy']
```

Z kolej metoda `join` (działająca na łańcuchach tekstowych) służy do łączenie elementów listy (lub krotki) podanej jako jej argumenty. Łącznikiem jest tekst, na którym ta metoda działa. Najlepiej zilustruje to przykład:

```python
lista = ['Kacper', 'Melchior', 'Baltazar']

łącznik = " + "

tekst = łącznik.join(lista)

print(tekst)    # Kacper + Melchior + Baltazar
```

W przypadku łańcuchów tekstowych metody działają też bezpośrednio dla wartości:

```python
lista = ['Kacper', 'Melchior', 'Baltazar']

tekst = " + ".join(lista)

print(tekst)    # Kacper + Melchior + Baltazar
```

## Eleganckie tworzenie list

Metodę `append` stosuje się do dodawania elementów do listy. Jeżeli da się tego uniknąć, lepiej jej nie stosować do tworzenia całych list, powtarzając ją wewnątrz pętli **for**. Python oferuje elegancją metodę tworzenia list zwaną _list comprehension_. Powyżej został przedstawiony przykład tworzenia listy za pomocą wymieniania jej elementów oddzielonych przecinkiem i umieszczonych w nawiasach kwadratowych `[...]`. Zamiast ręcznego wypisywania elementów można użyć pętli **for** o następującej składni:

```python
lista = [wyrażenie for licznik in sekwencja]
```

_Wyrażenie_ to znajduje się przed komendą **`for`** i nie ma nigdzie żadnego dwukropka. Wyrażenie to może wykorzystywać licznik pętli do wyliczenia kolejnych wartości wstawianych do listy. Najlepiej będzie zilustrować to na przykładzie. Załóżmy, że chcemy stworzyć listę zawierającą kwadraty liczb z zakresu 1–10:

```python
kwadraty = [i**2 for i in range(1, 11)]

print(kwadraty)
```

Proszę zwrócić uwagę, że taki zapis jest bardzo podobny do języka naturalnego: „niech lista _kwadraty_ składa się z wartości _i_ 2 dla _i_ w zakresie od 1 do 10”.

W bardzie zaawansowanej wersji, możemy dodać dodatkowy warunek, który musi spełniać licznik pętli, aby odpowiadające mu wyrażenie zostało włączone do listy:

```python
lista = [wyrażenie for licznik in sekwencja if warunek]
```

Na przykład, jeżeli do naszej listy kwadratów nie chcemy włączyć kwadratów liczb 3 i 7, możemy napisać:

```python
kwadraty = [i**2 for i in range(1, 11) if i not in (3, 7)]
```

Kilka ciekawych dodatkowych informacji o tym sposobie tworzenia pętli znajduje się na przykład [na tym blogu](https://programeria.pl/2018/08/29/list-comprehensions/).

## Ćwiczenie

Proszę napisać jak najkrótszy program, który stworzy listę zawierającą długości poszczególnych słów w zdaniu „_Litwo Ojczyzno Moja Ty jesteś jak zdrowie_” (dla uproszczenia pominięte zostały znaki interpunkcyjne).


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
