from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
            db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
            db.setDatabaseName('todo_db.db')

            if not db.open():
                QtWidgets.QMessageBox.critical(None, 'Cannot open database', 'Click Cancel to exit.', QtWidgets.QMessageBox.Cancel)
                return False
            query = QtSql.QSqlQuery()
            query.exec('CREATE TABLE IF NOT EXISTS tasks ('
                       'ID integer primary key AUTOINCREMENT, '
                       'name VARCHAR(255), '
                       'status VARCHAR(20), '
                       'date_create VARCHAR(20), '
                       'date_deadline VARCHAR(20), '
                       'description VARCHAR(255)) ')
            return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)

        query.exec()
        return query

    def add_new_task_query(self, name, status, date_create, date_deadline, description):
        sql_query = 'INSERT INTO tasks (name, status, date_create, date_deadline, description) VALUES(?, ?, ?, ?, ?)'
        self.execute_query_with_params(sql_query, [name, status, date_create, date_deadline, description])

    def update_task_query(self, name, status, date_create, date_deadline, description, id):
        sql_query = "UPDATE tasks SET name=?, status=?, date_create=?, date_deadline=?, description=? WHERE ID=?"
        self.execute_query_with_params(sql_query, [name, status, date_create, date_deadline, description, id])

    def delete_task_query(self, id):
        sql_query = "DELETE FROM tasks WHERE ID=?"
        self.execute_query_with_params(sql_query, [id])

    def export_data_to_excel(self):
        sql_query = 'SELECT * FROM tasks'
        query = self.execute_query_with_params(sql_query)
        return query
    
    def get_task_data(self, task_id):
        sql_query = 'SELECT * FROM tasks WHERE ID=?'
        query = self.execute_query_with_params(sql_query, [task_id])

        task_data = {}
        if query.next():
            task_data['id'] = query.value(0)
            task_data['name'] = query.value(1)
            task_data['status'] = query.value(2)
            task_data['date_create'] = query.value(3)
            task_data['date_deadline'] = query.value(4)
            task_data['description'] = query.value(5)
        else:
            print("No rows returned for task ID:", task_id)  # Отладочный вывод

        return task_data
