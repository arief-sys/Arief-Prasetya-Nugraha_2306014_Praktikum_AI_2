anakIbu(andi).
anakIbu(budi).
anakIbu(cika).
anakIbu(dani).
anakIbu(emil).
not(anakIbu(fadil)).

sukaPermen(andi).
sukaPermen(budi).
sukaPermen(cika).
not(sukaPermen(dani)).
not(sukaPermen(email)).

siapaanakibu(X):- anakIbu(X).
mendapatpermen(X):- anakIbu(X), sukaPermen(X).
mendapatuang(X):- anakIbu(X), not(sukaPermen(X)).
tidakdapat(X):- not(anakIbu(X)).
