---
parent: Exceptions
grand_parent: Technologie Informatyczne II
nav_order:  3
---

# Zgłaszanie wyjątków

Niejednokrotnie może się zdarzyć sytuacja, że samodzielnie chcemy zgłosić sytuację wyjątkową. Na przykład, rozpatrzmy funkcję do wprowadzania liczby całkowitej:

```python
def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Niepoprawna liczba. Zwracam 0.")
        return 0
```

Załóżmy, że wymagamy by liczba ta była z zakresu 1–10. Rozsądne jest, by w sytuacji gdy warunek ten nie jest spełniony, wygenerowany został wyjątek `ValueError`. Możemy taki wyjątek _zgłosić_ (wygenerować) za pomocą instrukcji **`raise`**:

```python
raise TypWyjątku(komunikat)
```

Typ wyjątku to jeden ze standardowych typów opisanych wcześniej, zaś _komunikat_ to opcjonalny komunikat, który pojawi się w przypadku gdy wyjątek nie zostanie obsłużony. Istnieje możliwość tworzenia własnych typów wyjątków (podobnie jak w ogóle tworzenia własnych typów zmiennych), ale jest to zagadnienie z zakresu programowania obiektowego i wybiega poza zakres niniejszego kursu — na chwilę obecną sugeruję wybranie najwłaściwszego typu spośród wyjątków standardowych.

Korzystając z tego, powyższa funkcja mogłaby wyglądać następująco:

```python
def input_int(prompt, min=1, max=10):
    try:
        liczba = int(input(prompt))
        if liczba < min or liczba > max:
            raise ValueError("Liczba poza zakresem")
    except ValueError:
        print("Niepoprawna liczba. Zwracam 0.")
        return 0
    else:
        return liczba
```

Nie ma obowiązku by zgłoszony wyjątek został w tej samej funkcji obsłużony. Proszę przepisać i uruchomić następujący program:

```python
def dziesiec_minus(liczba):
    if liczba < 0 or liczba > 10:
        raise ValueError("Liczba poza zakresem")
    return 10 - liczba

print(dziesiec_minus(2))
print(dziesiec_minus(12))  # spowoduje przerwanie programu, gdyż wyjątek nie został obsłużony
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
