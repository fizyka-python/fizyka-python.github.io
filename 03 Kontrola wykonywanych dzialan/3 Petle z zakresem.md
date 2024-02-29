---
parent: Flow Control
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Pętle z zakresem

Innym rodzajem pętli występującym w Pythonie jest pętla **for**. Ma ona zastosowanie wtedy gdy z góry jesteśmy w stanie przewidzieć ile razy chcemy tę pętlę wykonać, bądź gdy chcemy ją powtórzyć dla każdego elementu sekwencji. Składnia pętli **for** jest następująca:

<pre>
<b>for</b> <i>wskaźnik</i> <b>in</b> <i>sekwencja_po_której_powtarzamy</i><b>:</b>
    blok powtarzany dla każdego elementu sekwencji
    identyfikator podany jako <i>wskaźnik</i> będzie przyjmował
    wartości każdego elementu sekwencji po kolei
</pre>

W powyższej składni jako _wskaźnik_ podajemy poprawną nazwę zmiennej. Zmienna ta nie musi być wcześniej zdefiniowana (a jeżeli była, to jej dotychczasowa wartość zostanie usunięta). W każdym przebiegu pętli zmienna ta będzie przyjmować kolejne wartości z sekwencji, po której iterujemy. Oczywiście sekwencja ta musi istnieć — albo być podana jako stała, albo być przypisana do zmiennej.

Do tej pory zostały przedstawione dwa typy sekwencyjne: łańcuch znaków oraz krotka. Poniżej przedstawiony jest przykład pętli, w której sumowane są wszystkie elementy krotki:

```python
liczby = (1, 2, 3, 5, 7)
suma = 0
for liczba in liczby:
    suma += liczba
print("Suma liczb to", suma)
```

> **Uwaga!** W Pythonie wiele podstawowych operacji (jak np. sumowanie elementów zbioru) da się zrobić za pomocą jednej komendy, bądź funkcji (w tym przypadku wystarczyłoby napisać suma = `sum(liczby)`). W normalnych programach należy z takich skróconych form korzystać, gdyż są one czytelniejsze i z reguły działają szybciej. Niemniej na potrzeby przykładów i ćwiczeń wiele takich prostych operacji będziemy pisać ręcznie — w celach ilustracyjnych.

Iterować też można po elementach łańcucha tekstowego:

```python
imie = input("Jak masz na imie: ")
for litera in imie:
    print(litera)
```

Powyższy przykład zapyta użytkownika o imię, a następnie wypisze każdą literę w osobnej linii.

## Szyfr Cezara

