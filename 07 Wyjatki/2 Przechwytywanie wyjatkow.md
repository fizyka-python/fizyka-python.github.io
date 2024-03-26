---
parent: Exceptions
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Przechwytywanie wyjątków

Nie na wszystkie sytuacje wyjątkowe mamy wpływ pisząc program. Rozpatrzmy na przykład następującą funkcję:

```python
def input_float(prompt):
    return float(input(prompt))
```

Celem tej funkcji jest odczytanie z klawiatury liczny rzeczywistej. Jednakże nie wiemy co wprowadzi użytkownik. Jeżeli poda on łańcuch znaków, którego nie można przekonwertować na liczbę rzeczywistą, program zostanie przerwany. Nie jest to poprawne zachowanie. Prawidłowy program powinien w tej sytuacji poinformować użytkownika, że wprowadzony tekst jest niepoprawny i np. poprosić o ponowne jego wprowadzenie.

Aby móc samodzielnie zaprogramować zachowanie programu w sytuacjach wyjątkowych stosuje się następującą konstrukcję:

```python
try:
    blok komend, które mogą spowodować wyjątek
except TypWyjątku:
    blok komend wykonywanych w przypadku wystąpienia wyjątku
except InnyTypWyjątku:
    blok komend wykonywanych w przypadku wystąpienia wyjątku innego typu
```

Blok except musi być przynajmniej jeden.

Korzystając tego funkcja wprowadzająca liczbę mogłaby wyglądać następująco:

```python
def input_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Niepoprawna liczba. Zwracam 0.")
        return 0.

```

Funkcja ta po kolej wywołuje funkcję `input`, która prosi o podanie ciągu znaków. Następnie ten ciąg znaków jest konwertowany do typu `float`. Wynik konwersji jest zwracany jaki wynik funkcji. Jeżeli którykolwiek z tych etapów się nie powiedzie, wygenerowany zostanie wyjątek. Jeżeli jest to wyjątek typu `ValueError` (w tym przypadku może się pojawić na skutek nieudanej konwersji), to zostanie on _przechwycony_ i wydrukowany zostanie stosowny komunikat oraz funkcja zwróci wartość 0.

Wyjątki nie muszą być przechwytywane w tej samej funkcji, w której się pojawiły. Rozpatrzmy następujący program:

```python
def input_float(prompt):
    return float(input(prompt))

def popros_o_liczbe():
    return input_float("Podaj liczbę: ")

try:
    liczba = popros_o_liczbe()
    wynik = 10 + liczba
except ValueError:
    wynik = 0.

print(liczba)
```

W przypadku wprowadzenia błędnej wartości, funkcja `input_float` zostanie natychmiast przerwana. Przerwana zostanie także funkcja `popros_o_liczbe`. Cały program nie zakończy się jednak błędem, gdyż wyjątek jest przechwycony w kodzie głównym, który wywołuje funkcję `popros_o_liczbe`.

Konstrukcja **try**... **except** może mieć dodatkowo blok **else**, który jest wywoływany gdy nie wystąpił żaden wyjątek. Na przykład:

```python
try:
    liczba = popros_o_liczbe()
    wynik = 10 + liczba
except ValueError:
    wynik = 0.
else:
    print("Dziękuję")
```

Komunikat _Dziękuję_ zostanie wydrukowany wyłącznie gdy podano prawidłową liczbę rzeczywistą.

Komenda/y **`except`** przechwytuje wyłącznie wyjątki danego typu. Inne wyjątki są przez nią ignorowane i albo spowodują zatrzymanie programu, albo zostaną przechwycone w innym miejscu. Rozpatrzmy następujący kod:

```python
def input_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Niepoprawna liczba. Zwracam 0.")
        return 0.

try:
    liczba = input_float("Podaj liczbę: ")
except KeyboardInterrupt:
    liczba = -1
```

