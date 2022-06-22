import requests
from pprint import pprint
import time
from decorators import log_decorator, log_param_decorator

@log_decorator
def get_request_1(tag):
    todate = int(time.time())
    fromdate = todate - 172800
    url = f"https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow"
    resp = requests.get(url)
    return resp.json()


@log_param_decorator('function_log.log')
def get_request_2(tag):
    todate = int(time.time())
    fromdate = todate - 172800
    url = f"https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow"
    resp = requests.get(url)
    return resp.json()


if __name__ == '__main__':
    pprint(get_request_1('web'))
    pprint(get_request_2('python'))
