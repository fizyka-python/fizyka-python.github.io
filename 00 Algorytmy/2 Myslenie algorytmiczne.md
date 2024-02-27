---
parent: Algorytmy
grand_parent: Technologie Informatyczne II
nav_order: 2
---

# Myślenie algorytmiczne

Ważnym czynnikiem programów komputerowych napisanych w języku formalnym jest fakt, że muszą one być nieludzko precyzyjne. Wyobraźcie sobie, że prosicie kogoś „*Proszę zamknąć okno*”. Jeśli w pokoju są dwa okna i tylko jedno z nich jest otwarte, osoba ta domyśli się, że prosicie o zamknięcie okna, które jest otwarte. Jednak komputer wykonujący program nie jest tak sprytny! Zamiast tego musicie podać zestaw formalnych instrukcji:

1. Podejdź do *pierwszego okna*.
2. Jeśli *pierwsze okno* jest otwarte, zamknij *pierwsze okno*.
3. Podejdź do *drugiego okna*.
4. Jeśli *drugie okno* jest otwarte, zamknij *drugie okno*.

Dzielenie pojedynczego zadania zamknięcia okna na sekwencję bardziej precyzyjnych instrukcji nazywane jest podejściem **top-down**. Poniżej przeanalizujemy więcej problemów w ten sposób. Aby skupić się na operacjach, a nie na notacji, nie będziemy używać języka formalnego. Będziemy jednak trzymać się jednej prostej zasady: **nie używamy przyimków**. Zauważcie, że w powyższym przykładzie nie użyliśmy przyimka „*to*”, lecz zastosowaliśmy zamiast tego jawne nazwy *pierwsze okno* i *drugie okno*. Jeśli musimy operować na danych, których nie znamy w momencie pisania algorytmu (co zdarza się częściej niż rzadziej), używamy **etykiet**.

Aby to zilustrować, napiszmy algorytm *top-down*, który oblicza pole prostokąta. Aby to zrobić, musimy określić, jakich danych potrzebujemy na początku (nasze **wejście**) i jaki wynik powinien zostać wygenerowany (co jest **wyjściem** algorytmu).

![Prostokąt a b](rectangle.png)

```
WEJŚCIE:
  a - szerokość prostokąta
  b - wysokość prostokąta

KROKI:
  1. Oblicz a×b i nazwij wynik „polem”.

WYJŚCIE:
  pole
```

Jak widać, użyliśmy **etykiet** `a` i `b` dla danych wejściowych, które <u>muszą być dostarczone podczas wykonywania programu</u> (w tej chwili nie martwmy się jak), a także wykonaliśmy pewne obliczenia i **etykietowaliśmy** (nazwaliśmy) ich wynik jako `pole`. Na koniec możemy podać tę nazwaną wartość jako wynik algorytmu.

Spójrzmy na inny przykład. Weźmy pod uwagę dwie liczby *x*₁ i *x*₂, i obliczmy ich średnią. Algorytm wyglądałby następująco:

```
WEJŚCIE:
  x₁, x₂ - dane liczby

KROKI:
  - Oblicz x₁ + x₂ i nazwij wynik „suma”.
  - Oblicz „średnią” jako suma / 2.

WYNIK:
  średnia
```

To, co widzicie powyżej, to przepis. Zawiera on dwa proste kroki. Spróbujcie go prześledzić i zobaczyć, jak zmieniają się oznaczone wartości:

| KROK                    | *x*₁  | *x*₂  | *total* | *average* | WYNIK |
| ----------------------- | ----- | ----- | ------- | --------- | ----- |
| **WEJŚCIE**             | **2** | **4** |         |           |       |
| *suma* = *x*₁ + *x*₂.   | 2     | 4     | 6       |           |       |
| *średnia* = *suma* / 2. | 2     | 4     | 6       | 3         |       |
| **WYNIK**               | 2     | 4     | 6       | 3         | **3** |

Teraz coś bardziej skomplikowanego: weźmy dwie liczby i określmy, jaka jest wartość większej z nich:

