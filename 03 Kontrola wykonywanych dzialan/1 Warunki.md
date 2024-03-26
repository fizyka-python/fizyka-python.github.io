---
parent: Kontrola wykonywanych działań
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Warunki

Wszystkie dotychczasowe programy były wykonywane sekwencyjnie, wiersz po wierszu. Żadna linia nie mogła zostać pominięta.

Rozważmy następujący problem: dla danej liczby rzeczywistej _liczba_ określ jej wartość bezwzględną. Jeśli _liczba_ > 0 to program powinien wydrukować jej wartość, w przeciwnym razie powinien wydrukować –_liczba_. Tego zachowania nie można osiągnąć przy użyciu programu sekwencyjnego. Program powinien warunkowo wybrać następny krok. Do tego celu służy komenda **`if`**:

```python
liczba = float(input("Podaj liczbę: "))

if liczba > 0:
    wartosc_bewzgledna = liczba
else:
    wartosc_bewzgledna = -liczba

print(wartosc_bewzgledna)
```


Ten program używa instrukcji warunkowej, **`if`** . Po tym, `if` postawimy warunek `(liczba > 0)` po dwukropku. Następnie wstawiamy blok instrukcji, które będą wykonywane tylko wtedy, gdy warunek jest prawdziwy (tj. wartość wyrażenia `liczba > 0` jest równa `True` ). Po tym bloku może (ale nie musi) następować słowo **`else`** , dwukropek i inny blok instrukcji, które będą wykonywane tylko wtedy, gdy warunek jest fałszywy (tzn. ma wartość `False` ).

> **Bloki w Pythonie**
>
> W Pythonie _bloki_ oznacza się za pomocą wcięć — czyli spacji na początku linijki. Ilość tych spacji jest dowolna, ale istotne jest by było ich wystarczająco dużo aby blok był wizualnie wyróżniony. Każdy blok **musi** być oznaczony poprzez dwukropek (**`:`**) na końcu poprzedzającej go linii. Oczywiście tylko niektóre komendy mogą rozpoczynać nowy blok. W powyższym przykładzie są to komendy `if` oraz `else`. Przyporządkowane do nich bloki zostaną wykonane tylko w przypadku spełnienia (`if`) bądź niespełnienia (else) warunku. Blok kończymy poprzez usunięcie wcięcia pierwszej linii nienależącej do bloku.  
>
> Bloki mogą być zagnieżdżone — kolejne poziomy oznaczamy zwiększając ilość spacji na początku (np. 4, 8, 12 itd.), i każdy z nich kończymy cofając  odpowiednio wcięcia. (8, 4, 0). Możliwe jest jednoczesne usunięcie wcięć odpowiadających kilku blokom — wtedy kończymy je wszystkie jednocześnie.  
>
> Sposób oznaczania bloków za pomocą wcięć jest charakterystyczny dla Pythona. W innych językach programowania stosuje się specjalne znaki (najczęściej nawiasy klamrowe) do oznaczenia początku i końca bloku.

Podsumowując, instrukcja warunkowa w Pythonie ma następującą składnię:

<pre>
<b>if</b> <i>warunek</i><b>:</b>
    dowolna ilość komend wykonywanych
    jeżeli warunek jest prawdziwy (ma wartość True)
<b>else:</b>
    dowolna ilość komend wykonywanych  
    jeżeli warunek jest fałszywy (ma wartość False)
</pre>

słowo kluczowe `else` wraz z odpowiadającym mu blokiem może zostać pominięte, jeśli nic nie powinno zostać zrobione, jeśli warunek jest fałszywy. Na przykład możemy zastąpić zmienną `liczba` jej wartością bezwzględną w następujący sposób:

```python
liczba = float(input("Podaj liczbę: "))

if liczba < 0:
    liczba = -liczba

print(liczba)
```

W tym przykładzie zmienna `liczba` jest przypisana do `-liczba` tylko, jeśli `liczba < 0` . Natomiast polecenie `print(x)` jest wykonywane za każdym razem, ponieważ nie jest wcięte, więc nie należy do bloku wykonywanego tylko w przypadku gdy sprawdzony warunek jest prawdziwy.

## Zagnieżdżanie warunków

Każda instrukcja Pythona może być umieszczona w każdym z bloów, w tym w innej instrukcji warunkowej. W ten sposób uzyskujemy warunki zagnieżdżone. Bloki warunków wewnętrznych są wcięte z użyciem większej ilości spacji (np. 8 spacji). Zobaczmy przykład. Biorąc pod uwagę współrzędne punktu na płaszczyźnie, wydrukuj jego ćwiartkę:

```python
x = float(input("Podaj współrzędną x: "))  
y = float(input("Podaj współrzędną y: "))  

if x > 0:
    if y > 0:
        # x jest większe od 0, y jest większe od 0  
        print("Ćwiartka I")
    else:
        # x jest większe od 0, y jest mniejsze lub równe 0
        print("Ćwiartka IV")
else:
    if y > 0:
       # x jest mniejsze lub równe 0, y jest większe niż 0
        print("Ćwiartka II")
    else:
        # x jest mniejsze lub równe 0, y jest mniejsze lub równe 0
        print("Ćwiartka III")
```

Jeśli mamy więcej niż dwie opcje do rozróżnienia przy użyciu operatora warunkowego, możemy użyć instrukcji **`if... elif... else`**  (**`elif`** jest skrótem od _else if_):

<pre>
<b>if</b> <i>warunek</i><b>:</b>
    dowolna ilość komend wykonywanych
    jeżeli warunek jest prawdziwy
<b>elif <i>warunek2</i>:</b>
    dowolna ilość komend wykonywanych  
    jeżeli warunek1 jest fałszywy, zaś warunek2 jest prawdziwy
<b>elif <i>warunek3</i>:</b>
    dowolna ilość komend wykonywanych  
    jeżeli warunek1 oraz warunek2 są fałszywe, zaś warunek3 jest prawdziwy
<b>else:</b>
    dowolna ilość komend wykonywanych  
    jeżeli każdy powyższy warunek jest fałszywy
</pre>

Pokażmy, jak to działa, przepisując powyższy przykład:

```python
x = float(input("Podaj współrzędną x: "))  
y = float(input("Podaj współrzędną y: "))  

if x > 0 and y > 0:
    print("Ćwiartka I")
elif x > 0 and y < 0:
    print("Ćwiartka IV")
elif y > 0:
    print ("Ćwiartka II")
else:
    print ("Ćwiartka III")
```

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
