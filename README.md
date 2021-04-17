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

### [Design Requirement](Document/Markdown/Notes.md)
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