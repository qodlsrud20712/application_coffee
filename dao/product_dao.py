# insert

# select

# update

# delete
from mysql.connector import Error

from db_connection.connection_pool import ConnectionPool


class ProductDao():
    def __init__(self):
        pass

    def __do_query(self, query=None, arg=None):
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(query, arg)
            conn.commit()
        except Error as e:
            print(e)
            raise e
        finally:
            cursor.close()
            conn.close()

    def __iter_row(self, cursor, size=5):
        while True:
            rows = cursor.fetchmany(size)
            if not rows:
                break
            for row in rows:
                yield row

    def select(self, code = None):
        sql = 'select * from product'
        sql_where = 'select code, name from product where code like %s'
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            if code is None:
                #print(sql)
                cursor.execute(sql)
            else:
                args = (code,)
                #print(sql_where)
                cursor.execute(sql_where, args)

            data = []
            [data.append(row) for row in self.__iter_row(cursor, 5)]
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
            return data

    def insert_product(self, code, name):
        args = (code, name)
        insert_sql = 'insert into product values(%s, %s)'

        try:
            self.__do_query(query=insert_sql, arg=args)
            return True
        except Error as e:
            return False

    def update_product(self,name, code):
        args = (name, code)
        update_sql = "update product set name = %s where code = %s"

        try:
            self.__do_query(query=update_sql, arg=args)
            return True
        except Error as e:
            return False

    def delete_product(self, code):
        sql = "delete from product where code = %s"
        try:
            conn = ConnectionPool.get_instance().get_connection()
            cursor = conn.cursor()
            cursor.execute(sql, (code,))
            conn.commit()
        except Error as error:
            print(error)
        finally:
            cursor.close()
            conn.close()

