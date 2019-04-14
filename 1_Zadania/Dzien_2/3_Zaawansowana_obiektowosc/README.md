<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Zaawansowana obiektowość

### Zadanie 1 &ndash; zadanie rozwiązywane z wykładowcą
Stwórz klasę ```AdvancedCalculator```, która będzie dziedziczyła po klasie `Calculator` z poprzednich zadań. Do nowej klasy dopisz:

 1. Atrybut ```PI```, który będzie miał przypisaną wartość **3.14159265**.
 2. Statyczną (dodaj odpowiedni dekorator) funkcję ```compute_circle_radius(r)``` która będzie zwracała pole koła. Ta metoda nie będzie dopisywać obliczeń do tablicy (napisz w komentarzu, dlaczego nie może tego robić).

---

### Zadanie 2.
Zmień klasę `BankAccount` w taki sposób żeby konstruktor sam nadawał numer konta bankowego. Dla uproszczenia będziemy nadawać kolejne liczby całkowite zaczynając od jedynki. Zeby to zrobić:
 1. Dodaj do klasy prywatny atrybut `next_acc_number`.
 2. Nastaw jego wartość na 1.
 3. Zmodyfikuj konstruktor w taki sposób żeby nie przyjmował numeru konta, tylko przypisywał wartość atrybutu `next_acc_number` do swojego atrybutu `number`, a nastepnie zwiększał `next_acc_number` o jeden.

Przetestuj jak generowane są numery twoich kont.  