Przyjrzyjmy się teraz bardziej zaawansowanemu przykładowi. Zaimplementujemy [szyfr Cezara](https://pl.wikipedia.org/wiki/Szyfr_Cezara) (aczkolwiek ograniczymy się do alfabetu stosowanego w języku angielskim). Wpierw jednak konieczne jest wyjaśnienie w jaki sposób znaki przetrzymywane są w pamięci komputera. Otóż każdy komputer jest urządzeniem, które potrafi przeprowadzać działania na liczbach i tylko na liczbach. W związku z tym, aby zapisać dowolny tekst w pamięci komputera, każdemu znakowi musi być przyporządkowana pewna liczba. Jaka liczba odpowiada jakiej literze definiuje standard [ASCII](https://pl.wikipedia.org/wiki/ASCII) oraz [Unikod](https://pl.wikipedia.org/wiki/Unikod). W Pythonie istnieją dwie funkcje, które pozwalają sprawdzić jaka liczba odpowiada jakiem znakowi i na odwrót. Pierwsza z nich to funkcja `ord(znak)`, której argumentem może być wyłącznie jeden znak (czyli łańcuch tekstowy zawierający dokładnie jeden element). Zwróci ona kod numeryczny tego znaku. Odwrotna funkcja, to `chr(kod)`, która zwróci znak reprezentowany przez kod numeryczny podany jako jej argument. Proszę w interaktywnej konsoli sprawdzić:

```python
print(ord('A'))

print(chr(122))
```
Powyższe funkcje zostaną wykorzystane w programie szyfrującym za pomocą szyfru Cezara. Zastosujemy przesunięcie alfabetyczne równe 13, gdyż alfabet angielski ma 26 liter, w związku z czym dwukrotne zaszyfrowane wiadomości spowoduje jej przywrócenie (innymi słowy, ten sam program można wykorzystać do szyfrowania i odszyfrowywania wiadomości — taki wariant szyfru Cezara nosi nazwę [ROT-13](https://pl.wikipedia.org/wiki/ROT13)).

```python
# Odczytujemy tekst do zaszyfrowania
tekst_oryginalny = input("Podaj tekst to zaszyfrowania: ")
 
# Tekst zaszyfrowany na razie jest pusty; będziemy do niego dopisywali kolejne znaki
tekst_zaszyfrowany = ''

# W pętli iterujemy po każdym znaku
for znak in tekst_oryginalny:

    if 'A' <= znak <= 'Z': # warunek typu_ a < x < b _jest tożsamy z: a < x **and** x < b

        # Mamy wielką literę; obliczamy jej numer porządkowy
        # (tak, by literze „A” odpowiadało 0)
        kod = ord(znak) - ord('A')

        # Szyfrujemy znak: dodajemy 13 i zawijamy do 26 znaków (reszta z dzielenia)
        nowy_kod = (kod + 13) % 26

        # Dodajemy to zaszyfrowanego tekstu nowy znak:
        # najpierw nowy kod „przesuwamy”, tak by litera „A” miała właściwy kod,
        # następnie zamieniamy na znak i dodajemy do łańcucha z wynikiem
        tekst_zaszyfrowany += chr(nowy_kod + ord('A'))

    elif 'a' <= znak <= 'z':  # to samo co powyżej robimy dla małych liter
        kod = ord(znak) - ord('a')  # odejmujemy kod małej litery „a”
        nowy_kod = (kod + 13) % 26
        tekst_zaszyfrowany += chr(nowy_kod + ord('a'))

    else:
        # Pozostałe znaki przepisujemy bez zmian
        tekst_zaszyfrowany += znak

# Drukujemy wyniki
print(tekst_zaszyfrowany)
```

Proszę przekopiować poniższy przykład do nowego pliku (np. o nazwie rot13.py), a następnie go uruchomić w Spyderze. Bardzo proszę dokładnie przeanalizować jego składnie, tak by każdy z Państwa rozumiał każdą linijkę. W ramach zajęć będzie pisali bardziej zaawansowane programy niż powyższy.

W razie wątpliwości, proszę przedstawić je na forum.

## Zakresy liczbowe

Bardzo często zachodzi potrzeba powtórzenia pętli konkretną ilość razy. Możemy wtedy zastosować następującą formę:

<pre>
<b>for</b> <i>licznik</i> in <b>range</b>(<i>ilość_powtórzeń</i>)<b>:</b>
    blok powtarzany daną ilość razy
</pre>

W trakcie wykonywania tej pętli licznik będzie się zmieniał od 0, do wartości _ilość_powtórzeń_ – 1. Proszę wypróbować następujący przykład:

```python
for i in range(10): 
    print(i)
```
Proszę zwrócić uwagę, że liczba 10 nie została już wydrukowana.

Tak naprawdę `range` jest funkcją, która na bieżąco generuje sekwencję kolejnych liczb, zaś pętla **for** po prostu iteruje po tej generowanej sekwencji. Można jej używać na trzy sposoby:

Najbardziej podstawowy i najczęściej używany `range(stop)` utworzy sekwencję od 0 do wartości poprzedzającej  `stop`. Możemy też podać tej funkcji dwa argumenty:  `range(start, stop)`. Wtedy odliczanie zacznie się od wartości podanej jako `start` (jeżeli _start_ ≥ _stop_, zakres będzie pusty i pętla nie wykona się ani razu). Tak więc `range(stop)` jest równoważny `range(0, stop)`. Trzecią wersją jest postać `range(start, end, step)`, która dodaje do tego z jakim krokiem mamy za każdym razem zmieniać wartość. W tym przypadku iteracja zakończy się kiedy kolejna wartość osiągnie lub przekroczy wartość _stop_.

Zatem aby wydrukować liczby od 1 do 10 możemy zastosować:

```python
for i in range(1, 11): 
    print(i)
```

zaś by zrobić to od końca:

```python
for i in range(10, 0, -1): 
    print(i)
```

## Ćwiczenie

Proszę napisać program, który zapyta użytkownika o liczbę całkowitą, a następnie obliczy i wydrukuje jej silnię (czyli iloczyn liczb od 1 do podanej liczby włącznie). Jako wzoru można użyć powyższy przykład obliczający sumę liczb oraz przykłady zastosowania funkcji `range`. Proszę sprawdzić czy obliczone 5! równe jest 120, zaś 10! — 3628800.

## Przerywanie i kontynuacja pętli

Podobnie jak w przypadku pętli **while**, w pętli **for** można stosować komendy `break` oraz `continue`. Ich działanie jest identyczne jak w opisanym wcześniej przypadku. Także tutaj możliwe jest zastosowanie bloku `else:` po pętli, który zostanie wykonany tylko wtedy gdy pętla zakończy się normalnie (czyli po skończeniu iteracji po wszystkich elementach), a nie przez `break`. Przykład:


```python
mina = int(input("Podaj wartość miny: "))

for i in range (1, 11):
    if i == trap:
        print("Trafiłeś na minę!")
        break
    print(i) 
else: 
    print("Udało się uniknąć miny.")
```

## Zagnieżdżanie pętli

Nie ma żadnych przeszkód, aby wewnątrz jednej pętli umieścić drugą. Ważne jest tylko aby w zagnieżdżonych pętlach używać używać innych nazw ich liczników. Na przykład aby wyświetlić nazwy wszystkich pól na szachownicy możemy użyć następującego programu:

```python
for rzad in range(8, 0, -1):    # liczby od 8 do 1 włącznie od końca (8 rząd będzie na górze)
    for kolumna in "ABCDEFGH":
        print(kolumna, rzad, sep='', end=' ')  # znaczenie sep i end było wyjaśnione wcześniej
    print()    # na końcu każdego rzędu drukujemy tylko znak nowej linii (domyślne end)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
