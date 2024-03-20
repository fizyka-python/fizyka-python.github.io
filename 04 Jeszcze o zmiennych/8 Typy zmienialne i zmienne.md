---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  8
---

# Typy zmienialne i zmienne

Listy i słowniki są typami _zmienialnymi_. Oznacza to, że można dodawać, usuwać oraz zmieniać ich elementy. Z kolei w [temacie poświęconym zmiennym](https://ftims.edu.p.lodz.pl/mod/page/view.php?id=72247) wyjaśnione było, że zmienna to etykieta — kilka różnych zmiennych może wskazywać na ten sam obiekt.

Rozpatrzmy następujący przykład:

```python
lista1 = [1, 2, 3]
lista2 = lista1

lista2[2] = 10

print(lista1)
```

Powyższy kod wydrukuje na ekranie `[1, 2, 10]`. Stanie się tak dlatego, że `lista1` oraz `lista2` to są różne etykiety, ale wskazujące na ten sam obiekt. Aby wykonać kopię listy albo słownika, należy użyć metody `copy`:

```python
lista1 = [1, 2, 3]
lista2 = lista1.copy()

lista2[2] = 10

print(lista1)
```

Tym razem program wydrukuję `[1, 2, 10]`, ponieważ zmodyfikowaliśmy kopię listy `lista1`.

Aby sprawdzić czy dwie zmienne wskazują na ten sam obiekt można użyć operatora **`is`**. Proszę spróbować wpisać w konsoli:

```python
lista1 = [1, 2, 3]

lista2 = lista1

lista2 is lista1   # True
```

Kiedy utworzymy kopię, operator **`is`** pozwoli sprawdzić, że mamy do czynienia z różnymi obiektami. Z kolei operator porównania ( **`==`**) pokaże, że listy te są identyczne:

```python
lista1 = [1, 2, 3]

lista2 = lista1.copy()

lista2 is lista1   # False

lista2 == lista1   # True
```

Przeciwieństwem operatora **`is`** jest **`is not`**.


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
