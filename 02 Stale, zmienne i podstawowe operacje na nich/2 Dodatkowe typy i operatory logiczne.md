---
parent: Constants, Variables and Basic Operations
grand_parent: Technologie Informatyczne II
nav_order:  2
---

# Dodatkowe typy i operatory logiczne


## Typ None

Poza wymienionymi powyżej w Pythonie istnieje jeszcze specjalna stała None oznaczająca nic oraz dwie stałe logiczne. Znaczenie stałej None zostanie omówione później. Generalnie jest ona używana gdy chcemy podkreślić, że nie mamy do dyspozycji żadnej sensownej wartości.

## Typy i operatory logiczne

Typ logiczny nosi nazwę bool. Istnieją wyłącznie dwie wartości tego typu True (prawda) i False (fałsz). Zazwyczaj pojawiają się one jako wynik działania operatorów logicznych:

* `==` sprawdza czy dwie wielości są równe (**Uwaga! ten operator to <span style="color:red">podwojony</span> znak `=`**)
* `!=` sprawdza czy dwie wielości są różne
* `>`, `<`, `>=`, `<=` operatory porównujące dwa elementy

Proszę w konsoli sprawdzić wyniki następujących operacji:

```python
1 + 2 == 3  
  
1 - 2 != -1  
  
2 + 2 > 4  
  
2 + 2 >= 4  
  
(3, 2) == (1 + 2, 1 * 2)  
  
(1, 2) > (1, 3)  
  
(1, 2) < (1,)  
  
(1, 2) > (2,)  
  
"Ala" < "Basia"  
  
"a" < "Z"
```

Jak widać, możliwe jest porównywanie nie tylko liczb, ale także krotek i łańcuchów tekstowych. W pierwszym przypadku porównywane są po kolei elementy począwszy od pierwszego. W drugim porównywanie jest alfabetyczne, przy czym wszystkie wielkie litery są **mniejsze** od liter małych. Wynika to ze sposoby reprezentacji znaków w pamięci komputera. Szczegółowe omówienie w jaki sposób można porównywać ze sobą łańcuchy tekstowe bez rozróżniania wielkich i małych liter jest opisany w dalszej części wykładu.

Dla wartości logicznych istnieją też specjalne operatory logiczne są to negacja (`not`), koniunkcja (`and`), alternatywa (`or`). Proszę samodzielnie sprawdzić ich działanie. Np.:

```python
True and False or True  
  
False and not True
```

itp... Operatory te będą miały bardzo istotne znaczenie kiedy omawiane będą warunki.

---

Treść udostępniona na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
