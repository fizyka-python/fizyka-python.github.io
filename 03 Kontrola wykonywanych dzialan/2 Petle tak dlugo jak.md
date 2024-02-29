---
parent: Flow Control
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Pętle „tak długo jak”

Aby jakikolwiek język programowania był użyteczny, musi umożliwiać powtarzanie fragmentu programu więcej niż jeden raz. Tego typu powtórzenia nazywamy _pętlami_. W Pythonie istnieją dwa rodzaje pętli. Poniżej omówimy pierwszą z nich – pętlę **while** (ang. podczas gdy). Służy ona do powtarzania danego bloku tak długo jak długo spełniony jest określony warunek. Pętla ta ma następującą postać:

<pre>
<b>while</b> <i>warunek</i><b>:</b>
    blok instrukcji wykonywanych  
    tak długo dopóki warunek  
    jest spełniony
</pre>

Proszę zwrócić uwagę na dwukropek po warunku oraz wcięcie bloku — obowiązują tu te same zasady definiowania bloków, co w przypadku instrukcji `if`. Przykładowy kod:

```python
liczba = 0
while liczba < 1 or liczba > 10:
     liczba = int(input("Podaj liczbę całkowitą od 1 do 10: "))
print("Twoja liczba to", liczba)
```
W powyższym przykładzie użytkownik będzie proszony o podawanie liczby tak długo jak wartość zmiennej `liczba`, do której jest przypisywana wartość będzie albo mniejsza od 1 albo większa od 10.

Warunek w pętli **while** sprawdzany jest na samym początku, przed pierwszym wykonaniem tej pętli. Oznacza to, że pętla może nie być wykonana ani razu, jeżeli warunek już na samym początku nie będzie spełniony. Proszę zwrócić uwagę na pierwszą linijkę powyższego przykładu `liczba = 0`. Definiuje ona zmienną `liczba` i ustawia jej wartość na zero, co gwarantuje, że podczas pierwszego sprawdzenia warunek pętli **while** będzie spełniony (0 < 1), czyli użytkownik zostanie przynajmniej raz poproszony o podanie liczby.

## Przerwanie pętli

Standardowe zakończenie pętli **while** następuje w momencie kiedy warunek ma wartość `False`. Gdy ma on wartość `True`, blok pętli wykonywany jest w całości. Nie zawsze jest to pożądane. Dlatego możliwe jest przerwanie wykonywania pętli wewnątrz jej bloku za pomocą instrukcji `**break**`. Zobaczmy przykład prymitywnej wersji gry w oko:

```python
suma = 0  
podana_liczba = int(input("Podaj liczbę: "))  
while podana_liczba != 0:  
    suma += podana_liczba  # ten zapis to skrócona wersja przypisania postaci suma += suma + podana_liczba
    if suma > 21:  
        print("Przekroczyłeś 21 i przegrałeś!")  
        suma = 0  
        break  
    podana_liczba = int(input("Podaj liczbę (0 aby zakończyć): "))  
print("Twój wynik to", suma)
```

Normalne przerwanie pętli nastąpi w momencie gdy użytkownik wprowadzi liczbę 0 (nie będzie wtedy spełniony warunek `podana_liczba != 0`). Jednakże gdy obliczona suma przekroczy 21, pętla zostanie zatrzymana w sposób nadzwyczajny za pomocą polecenia break. W obu przypadkach program będzie kontynuowany od pierwszego polecenia poza blokiem pętli (`print("Twój wynik to", suma)`).

Po zakończonym bloku pętli możliwe jest dodanie polecenia **`else:`** wraz z następującym po nim blokiem, który zostanie wykonany wyłącznie wtedy gdy pętla zakończyła się normalnie (czyli nie poprzez polecenie `break`). Korzystając z tego można zapisać powyższy przykład w nieco bardziej elegancki sposób:

```python
suma = 0  
podana_liczba = int(input("Podaj liczbę: "))  
while podana_liczba != 0:  
    suma += podana_liczba  
    if suma > 21:  
        print("Przekroczyłeś 21 i przegrałeś!")  
        break  
    podana_liczba = int(input("Podaj liczbę (0 aby zakończyć): "))  
else:  
    print("Wygrałeś! Twój wynik to", suma)
```

Ostatnia linijka zostanie wypisana wyłącznie w sytuacji gdy pętla zakończy się podaniem zera, a nie poprzez przekroczenie 21.

### Kontynuacja pętli

Inną instrukcją używaną do kontrolowania wykonywania pętli jest **`continue`** . Jeśli interpreter Pythona natrafi na `continue` gdzieś w środku iteracji pętli, to pomija wszystkie pozostałe instrukcje i przechodzi do następnej iteracji. Przykład:

```python
i = -11  
while i < 10:  
    i += 1  
    if i == 0:  
        continue  
    print(1 / i)
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
