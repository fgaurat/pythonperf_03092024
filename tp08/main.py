from CustomerDAO import CustomerDAO

def main():
    dao = CustomerDAO('customers_db.db')
    customers = dao.findAll()
    print(customers)

if __name__=='__main__':
    main()
