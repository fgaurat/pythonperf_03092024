import csv
import sqlite3


def main():

    csv_file="MOCK_DATA.csv"
    sql= """INSERT INTO customers_tbl(first_name,last_name,email,gender,ip_address)
    VALUES(?,?,?,?,?)
    """
    con = sqlite3.connect("customers_db.db")

    with open(csv_file) as f:
        reader = csv.DictReader(f)
        for data in reader:
            print(data)
            del data['id']
            con.execute(sql,list(data.values()))
    
    con.commit()
    con.close()

if __name__=='__main__':
    main()