```
WEJŚCIE:
  x₁, x₂ - podane liczby

KROKI:
  - Jeśli x₁ > x₂, określ wartość x₁ na etykietą „większa”.
    W przeciwnym razie niech etykieta „większa” oznacza x₂.

WYJŚCIE:
  większa
```

Prześledźmy to dla przykładowych danych:

| KROK                         | *x*₁  | *x*₂  | *większa* | WYNIK |
| ---------------------------- | ----- | ----- | --------- | ------|
| **WEJŚCIE**                  | **2** | **1** |           |       |
| Sprawdzanie, czy *x*₁ > *x*₂ | 2     | 1     |           | tak   |
| *większa* = *x*₁             | 2     | 1     | 2         |       |
| **WYJŚCIE**                  | 2     | 1     | 2         | **2** |

Jak to będzie wyglądać dla innych danych?

| KROK                         | *x*₁  | *x*₂  | *larger* | WYNIK |
| ---------------------------- | ----- | ----- | -------- | ----- |
| **WEJŚCIE**                  | **2** | **3** |          |       |
| sprawdzanie, czy *x*₁ > *x*₂ | 2     | 3     |          | nie   |
| *większa* = *x*₂             | 2     | 3     | 3        |       |
| **WYJŚCIE**                  | 2     | 3     | 3        | **3** |

Powyższy algorytm nie został wykonany liniowo (po kolei). W zależności od jakiegoś warunku wykonywana była jedna lub druga operacja. Nazywa się to *warunkiem*.

