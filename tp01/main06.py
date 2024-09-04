
def main():
    p = r"c:\newProject\test"
    print(p)
    
    l = [10,20,30,40,50]
    
    for i in l:
        print(i)
        if i == 300:
            print("found")
            break
    else:
        print("not found")
    
    print("la suite")
    
if __name__=='__main__':
    main()
