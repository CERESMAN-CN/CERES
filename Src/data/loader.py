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
