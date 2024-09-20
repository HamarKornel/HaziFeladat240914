import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

# müveletek
osszeg = szam1+szam2
kulumbseg = szam1-szam2
szorzas = szam1*szam2
hanyados = szam1/szam2
maradek = szam1 % szam2
hatvany = szam1**szam2

# kiiratás
print(osszeg)
print(kulumbseg)
print(szorzas)
print(hanyados)
print(maradek)
print(hatvany)
