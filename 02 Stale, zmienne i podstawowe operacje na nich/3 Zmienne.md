---
parent: Constants, Variables and Basic Operations
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Zmienne

Napisanie jakiegokolwiek programu byłoby niemożliwe gdyby nie dało się zapamiętać wyliczonych wartości. Do tego celu służą **zmienne**.

Zmienna to nazwa (etykieta) miejsca w pamięci, które zawiera określoną wartość. Tworzy się ją za pomocą instrukcji `=` (pojedynczy znak, w odróżnieniu od opisanego wcześniej operatora porównania logicznego):

```python
a = 5  
b = 10  
c = a + b
```

Jaka będzie wartość zmiennej `c`? Można to sprawdzić albo wpisując polecenie `print(c)`, które zadziała zarówno w interaktywnej konsoli jak i w kodzie programu napisanego w edytorze, albo (wyłącznie w interaktywnej konsoli) wpisać po prostu

```python
In[4]: c
```

(`In[4]`: to tylko ilustracja tego co wypisuje konsola — nie należy tego wpisywać)
Oczywiście w każdym przypadku otrzymamy wyniki 15.

Powyższy kod działa dokładnie w sposób następujący:

1. Umieszcza liczbę 5 gdzieś w pamięci i nadaje jej etykietę `a`.
2. Umieszcza liczbę 10 gdzieś w pamięci i nadaje jej etykietę `b`.
3. Oblicza sumę wartości wskazywanej przez etykiety `a` i `b`, wynik umieszcza gdzieś w pamięci i nadaje mu etykietę `c`.

Bardzo ważną rzeczą jest to, że pojedynczy znak `\=` jest **instrukcją**, czyli bezpośrednim poleceniem wydanym komputerowi. Musi ona znajdować się zawsze w osobnej linijce i po lewej stronie może być wyłącznie nazwa zmiennej. Po prawej z kolei znajduje się **wyrażenie**, czyli coś co ma, bądź wylicza konkretną wartość (dowolnego typu). Podobnie jak w przypadku operatorów matematycznych, dobrym zwyczajem jest pisanie znaków spacji dookoła symbolu `=` (tak jak ma to miejsce we wszystkich przykładach w niniejszym wykładzie). Znacznie zwiększa to czytelność kodu.

Tę samą etykietę można wykorzystać wielokrotnie. Przyjrzyjmy się następującemu kodowi:

```python
a = 2  
a = a + 1
```

Ostatnia linijka nie jest niepoprawnym działaniem matematycznym, ale prawidłowym i często stosowanym ponownym przypisaniem. W pierwszej kolejności zostanie wykonane działanie po prawej stronie (czyli obliczona wartość wskazywana przez zmienną `a` i zapisana w gdzieś w pamięci), a następnie zmienna `a` zostanie ustawiona tak by wskazywała na tę nową wartość. Poprzednia wartość (2) zostanie uznana za już niepotrzebną i usunięta z pamięci.

Generalnie Python utrzymuje obiekty w pamięci tak długo jak istnieje choć jedna zmienna wskazująca na nie. Rozpatrzymy następujący przykład:

```python
teskt1 = "Use the Force, Luke!"  
tekst2 = tekst1
```

W tym wypadku tekst `"Use the Force, Luke!"` zostanie umieszczony w pamięci tylko raz, ale dwie zmienne będą na niego wskazywać. Jeżeli zmienną `tekst1` usuniemy:

```python
del tekst1    # polecenie del nazwa_zmiennej całkowicie ją usuwa
```

to oryginalne zdanie Obi-Wana wciąż będzie zapisane w pamięci komputera i będzie ono dostępne za pomocą zmiennej `tekst2`. Dopiero gdy i tę zmienną usuniemy lub zmienimy:

```python
text2 = 123  # Python nie wymaga by nowa wartość była tego samego typu
```


to zdanie to zostanie usunięte z pamięci (gdyż nie istnieje już zmienna na nie wskazująca) i zajmowane przez nie miejsce będzie mogło być wykorzystane ponownie.

## Przykład

Obliczmy ile czasu zajmie ciału swobodny spadek z wieżowca o wysokości 30 m. Ponieważ w ruchu jednostajnie przyspieszonym przebyta droga (w tym przypadku wysokość budynku _h_) wyraża się przez _h_ = _g_ _t_<sup>2</sup> / 2, gdzie _g_ to przyspieszenie grawitacyjne, to proste przekształcenie daje czas spadku równy _t_ = (2 _h_ / _g_)<sup>1/2</sup>. Zapiszmy to w Pythonie:

```python
g = 9.81                # przyśpieszenie grawitacyjne [m/s²]
h = 30                  # wysokość budynku [m]
t = (2 * h / g)**0.5   # wyliczony czas spadku [s]  
  
print("Czas spadku z wysokości", h, "m wynosi", t, "s.")
```

W ostatniej linijce użyliśmy funkcji `print` aby wydrukować odpowiedź w postaci pełnego zdania.

## Nazywanie zmiennych

W Pythonie nazwy zmiennych mogą być **prawie** dowolne. Muszą one jednak spełniać następujące warunki:

