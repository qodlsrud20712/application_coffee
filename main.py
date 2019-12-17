import sys
from PyQt5 import QtWidgets
from dao.product_dao import ProductDao
from dao.sale_dao import SaleDao
from dao.sale_detail_dao import Sale_Detail_Dao
from db_connection.connection_pool import ConnectionPool
from ui.ui_main import Application_form


if __name__ == '__main__':
    pdt = ProductDao()
    sdt = SaleDao()
    sdd = Sale_Detail_Dao()
    res = pdt.select()
    res2 = sdt.select_item()
    res3 = sdd.select_item()

    #연결
    pool = ConnectionPool.get_instance()
    connection = pool.get_connection()

    #ui연
    app = QtWidgets.QApplication(sys.argv)
    w = Application_form()
    w.load_data(res)
    w.load_data_sale(res2)
    w.load_data_sale_detail(res3)
    sys.exit(app.exec())


