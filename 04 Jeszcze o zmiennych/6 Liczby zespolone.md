---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  6
---

# Liczby zespolone

W Pythonie występuje natywnie typ reprezentujacy liczby zespolone ( `complex`). Można go tworzyć dopisując symbol **`j`** do liczb rzeczywistych dla oznaczenia liczb urojonych. Np:

```python
zespolona = 1 + 0.2j
```

Na tym typie można prowadzić normalnie obliczenia, wypisywać na ekran itp. Co jednak w sytuacji, gdy chcemy wyciągnąć z liczby zespolonej tylko część rzeczywistą, bądź urojoną? W tym celu stosujemy _atrybuty_ `real` oraz `imag`. Atrybuty są podobne do _metod_ — stosuje się je podając ich nazwy po kropce `zmienna.atrybut`, ale bez nawiasów. Na przykład:

```python
zespolona = 1 + 0.2j

print("Re =", zespolona.real)
print("Im =", zespolona.imag)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
