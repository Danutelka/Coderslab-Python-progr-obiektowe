<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Programowanie obiektowe w Pythonie &ndash; praca domowa.

> Kilka ważnych informacji

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki.

Każde zadanie rozwiązuj w oddzielnym pliku (np. zadanie 1. w pliku exercise_1.py, zadanie 2. w pliku exercise_2.py itd.)

## Jak zacząć?

1. Stwórz [*fork*][forking] repozytorium z zadaniami.
2. [*Sklonuj*][ref-clone] repozytorium na swój komputer.
3. Rozwiąż zadania i [*skomituj*][ref-commit] zmiany do swojego repozytorium.
4. [*Wypchnij*][ref-push] zmiany do swojego repozytorium na GitHubie.
5. Stwórz [*pull request*][pull-request] do oryginalnego repozytorium, gdy skończysz wszystkie zadania.


# Dzień 1


### Zadanie 1.

Napisz obiektowo program, który będzie obsługiwał skanowanie produktów w sklepie.

Stwórz klasę `Product`. Klasa ta ma posiadać podane atrybuty:
  * `id` - liczba całkowita. Powinna być unikalna w całym systemie (jak to osiągnąć będzie wyłumaczone w dalszej części zadania).
  * `name` - string. Jest to nazwa danego produktu.
  * `description` - string. Jest to opis danego produktu.
  * `price` - float. Jest to cena za jeden produkt. Powinna być większa od `0.01`.
  * `quantity` - liczba całkowita większa od zera.
 
 Klasa powinna mieć też nastepujące metody:

  * konstruktor - powinien przyjmować nazwę, opis, cenę i ilość produtku. 
  * atrybut id powiniem mieć możliwość wyłącznie odczytu.
  * metodę ```get_total_sum()``` która będzie zwracała łączną kwotę za dany produkt (wyliczaną jako ilość * cena produktu.
  * metodę ```get_id()```, która będzie zwracała numer ```id``` produktu

  
 #### Generowanie unikalnego id dla produktu:
 W dalszej części programu będziemy chcieli identyfikować nasze produkty po ich id. Dlatego musimy zagwarantować że każdy z stworzonych produktów będzie miał unikalny numer identyfikacyjny. W tym celu w klasie `Product` powinniśmy zdefiniować dodatkowy atrybut```next_id```.

 Zmienna ta będzie trzymała id ktore zostanie nadane następnemu stworzonemu produktowi. Nastepnie w kostruktorze klasy musimy wykonać następujące czynności: 
  * własnie tworzonemu produktowi przypisać id trzymane w zmiennej `next_id`,
  * zwiększyć wartość  `next_id` o jeden.
 
 ```python
# w konstruktorze
self.id = self.next_id
Product.next_id += 1
```
Dzieki temu żaden z naszych produktów nie będzie miał takiego samego id.
 
# Dzień 2

### Zadanie 2.

1. Napisz klasę `ShoppingCart`. Klasa ta ma posiadać podane atrybuty:
  * `products` - słownik z obiektami klasy `Product` gdzie kluczem powinno być `id` produktu. 
 
 Klasa powinna mieć też nastepujące metody:
  * `add_product(new_product)` - metoda ta powinna dodawać nowy produkt do listy z produktami.
  * `remove_product(product_id)` - metoda ta powinna usuwać produkt z koszyka. Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić.
  * `change_product_quantity(product_id, new_quantity)` - metoda ta powinna zmianiać ilość danego produktu w koszyku. Jeśli taki produkt nie był wcześniej zeskanowany, to ma nic nie robić.
  * `print_receipt()` - metoda drukująca paragon. Na paragonie powinno się znaleźć: lista wszystkich produktów, wraz z ich id, nazwą, ceną, ilością i łączą ceną (pamiętaj że masz do tego dedykowamą metodę w klasie `Product`) i łączna kwota za wszystkie produkty znajdujące się w koszyku. Metoda powinna **zwrócić** string ze wszystkimi ww. informacjami w postaci:
 ```
 nazwa_produkut - cena_produktu, ilość_produktu, łączna_cena
 ...
 Łączna kwota = całkowiata_kwota_paragonu
 ```

2. Zmodyfikuj klasę produktu tak, żeby umożliwiała nadawanie rabatu. Jeżeli ilość danego produktu jest większa lub równa 3 to metoda ```get_total_sum()``` powinna nadawać 20% zniżki na łączną kwotę za te produkty.

<!-- Links -->
[forking]: https://guides.github.com/activities/forking/
[ref-clone]: http://gitref.org/creating/#clone
[ref-commit]: http://gitref.org/basic/#commit
[ref-push]: http://gitref.org/remotes/#push
[pull-request]: https://help.github.com/articles/creating-a-pull-request
[ref-multiple-forms]: http://stackoverflow.com/a/14071321
