---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Zbiory

Ostatnim standardowym typem Pythona, który pozwala na przechowywanie innych elementów jest zbiór ( `set`). W odróżnieniu od listy, elementy znajdujące się w zbiorze nie są uporządkowane (nie mają przypisanych indeksów, ani — tak jak wartości w słowniku — kluczy).

Zbiory tworzy się w następujący sposób:

```python
zbiór = {element1, element2, element3...}
```

Nawiasy klamrowe są identyczne jak w przypadku tworzenia słownika, jednakże nie stosuje się dwukropka.

Wszystkie elementy zbioru muszą być niezmienialne (czyli nie mogą być nimi listy i krotki). Ponadto, w zbiorze nie może być dwóch identycznych elementów. Proszę sprawdzić w interaktywnej konsoli

```python
{1, 2, 3, 1} == {1, 2, 3}

```

Powyższe wyrażenie będzie miało wartość `True`, gdyż oba zbiory są identyczne.

Ilość elementów zbioru można poznać, tak jak dla każdej sekwencji czy słownika, za pomocą funkcji `len`. Podobnie można iterować po nich używając pętli **for** (kolejność iteracji będzie jednak nieokreślona). Np.

```python
primes = {2, 3, 5, 7, 11}
for num in primes:
    print(num)
```

Można też sprawdzić, czy dany element należy, bądź nie należy do zbioru za pomocą operatorów **`in`** oraz **`not in`**.

Do dodawania nowych elementów do zbioru, służy metoda `add` ( `zbior.add(nowy_element)`). Np.

```python
A = {1, 2, 3}
print(1 in A, 4 not in A)
A.add(4)
print(4 in A)
```

Istnieją dwie metody usuwania elementów ze zbioru: `discard` i `remove` . Ich zachowanie zmienia się tylko w przypadku, gdy usuwanego elementu nie ma w zbiorze. W takim przypadku metoda `discard` nic nie robi, a metoda `remove` powoduje wyjątek **KeyError**.

Ponieważ elementy zbioru nie mają ani indeksów ani kluczy, nie jest możliwy bezpośredni dostęp do pojedynczych elementów. Jeżeli jest to potrzebne, można przekształcić taki zbiór w listę ( `lista = list(zbiór)`).

## Operacja na zbiorach

Na zbiorach można wykonywać operacje matematyczne:

| Składnia Pythona                                | Znaczenie                                                                               |
| ----------------------------------------------- | --------------------------------------------------------------------------------------- |
| `A | b` lub `A.union(B)`                        | Zwraca zbiór, który zawiera elementy zarówno z `A` jak i z `B`                          |
| `A |= B` lub `A.update(B)`                      | Dodaje wszystkie elementy obecne w `B` do `A`                                           |
| `A & B` lub `A.intersection(B)`                 | Zwraca zbiór zawierający tylko elementy obecne w `A` i `B`                              |
| `A &= B` lub `A.intersection_update(B)`         | Usuwa wszystkie elementy z `A`, które nie są obecne w `B`                               |
| `A - B` lub `A.difference(B)`                   | Zwraca różnicę `A` i `B` (elementy obecne w `A`, ale nie w `B`)                         |
| `A -= B` lub `A.difference_update(B)`           | Usuwa wszystkie elementy obecne w `B` z `A`                                             |
| `A ^ B` lub `A.symmetric_difference(B)`         | Zwraca symetryczną różnicę `A` i `B` (elementy należące do `A` lub `B`, ale nie do obu) |
| `A ^= B` lub `A.symmetric_difference_update(B)` | Przechowuje symetryczną różnicę `A` i `B` w `A`                                         |
| `A <= B` lub `A.issubset(B)`                    | Zwraca `True`, jeśli `A` jest podzbiorem `B`                                            |
| `A >= B` lub `A.issuperset(B)`                  | Zwraca `True`, jeśli `B` jest podzbiorem `A`                                            |
| `A < B`                                         | Odpowiednik `A <= B` i `A != B`                                                         |
| `A > B`                                         | Równoważne `A >= B` i `A != B`                                                          |

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
