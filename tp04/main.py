from Rectangle import Rectangle


def main():
    # Red Green Refactor
    r = Rectangle(5,2)
    r1 = Rectangle(5,2)
    r2 = Rectangle(5,2)
    r3 = Rectangle()

    # print(r.get_longueur())
    # r.set_longueur(12)
    # print(r.get_longueur())

    print(r.longueur)
    r.longueur = 12
    print(r.longueur)

    # r.toto="truc"

    # print(r.toto)
    # print(r.__dict__)

    print("Rectangle.cpt",Rectangle.get_cpt())
    print("r.get_cpt()",r.get_cpt())
    print("r1.get_cpt()",r1.get_cpt())
    print("r2.get_cpt()",r2.get_cpt())
    print(50*'-')

    line = "5;6"
    r4 = Rectangle.buildFromStr(line)

    print(r4.longueur)
    print(r4.largeur)
if __name__=='__main__':
    main()
