from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAction




class Product_form():
    def __init__(self):
        pass

    def create_item(self, code, name):
        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)
        item_code.setData(Qt.DisplayRole, code)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        return item_code, item_name


