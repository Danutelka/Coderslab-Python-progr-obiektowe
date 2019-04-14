<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Wyrażenia regularne

### Zadanie 1
Wykorzystując moduł `re`, napisz funkcję `check_dice`, która przyjmie jeden parametr w postaci napisu.
Funkcja powinna sprawdzić czy w przekazanym parametrze znajduje się prawidłowy wzór rzutu kostką.

Wzór rzutu kostką ma następującą postać:

```
<liczba rzutów kostką>d/D<liczba ścianek na kostce>+/-<modyfikator wyniku>
```

np.

`2d10+20` - dwa rzuty 10-ścienną kostką, do wyniku dodajemy 20

`6D3-10`- sześć rzutów 3-ścienną kostką, od wyniku odejmujemy 10

`D6` - jeden rzut 6-ścienną kostką

Funkcja powinna zwrócić `True` jeżeli w przekazanym parametrze znajduje się prawidłowy wzór, w innym wypadku funkcja powinna zwrócić `False`.

Przykłady działania funkcji:

`check_dice("9d7+10")` - zwraca `True`

`check_dice("9s7+10")` - zwraca `False`

`check_dice("9D7+10 abcdefghijk")` - zwraca `True`

`check_dice("9d-h")` - zwraca `False`


### Zadanie 2

Otwórz plik `exercise_2.py`. Znajduje się w nim zmienna `text_to_search`, w której znajduje się tekst Szymona Askenazego (tekst pobrany z serwisu [wolnelektury.pl](https://wolnelektury.pl/katalog/lektura/uwagi-z-powodu-listu-polaka-do-ministra-rosyjskiego.html)).

Używając modułu `re` wykonaj następujące zadania:

1. Znajdź wszystkie wystąpienia wyrazu `autor`.
2. Znajdź wszystkie wystąpienia pasujące do wzoru `<ciąg_cyfr>%`.
3. Znajdź wszystkie wystąpienia wyrazów, które kończą się znakiem `.`.
4. Znajdź wszystkie wyrazy, w których znajduje się ciąg znaków `polski` (niezależnie od wielkości znaków).


