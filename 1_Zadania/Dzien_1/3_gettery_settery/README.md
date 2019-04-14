<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Ograniczenia dostępu i gettery/settery &ndash; zadania.

### Zadanie 1 &ndash; zadanie rozwiązywane z wykładowcą.

Miecze świetlne w świecie Gwiezdnych Wojen mogą mieć następujące kolory \*.
* niebieski (jasna strona mocy),
* zielony (jasna strona mocy),
* fioletowy (jasna strona mocy),
* czerwony (ciemna strona mocy). 


Utwórz klasę `Lightsaber` definiującą miecz świetlny. W konstruktorze dodaj własności:

* prywatną `_color`,
* nadpisz metodę `__str__()` tak, by zwracała napis: "Lighstaber: *kolor*, force: *jasna|ciemna*".

Niech konstruktor przyjmuje parametr `color`, wartość tego parametru przypisz do własności `_color`, stronę mocy wyświetl dynamicznie na podstawie koloru.

\* bierzemy pod uwagę filmy z aktorami, epizody I – VIII.

---

### Zadanie 2.

Utwórz setter i getter (`@property` i odpowiednio `@własność.setter`) o nazwie `color`, które zwrócą i nastawią prywatną własność `_color`. Sprawdź, czy podany kolor znajduje się na liście legalnych kolorów. Jeśli nie – wyrzuć wyjątek `ValueError` z komentarzem "Bad lightsaber color".

Zmodyfikuj odpowiednio metodę `__str__()`.

### Zadanie 3.

1. Utwórz własność wirtualną, `force_side`, która przyjmie odpowiednią wartość, zależnie od wartości własności `_color`:

* dla kolorów niebieskiego, zielonego i fioletowego – "light",
* dla koloru czerwonego – "dark".

2. Zmodyfikuj odpowiednio metodę `__str__()`.