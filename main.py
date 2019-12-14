import sys
from PyQt5 import QtWidgets
from dao.product_dao import ProductDao
from db_connection.connection_pool import ConnectionPool
from ui.product_main import Product_form


if __name__ == '__main__':
    pdt = ProductDao()
    res = pdt.select()

    #연결
    pool = ConnectionPool.get_instance()
    connection = pool.get_connection()

    #ui연
    app = QtWidgets.QApplication(sys.argv)
    w = Product_form()
    w.load_data(res)
    sys.exit(app.exec())


