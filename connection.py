from PyQt6 import QtWidgets, QtSql
import sys

class Data:
    def __init__(self):
        super(Data, self).__init__()
    
    def create_connection(self):
        try:
            state = False
            with open('connect_local.txt', 'r') as connect_file: #ПОТОМ ПОМЕНЯТЬ ДЛЯ WINDOWS SERVER
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
            if db.open():
                state = True
            return state
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed connection", "Не удалось подключиться к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
            return sys.exit()
    
    def create_connection_with_sql(self, username, password):
        try:
            state = False
            with open('connect_with_sql.txt', 'r') as connect_file:
                driver = connect_file.readline().strip()
                server = connect_file.readline().strip()
                database = connect_file.readline().strip()
            db = QtSql.QSqlDatabase.addDatabase('QODBC')
            db.setDatabaseName(
                f"Driver={driver};"
                f"Server={server};"
                f"Database={database};"
                f"UID={username};"
                f"PWD={password};"
            )
            if db.open():
                state = True
            return state
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
    
    def new_record_query(self, table, column, arr_add_text):
        try:
            arr_question = ['?' for x in range(len(arr_add_text))]
            sql_query = f"INSERT INTO [{table}] ({', '.join(column[1:])}) VALUES ({', '.join(arr_question)})"
            self.execute_query_with_params(sql_query, arr_add_text)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def edit_record_query(self, table, column, arr_edit_text):
        try:
            arr_for_edit = [x + ' = ?' for x in column]
            sql_query = f"UPDATE [{table}] SET {', '.join(arr_for_edit[1:])} WHERE {column[0]} = ?"
            self.execute_query_with_params(sql_query, arr_edit_text)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def del_record_query(self, table, column, id):
        try:
            sql_query = f"DELETE FROM [{table}] WHERE {column[0]} = ?"
            self.execute_query_with_params(sql_query, [id])
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def select_table_name(self):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec("SELECT Distinct TABLE_NAME FROM information_schema.TABLES")
            self.arr_table_name = []
            while sql.next():
                self.arr_table_name.append(sql.value(0))
            return self.arr_table_name
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def select_data_type(self, table):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '[{table}]';")
            self.arr_column_name = []
            while sql.next():
                self.arr_column_name.append(sql.value(0))
            return self.arr_column_name
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def select_column_name(self, table):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '[{table}]';")
            self.arr_column_name = []
            while sql.next():
                self.arr_column_name.append(sql.value(0))
            return self.arr_column_name
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def select_current_entry(self, table, id, column):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT * FROM [{table}] WHERE {column[0]} = '{id}';")
            self.arr_current_entry = []
            i = 0
            while sql.next():
                while sql.value(i) is not None:
                    print(sql.value(i))
                    self.arr_current_entry.append(sql.value(i))
                    i += 1
                i = 0
            return self.arr_current_entry
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def test(self):
        sql = QtSql.QSqlQuery()
        sql.exec("SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS;")
        self.arr_column_name = []
        while sql.next():
            self.arr_column_name.append(sql.value(0))
        return self.arr_column_name