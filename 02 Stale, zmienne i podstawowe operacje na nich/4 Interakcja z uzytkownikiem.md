---
parent: Stałe, zmienne i podstawowe operacje na nich
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Interakcja z użytkownikiem

Do tej pory skupialiśmy się na części back-endowej kodu (zobacz [Kuchnia i jadalnia](../00%20Algorytmy/3%20Kuchnia%20i%20jadalnia)). W najprostszych przypadkach pisanie poleceń Pythona w konsoli lub notatniku Jupyter pozwala zobaczyć wynik ostatnio ocenianego wyrażenia. Jednak w pełnych programach nie działa to w ten sposób. Potrzebujemy sposobu na interakcję z użytkownikiem naszego programu. Później, gdy zdobędziecie więcej doświadczenia, będziecie mogli spróbować stworzyć elegancki graficzny interfejs użytkownika lub użyć stron internetowych do tego celu. Na razie jednak pozostaniemy przy najprostszym rozwiązaniu: funkcjach `print` i `input`.

## Funkcja `print`

Funkcja `print` służy do drukowania stałych i zmiennych na ekranie. Domyślnie wypisuje ona na ekranie wszystkie wartości podane jako jej argumenty, oddzielając je spacjami. Na koniec drukuje ona znak nowej linii, tak że kolejne wywołania funkcji `print` będą argumenty w kolejnych liniach.

Istnieje możliwość zmiany znaku, jakim oddzielane są kolejne wartości do wydrukowania — zastępując domyślną spację dowolnym tekstem. W tym celu po argumentach do wydrukowania należy dopisać `sep='nowy łącznik'`. Podobnie można zmienić znaki drukowane na końcu (domyślnie przejście do nowej linii), dodając `end='nowy koniec'`. Na przykład:

```python
print(1, 2, 3, sep='...')            # 1...2...3
print(1, 2, 3, end='X')              # 1 2 3X
print(1, 2, 3, sep='...', end='XX')  # 1...2...3XX
```

W dwóch ostatnich przypadkach, nie zostanie wydrukowany znak nowej linii. Kolejne wywołanie funkcji `print` spowoduje drukowanie tekstu w tej samej linijce.

Warto pamiętać, że znak nowej linii, albo do łańcuch podany jako `end` będzie wydrukowany zawsze — nawet gdy nie zostanie podany żaden argument. Zatem wywołanie `print()` spowoduje po prostu przejście do nowej linii.

## Wprowadzanie danych z klawiatury

Do tej pory wartości zmiennych definiowane były w kodzie programu:

```python
zmienna1 = 1  
zmienna2 = 2
```

W rzeczywistych programach dane zazwyczaj są pobierane z zewnętrznych źródeł — mogą to być dane wprowadzone bezpośrednio przez użytkownika (w konsoli tekstowej, okienku graficznym, poprzez formularz na stronie WWW itp.), ale też mogą one być odczytane z pliku, przesłane z urządzenia zewnętrznego (np. aparatury pomiarowej), ściągnięte z internetu, podane jako argument wywołania programu uruchamianego z [wiersza poleceń](https://pl.wikipedia.org/wiki/Wiersz_polece%C5%84).

Dobrze napisany program powinien być niezależny od metody wprowadzania danych. Jak to dokładnie osiągnąć omówimy później. Poniżej zostanie omówione w jaki sposób odczytywać dane wprowadzane przez użytkownika bezpośrednio z klawiatury, jednak już **od samego początku należy zwrócić uwagę by ten etap był wydzielony od części obliczeniowej, podobnie jak wypisywanie wyniku na ekranie za pomocą funkcji `print`**.

Do wprowadzania danych z klawiatury służy funkcja `input`. Używa się jej w następujący sposób:

```python
wprowadzona_wartosc = input("Pytanie: ")
```

Argumentem tej funkcji (tekst umieszczony w nawiasach) jest pytanie jakie zostanie wyświetlone użytkownikowi. Kiedy zostanie ono wydrukowane, program zatrzyma się i będzie czekał na wprowadzenie dowolnego ciągu znaków przez użytkownika (ciąg ten powinien zostać zakończony wciśnięciem klawisza Enter). Następnie wprowadzona wartość zostanie _zwrócona_ przez funkcję `input`, czyli umieszczona gdzieś w pamięci i udostępniona np. do przypisania do zmiennej, w celu jej dalszego wykorzystania (w powyższym przykładzie zmienna o nazwie `wprowadzona_wartosc` będzie wskazywała na ciąg wprowadzony przez użytkownika).

Należy zwrócić uwagę, że w Pythonie 3 funkcja `input` zawsze zwraca łańcuch tekstowy, czyli zmienną typu `str`. Jeżeli potrzebujemy wartość liczbową, należy ją skonwertować na właściwy typ, tak jak to zostało już opisane wcześniej:

```python
odleglosc = float(input("Podaj odległość pomiędzy punktami [m]: "))
```

W tym przykładzie zostanie wyświetlona użytkownikowi prośba o podanie odległości, a następnie wprowadzona przez niego wartość zostanie od razu przekazana jako argument „funkcji” `float` w celu zamiany jej na liczbę rzeczywistą. Istotne jest tutaj, że w tym momencie nie mamy żadnej kontroli nad tym czy użytkowniki wprowadzi poprawną wartość, którą da się skonwertować na liczbę rzeczywistą. Jeżeli tak nie będzie, program zostanie przerwany z komunikatem błędu (proszę sprawdzić). W późniejszej części kursu zostanie opisana metoda poradzenia sobie z tym problemem.

## Kuchnia i jadalnia jeszcze raz!

Tak jak napisałem wcześniej, dobrym nawykiem jest oddzielanie części służącej wprowadzaniu i wyświetlaniu danych od części obliczeniowej. Dzięki temu w przyszłości dużo łatwiej będzie zmienić nasz program np. w taki sposób by dane odczytywał z jednego pliku i wyniki zapisywał do innego (zostanie to omówione później). Tak więc kiepsko napisanym programem jest:

```python
cale = 2.54 * float(input("Podaj długość w centymetrach: "))  
print("Długość w calach wynosi:", cale)
```

Znacznie lepiej wygląda:

```python
# Wprowadzanie danych  
centymetry = float(input("Podaj długość w centymetrach: "))  
  
# Część obliczeniowa  
cale = 2.54 * centymetry  
  
# Prezentacja wyniku  
print("Długość w calach wynosi:", cale)
```

Proszę już **od samego początku** zwrócić uwagę by pisać programy w ten drugi sposób!

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
