# Zadanie 3. (ładowanie przyczepy) Mamy przyczepę o pojemności K kilogramów oraz zbiór ładunków
# o wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki (czyli, na przykład, dla siedmiu ładunków
# wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16, a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i
# uzasadnić jego poprawność), który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona
# (ale bez przekraczania pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się
# np. załadować przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając
# jednego ładunku, to lepsze jest to pierwsze rozwiązanie).
#
#
#
# Sortujemy dostępne skrzynie malejąco po ich wagach i zachłannie dobieramy skrzynie, jeżeli tylko masa obecnie
# rozważanej skrzyni jest mniejsza od dostępnego miejsca. Algorytm kończy działanie, kiedy osiągnie maksymalną
# ładowność bądź przejdzie po całej tablicy wag dostępnych obiektów. Kiedy dany element został już w tablicy
# rozważony, to przesuwamy wskaźnik o jedną pozycję dalej. Mamy pewność, że podany zachłanny algorytm jest poprawny,
# ponieważ w każdej parze liczb w tablicy jedna jest wielokrotnością drugiej, zatem mając do wyboru np. skrzynię o
# masie 16 i kilka innych i biorąc kilka innych zamiast 16, aby osiągnąć maksymalną ładowność, i tak w pewnym momencie
# uzyskamy 16  kg.
