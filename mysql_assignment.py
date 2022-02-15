"""This module performs 4 sql queries like insert, update, delete and read which
is carried out on two database tables"""
import mysql.connector


class MysqlAssignment:
    """This is my Mysql Assignment given by my mentor Rushikesh
    which will insert, update, delete and read data from
    the respective tables"""
    list1 = []
    try:
        my_db = mysql.connector.connect(
            host="localhost",
            username="root",
            password="*******",
            database="mydatabase"
        )
    except ConnectionError:
        print("the connection to the database failed")
    my_cursor = my_db.cursor()

    @staticmethod
    def read_customers_table():
        """This method is reading the customers tables"""
        sql_display_table1 = "SELECT * FROM customers"
        MysqlAssignment.my_cursor.execute(sql_display_table1)
        my_result1 = MysqlAssignment.my_cursor.fetchall()
        for x_values in my_result1:
            print(x_values)

    @staticmethod
    def delete_customers_entry(key):
        """This method is deleting rows from the customers table"""
        sql = """DELETE FROM customers WHERE cust_id = %s"""
        value = (key,)
        MysqlAssignment.my_cursor.execute(sql, value)
        MysqlAssignment.my_db.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row of customers table deleted successfully")
        MysqlAssignment.read_customers_table()

    @staticmethod
    def delete_products_entry(key):
        """This method is deleting rows from products table"""
        sql = """DELETE FROM products WHERE prod_id = %s"""
        value = (key,)
        MysqlAssignment.my_cursor.execute(sql, value)
        MysqlAssignment.my_db.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row of products table deleted successfully")
        MysqlAssignment.read_products_table()

    @staticmethod
    def basic_input():
        """This method is fetching basic details from user"""
        try:
            option = input("What would you like to perform: insert -> 1,  update -> 2, "
                           "delete -> 3 or read -> 4? ")
        except ValueError:
            print("Please enter correct option")
        try:
            table_name = input("In which table: customers -> C or products -> P ? ")
        except ValueError:
            print("Please enter table name in upper case")
        return option, table_name

    @staticmethod
    def select_operation(option, table_name):
        """This method will select either of the 4 options"""
        # switcher = {
        #     '1': MysqlAssignment.insert_method(table_name),
        #     '2': MysqlAssignment.update_method(table_name),
        #     '3': MysqlAssignment.delete_method(table_name),
        #     '4': MysqlAssignment.read_method(table_name)
        # }
        if option == '1':
            MysqlAssignment.insert_method(table_name)
        elif option == '2':
            MysqlAssignment.update_method(table_name)
        elif option == '3':
            MysqlAssignment.delete_method(table_name)
        elif option == '4':
            MysqlAssignment.read_method(table_name)
        else:
            print("Invalid option selected")

    @staticmethod
    def insert_method(table_name):
        """This method will take inputs from the user and insert the data in the desired table"""
        if table_name == 'C':
            key = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            address = input("Enter Customer Address: ")
            MysqlAssignment.insert_into_customers_table(key, name, address)
        else:
            key = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            address = 'NA'
            MysqlAssignment.insert_into_products_table(key, name)

    @staticmethod
    def update_method(table_name):
        """This method will update either in Customers or Products table depending upon the table"""
        if table_name == 'C':
            MysqlAssignment.read_customers_table()
            print("Note* - Please update either name or address as ID is auto generated")
            key = input("Enter the correct ID of customer whose data you want to update :")
            note = input("Which field would you like to update: name or address? ")
            if note == 'name':
                new_field = input("Enter new name :")
            else:
                new_field = input("Enter new address :")
            MysqlAssignment.update_customers_table(note, new_field, key)
        else:
            MysqlAssignment.read_products_table()
            key = input("Enter the correct ID of product whose data you want to update :")
            new_field = input("Enter the updated product name: ")
            MysqlAssignment.update_products_table(new_field, key)

    @staticmethod
    def delete_method(table_name):
        """This method will delete the data"""
        if table_name == 'C':
            MysqlAssignment.read_customers_table()
            key = input("Enter which ID to delete: ")
            MysqlAssignment.delete_customers_entry(key)
        else:
            MysqlAssignment.read_products_table()
            key = input("Enter which ID to delete: ")
            MysqlAssignment.delete_products_entry(key)

    @staticmethod
    def read_method(table_name):
        """This method will read data from the specified folder"""
        if table_name == 'C':
            MysqlAssignment.read_customers_table()
        else:
            MysqlAssignment.read_products_table()

    @staticmethod
    def get_input_from_user():
        """This method is fetching input from user"""
        result_data = MysqlAssignment.basic_input()
        MysqlAssignment.select_operation(result_data[0], result_data[1])

    @staticmethod
    def insert_into_customers_table(key, name, address):
        """This method inserts values in the customers table"""
        sql = """INSERT INTO customers (cust_id, cust_name, cust_address) VALUES (%s, %s, %s)"""
        values = (key, name, address)
        MysqlAssignment.my_cursor.execute(sql, values)
        MysqlAssignment.my_db.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row inserted in customers table successfully")
        MysqlAssignment.read_customers_table()

    @staticmethod
    def update_customers_table(note, new_field, key):
        """This method will update customers table and will
        also display whole table for verification"""
        if note == 'address':
            sql = """UPDATE customers SET cust_address = %s WHERE cust_id = %s"""
        else:
            sql = """UPDATE customers SET cust_name = %s WHERE cust_id = %s"""
        new_values = (new_field, key)
        MysqlAssignment.my_cursor.execute(sql, new_values)
        MysqlAssignment.my_db.commit()
        MysqlAssignment.read_customers_table()

    @staticmethod
    def update_products_table(new_field, key):
        """This method will update products table and
        will display the updated entries for verification"""
        sql = """UPDATE products SET prod_name = %s WHERE prod_id = %s"""
        new_values = (new_field, key)
        MysqlAssignment.my_cursor.execute(sql, new_values)
        MysqlAssignment.my_db.commit()
        MysqlAssignment.read_products_table()

    @staticmethod
    def read_products_table():
        """This method will read all the data from products table"""
        sql_display_table2 = "SELECT * FROM products"
        MysqlAssignment.my_cursor.execute(sql_display_table2)
        my_result2 = MysqlAssignment.my_cursor.fetchall()
        for x_values in my_result2:
            print(x_values)

    @staticmethod
    def insert_into_products_table(key, name):
        """This method will insert values in the products table"""
        sql = """INSERT INTO products (prod_id, prod_name) VALUES (%s, %s)"""
        values = (key, name)
        MysqlAssignment.my_cursor.execute(sql, values)
        MysqlAssignment.my_db.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row inserted in products table successfully")
        MysqlAssignment.read_products_table()


sql_object = MysqlAssignment()
sql_object.get_input_from_user()

# if result is None:
#     print("")
# if (len(result) == 2 and
#       result[0] == 'C'):
#     sql_object.delete_customers_entry(result[1])
# elif (len(result) == 2 and
#       result[0] == 'P'):
#     sql_object.delete_products_entry(result[1])
# elif (len(result) == 3 and
#      result[2] != 'NA'):
#     sql_object.insert_into_customers_table(result[0], result[1], result[2])
# elif (len(result) == 3
#       and result[2] == 'NA'):
#     sql_object.insert_into_products_table(result[0], result[1])
# elif (len(result) == 3
#       and result[0] != 'NA'):
#     sql_object.update_customers_table(result)
# elif (len(result) == 3
#         and result[0] == 'NA'):
#     sql_object.update_products_table(result)