Spójrzmy na bardziej zaawansowany przykład — rozwiązanie [równania kwadratowego](https://pl.wikipedia.org/wiki/R%C3%B3wnanie_kwadratowe) postaci *a* *x*² + *b* *x* + *c* = 0. Mam nadzieję, że pamiętacie jak się to robi! Najprostszym i najbardziej naiwnym algorytmem byłoby:

```bash
WEJŚCIE:
  a, b, c - współczynniki równania.

KROKI:
  - Oblicz Δ = b² - 4×a×c
  - Oblicz pierwsze rozwiązanie x₁ = (-b - √Δ) / (2×a) # pamiętajcie o zasadach kolejności obliczeń
  - Oblicz drugie rozwiązanie x₂ = (-b + √Δ) / (2×a)   # i w razie potrzeby użyjcie nawiasów

WYJŚCIE:
  x₁, x₂
```

Tekst po `#` jest tylko komentarzem a nie częścią algorytmu.

Jeśli interesuje nas rozwiązania zespolone, to jest to (prawie) wystarczające. Jeśli jednak zależy nam tylko na rozwiązaniach rzeczywistych, musimy pamiętać, że ich istnienie zależy od wartości *Δ*. Musimy więc użyć warunków:

```
WEJŚCIE:
  a, b, c - współczynniki równania.

KROKI:
  - Oblicz Δ = b² - 4×a×c
  - Jeśli Δ > 0, wykonaj następujące czynności:
    │ - Oblicz pierwsze rozwiązanie x₁ = (-b - √Δ) / (2×a)
    │ - Oblicz drugie rozwiązanie x₂ = (-b + √Δ) / (2×a)
    W przeciwnym razie, jeśli Δ = 0:
    │ - Oblicz jedyne rozwiązanie -b / (2×a) i nazwij je "x₁" dla spójności
    │ - Oznacz drugie rozwiązanie (x₂) jako nieistniejące
    Jeśli żadne z powyższych nie jest prawdziwe (ponieważ Δ < 0), to:
    │ - Oznacz oba rozwiązania x₁ oraz x₂ jako nieistniejące

WYJŚCIE:
  x₁, x₂
```

Powyżej widać, że algorytm może przyjąć trzy ścieżki, w zależności od wartości *Δ*. Co ważne, w każdej ścieżce wymieniamy zarówno *x*₁, jak i *x*₂. Wynika to z faktu, że zidentyfikowaliśmy oba z nich jako wyjście naszego algorytmu, więc **musimy zdefiniować takie nazwy w każdej możliwej ścieżce!** Nawet w przypadkach, gdy jeden lub oba z nich nie istnieją, oznaczamy je jako nieistniejące (w tej chwili nie musicie się martwić, jak: języki programowania pozwalają to zrobić w ten czy inny sposób).

Algorytm wygląda więc dobrze... Prześledźmy go dla kilku danych:

Rozwiązanie *x*² + 2 *x* - 8 = 0:

| KROK                           | *a*   | *b*   | *c*    | *Δ* | *x*₁ | *x*₂ | WYNIK         |     |
| ------------------------------ | ----- | ----- | ------ | --- | ---- | ---- | ------------- | --- |
| **WEJŚCIE**                    | **1** | **2** | **-8** |     |      |      |               |     |
| *Δ* = *b*² - 4×*a*×*c*         | 1     | 2     | -8     | 36  |      |      |               |     |
| Sprawdzanie, czy *Δ* > 0       | 1     | 2     | -8     | 36  |      |      | tak           |     |
| *x*₁ = (-*b* - √*Δ*) / (2×*a*) | 1     | 2     | -8     | 36  | -4   |      |               |     |
| *x*₂ = (-*b* + √*Δ*) / (2×*a*) | 1     | 2     | -8     | 36  | -4   | 2    |               |     |
| **WYJŚCIE**                    | 1     | 2     | -8     | 36  | -4   | 2    | **-4**, **2** |     |

Rozwiązanie *x*² - 2 *x* + 1 = 0:

| KROK                     | *a*   | *b*    | *c*   | *Δ* | *x*₁ | *x*₂ | WYNIK            |
| ------------------------ | ----- | ------ | ----- | --- | ---- | ---- | ---------------- |
| **WEJŚCIE**              | **1** | **-2** | **1** |     |      |      |                  |
| *Δ* = *b*² - 4×*a*×*c*   | 1     | -2     | 1     | 0   |      |      |                  |
| sprawdzanie, czy *Δ* > 0 | 1     | -2     | 1     | 0   |      |      | nie              |
| Sprawdzenie, czy *Δ* = 0 | 1     | -2     | 1     | 0   |      |      | tak              |
| *x*₁ = -*b* / (2×*a*)    | 1     | -2     | 1     | 0   | 1    |      |                  |
| *x*₂ nie istnieje        | 1     | -2     | 1     | 0   | 1    | brak |                  |
| **WYJŚCIE**              | 1     | -2     | 1     | 0   | 1    | brak | **-4**, **brak** |

Rozwiązanie *x*² + 2 *x* + 3 = 0:

| KROK                     | *a*   | *b*   | *c*   | *Δ* | *x*₁ | *x*₂ | WYNIK              |
| ------------------------ | ----- | ----- | ----- | --- | ---- | ---- | ------------------ |
| **WEJŚCIE**              | **1** | **2** | **3** |     |      |      |                    |
| *Δ* = *b*² - 4×*a*×*c*   | 1     | 2     | 3     | 0   |      |      |                    |
| sprawdzanie, czy *Δ* > 0 | 1     | 2     | 3     | 0   |      |      | nie                |
| sprawdzanie, czy *Δ* = 0 | 1     | 2     | 3     | 0   |      |      | nie                |
| *x*₁ i *x*₂ nie istnieją | 1     | 2     | 3     | 0   |      | brak | brak               |
| **WYJŚCIE**              | 1     | 2     | 3     | 0   | brak | brak | **brak**, **brak** |

Rozważmy inny przypadek: *a* = 0, *b* = 2, *c* = 3:

| KROK                     | *a*                            | *b*   | *c*   | *Δ* | *x*₁ | *x*₂ | WYNIK                               |
| ------------------------ | ------------------------------ | ----- | ----- | --- | ---- | ---- | ----------------------------------- |
| **WEJŚCIE**              | **0**                          | **2** | **3** |     |      |      |                                     |
| *Δ* = *b*² - 4×*a*×*c*   | 0                              | 2     | 3     | 4   |      |      |                                     |
| sprawdzanie, czy *Δ* > 0 | 0                              | 2     | 3     | 4   |      |      | tak                                 |
| **WYJŚCIE**              | *x*₁ = (-*b* - √*Δ*) / (2×*a*) | 0     | 2     | 3   | 4    |      | <span style="color: red">0/0</span> |

Czy widzicie, co się stało? Nasz algorytm zawiódł dla przypadku, w którym *a* = 0! Co można z tym zrobić? Cóż, musimy sprawdzić ten przypadek osobno. Zatem algorytm będzie wyglądał następująco:

```
WEJŚCIE:
  a, b, c - współczynniki równania.

KROKI:
  - Sprawdź, czy a ≠ 0, jeśli tak:
    │ - Oblicz Δ = b² - 4×a×c
    │ - Jeśli Δ > 0, wykonaj następujące czynności:
    │ │ - Oblicz pierwsze rozwiązanie x₁ = (-b - √Δ) / (2×a)
    │ │ - Oblicz drugie rozwiązanie x₂ = (-b + √Δ) / (2×a)
    │ W przeciwnym razie, jeśli Δ = 0:
    │ │ - Oblicz jedyne rozwiązanie -b / (2×a) i nazwij je "x₁" dla spójności
    │ │ - Oznacz drugie rozwiązanie (x₂) jako nieistniejące
    │ Jeśli żadne z powyższych nie jest prawdziwe (ponieważ Δ < 0), to:
    │ │ - oznacz x₁, ani x₂ jako nieistniejące
    W przeciwnym razie (w odniesieniu do warunku a ≠ 0, więc faktycznie zajmiemy się przypadkiem a = 0 poniżej):
    │ - Oblicz jedyne rozwiązanie równania liniowego x₁ = -c / b
    │ - x₂ oczywiście nie istnieje (ale musimy pamiętać, aby o tym wspomnieć)

WYJŚCIE:
  x₁, x₂
```

To, co widać powyżej, to **zagnieżdżony warunek**. Najpierw sprawdzamy jeden warunek (*a* ≠ 0), a w jednym z przypadków sprawdzamy inny (*Δ* > 0 lub *Δ* = 0). Kiedy będziecie pisali własne algorytmy, wyraźnie zaznaczcie, który blok jest zagnieżdżony w którym!

Prześledźcie ten algorytm dla równań *x*²&nbsp;+&nbsp;2&nbsp;*x*&nbsp;-8&nbsp;=&nbsp;0, *x*²&nbsp;-&nbsp;2*x*&nbsp;+&nbsp;1&nbsp;=&nbsp;0, *x*²&nbsp;+&nbsp;2&nbsp;*x*&nbsp;+&nbsp;3&nbsp;=&nbsp;0 oraz 2&nbsp;*x*&nbsp;+&nbsp;4&nbsp;=&nbsp;0 (*a*&nbsp;=&nbsp;0).

## Podsumowanie

Podczas kursu nauczycie się formalnego języka programowania. Oznacza to, że będziecie musieli dokładnie przestrzegać jego reguł semantycznych, w których każdy pojedynczy znak ma znaczenie. Jednocześnie będziecie musieli napisać precyzyjny algorytm realizujący dane zadanie. Rozważanie tych dwóch kwestii na raz może być z początku zbyt dużym wyzwaniem. Z tego powodu proponuję najpierw pisać algorytmy przy użyciu języka naturalnego, jak pokazano powyżej. Musicie zawsze jasno określić wejście, wyjście i precyzyjnie napisać wszystkie niezbędne kroki. Pamiętajcie również, aby oznaczyć wszystkie wartości pośrednie i zawsze używać ich nazw (nie używajcie przyimków). Gdy już to zrobicie, prześledźcie swój algorytm ręcznie, jak pokazano powyżej.

Po wykonaniu tych czynności nie powinniście mieć problemu z przepisaniem algorytmu przy użyciu formalnego języka programowania, którego zasady poznacie w nadchodzących tygodniach.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
