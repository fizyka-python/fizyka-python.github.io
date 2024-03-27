---
parent: Operacje na plikach
grand_parent: Technologie Informatyczne II
nav_order:  4
---

# Zapisywanie i odczytywanie obiektów Pythona

Do tej pory zostało opisane ręczne zapisywanie i odczytywanie zawartości plików. Jest to użyteczne jeżeli chcemy operować na plikach z danymi i wynikami zapisanymi w postaci zwykłego tekstu. Jednakże jeżeli chcemy zapisać/odczytać zawartość dowolnych zmiennych Pythona (np. w celu zachowania stanu programu), ręczne tworzenie tekstu oraz jego interpretacja może być uciążliwa.

Na szczęście Python zawiera szereg modułów, które znacznie ułatwiają to zadania. Najbardziej podstawowym modułem jest moduł `pickle`. Pozwala on za pomocą jednej komendy zapisać, bądź odczytać dowolną zmienną. Jego wykorzystanie najlepiej zilustruje przykład:

```python
import pickle

# Zmienna dane zawiera słownik zabranych danych, które chcemy zapisać
dane = {'a': [1,2,3], 'b': "Ala ma kota", 'c': 123}

with open('dane.pickle', 'wb') as plik_zapisywany:
    pickle.dump(dane, plik_zapisywany)
```

Funkcja `dump(zmienna, plik)` z modułu `pickle` zapisuje zawartość _zmiennej_ do podanego _pliku_. Plik musi być otwarty w trybie binarnym (dodatkowy znak `b` w trybie otwarcia). Zawartość pliku jest specyficzna dla Pythona i nie powinien on być np. otwierany w edytorze tekstowym (tak naprawdę dokładna zawartość jest bez znaczenia — ważne, że Python potrafi ją poprawnie zinterpretować). Tak utworzony plik możemy odczytać w innym programie za pomocą funkcji `load(plik)` z modułu `pickle`, która zwróci uprzednio zapisaną zmienną:

```python
import pickle

with open('dane.pickle', 'rb') as plik_odczytywany:
    dane = pickle.load(plik_odczytywany)
```

Funkcje `dump` i `load` modułu pickle możemy wywołać kilkukrotnie dla danego pliku. Wtedy zapisywane są do niego kolejne zmienne, które po kolei mogą być odczytane. Jednakże w celu zapisania ustawień programu, zalecane jest stworzenie jednego słownika zawierającego je wszystkie i jednokrotne zapisanie/wczytanie go.

Analogicznie do modułu `pickle` działają moduły `json` oraz `yaml` (ten ostatni nie jest standardowym modułem Pythona, ale w dystrybucji Anaconda jest on domyślnie zainstalowany). W odróżnieniu od modułu `pickle` wymagają one plików otwartych w trybie tekstowym (bez znacznika `b`). Utworzą one pliki tekstowe w formatach [JSON](https://pl.wikipedia.org/wiki/JSON), bądź [YAML](https://pl.wikipedia.org/wiki/YAML), które mogą być odczytane i edytowane w zewnętrznych narzędziach. Jednocześnie nie zostanie utracona łatwość zapisu odczytu w Pythonie:

```python
import yaml

# Zmienna dane zawiera słownik zabranych danych, które chcemy zapisać
dane = {'a': [1,2,3], 'b': "Ala ma kota", 'c': 123}

with open('dane.yaml', 'w') as plik_zapisywany:
    yaml.dump(dane, plik_zapisywany)

with open('dane.yaml', 'r') as plik_odczytywany:
    print(yaml.load(plik_odczytywany))
```

Powyższy kod działa tak samo jak w przypadku modułu `pickle`. Proszę jednak otworzyć plik `dane.yaml` w edytorze tekstowym — jego zawartość powinna być czytelna i możliwa do ręcznej modyfikacji.

**Uwaga!** W przypadku korzystania z modułu `json`, nie jest możliwe zapisanie zmiennej każdego typu (np. krotek, które trzeba uprzednio zamienić na listy). `pickle` oraz `yaml` nie mają tego ograniczenia.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
