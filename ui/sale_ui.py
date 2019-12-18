from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAction

from dao.sale_dao import SaleDao


class Sale_form():
    def __init__(self):
        pass

    def create_item_sale(self, no, code, price, saleCnt, marginRate):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)
        item_no.setData(Qt.DisplayRole, no)

        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)
        item_code.setData(Qt.DisplayRole, code)

        item_price = QTableWidgetItem()
        item_price.setTextAlignment(Qt.AlignCenter)
        item_price.setData(Qt.DisplayRole, price)

        item_saleCnt = QTableWidgetItem()
        item_saleCnt.setTextAlignment(Qt.AlignCenter)
        item_saleCnt.setData(Qt.DisplayRole, saleCnt)

        item_marginRate = QTableWidgetItem()
        item_marginRate.setTextAlignment(Qt.AlignCenter)
        item_marginRate.setData(Qt.DisplayRole, marginRate)
        return item_no, item_code, item_price, item_saleCnt, item_marginRate

    def set_context_menu_sale(self, tv, func, func2,func3):
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

    def get_item_form_le_addsale(self, list = None):
        sdt = SaleDao()
        item_no = None
        code = list[0]
        price = list[1]
        saleCnt = list[2]
        marginRate = list[3]
        sdt.insert_item(code, price, saleCnt, marginRate)
        return self.create_item_sale(item_no, code, price, saleCnt, marginRate)

    def get_item_form_le_updatesale(self, list =None):
        sdt = SaleDao()
        no = list[0]
        code = list[1]
        price = list[2]
        saleCnt = list[3]
        marginRate = list[4]
        sdt.update_item(code, price, saleCnt, marginRate, no)
        return self.create_item_sale(no, code, price, saleCnt, marginRate)