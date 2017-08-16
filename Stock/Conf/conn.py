from sqlalchemy import create_engine


class Connection:

    @classmethod
    def conn_mysql(cls):
        conn = create_engine('mysql://root:zzzzzz@127.0.0.1/mystock?charset=utf8')
        return conn
