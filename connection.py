from PyQt6 import QtWidgets, QtSql
import pyodbc
import sys

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()
    
    def create_connection(self):
        try:
            with open('connect.txt', 'r') as connect_file:
                driver = connect_file.readline().strip()
                server = connect_file.readline().strip()
                database = connect_file.readline().strip()
                trusted_conneection = connect_file.readline().strip()
            db = QtSql.QSqlDatabase.addDatabase('QODBC')
            db.setDatabaseName(
                f"Driver={driver};"
                f"Server={server};"
                f"Database={database};"
                f"Trusted_Connection={trusted_conneection};"
            )
            db.open()
            query = QtSql.QSqlQuery()
            query.exec("SELECT * FROM Products")
            while query.next():
                id = int(query.value(0))
                prodname = query.value(1)
                manuf = str(query.value(2))
                prodcount = query.value(3)
                pricee = query.value(4)
                print(id, prodname, manuf, prodcount, pricee)
            sql = QtSql.QSqlQuery()
            sql.exec("SELECT Distinct TABLE_NAME FROM information_schema.TABLES")
            self.arr_table_name = []
            while sql.next():
                print(sql.value(0))
                self.arr_table_name.append(sql.value(0))
            '''with open('connect.txt', 'r') as connect_file:
                driver = connect_file.readline().strip()
                server = connect_file.readline().strip()
                database = connect_file.readline().strip()
                trusted_conneection = connect_file.readline().strip()
            self.conn = pyodbc.connect(
                f"Driver={driver};"
                f"Server={server};"
                f"Database={database};"
                f"Trusted_Connection={trusted_conneection};"
            )
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT * FROM Products")
            records = self.cursor.fetchall()
            for row in records:
                print(f"Строка: {row}")'''
            return print("Connection succesfull")
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed connection", "Не удалось подключиться к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
            return sys.exit()
    
    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)
        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        query.exec()
    
    def new_record_query(self, table, pname, manuf, pcount, price):
        try:
            sql_query = f"INSERT INTO {table} (ProductName, Manufacturer, ProductCount, Price) VALUES (?, ?, ?, ?)"
            self.execute_query_with_params(sql_query, [pname, manuf, pcount, price])
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def edit_record_query(self, pname, manuf, pcount, price, id):
        try:
            sql_query = "UPDATE Products SET ProductName = ?, Manufacturer = ?, ProductCount = ?, Price = ? WHERE Id = ?"
            self.execute_query_with_params(sql_query, [pname, manuf, pcount, price, id])
        except:
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def del_record_query(self, id):
        try:
            sql_query = "DELETE FROM Products WHERE Id = ?"
            self.execute_query_with_params(sql_query, [id])
        except:
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)