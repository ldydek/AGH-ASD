# Zadanie 4. (wieże) Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko
# ma klocki różnej wysokości. Pierwsze dziecko ma klocki o pewnych wysokościach w, drugie dziecko klocki o
# pewnych wysokościach itd.. Dzieci właśnie poszły zjeść deser zanim ułożą swoje wieże, ale jedno dziecko
# zostało. Ma teraz jedyną okazję, żeby podebrać kilka klocków innym dzieciom tak, żeby jego wieża była
# najwyższa. Proszę podać możliwie najszybszy algorytm rozwiązujący ten problem, który zabiera minimalną
# ilość klocków. (Proszę zwrócić uwagę, że liczby mogą być bardzo duże.)
#
#
#
# Zapisuję sobie w pomocniczej tablicy sumy wysokości budowli każdej z dzieci. Potem sortuję podane klocki
# malejąco po wysokościach i patrzę:
# 1) Jeżeli moja budowla będzie najwyższa, to zwracam 0
# 2) wpp. w następujący sposób: jeżeli wysokość największego klocka w najwyższej budowli jest co najwyżej dwa razy
# mniejsza, to biorę najwyższy klocek ogólnie, który jeszcze nie należy do mnie. Jeżeli ten warunek nie jest spełniony,
# to biorę właśnie ten klocek.
# Powtarzam ten krok do momentu uzyskania najwyższej budowli.

# Rozwiązanie z wykładu. Gdybyśmy mieli wysokość "T", którą musi osiągnąć nasza wieża (wysokość "T" lub więcej), to
# można skorzystać z miksu heurystyk. Najwyższa wieża musi zostać sprowadzona poniżej wysokości "T". Jeśli wysokość
# naszej wieży nadal nie jest wystarczająca, to używamy do budowy globalnie największych klocków do momentu aż wysokość
# zostanie osiągnięta. Konkretnej wysokości "T" nie znamy, lecz wiemy iż musi być ona o jeden większa od wysokości
# pewnego klocka w zestawieniu. Jeśli klocków jest "n", to problem jesteśmy w stanie rozwiązać w wielomianowy sposób.


