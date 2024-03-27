---
parent: Operacje na plikach
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Otwieranie plików

Praktycznie każdy program komputerowy korzysta z odczytywania i zapisywania plików na dysku. Mogą to być pliki zawierające aktualną konfigurację programu, a także pliki zawierające dane, które program przetwarza.

W Pythonie do otwarcia pliku służy komenda `open(nazwa_pliku, tryb)`, gdzie _nazwa\_pliku_ to nazwa pliku do otwarcia, zaś _tryb_ — tryb w jakim plik jest otwierany.

Nazwa pliku może zawierać opcjonalnie katalog, w którym plik się powinien znajdować — obowiązują tu standardowe reguły systemu operacyjnego

- Katalogi od plików oddziela się znakiem **`\\`** (należy go wpisać podwójnie, gdyż w łańcuchach tekstowych Pythona znak **`\`** oznacza symbol specjalny, np. **`\n`** dla oznaczenia nowej linii) w systemie Windows, bądź **`/`** w systemach MacOS i Linux.
- Jeżeli nazwa pliku zaczyna się od `X:\\` (Windows, _X_ to litera dysku), bądź **`/`** (MacOS i Linux) to traktowana jest jako pełna ścieżka. W przeciwnym wypadku plik jest lokalizowany względem bieżącego katalogu.

Tryb otwarcia pliku to łańcuch tekstowy, który może przyjąć jedną z następujących wartości:

- **`'r'`** — plik jest otwierany do odczytu,
- **`'w'`** — plik jest otwierany do zapisu od nowa — dotychczasowa zawartość pliku jest usuwana,
- **`'a'`** — plik jest otwierany do zapisu — dotychczasowa zawartość pliku jest zachowywana i nowe dane będą dopisywane na końcu pliku,
- **`'r+'`** — plik jest otwierany do odczytu i zapisu jednocześnie.

Dodatkowo, możemy do wybranego trybu dopisać znak `b`. Oznacza on otwarcie pliku w trybie binarnym — na chwilę obecną nie będziemy się nim zajmować.

Funkcja `open` zwraca zmienną typu **plik**, który jest specjalnym typem służącym do interakcji z otwartym plikiem (omówiona ona zostanie dokładnie w następnej części wykładu). Po zakończeniu odczytu/zapisu danych plik należy _zamknąć_. Szczególnie w przypadku zapisu jest to niezbędne, gdyż w przeciwnym razie nie mamy gwarancji, że dane zostaną faktycznie zapisane na dysku (dla zwiększenia wydajności Python oraz system operacyjny stosuje _buforowanie_ — zawartość pliku przechowywana jest w pamięci operacyjnej i dopiero jego zamknięcie powoduje faktyczny zapis na dysku). Do zamknięcia pliku służy metod `plik.close()`. Na przykład:

<div style="text-decoration: line-through;" onmouseover="this.style.textDecoration='none'" onmouseout="this.style.textDecoration='line-through'" markdown="1">

```python
plik = open('dane.txt', 'w')
# Zapisywanie danych...
plik.close()
```
</div>

Schemat z powyższego przykładu można spotkać w wielu samouczkach Pythona, jednakże ma on dwie istotne wady: po pierwsze musimy samodzielne pamiętać o zamknięciu pliku, po drugie jeżeli przed wywołaniem `plik.close()` ciąg komend zostanie przerwany (np. przez wyjątek), plik nie zostanie zamknięty. Z tego powodu zalecane jest, by zawsze otwierać plik korzystając z **kontekstu**, który w Pythonie tworzy się za pomocą komendy **`with`**:

```python
with open('dane.txt', 'w') as plik:
    # Blok operacji na otwartym pliku
```

Pierwsza linijka powyższego przykładu spowoduje otwarcie pliku, który wewnątrz bloku będzie dostępny pod zmienną `plik`. Po opuszczeniu bloku, plik zostanie automatycznie zamknięty — niezależnie od tego w jaki sposób ten blok został opuszczony (poprzez komendę **`return`**, wyjątek, czy też poprzez normalne zakończenie bloku). Z tego powodu proszę zapamiętać, że pliki otwieramy zawsze w następujący sposób:

```python
with open(nazwa_pliku, tryb) as nazwa_zmiennej:
    # Blok operacji na otwartym pliku
```

W kolejnych częściach wykładu omówione zostaną operacje, które można wykonywać wewnątrz utworzonego w ten sposób bloku, w zależności od trybu w jakim plik został otwarty.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
