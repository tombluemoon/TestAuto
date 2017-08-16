import urllib3
from Stock.Conf import const


def request_by_url(url):
    http = __create_http_manager()
    text = http.request("GET", url, timeout=const.CONST_REQUEST_TIMEOUT)
    http.clear()
    return text


def __create_http_manager():
    http = urllib3.PoolManager(retries=const.CONST_RETRIES_HTTP_REQUEST_TIMES)
    return http
