---
parent: Algorytmy
grand_parent: Technologie Informatyczne II
nav_order:  1
---

# Czym jest algorytm?

> **Składniki:**
> * 1 szklanka białego cukru
> * ½ szklanki masła
> * 2 jajka
> * 2 łyżeczki ekstraktu waniliowego
> * 1 ½ szklanki mąki uniwersalnej
> * 1 ¾ łyżeczki proszku do pieczenia
> * ½ szklanki mleka
>
> 1. Rozgrzej piekarnik do 175°C.
> 2. Natłuść i oprósz mąką formę o wymiarach 20x20 centymetrów.
> 3. W średniej misce ubij razem cukier i masło.
> 4. Wbijaj jajka, jedno po drugim, a następnie dodaj wanilię.
> 5. Zmieszaj mąkę i proszek do pieczenia, dodaj do śmietany i dobrze wymieszaj.
> 6. Dodaj mleko, aż ciasto będzie gładkie.
> 7. Wlej lub przelej łyżką ciasto do przygotowanej formy.
> 8. Piec przez 30 do 40 minut w rozgrzanym piekarniku. Ciasto jest gotowe, gdy sprężynuje przy dotyku.

Powyżej znajduje się przepis na ciasto waniliowe. Zawiera on niezbędne składniki i zestaw czynności, które należy wykonać (wskazówki). Efektem ich wykonania jest smaczne ciasto. Waszym pierwszym zadaniem domowym będzie zrobienie takiego (lub innego) ciasta i poczęstowanie nim prowadzącego zajęcia.

W matematyce lub świecie komputerów taki przepis nazywany jest *algorytmem*. Jest to skończona sekwencja dobrze zdefiniowanych, możliwych do zaimplementowania w komputerze instrukcji, zazwyczaj służących do rozwiązywania określonej klasy problemów lub wykonywania obliczeń. Zazwyczaj operuje on na pewnych danych (składnikach) i dostarcza pewien wynik (ciasto).

Algorytmy są określone w pewnym **formalnym języku**. Różni się on od codziennego (*naturalnego*) języka w taki sposób, że ma bardzo ścisłe reguły. Bardziej precyzyjnie jest to opisane w dostępnej online książce autorstwa Petera Wentwortha, Jeffreya Elknera, Allena B. Downeya i Chrisa Meyersa, "[How to Think Like a Computer Scientist](http://openbookproject.net/thinkcs/python/english3e/)" :

**Języki naturalne** to języki, którymi posługują się ludzie, takie jak angielski, hiszpański i francuski. Nie zostały one zaprojektowane przez ludzi (chociaż ludzie próbują narzucić im pewien porządek); ewoluowały naturalnie.

**Języki formalne** to języki zaprojektowane przez ludzi do konkretnych zastosowań. Na przykład notacja używana przez matematyków jest językiem formalnym, który jest szczególnie dobry w oznaczaniu relacji między liczbami i symbolami. Chemicy używają języka formalnego do reprezentowania struktury chemicznej cząsteczek. I co najważniejsze:

*Języki programowania są językami formalnymi, które zostały zaprojektowane do wyrażania obliczeń*

Języki formalne mają zwykle ścisłe reguły dotyczące składni. Na przykład, `3+3=6` jest poprawnym składniowo wyrażeniem matematycznym, ale `3=+6$` już nie. H<sub>2</sub>O jest poprawną składniowo nazwą chemiczną, ale nie jest nią <sub>2</sub>Zz.

Reguły składni występują w dwóch odmianach, odnoszących się do **tokenów** i struktury. Tokeny są podstawowymi elementami języka, takimi jak słowa, liczby i pierwiastki chemiczne. Jednym z problemów z `3=+6$` jest to, że `$` nie jest poprawnym tokenem w matematyce (przynajmniej o ile nam wiadomo). Podobnie, <sub>2</sub>Zz nie jest legalne, ponieważ nie ma pierwiastka o symbolu *Zz*.

