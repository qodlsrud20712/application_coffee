from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox, QAction
from dao.product_dao import ProductDao


def create_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # row단위선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 수정불가
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일 간격 재배치
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    return table


class Product_form(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/product.ui")
        self.table = create_table(table=self.ui.tableWidget, data=['code', 'name'])
        self.load_data()
        self.ui.btn_insert.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_delete.clicked.connect(self.del_item)
        self.ui.btn_init.clicked.connect(self.init_item)
        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.tableWidget)
        self.ui.show()

    def load_data(self, data=[]):
        for idx, (code, name) in enumerate(data):
            item_code, item_name = self.create_item(code, name)
            nextIdx = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(nextIdx)
            self.ui.tableWidget.setItem(nextIdx, 0, item_code)
            self.ui.tableWidget.setItem(nextIdx, 1, item_name)

    def create_item(self, code, name):
        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)
        item_code.setData(Qt.DisplayRole, code)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        return item_code, item_name

    def add_item(self):
        item_code, item_name = self.get_item_form_le()
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)
        self.ui.tableWidget.setItem(currentIdx, 0, item_code)
        self.ui.tableWidget.setItem(currentIdx, 1, item_name)
        self.init_item()

    def update_item(self):
        item_code, item_name = self.get_item_form_le2()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_code)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_name)
        self.init_item()
        QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def del_item(self):
        pdt = ProductDao()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        code = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        pdt.delete_product(code)
        self.ui.tableWidget.removeRow(selectionIdxs.row())

    def get_item_form_le(self):
        pdt = ProductDao()
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt.insert_product(code, name)
        return self.create_item(code, name)

    def get_item_form_le2(self):
        pdt = ProductDao()
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt.update_product(name, code)
        return self.create_item(code, name)

    def __update(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        returnIdxs1 = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        returnIdxs2 = self.ui.tableWidget.item(selectionIdxs.row(), 1).text()
        self.ui.le_code.setText(returnIdxs1)
        self.ui.le_name.setText(returnIdxs2)

    def __delete(self):
        pdt = ProductDao()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        code = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        self.ui.tableWidget.removeRow(selectionIdxs.row())
        pdt.delete_product(code)
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        delete_action = QAction('삭제', tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def init_item(self):
        self.ui.le_code.clear()
        self.ui.le_name.clear()
