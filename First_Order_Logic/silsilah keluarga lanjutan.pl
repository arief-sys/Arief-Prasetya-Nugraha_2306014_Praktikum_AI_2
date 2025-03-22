orangtua(david, john).
orangtua(amy, john).
orangtua(david, liza).
orangtua(amy, liza).
orangtua(jack, ray).
orangtua(karen, ray).
orangtua(jack, susan).
orangtua(karen, susan).
orangtua(john, peter).
orangtua(susan, peter).
orangtua(john, mary).
orangtua(susan, mary).

lakilaki(david).
lakilaki(jack).
lakilaki(john).
lakilaki(ray).
lakilaki(peter).

perempuan(amy).
perempuan(karen).
perempuan(liza).
perempuan(susan).
perempuan(mary).

saudara(john,liza).
saudara(ray,susan).
saudara(peter,mary).

ayah(X,Y):- orangtua(X,Y).
saudarakandung(Y, Z) :- orangtua(X, Y), orangtua(X, Z).
kakeknenek(X,Z) :- orangtua(X,Y), orangtua(Y,Z).
cucu(X,Y) :- orangtua(Y,X).


