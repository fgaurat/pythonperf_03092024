def add(*args):
    print(args)
    r = 0
    for i in args:
        r+=i
    
    return r

def hello(**kwargs):
    print("hello",kwargs)


def hello2(name,firstName,/): # positional only
    print(name,firstName)

def hello3(*,name,firstName): # keywords only
    print(name,firstName)


    
def main():
    l = [10,20,30,40,50]
    # print(l)
    # print(*l)
    # r = add(*l) #(10,20,30,40,50)
    # print(r) # 150
    
    # r = add(10,20,30,40,50)
    # print(r) # 150
    
    # a,b = l #ValueError: too many values to unpack (expected 2)
    # a,b,c,d,e,f = l # ValueError: not enough values to unpack (expected 6, got 5)
    a,b,c,*_ = l # ok
    
    print(a,b,c)
    
    hello(name="GAURAT",firstName="Fred")
    
    # hello2(name="GAURAT",firstName="Fred") Error :positional only
    hello2("GAURAT","Fred")
    
    hello3(firstName="Fred",name="GAURAT") # Error :keyword only
    
    print(50*'-')
    a = 2
    b=3
    s = "a:{0}, b:{1}".format(a,b)
    s = "a:{val_a}, b:{val_b}".format(val_a=a,val_b=b)
    #s = "{val_a=}, {val_b=}".format(val_a=a,val_b=b)  ne marche pas
    s = f"{a=}, {b=}"
    print(s)
    
    l = [10,20]
    # s = "v1: {},v2: {}".format(l[0],l[1])
    s = "v1: {},v2: {}".format(*l)
    d = {
        "name":"GAURAT",
        "firstName":"Fred"
    }
    # s = "name: {name},firstName: {firstName}".format(name=d['name'],firstName=d['firstName'])
    s = "name: {name},firstName: {firstName}".format(**d)
    print(s)


if __name__=='__main__':
    main()
