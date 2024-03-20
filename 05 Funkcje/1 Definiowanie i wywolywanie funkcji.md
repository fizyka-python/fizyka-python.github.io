---
parent: Funkcje
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Definiowanie i wywoływanie funkcji

Funkcja to wydzielony fragment kodu, który można wielokrotnie używać w różnych miejscach programu. Do tej pory kilkukrotnie pokazane była wykorzystanie funkcji, np. `print`, `len`, `range` itd. Nie trzeba było jej pisać samodzielnie, bo zrobili to już twórcy Pythona. Wystarczyło, wiedzieć jak one działają. Większość funkcji wymaga informacji z zewnątrz — liczb, tekstów, innych obiektów — są one podawane jako *argumenty funkcji*. Większość zwraca również jakiś wynik, który np. można przypisać do zmiennej, lub wykorzystać bezpośrednio w wyrażeniu.

## Definiowanie funkcji

W każdym współczesnym języku programowania istnieje możliwość samodzielnego definiowania funkcji. Bez nich praca zespołowa nad nawet średnim programem byłaby prawie niemożliwa. Nowe funkcje należy tworzyć zawsze gdy jesteśmy w stanie wydzielić fragment kodu, który wykonuje pewną określoną, zdefiniowaną operację dla określonych danych (i ewentualnie zwraca wynik). Także w przypadku, gdy pisząc program widzimy potrzebę użycia identycznego fragmentu kodu kilkukrotnie, należy umieścić go w osobnej funkcji — dzięki temu kod ten wystarczy napisać raz i w prosty sposób można go wykorzystać wielokrotnie.

Funkcje definiujemy za pomocą słowa kluczowego **`def`**:

```python
def nazwa_funkcji(argument1, argument2...):
    blok zawierający komendy
    wykonywane w funkcji
```

Nazwa funkcji oraz nazwy argumentów muszą spełniać dokładnie takie same zasady jak nazwy zmiennych. Na przykład poniżej znajduje się definicja funkcji drukująca napis w ramce:

```python
def wydrukuj_w_ramce(tekst):
    linia = "+-" + "-" * len(tekst) + "-+"
    print(linia)
    print("|", tekst, "|")
    print(linia)
```

Kiedy już funkcja została zdefiniowana, wywołuje się ją, podając jej nazwę, po której występują nawiasy okrągłe zawierające argumenty:

```python
wydrukuj_w_ramce("Cześć!")

wydrukuj_w_ramce("Jak się masz?")
```

**Uwaga!** Nawet w przypadku gdy funkcja nie przyjmuje żadnych argumentów, jej wywołanie wymaga podania nawiasów, nawet gdy w nich nic nie ma:

```python
def powitaj():
   print("Jak się masz?")

powitaj()
```

### Zwracanie wartości

Funkcje mogą też zwracać wartości jako wynik swojego działania. Służy do tego słowo kluczowe **`return`**, które może pojawić się wyłącznie wewnątrz funkcji. Po tym słowie kluczowym umieszczamy wartość do zwrócenia. Np.

```python
def suma(liczba1, liczba2):
    return liczba1 + liczba2
```

Wywołując taką funkcję, zwrócony przez nią wynik można w dowolny sposób wykorzystać np. przypisując do zmiennej lub używając bezpośrednio w wyrażeniu (było to już wielokrotnie demonstrowane np. przy użyciu funkcji `len` albo `range`). W przypadku powyższej funkcji może to mieć postać:

```python
liczba1 = float(input("Podaj pierwszą liczbę: "))
liczba2 = float(input("Podaj drugą liczbę: "))

print("Suma tych liczb to:", suma(liczba1, liczba2))
```

Wewnątrz funkcji komenda **`return`** może się znajdować w dowolnym miejscu — także w bloku warunkowym, bądź wewnątrz pętli. W każdym przypadku spowoduje ona natychmiastowe opuszczenie funkcji — wykonanie pętli zostanie przerwane, a polecenia znajdujące się poniżej nie zostaną wykonane. Np:

```python
def iloraz(dzielna, dzielnik):
    if dzielnik == 0:
        return
    iloraz = dzielna / dzielnik
    return iloraz
```

Sama komenda **`return`** bez podanej żadnej wartości do zwrócenia, spowoduje zwrócenie wartości `None`. Podobnie dzieje się gdy funkcja zakończy się bez komendy **`return`** (tak jak w pierwszym przykładzie funkcja `wydrukuj_w_ramce`). Zatem w Pythonie każda funkcja zwraca swój wynik — domyślnie jest to `None`, oznaczające Nic.

Funkcja może też zwrócić kilka wyników jednocześnie. W tym celu po komendzie return należy podać wszystkie wyniki oddzielone przecinkiem. Np.

```python
def suma_i_roznica(liczba1, liczba2):
    suma = liczba1 + liczba2
    roznica = liczba1 - liczba2
    return suma, roznica
```

