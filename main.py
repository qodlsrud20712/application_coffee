import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction

from db_connection.connection_pool import ConnectionPool
from ui.ui_main import Application_form


if __name__ == '__main__':
    #연결
    pool = ConnectionPool.get_instance()
    connection = pool.get_connection()

    #ui연결
    app = QtWidgets.QApplication(sys.argv)
    w = Application_form()
    sys.exit(app.exec())


