import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

# müveletek
osszeg = szam1+szam2
kulumbseg = szam1-szam2
szorzas = szam1*szam2
hanyados = szam1/szam2
maradek = szam1 % szam2
hatvany1 = szam1**szam2
hatvany2 = szam2**szam1

# kiiratás
print(str(szam1)+"+"+str(szam2)+"="+str(osszeg))
print(str(szam1)+"-"+str(szam2)+"="+str(kulumbseg))
print(str(szam1)+"*"+str(szam2)+"="+str(szorzas))
print(str(szam1)+"/"+str(szam2)+"="+str(hanyados))
print(str(szam1)+"%"+str(szam2)+"="+str(maradek))
print(str(szam1)+"^"+str(szam2)+"="+str(hatvany1))
print(str(szam2)+"^"+str(szam1)+"="+str(hatvany2))
