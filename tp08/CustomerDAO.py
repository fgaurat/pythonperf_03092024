import sqlite3
from Customer import Customer

class CustomerDAO:


    def __init__(self,db_file):
        self.con = sqlite3.connect(db_file)

    def findAll(self):
        
        sql = "SELECT id,first_name,last_name,email,gender,ip_address FROM customers_tbl"
        cur = self.con.cursor()
        rs = cur.execute(sql)
        for row in rs:
            c = Customer(*row)
            yield c
        

    def __del__(self):
        self.con.close()