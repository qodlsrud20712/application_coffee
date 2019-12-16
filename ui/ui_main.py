from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox, QAction
from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao
from ui.product_ui import Product_form
from ui.sale_ui import Sale_form


def create_table(table=None, data=None):
    table.setHorizontalHeaderLabels(data)
    # row단위선택
    table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # 수정불가
    table.setEditTriggers(QAbstractItemView.NoEditTriggers)
    # 균일 간격 재배치
    table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    return table


class Application_form(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("ui/application.ui")
        self.table = create_table(table=self.ui.tableWidget, data=['code', 'name'])
        self.table_sale = create_table(table = self.ui.tableWidget_2, data = ['no', 'code','price', 'saleCnt', 'marginRate'])
        #product 버튼 연결
        self.ui.btn_insert.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_delete.clicked.connect(self.del_item)
        self.ui.btn_init.clicked.connect(self.init_item)
        #sale 버튼 연결
        self.ui.btn_insert_2.clicked.connect(self.add_item_sale)
        self.ui.btn_update_2.clicked.connect(self.update_item_sale)
        self.ui.btn_delete_2.clicked.connect(self.del_item_sale)
        self.ui.btn_init_2.clicked.connect(self.init_item_sale)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.ui.tableWidget)
        self.set_context_menu_sale(self.ui.tableWidget_2)

        self.ui.show()

    def load_data(self, data=[]):
        pf = Product_form()
        for idx, (code, name) in enumerate(data):
            item_code, item_name = pf.create_item(code, name)
            nextIdx = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(nextIdx)
            self.ui.tableWidget.setItem(nextIdx, 0, item_code)
            self.ui.tableWidget.setItem(nextIdx, 1, item_name)

    def load_data_sale(self, data=None):
        sf = Sale_form()
        for idx, (no, code, price, saleCnt, marginRate) in enumerate(data):
            item_no, item_code, item_price, item_saleCnt, item_marginRate = sf.create_item_sale(no, code, price,
                                                                                                  saleCnt, marginRate)
            item_list = [item_no, item_code, item_price, item_saleCnt,item_marginRate]
            nextIdx = self.table_sale.rowCount()
            self.table_sale.insertRow(nextIdx)
            [self.table_sale.setItem(nextIdx, i, item_list[i]) for i in range(len(item_list))]

    def add_item(self):
        item_code, item_name = self.get_item_form_le_addpdt()
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)
        self.ui.tableWidget.setItem(currentIdx, 0, item_code)
        self.ui.tableWidget.setItem(currentIdx, 1, item_name)
        self.init_item()

    def add_item_sale(self):
        item_no, item_code, item_price, item_saleCnt, item_marginRate = self.get_item_form_le_addsale()
        item_list = [item_no, item_code, item_price, item_saleCnt, item_marginRate]
        currentIdx = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(currentIdx)
        [self.ui.tableWidget_2.setItem(currentIdx, i , item_list[i]) for i in range(len(item_list))]
        self.init_item_sale()

    def update_item(self):
        item_code, item_name = self.get_item_form_le_updatepdt()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_code)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_name)
        self.init_item()
        QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def update_item_sale(self):
        item_no, item_code, item_price, item_saleCnt, item_marginRate = self.get_item_form_le_updatesale()
        item_list = [item_no, item_code, item_price, item_saleCnt, item_marginRate]
        selectionIdxs = self.ui.tableWidget_2.selectedIndexes()[0]
        [self.ui.tableWidget_2.setItem(selectionIdxs.row(), i, item_list[i]) for i in range(len(item_list))]
        self.init_item_sale()
        QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def del_item(self):
        pdt = ProductDao()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        code = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        pdt.delete_product(code)
        self.ui.tableWidget.removeRow(selectionIdxs.row())

    def del_item_sale(self):
        sdt = SaleDao()
        selectionIdxs = self.table_sale.selectedIndexes()[0]
        no = self.table_sale.item(selectionIdxs.row(), 0).text()
        sdt.delete_item(no)
        self.table_sale.removeRow(selectionIdxs.row())

    def get_item_form_le_addpdt(self):
        pdt = ProductDao()
        pf = Product_form()
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt.insert_product(code, name)
        return pf.create_item(code, name)

    def get_item_form_le_updatepdt(self):
        pdt = ProductDao()
        pf = Product_form()
        code = self.ui.le_code.text()
        name = self.ui.le_name.text()
        pdt.update_product(name, code)
        return pf.create_item(code, name)

    def get_item_form_le_addsale(self):
        sdt = SaleDao()
        sf = Sale_form()
        currentIdx = self.ui.tableWidget_2.rowCount()
        if currentIdx > 0:
            item_no = self.ui.tableWidget_2.item(currentIdx - 1, 0).text()
            item_no = int(item_no) + 1
            item_no = str(item_no)
        else:
            item_no = '0'
        code = self.ui.le_code_2.text()
        price = self.ui.le_price.text()
        saleCnt = self.ui.le_saleCnt.text()
        marginRate = self.ui.le_marginR.text()
        sdt.insert_item(code, price, saleCnt, marginRate)
        return sf.create_item_sale(item_no, code, price, saleCnt, marginRate)

    def get_item_form_le_updatesale(self):
        sdt = SaleDao()
        sf = Sale_form()
        no = self.ui.le_no.text()
        code = self.ui.le_code_2.text()
        price = self.ui.le_price.text()
        saleCnt = self.ui.le_saleCnt.text()
        marginRate = self.ui.le_marginR.text()
        sdt.update_item(code, price, saleCnt, marginRate, no)
        return sf.create_item_sale(no, code, price, saleCnt, marginRate)

    def __update(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        returnIdxs1 = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        returnIdxs2 = self.ui.tableWidget.item(selectionIdxs.row(), 1).text()
        self.ui.le_code.setText(returnIdxs1)
        self.ui.le_name.setText(returnIdxs2)

    def __update_sale(self):
        selectionIdxs = self.ui.tableWidget_2.selectedIndexes()[0]
        sr = selectionIdxs.row()
        rtIdxs1, rtIdxs2,rtIdxs3,rtIdxs4,rtIdxs5 = None, None, None, None, None
        Idxs_list = [rtIdxs1,rtIdxs2,rtIdxs3,rtIdxs4,rtIdxs5]
        for i in range(len(Idxs_list)):
            Idxs_list[i] = self.ui.tableWidget_2.item(sr, i).text()
        le_list = [self.ui.le_no, self.ui.le_code_2, self.ui.le_price, self.ui.le_saleCnt, self.ui.le_marginR]
        [le_list[i].setText(Idxs_list[i]) for i in range(len(Idxs_list))]

    def __delete(self):
        pdt = ProductDao()
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        code = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        self.ui.tableWidget.removeRow(selectionIdxs.row())
        pdt.delete_product(code)
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def __delete_sale(self):
        sdt = SaleDao()
        selectionIdxs = self.ui.tableWidget_2.selectedIndexes()[0]
        no = self.ui.tableWidget_2.item(selectionIdxs.row(), 0).text()
        self.ui.tableWidget_2.removeRow(selectionIdxs.row())
        sdt.delete_item(no)
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        delete_action = QAction('삭제', tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def set_context_menu_sale(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction('수정', tv)
        delete_action = QAction('삭제', tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update_sale)
        delete_action.triggered.connect(self.__delete_sale)

    def init_item(self):
        self.ui.le_code.clear()
        self.ui.le_name.clear()

    def init_item_sale(self):
        self.ui.le_no.clear()
        self.ui.le_code_2.clear()
        self.ui.le_price.clear()
        self.ui.le_saleCnt.clear()
        self.ui.le_marginR.clear()


