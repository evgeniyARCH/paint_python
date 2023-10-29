def coord_isk(coord,mass):
    xcord = coord[0]
    ycord = coord[1]
    xmass = mass[ycord-1]
    symbol = xmass[xcord-1]
    return symbol


def coord_ris(ccord,mass):
    xcord = ccord[1]
    ycord = ccord[2]
    csymbol = ccord[0]
    xmass = mass[ycord-1]
    xmass[xcord-1] = csymbol
    return mass

def chislo_prov(prov,text):  
    nol = 1
    while nol==1:
        prov = input(text) 
        try:
            prov = int(prov)
            nol = 0
            return prov
        except ValueError:
            print("это не число")




