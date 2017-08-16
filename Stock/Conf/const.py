CONST_DELAY = 30
CONST_CHROME_PATH = "\\Stock\\Resource\\"
CONST_REQUEST_TIMEOUT = 10
CONST_RETRIES_HTTP_REQUEST_TIMES = 3

'''
新浪VIP
'''
CONST_SINA_STOCK_FINANCE_PROFIT_URL = 'http://vip.stock.finance.sina.com.cn/q/go.php/vFinanceAnalyze/kind/profit/index.phtml?\
s_i=&s_a=&s_c=&reportdate=%s&quarter=%s&p=%s'
REPORT_COLS = ['code', 'name', 'eps', 'eps_yoy', 'bvps', 'roe',
               'epcf', 'net_profits', 'profits_yoy']



CONST_SINA_STOCK_FINANCE_SUMMARY_URL = 'http://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/%s/displaytype/4.phtml'

CONST_QQ_STOCK_FINANCE_SUMMARY_URL = 'http://gu.qq.com/%s/gp'