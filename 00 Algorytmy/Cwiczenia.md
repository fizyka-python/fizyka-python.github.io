---
parent: Algorithms and Programs
grand_parent: Technologie Informatyczne II
nav_order:  E
---

# Ćwiczenia z myślenia algorytmami

   Poniżej znajduje się zestaw problemów. W każdym z nich zidentyfikuj i nazwij niezbędne dane wejściowe, napisz dokładnie wszystkie niezbędne kroki (jak w przykładach pokazanych wcześniej) i zidentyfikuj wynik algorytmu (wyjście).

1. Biorąc pod uwagę temperaturę wyrażoną w stopniach Celsjusza, przekonwertuj ją na jej odpowiednik w stopniach Fahrenheita.

   Wzór konwersji: *°F* = 9/5 × *°C* + 32

2. Bank umożliwia przewalutowanie części depozytu w euro na złotówki. Aktualny kurs konwersji wynosi 1 EUR = 4,60 PLN.
   Od każdej transakcji bank pobiera 2% prowizji. Stąd, na przykład, wymiana 100 EUR da 450,80 PLN. Pokaż algorytm konwersji.

3. Zasiłek rodzinny to kwota pieniężna wypłacana co miesiąc, aby pomóc rodzinom w utrzymaniu i edukacji dzieci.
   Aby otrzymać ten zasiłek, rodzina musi mieć dochód referencyjny równy lub niższy niż ustalona wartość 8803,62 EUR.
   Wiadomo, że dochód referencyjny jest obliczany przy użyciu następującego wzoru:

    *dochód referencyjny* = *całkowity dochód gospodarstwa domowego* / (*liczba dzieci* + 1)

    Określ, czy dana rodzina (z danym całkowitym dochodem gospodarstwa domowego i daną liczbą dzieci) kwalifikuje się do zasiłku (odpowiedź powinna brzmieć `Tak` lub `Nie`).

4. Zbuduj algorytm obliczający wskaźnik masy ciała (BMI) i kondycję fizyczną danej osoby. Wzór jest następujący
   *BMI* = *waga* / *wzrost*², gdzie *waga* jest podana w **kilogramach**, a *wzrost* w **metrach**.

   Kondycję danej osoby można odczytać z poniższej tabeli:

   | Stan                  | BMI kobiety | BMI mężczyźni |
   | --------------------- | ----------- | ------------- |
   | Niedowaga             | < 19.1      | < 20.7        |
   | Normalna waga         | 19.1 - 25.8 | 20.7 - 26.4   |
   | Nieznaczna nadwaga    | 25.8 - 27.3 | 26.4 - 27.8   |
   | Powyżej idealnej wagi | 27.3 - 32.3 | 27.8 - 31.1   |
   | Otyłość               | > 32.3      | > 31.1        |

   Określ stan osoby, biorąc pod uwagę wagę, wzrost w centymetrach i płeć.

5. Tempo metabolizmu jest obliczane przy użyciu następującego wzoru:

   *tempo metabolizmu* = 655 + 9,6 × *waga ciała w kg* + 1,8 × *wysokość w centymetrach* + 4,7 × *wiek*.

   Aby obliczyć liczbę kilokalorii, które dana osoba musi spożywać dziennie, należy określić jej tempo metabolizmu i pomnożyć je przez współczynnik korygujący, który zależy od stylu życia:

   | Współczynnik korygujący | Stopień aktywności fizycznej                             |
   | ----------------------- | -------------------------------------------------------- |
   | 1.200                   | Siedzący tryb życia                                      |
   | 1.375                   | Wykonuje lekkie ćwiczenia (1 do 3 razy w tygodniu)       |
   | 1,550                   | Wykonuje umiarkowane ćwiczenia (4 lub 5 razy w tygodniu) |
   | 1,725                   | Ma wysoki stopień aktywności (6 lub 7 razy w tygodniu)   |

   Określ liczbę kalorii, które należy spożywać, na podstawie liczby ćwiczeń w tygodniu i innych niezbędnych informacji.

6. W niektórych krajach europejskich podatek samochodowy zależy od pojemności silnika samochodu. Jest on obliczany jako:

   *podatek* = *pojemność silnika w cm³* × *stawka podatku* - *zniżka*

   gdzie *stawka* i *zniżka* są podane w poniższej tabeli:

   | Stawka podatku [EUR] | Pojemność cylindra [cm³] | Rabat [EUR] |
   | -------------------- | ------------------------ | ----------- |
   | 3,74                 | do 1250                  | 2417,56     |
   | 8,86                 | ponad 1250               | 8813,22     |

   Napisz algorytm obliczający podatek samochodowy. Pamiętaj, że podatek nie może być mniejszy od 0 (jest to mało prawdopodobny przypadek, ale i tak należy go rozważyć).


<hr/>

Opublikowano na licencji [Creative Commons Uznanie autorstwa-Użycie niekomercyjne-Na tych samych warunkach](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.pl).
