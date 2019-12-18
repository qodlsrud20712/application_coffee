from mysql.connector import Error

from dao.adc_dao import Dao
from db_connection.connection_pool import ConnectionPool

select_sql = "SELECT no, sale_price, addTax, supply_price, marginPrice FROM sale_detail"
select_sql_where = select_sql + "where no =%s"

class Sale_Detail_Dao(Dao):

    def select_item(self, no=None):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(select_sql) if no is None else cursor.execute(select_sql_where, (no,))
            res = []
            [res.append(row) for row in self.__iter_row(cursor, 5)]
            return res

        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    def insert_item(self, **kwargs):
        pass

    def update_item(self, **kwargs):
        pass

    def delete_item(self, **kwargs):
        pass

    def __iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def call_order_price_by_issale(self, query, isSale):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()

            args = [isSale, ]
            cursor.callproc(query, args)
            res = []
            for result in cursor.stored_results():
                rows = result.fetchall()
                for row in rows:
                    res.append(row)
            return res
        except Error as e:
            print(e)

        finally:
            cursor.close()
            conn.close()


