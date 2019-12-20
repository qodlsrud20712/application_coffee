import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget

from db_connection.connection_pool import ConnectionPool
from ui.ui_main import Application_form


if __name__ == '__main__':
    #ui연결
    app = QtWidgets.QApplication(sys.argv)
    w = Application_form()
    sys.exit(app.exec())


