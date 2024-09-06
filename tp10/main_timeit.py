import timeit

def init_loop():
    r = []
    for i in range(100):
        r.append(i)

def init_map():
    r = list(map(lambda i:i,range(100)))

def init_comp():
    r = [i for i in range(100)]

def main():
    t1 = timeit.timeit("init_loop()",setup="from __main__ import init_loop")
    t2 = timeit.timeit("init_map()",setup="from __main__ import init_map")
    t3 = timeit.timeit("init_comp()",setup="from __main__ import init_comp")
    print("init_loop",t1)
    print("init_map",t2)
    print("init_comp",t3)



def main01():
    l = ["val 01","val 02","val 03"]

    s = '-'.join(l)
    
    s = {i for i in range(4)}
    d = {i:'toto' for i in range(4)}
    print(type(l))
    print(type(d))
    print(type(s))
    t = 1,2,3
    t1 = (i for i in range(4))
    print(t,type(t))
    print(type(t1))
    print(t1,next(t1))



if __name__=='__main__':
    main()
