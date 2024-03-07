from PyQt6 import QtWidgets, QtSql
import sys

class Data:
    def __init__(self):
        super(Data, self).__init__()
    
    def create_connection(self, server):
        try:
            state = False
            with open('./_internal/connect/connect_with_windows.txt', 'r') as connect_file:
                driver = connect_file.readline().strip()
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
    
    def create_connection_with_sql(self, server, username, password):
        try:
            state = False
            with open('./_internal/connect/connect_with_sql.txt', 'r') as connect_file:
                driver = connect_file.readline().strip()
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
    
    def check_server_role(self):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec("IF IS_SRVROLEMEMBER ('sysadmin') = 1"
                     "SELECT 'yes'"
                     "ELSE SELECT 'no';")
            self.arr_roles = []
            while sql.next():
                self.arr_roles.append(sql.value(0))
            return self.arr_roles
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)

    
    def execute_query_with_params(self, sql_query, query_values=None):
        try:
            query = QtSql.QSqlQuery()
            query.prepare(sql_query)
            if query_values is not None:
                for query_value in query_values:
                    query.addBindValue(query_value)
            query.exec()
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def new_record_query(self, table, column, arr_add_text):
        try:
            check = self.check_identity(table, column[0])
            if check[0] == 0:
                arr_question = ['?' for x in range(len(arr_add_text))]
                sql_query = f"INSERT INTO [{table}] ([{'], ['.join(column)}]) VALUES ({', '.join(arr_question)});"
            else:
                arr_add_text = arr_add_text[1:]
                arr_question = ['?' for x in range(len(arr_add_text))]
                sql_query = f"INSERT INTO [{table}] ([{'], ['.join(column[1:])}]) VALUES ({', '.join(arr_question)});"
            self.execute_query_with_params(sql_query, arr_add_text)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def edit_record_query(self, table, column, arr_edit_text):
        try:
            check = self.check_identity(table, column[0])
            if check[0] == 0:
                arr_for_edit = ['[' + x + '] = ?' for x in column]
                sql_query = f"UPDATE [{table}] SET {', '.join(arr_for_edit)} WHERE [{column[0]}] = ?"
            else:
                arr_edit_text = arr_edit_text[1:]
                arr_for_edit = ['[' + x + '] = ?' for x in column]
                sql_query = f"UPDATE [{table}] SET {', '.join(arr_for_edit[1:])} WHERE [{column[0]}] = ?"
            self.execute_query_with_params(sql_query, arr_edit_text)
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def del_record_query(self, table, column, id):
        try:
            sql_query = f"DELETE FROM [{table}] WHERE [{column[0]}] = ?"
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
            sql.exec(f"SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}';")
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
            sql.exec(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}';")
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
            sql.exec(f"SELECT * FROM [{table}] WHERE [{column[0]}] = '{id}';")
            self.arr_current_entry = []
            i = 0
            while sql.next():
                while sql.value(i) is not None:
                    self.arr_current_entry.append(sql.value(i))
                    i += 1
                i = 0
            return self.arr_current_entry
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def test(self):
        table = 'Ведомость платежей'
        length = len(table)
        sql = QtSql.QSqlQuery()
        sql.exec(f"SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS WHERE constraint_type = 'FOREIGN KEY' AND table_name = '{table}';")
        self.arr_foreign_key = []
        while sql.next():
            foreign_key = sql.value(2)
            pos = foreign_key.find(table)
            start_pos = pos + length + 1
            self.arr_foreign_key.append(foreign_key[start_pos:])
        return self.arr_foreign_key
    
    def test2(self):
        table = 'Ведомость платежей'
        sql = QtSql.QSqlQuery()
        sql.exec(f"EXEC sp_MSdependencies N'dbo.{table}'")
        self.arr_foreign_key = []
        i = 1
        while sql.next():
            foreign_key = sql.value(1)
            if sql.value(3) == i:
                self.arr_foreign_key.append(foreign_key)
                i += 1
        return self.arr_foreign_key
    
    def select_relation(self, table):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT "
                     f"f.name AS foreign_key_name "
                     f",OBJECT_NAME(f.parent_object_id) AS table_name "
                     f",COL_NAME(fc.parent_object_id, fc.parent_column_id) AS constraint_column_name "
                     f",OBJECT_NAME (f.referenced_object_id) AS referenced_object "
                     f",COL_NAME(fc.referenced_object_id, fc.referenced_column_id) AS referenced_column_name "
                     f"FROM sys.foreign_keys AS f "
                     f"INNER JOIN sys.foreign_key_columns AS fc "
                     f"ON f.object_id = fc.constraint_object_id "
                     f"WHERE f.parent_object_id = OBJECT_ID('dbo.{table}');")
            self.arr_constraint_keys = []
            while sql.next():
                arr_temp = []
                arr_temp.append(sql.value(1))
                arr_temp.append(sql.value(2))
                arr_temp.append(sql.value(3))
                arr_temp.append(sql.value(4))
                self.arr_constraint_keys.append(arr_temp)
            return self.arr_constraint_keys
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def select_foreign_values(self, column, table):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT [{column}] FROM [{table}];")
            self.arr_constraint_values = []
            while sql.next():
                self.arr_constraint_values.append(str(sql.value(0)))
            return self.arr_constraint_values
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def convert_date(self, date_text):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT CONVERT(datetime2, '{date_text}');")
            self.arr_convert = []
            while sql.next():
                self.arr_convert.append(str(sql.value(0)))
            return self.arr_convert
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)
    
    def check_identity(self, table, column):
        try:
            sql = QtSql.QSqlQuery()
            sql.exec(f"SELECT is_identity FROM sys.columns WHERE object_id = object_id('{table}') AND name = '{column}';")
            self.arr_identity = []
            while sql.next():
                self.arr_identity.append(sql.value(0))
            return self.arr_identity
        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(None, "Failed request", "Не удалось выполнить запрос к базе данных", QtWidgets.QMessageBox.StandardButton.Cancel)