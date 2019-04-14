<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Dziedziczenie &ndash; zadania

### Zadanie 1. – rozwiązywane z wykładowcą.
Zajrzyj do pliku **exercise1.py**, znajdziesz tam klasę `Dinosaur`, która ma zaimplementowane następujące elementy:

* metodę `walk()`,
* metodę `make_sound()`.

Napisz klasę `Bird`, która będzie dziedziczyła po klasie `Dinosaur`. Klasa `Bird` ma:
* dostać nową metodę `fly()`, która będzie zwracała napis "Latam!",
* nadpisać metodę `make_sound()`, która ma zwracać napis "Ćwir ćwir!".

Przetestuj nową klasę.

---

### Zadanie 2.
Stwórz klasę `Circle`, która ma spełniać następujące wymogi:

1. Dziedziczyć po klasie definiującej kształt.
2. Mieć dodatkowy atrybut `radius` definiujący promień okręgu.
3. Mieć konstruktor przyjmujący zmienne określające wartości `x`, `y`, `color` i `radius`.  Konstruktor powinien wypisywać informacje o właśnie stworzonym okręgu.
4. Nadpisywać funkcje klasy `Shape` (nadpisz tylko te, które tego wymagają).
5. Mieć funkcję `area`, zwracającą pole powierzchni.
6. Mieć funkcję `perimeter` zwracającą obwód.

**Hint:** Wartość π znajdziesz w pakiecie `math` w zmiennej `pi`:
```python 
import math
print(math.pi)
```

### Zadanie 3.
Stwórz klasę `HourlyEmployee`, która ma reprezentować pracownika któremu pracodawca płaci za godziny. Klasa ma spełniać następujące wymogi:
 1. Dziedziczyć po klasie `Employee`.
 2. Mieć dodatkową metodę `compute_payment(hours)` która będzie zwracała kwotę do wypłacenia pracownikowi za liczbę wypracowanych godzin. 

### Zadanie 4.
Stwórz klasę `SalariedEmployee`, która ma reprezentować pracownika z którym pracodawca ma umowę miesięczną. Klasa ma spełniać następujące wymogi:
 1. Dziedziczyć po klasie `Employee`.
 2. Mieć dodatkową metodę `compute_payment()` która będzie zwracała kwotę do wypłacenia pracownikowi za miesiąc (dla uproszczenia możemy założyć że w każdym miesiącu jest 190 godzin pracujących). 
