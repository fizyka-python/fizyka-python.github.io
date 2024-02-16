---
parent: Python — wprowadzenie i instalacja
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Szybkie prototypowanie z Jupyter Notebooks

## Czym jest Jupyter?

Jupyter to projekt typu open-source, który pozwala łatwo łączyć tekst [Markdown](https://pl.wikipedia.org/wiki/Markdown) i wykonywalny kod źródłowy Pythona na jednej kanwie zwanej **notatnikiem**. Może on zawierać: dane wejściowe i wyjściowe kodu, sformatowany tekst, obrazy, filmy, ładne równania matematyczne i wiele więcej. Kod komputerowy jest wykonywalny, co oznacza, że można uruchomić fragmenty kodu bezpośrednio w dokumencie i wyświetlić dane wyjściowe tego kodu. Ten interaktywny sposób przetwarzania danych, w połączeniu z narracją multimedialną, pozwala na opowiadanie historii (nawet samemu sobie) z dodatkowymi mocami!

Program Jupyter można uruchomić za pomocą wiersza poleceń i korzystać z niego w przeglądarce internetowej. Alternatywnie, można bezpośrednio tworzyć, przeglądać i edytować notatniki w VS Code.

## Tworzenie notatnika w VSCode

Notatnik Jupyter można utworzyć, uruchamiając **Jupyter: Create Blank New Jupyter Notebook** z palety poleceń (`Ctrl+Shift+P`) lub tworząc nowy plik `.ipynb` w swoim obszarze roboczym.

![Blank Jupyter Notebook](jupyter-code-cells-01.png)

Następnie wybierz jądro za pomocą selektora jądra w prawym górnym rogu.

![Kernel Picker](jupyter-kernel-picker.png)

Jeśli masz istniejący notatnik Jupyter, możesz go otworzyć, klikając plik prawym przyciskiem myszy i otwierając go za pomocą VS Code lub za pomocą eksploratora plików VS Code.

## Komórki notatnika

Notatnik Jupyter używa *komórek*: bloków, które dzielą fragmenty tekstu i kodu. Każda zawartość tekstowa jest wprowadzana do komórki *Markdown*: zawiera ona tekst, który można formatować za pomocą prostych znaczników, aby uzyskać nagłówki, pogrubienie, kursywę, wypunktowanie, hiperłącza i inne.

Markdown jest łatwy do nauczenia, sprawdź składnię na stronie ["Daring Fireball"](https://daringfireball.net/projects/markdown/syntax) (autorstwa Johna Grubera). Kilka wskazówek:

* aby utworzyć tytuł, użyj hasha na początku linii: `# Title`
* aby utworzyć następny nagłówek, użyj dwóch hashy (i tak dalej): `## Nagłówek`
* aby pochylić słowo lub frazę, umieść je w gwiazdkach (lub myślnikach): `*italic*` lub `_italic_`
* aby je pogrubić, otocz je dwiema gwiazdkami: `**pogrubione**`
* aby utworzyć hiperłącze, użyj nawiasów kwadratowych i okrągłych: `[tekst hiperłącza](url)`

Obliczalna zawartość jest wprowadzana w komórkach kodu. Będziemy używać jądra IPython ("jądro" to nazwa używana dla silnika obliczeniowego), ale powinieneś wiedzieć, że Jupyter może być używany z wieloma różnymi językami obliczeniowymi. To niesamowite.

Komórka kodu wyświetli znak wejściowy, taki jak ten:

`W [ ]:`

Po dodaniu kodu i wykonaniu go, Jupyter doda numer ID do komórki wejściowej i wygeneruje wynik oznaczony w ten sposób:

`Out [1]:`

### Działające komórki

Gdy masz już Notatnik, możesz uruchomić komórkę kodu za pomocą ikony **Run** po lewej stronie komórki, a dane wyjściowe pojawią się bezpośrednio pod komórką kodu.

Do uruchamiania kodu można również użyć skrótów klawiaturowych. W trybie poleceń lub edycji użyj kombinacji klawiszy `Ctrl+Enter`, aby uruchomić bieżącą komórkę lub `Shift+Enter`, aby uruchomić bieżącą komórkę i przejść do następnej.

![Uruchom komórkę kodu Jupyter](jupyter-code-cells-03.png)

Możesz uruchomić wiele komórek używając **Run All**, **Run All Above** lub **Run All Below**.

### Tryby komórek kodu

Podczas pracy z komórkami kodu, komórka może znajdować się w trzech stanach: niewybrana, tryb poleceń i tryb edycji. Bieżący stan komórki jest wskazywany przez pionowy pasek po lewej stronie komórki kodu i obramowania edytora. Gdy pasek nie jest widoczny, komórka jest niezaznaczona.

Gdy komórka jest zaznaczona, może znajdować się w dwóch różnych trybach. Może znajdować się w trybie poleceń lub w trybie edycji. Gdy komórka znajduje się w trybie poleceń, można na niej operować i akceptować polecenia klawiaturowe. Tryb ten jest oznaczony pionowym paskiem po lewej stronie komórki.

Gdy komórka znajduje się w trybie edycji, ciągły pionowy pasek jest połączony z obramowaniem wokół edytora komórki. W tym trybie można modyfikować zawartość komórki (kod lub Markdown).

Aby przejść z trybu edycji do trybu poleceń, naciśnij klawisz `Esc`. Aby przejść z trybu poleceń do trybu edycji, naciśnij klawisz `Enter`. Możesz także użyć myszy, aby **zmienić tryb**, klikając pionowy pasek po lewej stronie komórki lub poza obszarem kodu/Markdown w komórce kodu.

### Przełączanie między kodem a Markdown

Edytor Notatnika umożliwia łatwą zmianę komórek kodu pomiędzy Markdown i kodem. Kliknięcie selektora języka w prawym dolnym rogu komórki umożliwia przełączanie między Markdown i, w stosownych przypadkach, dowolnym innym językiem obsługiwanym przez wybrane jądro.

![Zmień język](jupyter-language-picker-01.png)

Do zmiany typu komórki można również użyć klawiatury. Gdy komórka jest zaznaczona i w trybie poleceń, klawisz `M` przełącza typ komórki na Markdown, a klawisz `Y` przełącza typ komórki na kod.

Po ustawieniu Markdown można wprowadzić sformatowaną zawartość Markdown do komórki kodu.

![Surowy Markdown wyświetlany w komórce kodu](jupyter-markdown-not-rendered.png)

Aby wyrenderować komórki Markdown, można zaznaczyć znacznik wyboru na pasku narzędzi komórki lub użyć skrótów klawiaturowych `Ctrl+Enter` i `Shift+Enter`.

![Wyrenderowany Markdown wyświetlany w komórce kodu](jupyter-markdown-rendered.png)

## Eksplorator zmiennych i przeglądarka danych

W notatniku Python możliwe jest przeglądanie, sprawdzanie, sortowanie i filtrowanie zmiennych w bieżącej sesji Jupyter. Wybierając ikonę **Variables** na głównym pasku narzędzi po uruchomieniu kodu i komórek, zobaczysz listę bieżących zmiennych, która będzie automatycznie aktualizowana, gdy zmienne będą używane w kodzie. Okienko zmiennych zostanie otwarte w dolnej części notatnika.

eksplorator zmiennych](jupyter-variable-explorer-01.png)

![Eksplorator zmiennych](jupyter-variable-explorer-02.png)


## Interaktywne obliczenia w notatniku

Możesz przetestować komórkę kodu, pisząc kilka operacji arytmetycznych. Operatory Pythona to:

| Operator | Znaczenie                        |
| -------- | -------------------------------- |
| `+`      | dodawanie                        |
| `-`      | odejmowanie                      |
| `*`      | mnożenie                         |
| `/`      | dzielenie                        |
| `**`     | wykładnik (`3**2` oznacza 3²)    |
| `%`      | modulo (reszta z dzielenia)      |
| `//`     | dzielenie podłogowe (bez reszty) |

Utwórz nową komórkę kodu Pythona i wpisz:

```python
1 + 2
```

Następnie naciśnij `Shift+Enter`. Co widzisz? Wypróbuj inne obliczenia, w tym bardziej złożone, takie jak:

```python
2 + 2 * 2
```

lub

```python
9**1/2
```

Jaki jest wynik ostatniej operacji? Dlaczego jest to `4,5`? Czy 9 do potęgi 1/2 nie jest po prostu pierwiastkiem kwadratowym z 9, czyli 3? Porównaj z tym:

```python
9**(1/2)
```

Widzisz, Python wie o [arytmetyce/kolejności operacji](https://en.wikibooks.org/wiki/Arithmetic/Order_of_Operations).


## Ćwiczenia

Użyj notatnika Jupyter (jako kalkulatora), aby rozwiązać następujące dwa problemy:

1. Objętość kuli o promieniu *r* wynosi 4/3 *π* *r*³. Jaka jest objętość kuli o średnicy 6,65 cm?
   Dla wartości *π* użyj 3.1415926 (na razie).

2. Załóżmy, że cena okładkowa książki wynosi 24,95 EUR, ale księgarnie otrzymują 40% zniżki.
   Koszt wysyłki wynosi 3 EUR za pierwszy egzemplarz i 75 centów za każdy kolejny.
   Jaki jest całkowity koszt hurtowy dla 60 egzemplarzy?


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).

Based on a [lecture by Loreena Barba](https://github.com/engineersCode/EngComp1_offtheground) and VS Code documentation at <https://code.visualstudio.com/docs/datascience/jupyter-notebooks>.
