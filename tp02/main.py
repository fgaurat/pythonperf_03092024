def do_log(file_name):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(f'LOG to {file_name}',*args,**kwargs)
            r = func(*args,**kwargs)
            print(f'LOG RETURN to {file_name}',r)
            return r

        return wrapper
    return decorator

@do_log(file_name='toto.log')
def say_hello(name):
    r = f'Hello {name}'
    return r

def main():
    pass
    # n = "Fred"
    # r = say_hello(n)
    
    # print(r)



if __name__=='__main__':
    main()
