from Carre import Carre
from Cercle import Cercle
from Rectangle import Rectangle
from typing import Protocol



class SurfaceAble(Protocol):
    @property
    def surface(self): 
        pass

def showSurface(o:SurfaceAble):
    print("showSurface",o.surface)

def main():
    c = Carre(2)
    print(c.surface)
    c.cote= 3
    print(c.cote)
    print(c.longueur)
    print(c.largeur)

    print(c.surface)
    print(50*'-')
    ce = Cercle(2)
    print(ce.surface)
    r = Rectangle(2,3)

    
    showSurface(r)
    showSurface(c)
    showSurface(ce)
if __name__=='__main__':
    main()
