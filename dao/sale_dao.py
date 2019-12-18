import inspect
from mysql.connector import Error
from dao.adc_dao import Dao
from db_connection.connection_pool import ConnectionPool

insert_sql = "insert into sale values(null, %s, %s, %s, %s)"
update_sql = "UPDATE sale SET code = %s, price=%s, saleCnt=%s, marginRate=%s WHERE no=%s"
delete_sql = "DELETE FROM sale WHERE no =%s"
select_sql = "SELECT no, code, price, saleCnt, marginRate FROM sale"
select_sql_where = select_sql + "where no =%s"

class SaleDao(Dao):
    def select_item(self, no = None):
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

    def find_item(self, code = None):
        sql_where = "SELECT no, code, price, saleCnt, marginRate FROM sale where code like %s"
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            args = (code,)
            cursor.execute(sql_where, args)

            data = []
            [data.append(row) for row in self.__iter_row(cursor, 5)]
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            return data

    def insert_item(self, code = None, price=None, saleCnt =None, marginRate= None):
        args = (code, price, saleCnt, marginRate)
        try:
            super().do_query(query=insert_sql, kargs=args)
            return True
        except Error:
            return False

    def update_item(self, code = None, price = None, saleCnt = None, marginRate = None, no = None):
        args = (code, price, saleCnt, marginRate, no)
        try:
            super().do_query(query = update_sql, kargs = args)
        except Error:
            return False

    def delete_item(self, no = None):
        args =(no,)
        try:
            super().do_query(query=delete_sql, kargs = args)
        except Error:
            return False

    def __iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row