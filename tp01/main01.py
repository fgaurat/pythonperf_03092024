import lib


c =50

def scope_var():
    global c
    a=2
    print("scope_var")
    c= 1542
    print("c",c)

    print(a)
    
    if True:
        b=12
    print(b)
    
    
def main():
    print("Hello")
    lib.hello()
    print(lib.a)
    
    print("c",c)
    scope_var()
    print("end c",c)

if __name__ == "__main__":
    main()