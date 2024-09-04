
def div(a,b):
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
        b=0
        c = call_div(a, b)
        print(c)
        
    except Exception as e :
        print(e)
    print("la suite")
if __name__=='__main__':
    main()
