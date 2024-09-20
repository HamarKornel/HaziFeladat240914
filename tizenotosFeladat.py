import beolvas

szam1 = beolvas.egszSzamBeolvas()
szam2 = beolvas.egszSzamBeolvas()
szam3 = beolvas.egszSzamBeolvas()

if szam1>szam2:
    if szam1<szam3:
        kozepsoSzam = szam1
    elif szam2>szam3:
        kozepsoSzam = szam2
    else:
        kozepsoSzam = szam3
        
else:
    if szam1>szam3:
        kozepsoSzam = szam1
    elif szam2<szam3:
        kozepsoSzam = szam2
    else:
        kozepsoSzam = szam3
        

print("A középsö szám értéke:", kozepsoSzam)