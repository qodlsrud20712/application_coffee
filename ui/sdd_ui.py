from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem


class Sale_Detail_form():
    def __init__(self):
        pass

    def create_item_sdd(self, no_sd, salePrice, addTax, supPrice, marPrice):
        item_no_sd = QTableWidgetItem()
        item_no_sd.setTextAlignment(Qt.AlignCenter)
        item_no_sd.setData(Qt.DisplayRole, no_sd)

        item_salePrice = QTableWidgetItem()
        item_salePrice.setTextAlignment(Qt.AlignCenter)
        item_salePrice.setData(Qt.DisplayRole, salePrice)

        item_addTax = QTableWidgetItem()
        item_addTax.setTextAlignment(Qt.AlignCenter)
        item_addTax.setData(Qt.DisplayRole, addTax)

        item_supPrice = QTableWidgetItem()
        item_supPrice.setTextAlignment(Qt.AlignCenter)
        item_supPrice.setData(Qt.DisplayRole, supPrice)

        item_marPrice = QTableWidgetItem()
        item_marPrice.setTextAlignment(Qt.AlignCenter)
        item_marPrice.setData(Qt.DisplayRole, marPrice)
        return item_no_sd, item_salePrice, item_addTax, item_supPrice, item_marPrice