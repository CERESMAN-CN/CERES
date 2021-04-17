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

# ---------------------------- system requirement ---------------------------- #
import os
import time
# ---------------------------------- Tushare --------------------------------- #


from data.loader import load
class stock(load):
    def __init__(self,
        code=None,
        name=None,
        ):
        """[summary]

        Args:
            code ([int], optional): [code of stock]. Defaults to None.
            name ([str], optional): [name of stock]. Defaults to None.
        """
        load.__init__(self,code=code,name=name)
        if not code is None or not name is None:
            print("# ------------- stock class init with ,code :",code," name :",name)
        self.current_time=list(time.localtime(time.time()))[:3]
        self.current_time=[str(0)+str(i) if len(str(i))==1 else str(i) for i in self.current_time]
        self.current_time="".join(self.current_time)
        print("Current Time :",self.current_time)
        if not name is None:
            self.loadByName(name)
        if not code is None:
            self.loadByCode(code)
  

    def find(self,nickname):
        """[summary]

        Args:
            nickname ([str]): [
                nickname of stock ,the function will search stock by nickname like 'APPLE','Google','Tesla'
                # basic idea : transform the name to list & find str in item of list
                ]
        """



    def plot(self):
        pass



    def loadByName(self,name):
        """[summary]

        Args:
            name ([str]): [full name of stock]
        """
        
        self.stock_=self.base_data[self.base_data['name']==name]
        self.loadtradeInfo()
 
      

    
    def loadByCode(self,code):
        """[summary]

        Args:
            code ([code]): [code of stock]
        """
        self.stock_=self.base_data[self.base_data['ts_code']==code]
        self.loadtradeInfo()






def main():
    print("# --------------------------- STOCK CLASS TEST Demo -------------------------- #")
    zhongxinguoji=stock(name="中芯国际")
    # df = pdl.get_data_tiingo('MSFT', api_key=os.getenv('TIINGO_API_KEY'))
    # print(df)

if __name__ == '__main__':
    main()
