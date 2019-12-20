from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAction, QMessageBox
from dao.product_dao import ProductDao


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

    def set_context_menu(self, tv, func, func2, func3):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        delete_action = QAction('삭제', tv)
        find_action = QAction('검색', tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        tv.addAction(find_action)
        update_action.triggered.connect(func)
        delete_action.triggered.connect(func2)
        find_action.triggered.connect(func3)

    def get_item_form_le_addpdt(self, le_code, le_name):
        pdt = ProductDao()
        code = le_code
        name = le_name
        pdt.insert_product(code, name)
        return self.create_item(code, name)

    def get_item_form_le_updatepdt(self, le_code, le_name):
        pdt = ProductDao()
        code = le_code
        name = le_name
        pdt.update_product(name, code)
        return self.create_item(code, name)
