def old_mult2(l):
    r = []
    for i in l:
        r.append(i*2)
    return r


def mult2(item):
    return item*2

def main():
    l=[10,20,30,40,50]
    l2 = mult2(l) #  [20,40,60,80,100]
    print(l2)
    # l2 = list(map(mult2,l))
        
    l2 = list(map(lambda item:item*2,l))
    print(l2)
    # for i in l2:
    #     print(i)
    l2 = [i*2 for i in l]
    print(l2)

if __name__=='__main__':
    main()
