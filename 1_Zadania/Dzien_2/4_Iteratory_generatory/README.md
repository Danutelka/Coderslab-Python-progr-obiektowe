<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

# Iteratory i genereatory

### Zadanie 1 &ndash; kostka
Napisz klasę `Dice`, która będzie miała własność `dice_type`. W tej własności będziesz przechowywać liczbę ścianek kostki. Kostka może być 3, 4, 6, 8, 10, 12, 20 lub 100-ścienna.

Napisz metodę `roll()`, która wylosuje liczbę z zakresu `1..dice_type`, czyli zasymuluje rzut kostką.

### Zadanie 2 &ndash; generator
Napisz funkcję generatora `roll`, która zwróci dokładnie 10 rzutów koścmi.

### Zadanie 3 &ndash; piosenka
Napisz funkcję generatora, która będzie zwracała kolejne linie pierwszej zwrotki piosenki 'Wlazł kotek na płotek'.

```
Wlazł kotek na płotek
i mruga,
ładna to piosenka,
nie długa.
Nie długa, nie krótka,
lecz w sam raz,
zaśpiewaj koteczku,
jeszcze raz.
```

### Zadanie 4 &ndash; Fibonacci
Napisz generator, który będzie obliczał kolejne elementy ciągu Fibonacciego, aż do N-elementu przekazanego do generatora jako parametr.

```python
for element in fib(5):
    print(element)
```



```shell
1
1
2
3
5
```
