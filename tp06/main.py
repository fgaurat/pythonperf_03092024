from Rectangle import Rectangle
from RectangleMetaSingleton import RectangleMetaSingleton
from RectangleSingletonDeco import RectangleSingletonDeco
def main():
    r = Rectangle()
    r1 = Rectangle()
    print(id(r))
    print(id(r1))

    print(type(r))
    print(type(Rectangle))

    r1 = RectangleMetaSingleton(1,2)
    print(id(r1),r1)
    r2 = RectangleMetaSingleton(3,4)
    print(id(r2),r2)
    print(50*'-')
    r1 = RectangleSingletonDeco()
    r2 = RectangleSingletonDeco()
    print(id(r1),r1)
    print(id(r2),r2)

if __name__=='__main__':
    main()
