import sqlite3
from Customer import Customer

class CustomerDAO:


    def __init__(self,db_file):
        self.con = sqlite3.connect(db_file)


    def __enter__(self):
        return self

    def __exit__(self, exc_type,exc_value,exc_traceback):
        if exc_type is None:
            self.con.commit()
        else:
            self.con.rollback()
        
        self.con.close()
        self.con = None


    def findAll(self):
        
        sql = "SELECT id,first_name,last_name,email,gender,ip_address FROM customers_tbl"
        cur = self.con.cursor()
        rs = cur.execute(sql)
        for row in rs:
            c = Customer(*row)
            yield c
        

    def __del__(self):
        if self.con is not None:
            self.con.close()