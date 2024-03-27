---
parent: Tablice numeryczne i tworzenie wykresów
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# NumPy — rachunki numeryczne na tablicach liczb

## Pakiet Numpy

Moduł [Numpy](http://numpy.scipy.org/) jest podstawowym zestawem narzędzi dla języka Python umożliwiającym zaawansowane obliczenia matematyczne, w szczególności do zastosowań naukowych (tzw. _obliczenia numeryczne_, jak mnożenie i dodawanie macierzy, diagonalizacja czy odwrócenie, całkowanie, rozwiązywanie równań, itd.). Daje on nam do dyspozycji specjalizowane typy danych, operacje i funkcje, których nie ma w typowej instalacji Pythona. Natomiast moduł [Scipy](http://scipy.org/) pozwala na dostęp do bardziej złożonych i różnorodnych algorytmów wykorzystujących narzędzia dostarczone w Numpy.

Przedstawimy tutaj tylko wstęp do Numpy. Wynika to z faktu, że opisanie licznych funkcji dostępnych w bibliotece Numpy jest ogromną pracą, która zupełnie nie ma sensu — równie dobrze można zajrzeć bezpośrednio do źródła, [http://docs.scipy.org/doc/numpy/reference/](http://docs.scipy.org/doc/numpy/reference/).

Najważniejszym obiektem, na którym bazuje pakiet Numpy i szereg pakietów z niego korzystających jest klasa `ndarray` wprowadzająca obiekty `array`. Obiekty `array` możemy traktować jako uniwersalne pojemniki na dane w postaci _macierzy_ (czyli _wektorów_ lub _tablic_). W porównaniu ze standardowymi typami sekwencji Pythonowych (lista, krotka) jest kilka różnic w operowaniu tymi obiektami:

1. obiekty przechowywane w tablicy `array` muszą być wszystkie tego samego typu;
2. obiekty `array` zachowują swój rozmiar; przy zmianie rozmiaru takiego obiektu powstaje nowy obiekt, a obiekt sprzed zmiany zostaje usunięty;
3. obiekty `array` wyposażone są w bogaty zestaw funkcji operujących na wszystkich przechowywanych w obiekcie danych, specjalnie optymalizowanych do przetwarzania dużych ilości danych. Jak to działa zostanie zaprezentowane poniżej.

## Tworzenie tablic

Najprostszym sposobem stworzenia tablicy Numpy jest wywołanie funkcji `array` z argumentem w postaci listy liczb. Jeśli zamiast listy liczb użyjemy listy zawierającej inne listy (tzw. listy _zagnieżdżone_), to otrzymamy tablicę wielowymiarową. Na przykład jeśli listy są podwójnie zagnieżdżone, to otrzymujemy tablicę dwuwymiarową (macierz).

```python
import numpy as np  # np is a popular alias for numpy
A = np.array([ 1, 3, 7, 2, 8])
B = np.array([[1, 2, 3], [4, 5, 6]])
print(A, end='\n\n')
print(B, end='\n\n')
print(B.transpose())
```

Wynikiem będzie:

```
[1 3 7 2 8]

[[1 2 3]
 [4 5 6]]

[[1 4]
 [2 5]
 [3 6]]
```

Innym sposobem tworzenia tablicy jest funkcja `numpy.arange`, która działa analogicznie do `range`, tyle tylko, że zwraca tablicę NumPy zamiast listy, i dopuszcza parametry ułamkowe — a nie tylko całkowite.

Argumenty są takie same:

1. indeks początkowy \[opcjonalnie, domyślnie 0\]
2. indeks następny po końcowym
3. krok \[opcjonalnie, domyślnie 1\]

```python
print(np.arange(1000000))
print(np.arange(0.1, 0.2, 0.01))
print(np.arange(0.9, 0.0, -0.1))
```

```
[     0      1      2 ... 999997 999998 999999]
[0.1  0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19]
[0.9 0.8 0.7 0.6 0.5 0.4 0.3 0.2 0.1]
```

Jak było już wspomniane, w przypadku tablicy `array` typowe operacje matematyczne możemy przeprowadzić dla wszystkich elementów tablicy przy użyciu jednego operatora lub funkcji. Zachowanie takie jest odmienne niż w przypadku list czy innych sekwencji Pythona. Jeśli chcielibyśmy na przykład pomnożyć wszystkie elementy listy `L` przez liczbę `a`, musimy użyć pętli:

```python
L = [1, 3, 5, 2, 3, 1]
for k, x in enumerate(L):
    L[k] = a * x
```

Można też zapisać to zwięźlej, używając wyrażenia generatorowego:

```python
L = [1, 3, 5, 2, 3, 1]
L = [a * x for x in L] # w odróżnieniu od wersji z pętlą, tu L będzie zastąpione przez nową listę
L[::] = [a * x for x in L] # a to zachowa tożsamość listy L, tak jak wersja z pętlą
```

jest to jednak poniekąd tylko uproszczony zapis pętli. Natomiast mnożenie wszystkich elementów tablicy `M` przez liczbę `a` wygląda tak:

```python
M = numpy.array([1, 3, 5, 2, 3, 1])
M = a * M
```

Operacje wykonywane od razu na całych macierzach mają wiele zalet. Kod programu jest prostszy i krótszy, przez co mniej podatny na błędy. Poza tym nie musimy przejmować się konkretną realizacją danej operacji — robi to za nas funkcja pakietu Numpy, która jest specjalnie optymalizowana, żeby działała jak najszybciej.

Inne funkcje do tworzenia tablic to: [`linspace`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html), [`zeros`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html), [`ones`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.ones.html), [`eye`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.eye.html), [`meshgrid`](http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html).

## Kształt tablicy

Jak już pewnie zauważyliście, tablice NumPy mogą się odznaczać różną liczbą wymiarów:

- jednowymiarowa tablica `A` to odpowiednik wektora, jej elementy `A[k]` ponumerowane są wartością pojedynczego indeksu (wskaźnika), w zakresie od 0 do `len(A) - 1` — analogicznie jak lista w ,,zwykłym" Pythonie
- dwuwymiarowa tablica, powiedzmy: `M`, to odpowiednik _macierzy_ o elementach `M[k,l]`; jeżeli ich zakresy to `k = 0, ...K, l = 0, ...L`, to posiada ona `K * L` elementów
- w ogólności, żeby opisać _kształt_ tablicy NumPy, podaje się krotkę liczb całkowitych dodatnich, opisujących zakres wartości jej poszczególnych wskaźników (a liczba elementów tej krotki, to oczywiście liczba wskaźników numerujących element tablicy). Krotka ta dana jest przez atrybut `M.shape`:

```python
M = np.array([[0.61064052, 0.51970673, 0.06353282],
              [0.50159111, 0.83545043, 0.10928144]])
print(M.shape)
```

```
(2,  3)
```

Kształt tablicy jednowymiarowej jest oczywiście krotką jednoelementową (a nie — pojedynczą liczbą); zapisuje się ją jako `(n,)`.

**Uwaga**: funkcja `len(A)` zastosowana do tablicy NumPy `A` zwróci jedynie liczbę możliwych wartości **pierwszego wskaźnika**, a nie — liczbę elementów tablicy. Liczba elementów tablicy dane jest przez atrybut `A.size`.

Szereg funkcji tworzących nowe tablice przyjmuje kształt tablicy jaka ma powstać (tj. krotkę liczb naturalnych) jako argument (lub jeden z argumentów), np. `numpy.zeros(shape), numpy.ones(shape)` tworzą odpowiednio tablicę zer i tablicę jedynek o dowolnym zadanym kształcie. Istnieją też operacje pozwalające uzyskać tablicę o zmienionym kształcie, wypełnioną danymi z tablicy już istniejącej:

```python
M.reshape((3,  2))
# array([[0.61064052, 0.51970673],
#        [0.06353282, 0.50159111],
#        [0.83545043, 0.10928144]]))

M.reshape((6,))
# array([0.61064052, 0.51970673, 0.06353282, 0.50159111, 0.83545043, 0.10928144])
```

zamiast tego ostatniego, można użyć `M.flatten()` czyli operacji ,,spłaszczenia" tablicy.

**Uwaga:** Rozmiary tablicy przed i po przekształceniu (tzn. liczba elementów) muszą się zgadzać.

Można również nadać nową wartość atrybutowi `shape`:

```python
M.shape = (2, 3)
# array([[0.61064052, 0.51970673, 0.06353282],
#        [0.50159111, 0.83545043, 0.10928144]])
```

ale wówczas zmieniamy kształt istniejącej tablicy. Naturalnie również w tym przypadku rozmiary (początkowy i końcowy) muszą się zgadzać.

## Różne tablice jako widoki na dane

W Pythonie operacje na danych typów złożonych i modyfikowalnych (np. listy, które mogą zmieniać swoją zawartość z zachowaniem tożsamości) mogą albo zmieniać zawartość obiektu, albo tworzyć nowy obiekt z zawartością opartą na zawartości danego. Przy czym jeżeli pod różnymi nazwami występuje _ten sam obiekt_, to w obu przypadkach jest to obiekt tego samego typu. W NumPy jest nieco inaczej: tablice w rozmaity sposób przekształcone (np. przez operację `reshape()`) często okazują się być różnymi _widokami_ na _te same dane_. Dla przykładu:

```python
A = np.arange(24)
print(A)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]

B = A.reshape(6, 4)
print(B)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22 23]]

A[-1] = 0
print(B)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]
#  [16 17 18 19]
#  [20 21 22  0]]

print(A is B)    # False
print(A == B)    # False
```

Zmieniliśmy element tablicy `A`, ale zmianie uległ również odpowiadający mu element tablicy `B` — chociaż na niej nie wykonaliśmy żadnej operacji, i jest ona innego kształtu niż `A`.

Takie zachowanie wynika (m. in.) z chęci optymalizacji: NumPy jest pomyślany do operacji na raczej dużych tablicach danych, usiłuje się więc unikać zbędnego kopiowania danych pomiędzy tablicami, angażującego pamięć operacyjną i inne zasoby systemowe. Należy jednak pamiętać, że jeżeli potrzebna jest nam rzeczywiście niezależna od oryginału tablica zawierająca te same co on (lub pochodne od nich) dane, to lepiej te dane _explicite_ skopiować (np. funkcją `numpy.copy` — lub uważnie zapoznać się z dokumentacją używanych funkcji i metod, zwłaszcza że reguły rządzące tym, czy mamy do czynienia z kopią danych czy nowym widokiem nie są zbyt konsekwentne.

## Wydobywanie danych

<img style="float: right;" src="macierz.png" alt="Macierz" width="30%">

### Pojedyncze liczby

Dostęp do elementów (i pod-tablic) jest możliwy poprzez użycie notacji indeksowej ( `tablica[i]`) jak i wycinkowej ( `tablica[i:j]`).

Indeksy dotyczące poszczególnych wymiarów można podać w pojedynczej parze nawiasów oddzielone przecinkami.

Dostęp do pojedynczego elementu:

```python
A =  np.array([[1, 2, 3], [4, 5, 6]])
print(A)
# [[1 2 3]
#  [4 5 6]]

print(A[0, 2])  # 3
```

Macierz `A` jest tablicą dwuwymiarową, i sposób numerowania zawartych w niej obiektów jest następujący: pierwszy indeks przebiega pierwszy wymiar (wybiera wiersz), drugi indeks przebiega drugi wymiar (wybiera kolumnę).

### Pod-tablice

Dostęp do pod-tablic:

```python
print(A[1])              # 1 line
# [4 5 6]

print(A[1, :])           # line 1, all columns of
# [4 5 6]

print(A[:, 1])           # all lines, column 1
# [2 5]
```

Jak widać, ograniczenie się do pojedynczego punktu w danym wymiarze, powoduje degenerację tego wymiaru. Uzyskuje się tablicę, w której liczba wymiarów jest mniejsza o jeden.

```python
print(A[:, 1:])
# [[2 3]
#  [5 6]]
```

W pierwszym wymiarze (wiersze) bierzemy wszystko, natomiast w drugim od 1 do końca. Efektywnie wycinamy kolumnę 0.

### Indeksowanie tablic tablicami

Do wybrania elementów z tablicy można tez użyć innej tablicy. Może to być

- tablica liczb — wówczas są one traktowane jako indeksy. Wybieramy te elementy, które uzyskalibyśmy indeksując każdym z indeksów z osobna
- tablica wartości logicznych ( _boolean_) rozmiaru macierzy z danymi. Wybieramy te elementy, którym odpowiada `True` w macierzy indeksującej.

**Uwaga:** W wyniku dostajemy tablicę jedno wierszową.

Przykład:

```python
print(A)
# [[1 2 3]
#  [4 5 6]]

print(A >  2)
# [[False False  True]
#  [ True  True  True]]

print(A[A > 2])
# [3 4 5 6]

print(A[A % 2 == 0])
# [2 4 6]
```

### Przypisywanie nowych wartości do tablic

Możecie przypisać nowe wartości do wybranych elementów tablicy, używając takiego samego indeksowania jak do odczytu:

```python
A = np.array([[1,2,3], [4,1,1], [0,8,9]])
print(A)

A[1, 1:] = [5, 0]
print(A)

A[A == 0] = 6, 7
print(A)

A[A < 5] = 0
print(A)
```

Warunkiem jest, aby liczba przypisywanych wartości była równa liczbie wybranych elementów. W przeciwnym razie Numpy zgłosi błąd.

Więcej informacji można znaleźć na stronie <http://docs.scipy.org/doc/numpy/user/basics.indexing.html>.


## Operacje na danych w tablicach Numpy

### Arytmetyka

Aby umożliwić wygodną obróbkę danych ujętych w tablice Numpy, podstawowe operacje arytmetyczne są w Numpy rozszerzone tak, by można było nimi obejmować zawartość tablicy bez (zazwyczaj) pisania jakichkolwiek pętli. Na przykład, tablicę można pomnożyć przez liczbę, dodać do niej liczbę, itd. i operacja ta będzie dotyczyła wszystkich elementów tablicy:

```python
M = np.arange(24).reshape((4, 6)) * 2 + 1
print(M)
# [[ 1  3  5  7  9 11]
#  [13 15 17 19 21 23]
#  [25 27 29 31 33 35]
#  [37 39 41 43 45 47]]
```

Co więcej, można również wykonywać operacje arytmetyczne na dwóch (i więcej) tablicach:

```python
N = 1 / M
print(N)
# [[1.         0.33333333 0.2        0.14285714 0.11111111 0.09090909]
#  [0.07692308 0.06666667 0.05882353 0.05263158 0.04761905 0.04347826]
#  [0.04       0.03703704 0.03448276 0.03225806 0.03030303 0.02857143]
#  [0.02702703 0.02564103 0.02439024 0.02325581 0.02222222 0.0212766 ]]

print(N * M)
# [[1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1.]]
```

A więc np. tablice o zgodnych kształtach można dodawać do siebie, mnożyć itd. i operacje te będą wykonywane parami na wszystkich elementach.

> Uwaga: nie jest to tak całkiem realizacja przyjętych w matematyce definicji operacji arytmetycznych na wektorach, macierzach itd. W szczególności, w matematyce [mnożenie macierzy](https://pl.wikipedia.org/wiki/Mno%C5%BCenie_macierzy) nie oznacza mnożenia elementów parami. W NumPy mnożenie macierzowe jest możliwe za pomocą nowego operatora '@':

```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[-4, 2], [3, -1]])

print(A * B)
# [[-4  4]
#  [ 9 -4]]

print(A @ B)
# [[2 0]
#  [0 2]]
```

### Funkcje matematyczne

Ponadto, moduł `numpy` zawiera realizacje podstawowych funkcji pojawiających się we wzorach fizycznych i matematycznych, takich jak `sin`, `cos`, `exp`, `log` i sporo innych, w wersji dostosowanej do operowania na danych tablicowych, również element po elemencie. Jeszcze więcej takich funkcji dostarczają inne (pod)moduły z pakietu Numpy, oraz pakiet Scipy (Scientific Python). Na przykład:

```python
X = np.arange(0, 2 * np.pi, 0.1)

print(np.sin(X)**2 + np.cos(X)**2)
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
#  1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.
#  1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
```

Powyższy rachunek sprawdza słuszność wzoru na ,,jedynkę trygonometryczną" w zakresie jednego okresu, z rozdzielczością 0.1 radianów ;)

## Dlaczego warto używać Numpy?

Pierwsza przyczyna, zazwyczaj najmniej istotna, to **wydajność**. Jeśli mamy pomnożyć 100 elementów, to szybkość operacji na pojedynczym elemencie nie ma znaczenia. Podobnie jest z rozmiarem pojedynczego elementu. Jeśli elementów jest 106, to również wtedy narzut nie ma większego znaczenia. Policzmy: 1000000 razy 12 bajtów, to 12 MB. Typowy komputer ma obecnie 1-4 GB pamięci, czyli używamy od 1,2% do 0,27% dostępnej pamięci — jaki problem? Dopiero gdy miejsce zajmowane przez dane jest tego samego rzędu co całość dostępnej pamięci, to czy pojedyncza komórka zajmuje 8 czy 16 bajtów, zaczyna mieć znaczenie.

Druga przyczyna, istotna ze względu na przyjemność pracy, to **notacja** obiektowa i infixowa. Ta pierwsza to oczywiście „notacja z kropką” — dostęp do metod i atrybutów na obiekcie. Jej użycie, zwłaszcza w połączeniu z dopełnieniem TAB-em upraszcza pisanie. Przykład notacji obiektowej:

```python
a.transpose().min()
# instead of
numpy.min(numpy.transpose(a))
```

Ta druga (infixowa) to stara dobra „notacja matematyczna” — umiejscowienie operatorów dwuargumentowych pomiędzy obiektami na które działają. Przykład notacji infixowej:

```python
a + b * c
# zamiast
numpy.add(a, numpy.multiply(b, c))
```

Oczywiście notacja obiektowa i infixowa jest używane wszędzie w Pythonie, ale warto wspomnieć, że Numpy od niej nie odchodzi. Niemniej Numpy odchodzi od Pythonowej interpretacji niektórych działań. W Pythonie takie operacje jak mnożenie list wywodzą się z działań na ciągach znaków. W obliczeniach numerycznych podstawą są działania na elementach, tak więc w Numpy wszystkie operatory domyślnie działają na indywidualnych parach elementów.

Trzecia przyczyna, chyba najważniejsza, to **biblioteka funkcji numerycznych**. Odejście od obiektowości danych pozwala na eksport wartości i komunikację z bibliotekami napisanymi w zupełnie innych językach programowania. Na przykład Scipy może korzystać z biblioteki [LAPACK](http://www.netlib.org/lapack/) (Linear Algebra PACKage, napisanej w Fortranie 77). To że funkcje napisane w różnych językach mogą wymieniać się danymi w pamięci bez skomplikowanego tłumaczenia danych, wynika z faktu, że tak jak to w poprzednim podrozdziale było opisane, ostatecznie wszystkie liczby są w formacie akceptowanym przez procesor.

Możliwość użycia kodu napisanego w C czy Fortranie pozwala na wykorzystanie starych, zoptymalizowanych, sprawdzonych rozwiązań.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).  

Oryginalny autor Robert J. Budzyński. Źródło: [https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy](https://brain.fuw.edu.pl/edu/index.php/PPy3/NumPy).
