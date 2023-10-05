import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from main2_ui import Ui_MainWindow
from connection import Data
from task_ui import Ui_Add_Task
from PySide6.QtSql import QSqlTableModel
from PySide6 import QtWidgets
import datetime
from openpyxl import Workbook
from PySide6 import QtCore

class TaskList(QMainWindow):
    def __init__(self):
        super(TaskList, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.btn_add_task.clicked.connect(self.open_task_ui)
        self.ui.btn_edit_task.clicked.connect(self.open_task_ui)
        self.ui.btn_delete_task.clicked.connect(self.delete_task)
        self.ui.btn_export_xls.clicked.connect(self.export_data)

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('tasks')
        self.model.select()
        self.ui.tbl_tasklist.setModel(self.model)

    def open_task_ui(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Add_Task()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == 'Add task':
            self.ui_window.btn_save.clicked.connect(self.add_new_task)
            self.ui_window.btn_cancel.clicked.connect(self.new_window.close)
        else:
            self.ui_window.btn_save.clicked.connect(self.edit_task)
            self.ui_window.btn_cancel.clicked.connect(self.new_window.close)

            # Получение индекса выбранной задачи
            indexes = self.ui.tbl_tasklist.selectedIndexes()
            if indexes:
                index = indexes[0]
                row = index.row()
                task_id = str(self.ui.tbl_tasklist.model().data(index.sibling(row, 0)))

            # Получение текущих данных задачи
            task_data = self.conn.get_task_data(task_id)

            # Предзаполнение полей окна редактирования
            self.ui_window.name_value.setPlainText(task_data['name'])
            self.ui_window.status_value.setCurrentText(task_data['status'])
            self.ui_window.deadline_value.setDate(QtCore.QDate.fromString(task_data['date_deadline'], "dd.MM.yyyy"))
            self.ui_window.description_value.setPlainText(task_data['description'])

    def add_new_task(self):
        date_create = datetime.date.today().strftime("%d.%m.%Y")
        date_deadline = self.ui_window.deadline_value.text()
        status = self.ui_window.status_value.currentText()
        name = self.ui_window.name_value.toPlainText()
        description = self.ui_window.description_value.toPlainText()

        self.conn.add_new_task_query(name, status, date_create, date_deadline, description)
        self.view_data()
        self.new_window.close()

    def edit_task(self):
        index = self.ui.tbl_tasklist.selectedIndexes()[0]
        id = str(self.ui.tbl_tasklist.model().data(index))

        date_create = datetime.date.today().strftime("%d.%m.%Y")
        date_deadline = self.ui_window.deadline_value.text()
        status = self.ui_window.status_value.currentText()
        name = self.ui_window.name_value.toPlainText()
        description = self.ui_window.description_value.toPlainText()

        self.conn.update_task_query(name, status, date_create, date_deadline, description, id)
        self.view_data()
        self.new_window.close()
    
    def delete_task(self):
        indexes = self.ui.tbl_tasklist.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            id = str(self.ui.tbl_tasklist.model().data(index.sibling(row, 0)))

        self.conn.delete_task_query(id)
        self.view_data()

   
    def export_data(self):
        query = self.conn.export_data_to_excel()
        tasks = []
        while query.next():
            task = [
                str(query.value(0)),  # ID
                query.value(1),       # Name
                query.value(2),       # Status
                query.value(3),       # Date Create
                query.value(4),       # Date Deadline
                query.value(5)        # Description
            ]
            tasks.append(task)

        self.export_to_excel(tasks)

    def export_to_excel(self, tasks):
        wb = Workbook()
        ws = wb.active
        headers = ['ID', 'Name', 'Status', 'Date Create', 'Date Deadline', 'Description']
        ws.append(headers)

        for task in tasks:
            ws.append(task)

        wb.save('Tasks ToDoApp.xlsx')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TaskList()
    window.show()
    sys.exit(app.exec())