# Copyright 2021 Tom Winshare
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tushare as ts
from .config import ts_token,tingo_token
ts_client = ts.pro_api(ts_token)

import pandas_datareader as pdl




import rqdatac

class EXCHANGE():
    XSHG = 'XSHG'
    SSE = 'XSHG'
    SH = 'XSHG'
    XSHE = 'XSHE'
    SZ = 'XSHE'
    SZE = 'XSHE'

def normalize_code(symbol, pre_close=None):
    """
    [exchange the code from stock to qutanum system like code]

    :param symbol: [original style code like 000001]
    :type symbol: [str]
    :param pre_close: [description], defaults to None
    :type pre_close: [str], optional
    :return: [description]
    :rtype: [type]
    """    

    # """
    # 归一化证券代码

    # :param code 如000001
    # :return 证券代码的全称 如000001.XSHE
    # """
    if (not isinstance(symbol, str)):
        return symbol

    if (symbol.startswith('sz') and (len(symbol) == 8)):
        ret_normalize_code = '{}.{}'.format(symbol[2:8], EXCHANGE.SZ)
    elif (symbol.startswith('sh') and (len(symbol) == 8)):
        ret_normalize_code = '{}.{}'.format(symbol[2:8], EXCHANGE.SH)
    elif (symbol.startswith('00') and (len(symbol) == 6)):
        if ((pre_close is not None) and (pre_close > 2000)):
            # 推断是上证指数
            ret_normalize_code = '{}.{}'.format(symbol, EXCHANGE.SH)
        else:
            ret_normalize_code = '{}.{}'.format(symbol, EXCHANGE.SZ)
    elif ((symbol.startswith('399') or symbol.startswith('159') or \
        symbol.startswith('150')) and (len(symbol) == 6)):
        ret_normalize_code = '{}.{}'.format(symbol, EXCHANGE.SH)
    elif ((len(symbol) == 6) and (symbol.startswith('399') or \
        symbol.startswith('159') or symbol.startswith('150') or \
        symbol.startswith('16') or symbol.startswith('184801') or \
        symbol.startswith('201872'))):
        ret_normalize_code = '{}.{}'.format(symbol, EXCHANGE.SZ)
    elif ((len(symbol) == 6) and (symbol.startswith('50') or \
        symbol.startswith('51') or symbol.startswith('60') or \
        symbol.startswith('688') or symbol.startswith('900') or \
        (symbol == '751038'))):
        ret_normalize_code = '{}.{}'.format(symbol, EXCHANGE.SH)
    elif ((len(symbol) == 6) and (symbol[:3] in ['000', '001', '002', 
                                                 '200', '300'])):
        ret_normalize_code = '{}.{}'.format(symbol, EXCHANGE.SZ)
    else:
        print(symbol)
        ret_normalize_code = symbol

    return ret_normalize_code



class load():
    def __init__(self,code=None,name=None,Nickname=None):
        """
        [summary]

        :param code: [stock code like 399001深证综指], defaults to None
        :type code: [str], optional
        :param name: [stock name like GOOG], defaults to None
        :type name: [str], optional
        :param Nickname: [stock nickname or company name like Google], defaults to None
        :type Nickname: [str], optional
        """
        self.client=ts_client
        self.base_data=self.client.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name')
        # super().__init__()
        print(self.base_data)
        self.TSCODE=normalize_code(code)
        print("# -------------------------- The TS Code is {TSCODE} ------------------------- #".format(TSCODE=self.TSCODE))
    
    def loadtradeInfo(self):
        self.daily=self.client.daily(
            ts_code=self.stock_["ts_code"].values[0],
            start_date='19700101', 
            end_date=self.current_time
            )
        self.weekly=self.client.weekly(
            ts_code=self.stock_["ts_code"].values[0],
            start_date='19700101', 
            end_date=self.current_time
        )
        self.monthly=self.client.monthly(
            ts_code=self.stock_["ts_code"].values[0],
            start_date='19700101', 
            end_date=self.current_time
        )

    def info(self):
        print("\n\nDaily:\n\n",self.daily)
        print("\n\nWeekly:\n\n",self.weekly)
        print("\n\nMonthly:\n\n",self.monthly)
