import sys

def main():
    a=2
    b=2
    print("a",a,hex(id(a)))
    print("b",b,hex(id(b)))
    a=3
    print(a,hex(id(a)))

    
    
    print("getrefcount",sys.getrefcount(4567841789752498456))
    a = 4567841789752498456
    print("getrefcount",sys.getrefcount(4567841789752498456))
if __name__=='__main__':
    main()
