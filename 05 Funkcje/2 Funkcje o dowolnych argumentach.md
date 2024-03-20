---
parent: Funkcje
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Funkcje o dowolnych argumentach

W Pythonie istnieje możliwość tworzenia funkcji o dowolnej — nieokreślonej z góry — liczbie argumentów. W tym celu, przy definiowaniu funkcji podajemy specjalny argument `*args` (ważna jest gwiazdka `*` na początku — nazwa może być dowolna, ale zwyczajowo stosuje się _args_ i zalecam trzymanie się tej konwencji):

```python
def funkcja1(*args):
    print(args)
```

Wywołując tę funkcję można podać dowolną ilość argumentów pozycyjnych. Wewnątrz funkcji argument `args` będzie **krotką** zawierającą wszystkie podane argumenty. Np.:

```python
funkcja1(1, 2, 3)    # (1, 2, 3)
```

W analogiczny sposób funkcja może przyjąć dowolną ilość argumentów podanych przez nazwę. W tym celu, definiując ją podajemy specjalny argument `**kwargs` (istotne są dwie gwiazdki `**`, nazwa _kwargs_ jest zwyczajowa):

```python
def funkcja2(**kwargs):
    print(kwargs)

```

Wywołując tę funkcję można podać dowolną ilość argumentów o dowolnej nazwie. Wewnątrz funkcji argument `kwargs` będzie **słownikiem** zawierającą wszystkie podane argumenty. Np.:

```python
funkcja2(a=1, b=2, c=3)    # {'a': 1, 'b': 2, 'c: 3}
```

Najczęściej stosuje się oba rodzaje argumentów jednocześnie:

```python
def funkcja3(*args, **kwargs):
    print(args, kwargs)
```

Wtedy funkcję taką można wywoływać z dowolnymi argumentami pozycyjnymi oraz podanymi przez nazwę — zostaną one odpowiednio przypisane do krotki `args` i słownika `kwargs`. Np.:

```python
funkcja3(1, 2, a=3, b=4)    # (1, 2) {'a': 3, 'b': 4}
```

Argumenty specjalne `*args` i `**kwargs` można łączyć z normalnymi argumentami. Wtedy `args` i `kwargs` będą zawierały tylko odpowiednie wartości niepodane na liście argumentów:

```python
def funkcja4(x, y, *args, **kwargs):
    print(x, y, args, kwargs)
```

Przykłady wywołania:

```python
funkcja4(1, 2, a=3, b=4)    # 1 2 () {'a': 3, 'b': 4}

funkcja4(1, y=2, a=3, b=4)  # 1 2 () {'a': 3, 'b': 4}

funkcja4(1, 2, 3, a=4)      # 1 2 (3,) {'a': 4}
```

Ciekawym przypadkiem jest umieszczenie normalnych argumentów po `**args`. Wtedy te parametry mogą być przekazane wyłącznie przez nazwę. Zasadne jest wtedy stosowanie wartości domyślnych. Np.:

```python
def funkcja5(*args, x=None, y=None, **kwargs):
    print(x, y, args, kwargs)
```

Przykłady wywołania:

```python
funkcja4(1, 2, a=3, b=4)            # None None (1, 2) {'a': 3, 'b': 4}

funkcja4(1, 2, x=3, y=4, a=5, b=6)  # 3 4 (1, 2) {'a': 5, 'b': 6}

funkcja4(1, 2, 3 y=4)               # None 4 (1, 2, 3) {}
```

Przykładem funkcji wykorzystującej to jest `print`. Jej definicja wygląda następująco:

```python
def print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    wydrukuj wszystkie elementy z krotki args
    sep, end, file oraz flush to argumenty przekazywane wyłącznie przez nazwę
    (jak dotąd wyjaśniono znaczenie sep oraz end).
```

## Wywoływanie funkcji z dowolnymi argumentami

Podobnie jak w definicji funkcji, można używać symboli `*` i `**` podczas ich wywoływania. Spójrzcie na poniższy przykład:

```python
def function(a, b, c):
    print(a, b, c)

data = [1, 2, 3]
function(*data)
```

Jest to równoważne wywołaniu tej funkcji jako

```python
function(1, 2, 3)
```

Ogólnie rzecz biorąc, podczas wywoływania funkcji jako `funkcja(*sekwencja)`, sekwencja jest rozwijana, a jej elementy są przekazywane jako parametry pozycyjne. Podobnie, `funkcja(**słownik)` jest równoważne przekazaniu elementów słownika jako nazwanych parametrów. Tak więc funkcja z powyższego przykładu może być wywołana jako

```python
params = {'a': 1, 'b': 2, 'c':  3}
function(**params)
```

Klucze słownika przekazywane do funkcji z `**` **muszą być łańcuchami**. W innym przypadku zostanie zgłoszony wyjątek `TypeError`.

Powyższa metoda wywoływania funkcji może być używana niezależnie od jej definicji: będzie działać zarówno dla klasycznych funkcji, jak i funkcji z dowolnymi argumentami opisanymi powyżej.

Typowym przypadkiem użycia jest wypisanie wszystkich elementów sekwencji oddzielonych przecinkami:

```python
data = [1, 2, 3, 4]
print(*data, sep=', ')
```

lub nawet

```python
print(*"abcd", sep='-')
```

Ostatni przykład wypisze „`a-b-c-d`”.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
