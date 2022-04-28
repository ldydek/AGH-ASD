# Zadanie 2. (wybór zadań z terminami) Mamy dany zbiór zadań T = {t1, . . . , tn}. Każde zadanie ti
# dodatkowo posiada: (a) termin wykonania d(ti) (liczba naturalna) oraz (b) zysk g(ti) za wykonanie w
# terminie (liczba naturalna). Wykonanie każdego zadania trwa jednostkę czasu. Jeśli zadanie ti zostanie
# wykonane przed przekroczeniem swojego terminu d(ti), to dostajemy za nie nagrodę g(ti) (pierwsze wybrane
# zadanie jest wykonywane w chwili 0, drugie wybrane zadanie w chwili 1, trzecie w chwili 2, itd.).
# Proszę podać algorytm, który znajduje podzbiór zadań, które można wykonać w terminie i który prowadzi
# do maksymalnego zysku. Proszę uzasadnić poprawność algorytmu.
#
#
# Sortuję tablicę krotek postaci: (termin wykonania zadania, zysk za zadanie). Iteruję po elementach te tablicy od
# początku i do dodatkowej tablicy zapisuję te zadania w taki sposób, żeby dane zadanie zostało wykonane możliwie
# najblżej deadline'u tak, aby zostawić poprzednie godziny na wykonanie mniej wartościowych zadań. W ten sposób
# w tablicy rozmieszczę wykonania tych zadań w odpowiedniej kolejności, aby zmaksymalizować zysk.