Jeżeli w funkcji `input_float` pojawi się wyjątek `ValueError`, to wypisze ona komunikat i zwróci wartość 0. Jednakże naciśniecie kombinacji klawiszy Ctrl+C lub Ctrl+Delete spowoduje wygenerowanie wyjątku `KeyboardInterrupt`, który przerwie bieg tej funkcji. Zostanie on jednak przechwycony w miejscu, w którym ta funkcja została wywołana i do zmiennej `liczba` zostanie przypisana wartość –1.

## Lepiej prosić o wybaczenie niż o pozwolenie

W Pythonie wyjątki są czymś normalnym i należy je stosować. Przyjrzyjmy się funkcji, która zwraca odwrotność liczby podanej jako jej argument:

```python
def odwrotnosc(x):
    return 1 / x
```

Załóżmy, że chcemy zabezpieczyć się na wypadek gdyby podanym argumentem było 0. Załóżmy, że chcemy w takim przypadku zwrócić wartość 0 (co oczywiście matematycznie jest niepoprawne, ale może być w pewnych sytuacjach przydatne). Możemy zrobić to na dwa sposoby:

```python
def odwrotnosc(x):
    if x == 0:
        return 0
    else:
        return 1 / x
```

bądź

```python
def odwrotnosc(x):
    try:
        return 1 / x
    except ZeroDivisionError:
        return 0
```

W pierwszym przypadku „prosimy o pozwolenie”, czyli za pomocą warunku sprawdzamy czy operację da się wykonać. W drugim z kolei „błagamy o wybaczenie” — czyli po prostu wykonujemy operację, a w razie problemów rozwiązujemy je. Generalnie drugi sposób jest lepszy. W przypadku bardziej rozbudowanych programów skutkuje bardziej czytelnym kodem oraz łatwiej dodać obsługę innych wyjątków, których w momencie pisania pierwotnej wersji programu nie jesteśmy w stanie przewidzieć. Ponadto nie wszystko jesteśmy w stanie sprawdzić wcześniej, a nawet jeśli jest to możliwe, to może to być niewiarygodne — dotyczy to w szczególności operacji na plikach, które zostaną omówione w kolejnym wykładzie. Jeżeli na przykład najpierw sprawdzimy czy dany plik istnieje, a później go otwieramy, to istnieje niezerowe prawdopodobieństwo, że w ciągu mikrosekund jakie następują pomiędzy sprawdzeniem istnienia pliku a jego otwarciem zostanie on skasowany (prawdopodobieństwo to nie jest wcale takie małe jeżeli np. dysk komputera jest uszkodzony). W takiej sytuacji otrzymamy pozwolenie na wykonanie operacji (warunek potwierdzi istnienie pliku), ale ona sama się nie powiedzie. Korzystając z przechwytywania wyjątków zabezpieczamy się przed taką sytuacją. Innym powodem, dla którego „błaganie o wybaczenie” jest lepsze, jest wydajność programu — sprawdzając najpierw warunek musimy wykonać pewne operacje, które potem najprawdopodobniej są powtarzane. Gdy korzystamy z wyjątków, daną operację wykonujemy tylko raz. Różnica może wynosi kilka mikrosekund, ale staje się zauważalna, gdy daną funkcję powtarzamy kilkadziesiąt milionów razy (co w większych programach do analizy danych bądź obliczeń naukowych nie jest niespotykane).

## Jak posprzątać po bałaganiarzu?

Instrukcja **`try`** posiada jeszcze jedną, opcjonalną klauzulę, która służy do definiowania działań, mających na celu dokonanie koniecznych pod wszelkimi względami porządków. Na przykład:

```python
try:
    liczba = float('dwa')  # to spowoduje wyjątek ValueError
finally:
    print('Żegnaj, świecie!')
```

Klauzula **`finally`** jest wykonywana niezależnie od tego, czy pojawił się wyjątek, czy też nie. Kod zawarty w tym bloku jest również wykonywany, gdy blok try zostanie „opuszczony” za pomocą instrukcji **`break`** lub **`return`**.

Instrukcja **`try`** musi posiadać co najmniej jeden blok **`except`** lub jeden blok **`finally`**.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
