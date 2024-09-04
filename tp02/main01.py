
def make_incrementor(inc_value):
    # arr = copy
    def f(i):
        return inc_value+i
    
    return f

def main():
    
    do_inc = make_incrementor(10)
    r = do_inc(5)
    print(r) # 15

    r = do_inc(7)
    print(r) 
    r = do_inc(18)
    print(r) 
    r = do_inc(15)
    print(r) 

if __name__=='__main__':
    main()
