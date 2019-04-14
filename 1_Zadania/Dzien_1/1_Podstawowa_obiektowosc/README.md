<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Podstawowa obiektowość &ndash; zadania.

### Zadanie 1 &ndash; zadanie rozwiązywane z wykładowcą.
Stwórz klasę ```Calculator```. Konstruktor ma nie przyjmować żadnych danych. Każdy nowo stworzony obiekt powinien mieć pustą listę, w której będzie trzymać historię wywołanych operacji (stwórz ją w konstruktorze).
Następnie dodaj do klasy następujące metody:

1. ```add(num1, num2)``` &ndash; metoda ma dodać do siebie dwie zmienne i zwrócić wynik. Dodatkowo na liście operacji ma zapamiętać napis: "added ```num1``` to ```num2``` got ```result```".
2. ```multiply(num1, num2)``` &ndash; metoda ma pomnożyć przez siebie dwie zmienne i zwrócić wynik. Dodatkowo na liście operacji ma zapamiętać napis: "multiplied ```num1``` with ```num2``` got ```result```".  
5. ```print_operations()``` &ndash; metoda ma wypisać wszystkie zapamiętane operacje.

Pamiętaj o używaniu ```self``` w odpowiednich miejscach.
Stwórz kilka kalkulatorów i przetestuj ich działanie.

---

### Zadanie 2.
Stwórz klasę `Shape`, która ma spełniać następujące wymogi:

1. Mieć atrybuty:
`x`, `y` (określające środek tego kształtu) i `color`,
2. mieć metodę `describe`, wypisującą informacje o tym kształcie,
3. mieć metodę `distance`, zwracającą odległość od innego kształtu,
4. mieć nadpisaną metodę `__str__` tak, aby po rzutowaniu obiektu do napisu program zwracał: "Figura koloru *kolor* o środku w punkcie (*x*, *y*)".

### Zadanie 3.
Stwórz klasę `BankAccount`, która ma spełniać następujące wymogi:

1. Mieć atrybuty:
 * `number` - atrubyt ten powinien trzymać numer identyfikacyjny konta (dla uproszczenia możemy założyć że numerem konta może być dowolna liczba całkowita),
 * `cash` - atrybut określający ilość pieniędzy na koncie. Ma to być liczba zmiennoprzecinkowa. 
2. Posiadać konstruktor przyjmujący tylko numer konta. Atrybut `cash` powinien być zawsze nastawiany na 0.0 dla nowo tworzonego konta.
3. Posiadać metodę `deposit_cash(amount)` której rolą będzie zwiększenie wartości atrybutu `cash` o podaną watość. Pamiętaj o sprawdzeniu czy podana wartość jest większa od 0.0
4. Posiadać metodę `withdraw_cash(amount)` której rolą będzie zmniejszenie wartości atrybutu `cash` o podaną watość. Metoda ta powinna zwracać ilość wypłaconych pieniędzy. Dla uproszczenia zakładamy że ilośc pieniędzy na koncie nie może zejść poniżej 0.0, np. jeżeli z konta na którym jest 300zł próbujemy wypłacić 500zł to metoda zwroci nam tylko 300zł. Pamiętaj o sprawdzeniu czy podana wartość jest większa od 0.0
5. Posiadać metodę `print_info()` nie przyjmującą żadnych parametrów. Metoda ta ma wyświetlić informację o numerze konta i jego stanie.

### Zadanie 4.
Stwórz klasę `Employee`, która ma spełniać następujące wymogi:

1. Mieć atrybuty:
 * `id` - atrubyt ten powinien trzymać numer identyfikacyjny pracownika, 
 * `first_name` - atrybut określający imię pracownika,
 * `last_name` - atrybut określający nazwisko pracownika,
 * `salary` - atrybut określający ile pracownik zarabia za godzinę, powinien być prywatny.
2. Posiadać konstruktor przyjmujący id, imię, nazwisko.
3. Posiadać metodę `set_salary(salary)` której rolą będzie ustawienie wartości atrybutu `salary`. Pamiętaj o sprawdzeniu czy podana wartość jest:
 * Wartością numeryczną,
 * Wieksza (lub równa) od 0.0
