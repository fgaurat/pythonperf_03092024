from Carre import Carre

def main():
    c = Carre(2)
    print(c.surface)
    c.cote= 3
    print(c.cote)
    print(c.longueur)
    print(c.largeur)

    print(c.surface)


if __name__=='__main__':
    main()
