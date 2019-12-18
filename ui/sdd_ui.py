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

    def create_item_sdd_proc(self, rank, code, name, price, saleCnt, supply_price, addTax, sale_price, marginRate, marginPrice):
        item_rank = QTableWidgetItem()
        item_rank.setTextAlignment(Qt.AlignCenter)
        item_rank.setData(Qt.DisplayRole, rank)

        item_code = QTableWidgetItem()
        item_code.setTextAlignment(Qt.AlignCenter)
        item_code.setData(Qt.DisplayRole, code)

        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)

        item_price = QTableWidgetItem()
        item_price.setTextAlignment(Qt.AlignCenter)
        item_price.setData(Qt.DisplayRole, price)

        item_saleCnt = QTableWidgetItem()
        item_saleCnt.setTextAlignment(Qt.AlignCenter)
        item_saleCnt.setData(Qt.DisplayRole, saleCnt)

        item_supply_price = QTableWidgetItem()
        item_supply_price.setTextAlignment(Qt.AlignCenter)
        item_supply_price.setData(Qt.DisplayRole, supply_price)

        item_addTax = QTableWidgetItem()
        item_addTax.setTextAlignment(Qt.AlignCenter)
        item_addTax.setData(Qt.DisplayRole, addTax)

        item_sale_price = QTableWidgetItem()
        item_sale_price.setTextAlignment(Qt.AlignCenter)
        item_sale_price.setData(Qt.DisplayRole, sale_price)

        item_marginRate = QTableWidgetItem()
        item_marginRate.setTextAlignment(Qt.AlignCenter)
        item_marginRate.setData(Qt.DisplayRole, marginRate)

        item_marginPrice = QTableWidgetItem()
        item_marginPrice.setTextAlignment(Qt.AlignCenter)
        item_marginPrice.setData(Qt.DisplayRole, marginPrice)
        return item_rank, item_code, item_name, item_price, item_saleCnt, item_supply_price,item_addTax,item_sale_price, item_marginRate, item_marginPrice