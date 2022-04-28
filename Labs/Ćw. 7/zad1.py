# Zadanie 1. (pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {x1, . . . , xn} na
# prostej. Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba dwóch
# przedziałów, np. [0.2, 1.2] oraz [1.4, 2.4]).
#
#
# Sortujemy podane punkty rosnąco. Następnie zaczynamy od najmniejszego punktu i sprawdzamy ile punktów w tej
# tablicy jest mniejszych bądź równych od wartości tego punktu plus jeden. O tyle miejsc się przesuwamy i podaną
# operację wykonujemy jeszcze więcej razy do momentu aż nie przejdziemy całej tablicy, zwiększając na bieżąco
# licznik tych operacji, a więc licznik przedziałów.
