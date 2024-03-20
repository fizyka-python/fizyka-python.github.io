---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  5
---

# Kilka uwag o iteracji po sekwencjach

## Poprawne iterowanie po sekwencjach

Podczas iteracji po sekwencji można pokusić się o użycie czegoś takiego jak:

<div style="text-decoration: line-through;" onmouseover="this.style.textDecoration='none'" onmouseout="this.style.textDecoration='line-through'" markdown="1">

```python
for i in range(len(sekwencja)):
    element = sekwencja[i]
    operacja na elemencie
```

</div>

Jest to szczególnie powszechne wśród osób, które mają pewne doświadczenie z różnymi językami programowania, takimi jak C++. **W Pythonie jest to błędne!** Zamiast tego należy po prostu iterować po elementach sekwencji, pomijając ich indeksy:

```python
for element in sekwencja:
    operacja na elemencie
```

## Numeracja elementów w pętli

Czasami istnieje potrzeba iteracji po sekwencji zbioru i jednoczesnej numeracji ich. Można to zrobić następująco:

<div style="text-decoration: line-through;" onmouseover="this.style.textDecoration='none'" onmouseout="this.style.textDecoration='line-through'" markdown="1">

```python
numer = 0
for element in sekwencja:
    blok pętli
    numer += 1
```

</div>

Nie jest to jednak najlepsze rozwiązanie. Zdecydowanie lepiej użyć funkcji `enumerate(sekwencja)`, która w każdym przebiegu pętli będzie generowała kolejne elementy sekwencji oraz ich numery:

```
for numer, element in enumerate(sekwencja):
   print("Elementem nr", numer, "sekwencji jest", element)
```

## Iteracja po kilku sekwencjach jednocześnie

Możliwa jest też jednoczesna iteracja po kilku sekwencjach. Służy to tego funkcja `zip(sekwencja1, sekwencja2...)`. Ilość sekwencji do jednoczesnej iteracji jest dowolna. Warunkiem jest, że wszystkie te sekwencje muszą być tej samej długości (tak naprawdę nie jest to konieczne — pod uwagę zostanie wzięte tylko tyle elementów ile jest w najkrótszej sekwencji). Iteracja ta ma postać:

```python
for element1, element2, element3 in zip(sekwencja1, sekwencja2, sekwencja3):
   blok pętli
```

Na przykład:

```python
imiona = ["Harry", "Frodo", "James"]
nazwiska = ["Potter", "Baggins", "Bond"]

for imie, nazwisko in zip(imiona, nazwiska):
    print(imie, nazwisko)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
