
class DivBy12Error(Exception):
    
    def __init__(self):
        super().__init__("Division par 12 !")
    
def div(a,b):
    if b==12:
        # raise Exception('Division par 12 !')
        raise DivBy12Error()
    return a/b

def call_div(a,b):
    r=0
    try:
        print('OPEN LOG')
        r = div(a,b)
    finally:
        print('CLOSE LOG')

    return r

def main():
    try:
        a = 2
        b = 12
        c = call_div(a, b)
        print(c)
        
    except DivBy12Error as e :
        print("DivBy12Error",e)
    except Exception as e :
        print(e)
    print("la suite")
if __name__=='__main__':
    main()
