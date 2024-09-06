from CustomerDAO import CustomerDAO


def filterFemale(stream):

    for elem in stream:
        if elem.gender == "Female":
            yield elem

def main():
    # dao = CustomerDAO('customers_db.db')

    with CustomerDAO('customers_db.db') as dao:
        customers = dao.findAll()
        # c1 = next(customers)
        # print(c1)
        # c2 = next(customers)
        # print(c2)


        # all = list(customers)

        for c in filterFemale(customers):
            print(c)
if __name__=='__main__':
    main()
