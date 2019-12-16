import inspect
from abc import ABCMeta, abstractmethod

from mysql.connector import Error

from db_connection.connection_pool import ConnectionPool


class Dao(metaclass=ABCMeta):
    def __init__(self):
        self.connection_pool = ConnectionPool.get_instance()

    @abstractmethod
    def insert_item(self, **kwargs):
        raise NotImplementedError('Subclass must implement abstract method')

    @abstractmethod
    def update_item(self, **kwargs):
        raise NotImplementedError('Subclass must implement abstract method')

    @abstractmethod
    def delete_item(self, **kwargs):
        raise NotImplementedError('Subclass must implement abstract method')

    @abstractmethod
    def select_item(self, **kwargs):
        raise NotImplementedError('Subclass must implement abstract method')

    def do_query(self, **kwargs):
        try:
            conn = self.connection_pool.get_connection()
            cursor = conn.cursor()
            if kwargs is not None:
                cursor.execute(kwargs['query'], kwargs['kargs'])
                conn.commit()

            else:
                cursor.execute(kwargs['query'])
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