* nazwy zmiennych muszą składać się z liter (małych i wielkich), cyfr, oraz znaku podkreślenia _;
* pierwszy znak nie może być cyfrą;
* nazwa zmiennej nie może być taka sama jak jedno z zastrzeżonych słów kluczowych (**`and`**, **`as`**, **`assert`**, **`async`**, **`await`**, **`break`**, **`class`**, **`continue`**, **`def`**, **`del`**, **`elif`**, **`else`**, **`except`**, **`False`**, **`finally`**, **`for`**, **`from`**, **`global`**, **`if`**, **`import`**, **`in`**, **`is`**, **`lambda`**, **`nonlocal`**, **`None`**, **`not`**, **`or`**, **`pass`**, **`raise`**, **`return`**, **`True`**, **`try`**, **`while`**, **`with`**, **`yield`**).

Prawidłowymi nazwami zmiennych są zatem: `a`, `b`, `liczba1`, `pierwszy_wynik`, `_dane_tymczasowe`, `ilość_rozwiązań` (w Pythonie 3 „polskie litery” mogą być stosowane w nazwach zmiennych — jest to jednak niezalecane), `ilosc_rozwiazan`.

Nieprawidłowymi nazwami są `12malp`, `dane-tymczasowe`, `wazna_zmienna!`, `lambda`. W pierwszym przypadku nazwa zmiennej zaczyna się od cyfry, w dwóch następnych zawiera ona niedozwolony znak. Ostatni przypadek to zastrzeżone słowo kluczowe.

Poza wymogami formalnymi, istotne jest aby nazwy zmiennych były jasne i zrozumiałe. Bardzo często zdarza się, że jesteśmy zmuszeni do analizy programów napisanych przez kogoś innego. Także programy napisane przez nas samych, zapominamy po kilku tygodniach i musimy być w stanie ze zrozumieniem przeczytać ich kod. Proszę się przyjrzeć następującemu fragmentowi kodu i odpowiedzieć co on robi:

```python
z1q3z5ocdval = 35.0 
z1q3z5afdval = 12.50
z1q3p5afdval = z1q3z5ocdval * z1q3z5afdval
print(z1q3p5afdval)
```
Czy kod przedstawiony w wersji poniżej jest czytelniejszy?

```python
x = 3.14 
y = 100 
z = x * y 
print(z)
```

Pozornie wydawałoby się, że tak — zmienne są krótkie i łatwo je rozróżnić. Jednak ich znaczenie nie jest nadal jasne — powyższy kod miałby uzasadnienie gdyby `x`, `y` i `z` były współrzędnymi w przestrzeni trójwymiarowej (ale wtedy działanie `z = x * y` nie miałoby fizycznego sensu).

Co robi poniższy kod?

```python
godziny = 35.0   
stawka = 12.50   
wynagrodzenie = godziny * stawka  
print(wynagrodzenie)
```

W tym przypadku wszystko jest jasne. Podobnie w przedstawionym wcześniej przykładzie zostały użyte jednoliterowe zmienne `h`, `g`, `t`. Ich znaczenie jest jednak jasne, gdyż są to ogólnie przyjęte symbole wielości fizycznych. Proszę jednak zwrócić uwagę, że w komentarzu zostały one dodatkowo opisane oraz podana została jednostka (w fizyce jest ona kluczowa)!

> ### Uwaga!
>
> **W Pythonie w nazwach zmiennych ma znaczenie wielkość liter**. W związku  tym zmienne o nazwach `liczba`, `Liczba` i `LICZBA` są trzema różnymi i niezależnymi zmiennymi. Można to wykorzystać dla zwiększenia czytelności progamu, jednakże dobrym zwyczajem jest stosowanie wyłącznie małych liter do nazw zmiennych (nie jest to jednak niezbędny wymóg).

### Nazwy z zastosowaniem znaków spoza alfabetu łacińskiego

W Pythonie 3 możliwe jest umieszczanie liter spoza alfabetu łacińskiego w nazwach zmiennych. Zatem poniższy kod jest absolutnie poprawny:

```python
印 = print

數 = 10
印("這是一個數: ", 數)

θ = 90
印("這是一個角度: ", θ)

def 算到(一個數):
    ξ = 1
    while ξ <= 一個數:
        印(ξ)
        ξ = ξ + 1

算到(10)
```

Sami zdecydujecie czy dobrym pomysłem jest stosowanie lokalnych znaków w swoim kodzie...


## Wielokrotne przypisane

W języku Python możliwe jest, aby pojedyncza instrukcja przypisania zmieniała wartość wielu zmiennych:

```python
a, b = 0, 1
```

co jest równoważne zapisowi:

```python
a = 0 
b = 1
```

Wielokrotne przypisanie jest przydatne, gdy zachodzi potrzeba wymiany wartości dwóch zmiennych. W starszych językach programowania bez obsługi wielokrotnego przypisania wymaga to użycia zmiennej pomocniczej. W Pythonie można po prostu napisać:

```python
a, b = b, a
```

Po lewej stronie znaku `=` powinna się znajdować rozdzielona przecinkami lista nazw zmiennych. Prawa strona może być dowolnymi wyrażeniami oddzielonymi przecinkami. Ilość elementów po lewej i po prawej stronie musi być identyczna.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
