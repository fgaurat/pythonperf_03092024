import copy


def main():
    l = [10,20,30,40,50]
    print(l)
    l[0] = 1000
    print(l[len(l)-1])
    print(l[-1])
    print(l[-2])
    l2 = l[2:4] # 1er elem est inclus, dernier exclue [2:4[
    l3 = l[2:]
    l4 = l[:4]
    l5 = l[:]
    print(l)
    l1 = l[:] # l1 = l shallow copy
    l1_1 = l.copy() # l1_1 = l shallow copy
    l1_2 = copy.copy(l) # l1_2 = l shallow copy
    
    l[0] = 10
    print(l) # [10,20,30,40,50]
    print(l1) # ?
    
    l = [
        [10,20,30],
        [40,50,60],
        [70,80,90]
    ]
    
    l1 = l[:] # shallow
    l1 = copy.deepcopy(l)
    l[1][1] = 1000
    print(l)
    print(l1)
    
    
    
    
    

if __name__=='__main__':
    main()