Wywołując taką funkcję można jej wynik przypisać do dwóch zmiennych, rozdzielonych przecinkiem:

```python
suma21, roznica21 = suma_i_roznica(2, 1)
```

Można też wyniki takiej funkcji przypisać do jednej zmiennej, lub użyć bezpośrednio w wyrażeniu. W takim przypadku zostanie on potraktowany jako krotka zawierająca daną liczbę elementów:

```python
wynik = suma_i_roznica(5, 3)    # wynik = (8, 2)
print(type(wynik))              # tuple
```

Użyta w powyższym przykładzie funkcja `type` zwraca typ wartości podanej jako jej argument.

### Zmienne lokalne i globalne

Zmienne zdefiniowane poza funkcjami (tak jak we wszystkich wcześniejszych lekcjach) są to *zmienne globalne*. Dostępne są one w całym programie od momentu ich definicji (przypisania wartości). W niektórych powyższych przykładach zmienne były definiowane także wewnątrz funkcji. Są to *zmienne lokalne* — są one widoczne wyłączne wewnątrz funkcji i po jej opuszczeniu są one niszczone. Argumenty funkcji także traktowane są jako zmienne lokalne (o wartościach zdefiniowanych w momencie wywołania funkcji).

Jeżeli wewnątrz i na zewnątrz funkcji istnieją zmienne o takich samych nazwach, to przypisane wartości do zmiennej lokalnej nie spowoduje zmiany zmiennej globalnej:

```python
def funkcja():
   zmienna = 2
   print("Zmienna lokalna:", zmienna)    # 2

zmienna = 1
funkcja()
print("Zmienna globalna:", zmienna)      # 1
```

Dwie zmienne w powyższym przykładzie mają taką samą nazwę. Są one jednak zupełnie od siebie niezależne. Wewnątrz funkcji nie ma dostępu do zmiennej globalnej, gdyż jest ona „zasłonięta” przez zmienną lokalną o tej samej nazwie. Jeżeli nie przypisujemy żadnej wartości do zmiennej wewnątrz funkcji, to możemy odczytać i wykorzystać wartość zmiennej globalnej:

```python
def funkcja():
    print("Zmienna globalna:", zmienna)    # 1

zmienna = 1
funkcja()
```

**Uwaga!** Aby zmienna była potraktowana jako zmienna lokalna wystarczy, że jest to niej przypisana wartość gdziekolwiek wewnątrz funkcji. Poniższy kod nie zadziała:

```python
def funkcja():
    print("Zmienna globalna:", zmienna)    # BŁĄD — zmienna lokalna nie jest jeszcze zdefiniowana
    zmienna = 2

zmienna = 1
funkcja()
```

Możliwe jest wymuszenie traktowania zmiennych wewnątrz funkcji jako globalne za pomocą komendy **`global`**, po której następuje lista nazw zmiennych globalnych.Przypisanie do nich wartości wewnątrz tej funkcji powoduje zmianę zmiennej globalnej:

```python
def funkcja():
   global zmienna
   zmienna = 2
   print("Zmienna globalna:", zmienna)    # 2

zmienna = 1
funkcja()
print("Zmienna globalna:", zmienna)       # 2
```

**<u>Ważna zasada!</u>**

Każdy dający się wydzielić fragment kodu należy umieścić w osobnej funkcji. Należy też zwrócić uwagę na to by funkcje wykonujące obliczenia nie drukowały niczego na ekranie ani nie zmieniały żadnych zmiennych globalnych (generalnie należy unikać stosowania słowa kluczowego **`global`**). Pisząc funkcję często nie jesteśmy w stanie przewidzieć ile razy będzie ona wykonana. Mogą to być tysiące razy — w takim przypadku jakikolwiek komunikat wewnątrz funkcji zostanie wypisany tysiące razy. Ogólnie, fragmenty programu odpowiedzialne za obliczenia oraz za interakcję z użytkownikiem (np. poprzez funkcje `print` oraz `input`) powinny być wyraźnie od siebie oddzielone. Dzięki temu w przyszłości możliwa i stosunkowo prosta będzie zmiana sposobu komunikacji z użytkownikiem, np. na wersję okienkową albo za pośrednictwem strony internetowej. W żadnym razie nie wolno w funkcjach, których celem nie jest bezpośrednio i wyłącznie wczytywanie danych z klawiatury stosować funkcji `input`. Wszystkie niezbędne dane muszą być podane jako argumenty funkcji, a wynik zwrócony za pomocą **`return`**.

## Wywoływanie funkcji

Wywołanie funkcji zawsze odbywa się poprzez podanie jej nazwy, po której występują nawiasy okrągłe. Wewnątrz tych nawiasów umieszczone są argumenty funkcji. Ich ilość musi być identyczna jak ilość argumentów podanych przy definicji funkcji (z wyjątkiem argumentów domyślnych i funkcji o zmiennej liczbie argumentów, które są opisane poniżej).