Drugi typ reguły składni odnosi się do **struktury** wypowiedzi — czyli sposobu, w jaki tokeny są ułożone. Stwierdzenie `3=+6$` jest strukturalnie niepoprawne, ponieważ nie można umieścić znaku plus bezpośrednio po znaku równości. Podobnie, formuły molekularne muszą mieć indeksy dolne po nazwie pierwiastka, a nie przed.

Kiedy czytasz zdanie w języku polskim, czy angielskim lub wypowiedź w języku formalnym, musisz dowiedzieć się, jaka jest struktura zdania (chociaż w języku naturalnym robicie to podświadomie). Proces ten nazywany jest **przetwarzaniem** lub **parsowaniem** (od angielskiego słowa *parsing* — przetwarzanie).

Na przykład, gdy słyszycie zdanie "Drugi but spadł", rozumiecie, że *drugi but* jest podmiotem, a *spadł*, jako czasownik, jest orzeczeniem. Po przeanalizowaniu zdania możecie dowiedzieć się, co ono oznacza, czyli poznać jego **semantykę**. Zakładając, że wiecie, czym jest but i co oznacza upadek, zrozumiecie ogólne znaczenie tego zdania.

Chociaż języki formalne i naturalne mają wiele cech wspólnych — tokeny, strukturę, składnię i semantykę — istnieje wiele różnic:

* **jednoznaczność**
  
  Języki naturalne są pełne niejednoznaczności, z którą ludzie radzą sobie używając wskazówek kontekstowych i innych informacji. Języki formalne są zaprojektowane tak, aby były prawie lub całkowicie jednoznaczne, co oznacza, że każde stwierdzenie ma dokładnie jedno znaczenie, niezależnie od kontekstu.

* **redundancja**
  
  Aby zrekompensować niejednoznaczność i ograniczyć nieporozumienia, języki naturalne wykorzystują wiele redundancji. W rezultacie są one często bardzo rozwlekłe. Języki formalne są mniej redundantne i bardziej zwięzłe.

* **dosłowność**
  
  Języki naturalne są pełne idiomów i metafor. Jeśli ktoś mówi: "spadł drugi but", to prawdopodobnie nie ma żadnego buta i nic nie spada. Języki formalne oznaczają dokładnie to, co mówią.

Ludzie, którzy dorastali mówiąc językiem naturalnym — czyli po prostu wszyscy — często mają trudności z dostosowaniem się do języków formalnych. Pod pewnymi względami różnica między językiem formalnym a naturalnym przypomina różnicę między poezją a prozą, ale jest większa:

* **Poezja**

   Słowa są używane zarówno dla ich dźwięków, jak i znaczenia, a cały wiersz razem tworzy efekt lub reakcję emocjonalną. Dwuznaczność jest nie tylko powszechna, ale często celowa.

* **Proza**

   Dosłowne znaczenie słów jest ważniejsze, a struktura wnosi więcej znaczenia. Proza jest bardziej podatna na analizę niż poezja, ale nadal często jest niejednoznaczna.

* **Programy**

   Znaczenie programu komputerowego jest jednoznaczne i dosłowne, i może być zrozumiane całkowicie poprzez analizę tokenów i struktury.

Oto kilka sugestii dotyczących czytania programów (i innych języków formalnych). Po pierwsze, należy pamiętać, że języki formalne są znacznie bardziej skondensowane niż języki naturalne, więc ich czytanie zajmuje więcej czasu. Ponadto, struktura jest bardzo ważna, więc zazwyczaj nie jest dobrym pomysłem czytanie od góry do dołu, od lewej do prawej. Zamiast tego należy nauczyć się analizować program w głowie, identyfikując tokeny i interpretując strukturę. Wreszcie, szczegóły mają znaczenie. Drobne rzeczy, takie jak błędy ortograficzne i zła interpunkcja, które mogą ujść na sucho w językach naturalnych, mogą mieć duże znaczenie w języku formalnym.

<hr/>

Opublikowano na licencji [GNU Free Documentation License](https://www.gnu.org/licenses/fdl-1.3.html).
