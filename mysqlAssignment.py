import mysql.connector


class MysqlAssignment:
    try:
        my_database = mysql.connector.connect(
            host="localhost",
            username="root",
            password="*******",
            database="mydatabase"
        )
    except:
        print("the connection to the database failed")
    my_cursor = my_database.cursor()

    @staticmethod
    def readCustomersTable():
        sql_display_table1 = "SELECT * FROM customers"
        MysqlAssignment.my_cursor.execute(sql_display_table1)
        my_result1 = MysqlAssignment.my_cursor.fetchall()
        for x in my_result1:
            print(x)

    @staticmethod
    def deleteCustomersEntry(id):
        sql = """DELETE FROM customers WHERE cust_id = %s"""
        value = (id,)
        MysqlAssignment.my_cursor.execute(sql, value)
        MysqlAssignment.my_database.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row of customers table deleted successfully")
        MysqlAssignment.readCustomersTable()

    @staticmethod
    def deleteProductsEnter(id):
        print(id)
        sql = """DELETE FROM products WHERE prod_id = %s"""
        value = (id,)
        MysqlAssignment.my_cursor.execute(sql, value)
        MysqlAssignment.my_database.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row of products table deleted successfully")
        MysqlAssignment.readProductsTable()

    @staticmethod
    def basicInput():
        option = input("What would you like to perform: insert -> 1,  update -> 2, delete -> 3 or read -> 4? ")
        table_name = input("In which table: customers -> C or products -> P ? ")
        return option, table_name

    @staticmethod
    def getInputFromUser():
        result_data = MysqlAssignment.basicInput()
        option = result_data[0]
        table_name = result_data[1]
        try:
            if option == '1':
                if table_name == "C":
                    id = input("Enter Customer ID: ")
                    name = input("Enter Customer Name: ")
                    address = input("Enter Customer Address: ")
                    return option, table_name, id, name, address
                else:
                    id = input("Enter Product ID: ")
                    name = input("Enter Product Name: ")
                    return option, table_name, id, name
            elif option == '2':
                if table_name == 'C':
                    MysqlAssignment.readCustomersTable()
                    print("Note* - Please update either name or address as ID is auto generated")
                    id = input("Enter the correct ID of customer whose data you want to update :")
                    note = input("Which field would you like to update: name or address? ")
                    if note == 'name':
                        new_name = input("Enter new name :")
                        return note, new_name, id
                    else:
                        new_add = input("Enter new address :")
                        return note, new_add, id
                elif table_name == 'P':
                    MysqlAssignment.readProductsTable()
                    id = input("Enter the correct ID of product whose data you want to update :")
                    name = input("Enter the updated product name: ")
                    return id, name
            elif option == '3':
                if table_name == 'C':
                    MysqlAssignment.readCustomersTable()
                    id = input("Enter which ID to delete: ")
                    return table_name, id
                elif table_name == 'P':
                    MysqlAssignment.readProductsTable()
                    id = input("Enter which ID to delete: ")
                    return table_name, id
            elif option == '4':
                # if table_name == 'C':
                #     name = MysqlAssignment.readCustomersTable()
                # else:
                #     name = MysqlAssignment.readProductsTable()
                # return name
                name = MysqlAssignment.readCustomersTable() if table_name == 'C' else MysqlAssignment.readProductsTable()
                return name
        except:
            print("Please input correct option and table name")

    @staticmethod
    def insertIntoCustomersTable(id, name, address):
        sql = """INSERT INTO customers (cust_id, cust_name, cust_address) VALUES (%s, %s, %s)"""
        values = (id, name, address)
        MysqlAssignment.my_cursor.execute(sql, values)
        MysqlAssignment.my_database.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row inserted in customers table successfully")
        MysqlAssignment.readCustomersTable()

    @staticmethod
    def updateCustomersTable(values):
        if values[0] == 'address':
            sql = """UPDATE customers SET cust_address = %s WHERE cust_id = %s"""
        elif values[0] == 'name':
            sql = """UPDATE customers SET cust_name = %s WHERE cust_id = %s"""
        new_values = (values[1], values[2])
        MysqlAssignment.my_cursor.execute(sql, new_values)
        MysqlAssignment.my_database.commit()
        MysqlAssignment.readCustomersTable()

    @staticmethod
    def updateProductsTable(values):
        sql = """UPDATE products SET prod_name = %s WHERE prod_id = %s"""
        new_values = (values[1], values[0])
        MysqlAssignment.my_cursor.execute(sql, new_values)
        MysqlAssignment.my_database.commit()
        MysqlAssignment.readProductsTable()

    @staticmethod
    def readProductsTable():
        sql_display_table2 = "SELECT * FROM products"
        MysqlAssignment.my_cursor.execute(sql_display_table2)
        my_result2 = MysqlAssignment.my_cursor.fetchall()
        for x in my_result2:
            print(x)

    @staticmethod
    def insertIntoProductsTable(id, name):
        sql = """INSERT INTO products (prod_id, prod_name) VALUES (%s, %s)"""
        values = (id, name)
        MysqlAssignment.my_cursor.execute(sql, values)
        MysqlAssignment.my_database.commit()
        print(MysqlAssignment.my_cursor.rowcount, "row inserted in products table successfully")
        MysqlAssignment.readProductsTable()


sql_object = MysqlAssignment()
result = sql_object.getInputFromUser()

if result is None:
    print("")
elif (len(result) == 2 and
      result[0] == 'C'):
    sql_object.deleteCustomersEntry(result[1])
elif (len(result) == 2 and
      result[0] == 'P'):
    sql_object.deleteProductsEnter(result[1])
elif (len(result) == 5 and
      result[0] == '1'):
    sql_object.insertIntoCustomersTable(result[2], result[3], result[4])
elif (len(result) == 4 and
      result[0] == '1'):
    sql_object.insertIntoProductsTable(result[2], result[3])
elif len(result) == 3:
    sql_object.updateCustomersTable(result)
elif len(result) == 2:
    sql_object.updateProductsTable(result)

