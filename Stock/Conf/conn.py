from sqlalchemy import create_engine


class Connection:

    @classmethod
    def conn_mysql(cls):
        conn = create_engine('mysql://root:111111@127.0.0.1/mystock?charset=utf8')
        return conn
