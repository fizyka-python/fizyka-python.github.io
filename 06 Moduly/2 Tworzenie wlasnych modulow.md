---
parent: Moduły
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Tworzenie własnych modułów

Pisząc bardziej rozbudowane programy możemy tworzyć własne moduły. Dzięki temu możliwy jest podział programu na kilka plików, co w przypadku dłuższych programów jest pożądane. Ponadto możemy zebrać często używane funkcje w pojedynczy moduł i korzystać z nich wielokrotnie w różnych projektach.

Najprostszy moduł to plik źródłowy Pythona (z rozszerzeniem `.py`) umieszczony w tym samym katalogu, w którym znajduje się główny program. Wtedy możemy go zaimportować za pomocą komendy

```python
import nazwa
```

gdzie _nazwa_ to nazwa pliku bez rozszerzenia. Na przykład jeżeli mamy plik `nasz_modul.py` o następującej zawartości:

```python
def hello():
    print("Cześć")
```

to w głównym programie (w innym pliku, który bezpośrednio importujemy) możemy napisać:

```python
import nasz_modul

nasz_modul.hello()
```

## Pakiety

Istnieje też możliwość tworzenia hierarchii modułów. W tym celu należy utworzyć katalog o nazwie odpowiadającej nazwie modułu (bez żadnych rozszerzeń) i w tym katalogu umieścić plik o nazwie `__init__.py` (na początku i na końcu nazwa dwa znaki podkreślenia). Wtedy komenda

```python
import nazwa_katalogu
```

spowoduje wczytanie modułu z pliku `__init__.py`. Katalog taki nazywamy **pakietem**. Możemy w nim umieścić inne pliki źródłowe Pythona (z rozszerzeniem `.py`), które możemy importować przez

```python
import nazwa_katalogu.nazwa_pliku
```

lub w inny dowolny sposób, jak to było pokazane wcześniej. Możemy też zwiększyć ilość poziomów hierarchii, umieszczając w naszym katalogu podkatalog, w którym znowu utworzymy plik `__init__.py` (plik ten musi zawsze być obecny, nawet jeśli miałby być pusty).

Tworzenie pakietów przydatne jest w przypadku pisania bardziej rozbudowanych programów.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
