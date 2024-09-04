import traceback


def main():
    try:
        a = 2
        b = int(input("b: "))
        c = a/b
        print("c", c)
    except ValueError as e:
        print("Erreur !", e)
    except TypeError as e:
        print("Erreur !", e)
    except ZeroDivisionError as e:
        print("Erreur !", e)
        # traceback.print_exc()
    except Exception as e:
        print("Erreur !", e, type(e))
        # traceback.print_exc()
    else:
        print("pas d'erreur")
    finally:
        print("finally")
        

    print("la suite du code")

if __name__ == '__main__':
    main()
