"""This module performs 4 sql queries like insert, update, delete and read which
is carried out on two database tables"""
import mysql.connector
from _testcapi import instancemethod


class MysqlAssignment:
    """This is my Mysql Assignment given by my mentor Rushikesh
    which will insert, update, delete and read data from
    the respective tables"""

    def __init__(self):
        try:
            self.my_db = mysql.connector.connect(
                host="localhost",
                username="root",
                password="*@@@@@@",
                database="mydatabase"
            )
        except ConnectionError:
            print("the connection to the database failed")
        self.my_cursor = self.my_db.cursor()

    @staticmethod
    def basic_input():
        """This method is fetching basic details from user"""
        option_num = int(input("What would you like to perform: insert -> 1,  update -> 2, "
                               "delete -> 3 or read -> 4? "))
        table_name = input("In which table: customers -> C or products -> P ? ")
        return option_num, table_name

    @instancemethod
    def read_customers_table(self):
        """This method is reading the customers tables"""
        sql_display_table1 = "SELECT * FROM customers"
        self.my_cursor.execute(sql_display_table1)
        my_result1 = self.my_cursor.fetchall()
        for x_values in my_result1:
            print(x_values)

    @instancemethod
    def insert_method(self, table_name):
        """This method will take inputs from the user and insert the data in the desired table"""
        if table_name == 'C':
            key = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            address = input("Enter Customer Address: ")
            sql = """INSERT INTO customers (cust_id, cust_name, cust_address) VALUES (%s, %s, %s)"""
            values = (key, name, address)
            self.my_cursor.execute(sql, values)
            self.my_db.commit()
            print(self.my_cursor.rowcount, "row inserted in customers table successfully")
        else:
            key = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            sql = """INSERT INTO products (prod_id, prod_name) VALUES (%s, %s)"""
            values = (key, name)
            self.my_cursor.execute(sql, values)
            self.my_db.commit()
            print(self.my_cursor.rowcount, "row inserted in products table successfully")

    @instancemethod
    def update_method(self, table_name):
        """This method will update either in Customers or Products table depending upon the table"""
        if table_name == 'C':
            print("Note* - Please update either name or address as ID is auto generated")
            key = input("Enter the correct ID of customer whose data you want to update :")
            note = input("Which field would you like to update: name or address? ")
            if note == 'name':
                new_field = input("Enter new name :")
                sql = """UPDATE customers SET cust_name = %s WHERE cust_id = %s"""
            else:
                new_field = input("Enter new address :")
                sql = """UPDATE customers SET cust_address = %s WHERE cust_id = %s"""
            new_values = (new_field, key)
            self.my_cursor.execute(sql, new_values)
            self.my_db.commit()
        else:
            key = input("Enter the correct ID of product whose data you want to update :")
            new_field = input("Enter the updated product name: ")
            sql = """UPDATE products SET prod_name = %s WHERE prod_id = %s"""
            new_values = (new_field, key)
            self.my_cursor.execute(sql, new_values)
            self.my_db.commit()

    @instancemethod
    def delete_method(self, table_name):
        """This method will delete the data"""
        if table_name == 'C':
            key = input("Enter which ID to delete: ")
            sql = """DELETE FROM customers WHERE cust_id = %s"""
            value = (key,)
            self.my_cursor.execute(sql, value)
            self.my_db.commit()
            print(self.my_cursor.rowcount, "row of customers table deleted successfully")
        else:
            key = input("Enter which ID to delete: ")
            sql = """DELETE FROM products WHERE prod_id = %s"""
            value = (key,)
            self.my_cursor.execute(sql, value)
            self.my_db.commit()
            print(self.my_cursor.rowcount, "row of products table deleted successfully")

    @instancemethod
    def read_products_table(self):
        """This method will read all the data from products table"""
        sql_display_table2 = "SELECT * FROM products"
        self.my_cursor.execute(sql_display_table2)
        my_result2 = self.my_cursor.fetchall()
        for x_values in my_result2:
            print(x_values)


sql_object = MysqlAssignment()
option, table = sql_object.basic_input()

if option == 1:
    if table == 'C':
        sql_object.insert_method(table)
        sql_object.read_customers_table()
    else:
        sql_object.insert_method(table)
        sql_object.read_products_table()
elif option == 2:
    if table == 'C':
        sql_object.read_customers_table()
        sql_object.update_method(table)
        sql_object.read_customers_table()
    else:
        sql_object.read_products_table()
        sql_object.update_method(table)
        sql_object.read_products_table()
elif option == 3:
    if table == 'C':
        sql_object.read_customers_table()
        sql_object.delete_method(table)
        sql_object.read_customers_table()
    else:
        sql_object.read_products_table()
        sql_object.delete_method(table)
        sql_object.read_products_table()
elif option == 4:
    if table == 'C':
        sql_object.read_customers_table()
    else:
        sql_object.read_products_table()
