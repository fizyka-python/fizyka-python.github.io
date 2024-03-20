---
parent: Jeszcze o zmiennych
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Operacje na sekwencjach

o tej pory przedstawione zostały dwa typy będące sekwencjami (czyli zawierające uporządkowany ciąg danych) — krotka ( `tuple`) oraz łańcuch znaków ( `str`). Pokazane zostało jak można iterować po każdym elemencie za pomocą pętli **for**. Poniżej znajduje się opis innych przydatnych operacji, jakie możemy wykonać na każdej sekwencji (nie tylko na dwóch powyższych, ale także na innych, które zostaną niedługo przedstawione).

## Długość sekwencji

Pierwszą operacją, która może być przydatna jest poznanie długości sekwencji. Służy do tego funkcja `len(sekwencja)`, która zwraca liczbę elementów w sekwencji podanej jako jej argument (czyli w nawiasach). Na przykład:

```python
dane = (1, 2, 3, 10)
print(len(dane))

dlugosc = len("Ala ma kota.")
print("Zdanie ma", dlugosc, "liter.")
```

Jako ćwiczenie proponuję zmodyfikować zadanie **Hasło** z poprzedniego tematu (bez wysyłania) i dodać dodatkowy test na bezpieczeństwo wprowadzonego hasła: musi ono mieć przynajmniej 8 liter.

> **Uwaga!**
>
> Stosując pętlę **for**, nie należy iterować po indeksach elementów w następujący sposób `for i in range(len(sekwencja)):`. Zamiast tego powinno się stosować prostą składnię `for element in sekwencja`. Jeżeli wewnątrz potrzebny jest numer elementu, albo chcemy iterować po kilku sekwencjach jednocześnie, to stosowne metody opisane [są na osobnej stronie](https://ftims.edu.p.lodz.pl/mod/page/view.php?id=73294).

### Czy sekwencja zawiera element?

Inną przydatną operacją jest sprawdzenie czy dany element występuje w sekwencji. Służy do tego operator **`in`**, bądź **`not in`**. Na przykład:

```python
if 'a' in 'Alicja':
    print("Słowo 'Alicja' zawiera literkę 'a'")

if 4 not in (2, 3, 5, 7, 11, 13, 17, 19):
    print("Czwórka nie jest żadną z liczb pierwszych mniejszych od 20")
```

### Dostęp do poszczególnych elementów sekwencji

Skoro sekwencje są uporządkowanym zbiorem elementów, to konieczna jest możliwość uzyskania dostępu do elementu o konkretnym numerze. W tym celu, w Pythonie, stosuje się nawiasy kwadratowe bezpośrednio za sekwencją, lub (częściej) nazwą zmiennej ją reprezentującą:

```python
dane = ('A', 'B', 'C')
print(dane[0])  # drukuje pierwszy element krotki ('A')
print(dane[2])  # drukuje trzeci element krotki ('C')

wyraz = "Kalambur"
for i in (1, 3, 6):
    # wydrukuj drugą, czwartą i siódmą literę
    print(wyraz[i])
```

Wewnątrz nawiasów kwadratowych musi znajdować się liczba całkowita (bądź zmienna, taką liczbę reprezentująca), zwana _indeksem_. Wskazuje ona na numer elementu w danej sekwencji, przy czym **pierwszy element ma numer 0**. Jest to nieco nieintuicyjne i wynika z faktu, że w większości starszych języków programowania, taka konwencja była historycznie stosowana. Proszę zwrócić uwagę, że takie zachowanie jest spójne z działaniem omówionej wcześniej funkcji `range` — Python zawsze liczy od 0.

W Pythonie możliwe jest także stosowanie jako indeksów liczb ujemnych. Wtedy odliczanie następuje od końca. Zatem `sekwencja[-1]` oznacza ostatni element sekwencji, `sekwencja[-2]` — przedostatni itd. Przykład:

```python
imie = input("Podaj swoje imię: ")

if imie[-1] == 'a':  # w języku polskim, imiona żeńskie kończą się na „a”
    print("Jesteś kobietą")
else:
    print("Jesteś mężczyzną")
```

Jako proste ćwiczenie proszę zmodyfikować powyższy przykład tak, by każdy _Kuba_ został potraktowany jak mężczyzna ☺.

### Wycinki zakresów

Nawiasy kwadratowe można stosować do wyłuskiwania nie tylko pojedynczych elementów sekwencji, ale także ich wycinków. Takie wycinki mają następującą postać `sekwencja[start:stop:krok]`, gdzie _start_ to indeks pierwszego elementu wchodzącego do wycinka, _stop_ — index pierwszego elementu nie wchodzącego już do wycinka, zaś _krok_ to krok z jakim brane są kolejne elementy (proszę zwrócić uwagę, że istnieje to pewne podobieństwo do argumentów funkcji `range`). Każda z liczb _start_, _stop_ oraz _krok_ może być pominięta.

Działanie wycinków najlepiej zobrazuje przykład. Proszą przepisać go w konsoli interaktywnej i spróbować dokładnie zrozumieć w jaki sposób odliczane są kolejne elementy każdego wycinka.

```python
cyfry = tuple(range(10)) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

cyfry[2:7]               # (2, 3, 4, 5, 6)
cyfry[2:7:2]             # (2, 4, 6)
cyfry[:5]                # (0, 1, 2, 3, 4)
cyfry[5:]                # (5, 6, 7, 8, 9)
cyfry[::3]               # (0, 3, 6, 9)
cyfry[7:2:-1]            # (7, 6, 5, 4, 3)
cyfry[-1:3:-2]           # (9, 7, 5)
cyfry[6::-2]             # (6, 4, 2, 0)
cyfry[::-1]              # (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)
cyfry[:-4:-1]            # (9, 8, 7)
```

**Ważne!** Proszę zwrócić uwagę, że element o indeksie _stop_ nie wchodzi już w skład wycinka.

Przykład dla łańcuchów tekstowych:

```python
tekst = input("Podaj tekst: ")
print("Twój tekst wspak wygląda tak:", tekst[::-1])
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
