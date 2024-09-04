from Rectangle import Rectangle
from DataRectangle import DataRectangle


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
    
    print(50*'-')
    r = Rectangle(25,2)
    r1 = Rectangle(25,2)
    print(r)

    if r==r1:
        print('ok')
    else:
        print('ko')

    print(50*'-')
    d = DataRectangle(5,9)
    d1 = DataRectangle(5,9)
    if d==d1:
        print("ok DataRectangle")
    else:
        print("ko DataRectangle")
    print(d)
    print(d.surface)

if __name__=='__main__':
    main()
