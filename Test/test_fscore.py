import unittest

import re
from lxml import etree
import pandas as pd
import lxml.html as html
from Stock.Conf.conn import Connection
import Utils.http_request as rq
import Stock.Conf.const as const
from pandas.compat import StringIO


class TestFscore(unittest.TestCase):
    def setUp(self):
        print("test")

    def tearDown(self):
        pass

    def test_case1(self):
        print("test1")

    def test_process(self):
        # num_top_company = 10
        self.__get_fscore_from_internet()
        # self.__analysis_fscore_now()
        # self.__list_top_stock(num_top_company)

    @staticmethod
    def __get_fscore_from_internet():
        arr_year = [1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004,
                    2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]
        arr_quarter = [1, 2, 3, 4]
        data_arr = pd.DataFrame()
        for _year in arr_year:
            for _quarter in arr_quarter:
                page_num = 1
                while int(page_num) > 0:
                    response = rq.request_by_url(
                        const.CONST_SINA_STOCK_FINANCE_PROFIT_URL % (_year, _quarter, page_num))

                    html_str = response.data.decode("GBK")

                    print(str(_year)+":"+str(_quarter)+":"+str(page_num))

                    df = pd.read_html(html_str, attrs={'id': 'dataTable'})[0]
                    if len(df.index) <= 1:
                        break
                    df.columns = const.REPORT_COLS
                    data_arr = data_arr.append(df, ignore_index=True)

                    data_arr['code'] = data_arr['code'].map(lambda x: str(x).zfill(6))
                    data_arr.insert(1, 'date', str(_year) + ":" + str(_quarter * 3) + ":" + str(page_num))
                    _html = html.parse(StringIO(html_str))
                    next_page = _html.xpath('//div[@class=\"pages\"]/a[last()]/@onclick')

                    conn = Connection.conn_mysql()
                    data_arr.to_sql(con=conn, name='table_name_test', if_exists='append')
                    data_arr = pd.DataFrame()

                    if len(next_page) > 0:
                        page_num = re.findall(r'\d+', next_page[0])[0]
                    else:
                        break

    def __analysis_fscore_now(self):
        pass

    def __list_top_stock(self, num_top_company):
        pass

if __name__ == '__main__':
        unittest.main()
