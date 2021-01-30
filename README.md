<!--
 Copyright 2021 winshare
 
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 
     http://www.apache.org/licenses/LICENSE-2.0
 
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
-->

# Ceres

## [Design Requirement](./Ceres/Document/Markdown/Notes.md)
### 初版源代码结构
```

｜---Src                        # Root
    |---account.py              # 账户类设计
    |---backtest.py             # 设计实现回测类，关键操作需要高度包装
    |---stock.py                # 元数据与类结构设计
    |---io\
        |---loader.py           # 数据接口数据获取
        |---saver.py            # 数据组织形式设计
        |---sync.py             # 针对数据库的增删查改接口
    |---format\
        |---formater.py         # 数据向通用过渡的pandas格式转换接口 & 财报数据结构化处理与对应
    |---model\
        |---dl.py               # 基于GPU的LSTM基础模型训练
        |---tree.py             # 基于CPU的XGBoost等模型运作
    |---strategies\
        |---strategy.py         # 单策略类需要继承的类函数需要共有设计的内容以及调用相应的方法
        |---pool.py             # 策略池
    |---trade\
        |---trader.py           # 交易类/回测端的模拟交易/实盘的真实交易 
    |---analysis\               # 分析统计
        |---statistic.py        # 回测输出的统计，计算，并关联账户类
        |---graph.py            #回测数据转换为供绘图的中间数据相关类与方法 & 针对供绘图的中间数据格式，产出固定类型的数据图表，相应的绘图保有类
    |---factor\
        |---factor.py           # 单因子类输入，输出，结构，关联关系等
        |---pool.py             # 因子池

```

第一阶段执行串流：

1，数据获取

2，数据入库

3，从库中获取个股数据

4，从模型库中选择模型

5，从因子库中获取因子组合，并给出因子组合结合在模型上和股价的相关性（选股模型部分）

6，从交易策略库中，得到交易策略，按照在选股上模型上的股价相关性给出买卖策略（交易模型）

7，启动回测对选定的交易模型进行回测

8，将回测结果进行出图分析。

# 参考代码