from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QAbstractItemView, QHeaderView, QTableWidgetItem, QMessageBox, QAction
from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao
from dao.sale_detail_dao import Sale_Detail_Dao
from ui.product_ui import Product_form
from ui.sale_ui import Sale_form
from ui.sdd_ui import Sale_Detail_form


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
        pf = Product_form()
        sf = Sale_form()
        self.ui = uic.loadUi("ui/application.ui")
        self.table = create_table(table=self.ui.tableWidget, data=['code', 'name'])
        self.table_sale = create_table(table=self.ui.tableWidget_2,
                                       data=['no', 'code', 'price', 'saleCnt', 'marginRate'])
        self.table_sdd = create_table(table=self.ui.table_sd,
                                      data=['no', 'sale_price', 'addTax', 'supply_price', 'marginPrice'])
        # product 버튼 연결
        self.ui.btn_insert.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_delete.clicked.connect(self.del_item)
        self.ui.btn_init.clicked.connect(self.init_item)
        # sale 버튼 연결
        self.ui.btn_insert_2.clicked.connect(self.add_item_sale)
        self.ui.btn_update_2.clicked.connect(self.update_item_sale)
        self.ui.btn_delete_2.clicked.connect(self.del_item_sale)
        self.ui.btn_init_2.clicked.connect(self.init_item_sale)

        # 마우스 우클릭시 메뉴
        pf.set_context_menu(self.ui.tableWidget, self.__update, self.__delete)
        sf.set_context_menu_sale(self.ui.tableWidget_2, self.__update_sale, self.__delete_sale)
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
            item_list = [item_no, item_code, item_price, item_saleCnt, item_marginRate]
            nextIdx = self.table_sale.rowCount()
            self.table_sale.insertRow(nextIdx)
            [self.table_sale.setItem(nextIdx, i, item_list[i]) for i in range(len(item_list))]

    def load_data_sale_detail(self, data=None):
        sdd = Sale_Detail_form()
        for idx, (no, salePrice, addTax, supPrice, marPrice) in enumerate(data):
            item_no, item_salePrice, item_addTax, item_supPrice, item_marPrice = sdd.create_item_sdd(no, salePrice,
                                                                                                     addTax, supPrice,
                                                                                                     marPrice)
            item_list = [item_no, item_salePrice, item_addTax, item_supPrice, item_marPrice]
            nextIdx = self.ui.table_sd.rowCount()
            self.ui.table_sd.insertRow(nextIdx)
            [self.ui.table_sd.setItem(nextIdx, i, item_list[i]) for i in range(len(item_list))]

    def add_item(self):
        pf = Product_form()
        item_code, item_name = pf.get_item_form_le_addpdt(self.ui.le_code.text(), self.ui.le_name.text())
        currentIdx = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(currentIdx)
        self.ui.tableWidget.setItem(currentIdx, 0, item_code)
        self.ui.tableWidget.setItem(currentIdx, 1, item_name)
        self.init_item()

    def add_item_sale(self):
        sf = Sale_form()
        le_list = [self.ui.le_code_2.text(), self.ui.le_price.text(),self.ui.le_saleCnt.text(),  self.ui.le_marginR.text()]
        item_no, item_code, item_price, item_saleCnt, item_marginRate = sf.get_item_form_le_addsale(le_list)
        item_list = [item_no, item_code, item_price, item_saleCnt, item_marginRate]
        currentIdx = self.ui.tableWidget_2.rowCount()
        self.ui.tableWidget_2.insertRow(currentIdx)
        [self.ui.tableWidget_2.setItem(currentIdx, i, item_list[i]) for i in range(len(item_list))]
        self.init_item_sale()

    def update_item(self):
        pf = Product_form()
        item_code, item_name = pf.get_item_form_le_updatepdt(self.ui.le_code.text(),self.ui.le_name.text())
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        self.ui.tableWidget.setItem(selectionIdxs.row(), 0, item_code)
        self.ui.tableWidget.setItem(selectionIdxs.row(), 1, item_name)
        self.init_item()
        QMessageBox.information(self, 'Update', '확인', QMessageBox.Ok)

    def update_item_sale(self):
        sf = Sale_form()
        le_list = [self.ui.le_no.text(), self.ui.le_code_2.text(), self.ui.le_price.text(), self.ui.le_saleCnt.text(),
                   self.ui.le_marginR.text()]
        item_no, item_code, item_price, item_saleCnt, item_marginRate = sf.get_item_form_le_updatesale(le_list)
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
        self.ui.table_sd.removeRow(selectionIdxs.row())

    def __update(self):
        selectionIdxs = self.ui.tableWidget.selectedIndexes()[0]
        returnIdxs1 = self.ui.tableWidget.item(selectionIdxs.row(), 0).text()
        returnIdxs2 = self.ui.tableWidget.item(selectionIdxs.row(), 1).text()
        self.ui.le_code.setText(returnIdxs1)
        self.ui.le_name.setText(returnIdxs2)

    def __update_sale(self):
        selectionIdxs = self.ui.tableWidget_2.selectedIndexes()[0]
        sr = selectionIdxs.row()
        rtIdxs1, rtIdxs2, rtIdxs3, rtIdxs4, rtIdxs5 = None, None, None, None, None
        Idxs_list = [rtIdxs1, rtIdxs2, rtIdxs3, rtIdxs4, rtIdxs5]
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
        self.ui.table_sd.removeRow(selectionIdxs.row())
        sdt.delete_item(no)
        QMessageBox.information(self, 'Delete', '확인', QMessageBox.Ok)

    def init_item(self):
        pdt = ProductDao()
        res = pdt.select()
        self.ui.le_code.clear()
        self.ui.le_name.clear()
        row_res = self.ui.tableWidget.rowCount()
        [self.ui.tableWidget.removeRow(i) for i in reversed(range(row_res))]
        self.load_data(res)

    def init_item_sale(self):
        sdt = SaleDao()
        sdd = Sale_Detail_Dao()
        res2 = sdt.select_item()
        res3 = sdd.select_item()
        le_list = [self.ui.le_no, self.ui.le_code_2, self.ui.le_price, self.ui.le_saleCnt, self.ui.le_marginR]
        [le_list[i].clear() for i in range(len(le_list))]
        row_res = self.ui.tableWidget_2.rowCount()
        for i in reversed(range(row_res)):
            self.ui.tableWidget_2.removeRow(i)
            self.ui.table_sd.removeRow(i)
        self.load_data_sale(res2)
        self.load_data_sale_detail(res3)