Argumenty do funkcji można przekazywać na dwa sposoby — poprzez pozycję oraz nazwę. Aby to wyjaśnić, załóżmy, że mamy zdefiniowaną funkcję:

```python
def funkcja(a, b, c, d, e):
   blok funkcji
```

Przyjmuje ona 5 argumentów. W podstawowym sposobie wywołania funkcji, podajemy w nawiasach 5 wartości oddzielonych od od siebie przecinkami:

```python
funkcja(1, 2, 3, 4, 5)
```

Wtedy pierwszy argument ( `a`) przyjmie dla danego wywołania wartość 1, drugi ( `b`) 2 itd. Wywołując funkcję, jej argumenty możemy także przekazywać przez nazwę podając `nazwa_argumentu=wartość` (z pojedynczym znakiem `=` jak w komendzie przypisania do zmiennej):

```python
funkcja(a=1, c=3, b=2, e=5, d=4)
```

W takim przypadku nie ma znaczenia kolejność w jakiej podaliśmy argumenty. Argument `a` przyjmie wartość 1, `b` — 2, `c` — 3, `d` — 4 i `e` — 5\. Możliwe jest także połączenie obu powyższych sposobów. Wtedy w pierwszej kolejności podajemy dowolną ilość argumentów przez pozycje, a następnie argumenty przez nazwę (bez konieczności zachowania kolejności:

```python
funkcja(1, 2, d=4, c=3, e=5)
```

W tym przypadku wartości 1 i 2 zostaną przypisane do argumentów `a` i `b` (gdyż one występują w definicji jako pierwszy i drugi argument), zaś pozostałe argumenty przekazane zostały przez nazwę (czyli `c` — 3, `d` — 4 i `e` — 5).

**Uwaga**! Kiedy zaczniemy podawać argumenty używając ich nazw, nie wolno w tym samym wywołaniu powrócić do podawania pozycyjnego. Spowoduje to błąd składni.

### Argumenty domyślne

Często zdarza się tak, że niektóre argumenty funkcji mają sensowne wartości domyślne. Wtedy w momencie definicji funkcji możemy podać te wartości domyślne za pomocą znaku `=`:

```python
def funkcja(a, b, c, d=0, e=None):
   blok funkcji
```

Istotne jest to, że wszystkie argumenty z wartościami domyślnymi muszą być na końcu listy argumentów. Oznacza to, że jeżeli dla jakiegokolwiek argumentu podany wartość domyślną, każdy następny argument też musi mieć jakąś wartość domyślną.

Wywołując tak zdefiniowaną funkcję, możemy te argumenty pominąć. Wtedy przy wywołaniu przyjęte zostaną ich wartości domyślne:

```python
funkcja(1, 2, 3)
```

Przy powyższym wywołaniu za wartość argumentu `d` zostanie przyjęte 0, zaś argumentu `e` — `None`. Wywołanie:

```python
funkcja(1, 2, 3, 4)
```

W wywołaniu tym argument `d` będzie miał wartość 4, zaś `e` pozostanie przy wartości domyślnej.

W przypadku użycia argumentów domyślnych, bardzo przydatne jest podawanie argumentów przez nazwę. Zobaczmy następujący przykład wywołania:

```python
funkcja(1, 2, 3, e=5)
```

W tym przypadku argument `d` zachowa swoją wartość domyślną, zaś argument `e` przyjmie wartość podaną w wywołaniu (5). Dzięki temu w Pythonie często stosuje się funkcje z bardzo dużą liczbą argumentów, z których większość ma wartości domyślne. Wywołując taką funkcję można w łatwy sposób zmieniać tylko te argumenty, które trzeba.

**Uwaga!** Wartości argumentów domyślnych są wyliczane w momencie definiowania funkcji, a nie jej wywołania. Z tego powodu nie należy stosować typów zmienialnych (list i słowników) jako argumentów domyślnych. Zamiast

```python
def funkcja(liczby=[1, 2, 3]):
    ciało funkcji
```

powinno się napisać

```python
def funkcja(liczby=None):
    if liczby is None:
        liczby = [1, 2, 3]
    ciało funkcji
```

## Rekurencja

W celu rozwiązania problemu funkcja może wywoływać samą siebie. Taką funkcję nazywamy _funkcją rekurencyjną_. Przykład — obliczanie silni:

```python
def silnia(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * silnia(n-1)
    else:
        return None
```

Aby funkcja rekurencyjna działała prawidłowo, każde jej kolejne wywołanie musi nastąpić dla innej wartości parametru sterującego rekurencją (w powyższym przykładzie jest to: `silnia(n-1)`). Musi być również zagwarantowane zatrzymanie kolejnych wywołań funkcji, gdy wartość parametru sterującego rekurencją osiągnie zadaną wartość (w przykładzie nastąpi to dla _n_ równego 1).


---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
