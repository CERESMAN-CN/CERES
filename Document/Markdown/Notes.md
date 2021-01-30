

# 阶段性目标

项目整体分为三个阶段。每个阶段有相应的设计要求与最佳实践。最终目标为达成方便的进行数据因子构建和实验，快速测试回撤，与自动参数调节。


- [阶段性目标](#阶段性目标)
  - [阶段一](#阶段一)
    - [0，规范](#0规范)
    - [1，数据导入/存储](#1数据导入存储)
    - [2，分析](#2分析)
    - [3，因子构建](#3因子构建)
    - [4，模型训练](#4模型训练)
    - [5，回测](#5回测)
    - [6，评估](#6评估)
    - [7，绘图的整体最简实现](#7绘图的整体最简实现)
  - [阶段二](#阶段二)
    - [实验环境](#实验环境)
    - [后端服务](#后端服务)
    - [前端部分](#前端部分)
  - [阶段三](#阶段三)
- [后端与数据部分相关信息](#后端与数据部分相关信息)
  - [交易接口API](#交易接口api)
  - [数据接口API](#数据接口api)
  - [回测接口API](#回测接口api)
  - [可视化数据接口API](#可视化数据接口api)
  - [因子库接口](#因子库接口)
  - [策略库](#策略库)
- [前端部分相关信息](#前端部分相关信息)
  - [数据可视化](#数据可视化)
  - [可交互](#可交互)
  - [框架](#框架)
- [Reference](#reference)

成熟的量化交易系统包括了以下部分：

## 阶段一

该阶段的主要设计目标是完成：

### 0，规范

- [ ]  代码规范

[PEP 8: The Style Guide for Python Code](https://pep8.org/)

- [ ]  Repo标准

    部署私有Gitlab服务器

[Download and install GitLab](https://about.gitlab.com/install/)

- [ ]  注释与文档系统
    - [ ]  规范函数注释规则

[Projects using Sphinx - Sphinx 4.0.0+ documentation](https://www.sphinx-doc.org/en/master/examples.html)

### 1，数据导入/存储

- [ ]  元数据与类结构设计
- [ ]  账户类设计
- [ ]  python数据接口数据获取
- [ ]  数据库构建
- [ ]  数据组织形式设计
- [ ]  python针对数据库的增删查改接口
- [ ]  数据向通用过渡的pandas格式转换接口

### 2，分析

- [ ]  将pandas dataframe处理为K线数据
- [ ]  编写移动平均等股票数据处理方法
- [ ]  财报数据结构化处理与对应

### 3，因子构建

- [ ]  设计单因子类输入，输出，结构，关联关系等
- [ ]  对因子的属性字段做出梳理，分析，依据来源，种类，相关性等信息作为因子描述字段，同时索引对应的相关关系

### 4，模型训练

- [ ]  基于CPU的XGBoost等模型运作
- [ ]  基于GPU的LSTM基础模型训练

### 5，回测

- [ ]  设计实现回测类，关键操作需要高度包装
    - [ ]  动态时间序列
    - [ ]  关键输入数据
    - [ ]  关键输出数据
    - [ ]  关键字段权限与属性
    - [ ]  完善的兼容和自动分析不同数据类功能
    - [ ]  开放性的字段扩展性
    - [ ]  使用配置文件保存关键操作属性信息
- [ ]  输出的归一化。使各数据项数据范围统一并且保留恢复方法

### 6，评估

- [ ]  针对回测输出的统计，计算，并关联账户类
- [ ]  设计回测数据转换为供绘图的中间数据相关类与方法

### 7，绘图的整体最简实现

- [ ]  针对供绘图的中间数据格式，产出固定类型的数据图表，相应的绘图保有类

---

- 最佳实践：
    - 运行一键数据入库
    - 高级API进行一键出图
        - 个股出图
        - 多股对比出图
    - 策略方法固定输入输出
    - 一键回测

## 阶段二

在阶段1的基础上，实现了基本策略的设计，验证，交易等关键操作。并假设已产生足够的盈利的情况下，整体的诉求将会进一步扩展：

1，需要实现关键部分自研的替代；

2，需要更严格的数据加密手段，例如全局RSA加密传输等等；

3，需要全链路保证数据安全；

4，需要真正的实验环境+前后端+用户界面；

因此第二阶段的任务主要分为以下重要部分：

### 实验环境

- [ ]  线上编辑器
    - [ ]  python作为语法，生成规格化的方法外壳，固定输入输出和执行方式，类似Leetcode；
    - [ ]  支持数据项检索，拖拽，可视化
    - [ ]  支持数据因子库检索，拖拽，可视化
    - [ ]  支持回测，以及对应产生数据的可视化
    - [ ]  自制基础镜像以及衍生的特殊环境镜像用来处理不同类型任务
        - [ ]  DeepLearning（Pytorch）；
        - [ ]  GIS（GDAL）；
        - [ ]  Scipy；Boost；(Scikit-Learn,XGBoost)
        - [ ]  Basic；(Important DockerFile)

### 后端服务

- [ ]  自动交易委托服务
- [ ]  自动盯盘服务
- [ ]  大盘简报服务
- [ ]  企业官网
- [ ]  整体的加密解密方案
- [ ]  隔离环境
- [ ]  微服务化（可长期不做）

### 前端部分

供给后端，数据统计，数据实验，展示，以及企业官网。放弃AdobeFlash支持。只支持Chromium内核浏览器。

- [ ]  利用可交互数据可视化框架在元数据类层级，绘制相关信息
- [ ]  利用Vue3.0完成基础逻辑框架的搭建
    - [ ]  官网主页
    - [ ]  官网设计元素
        - [ ]  动效
        - [ ]  可交互样例
- [ ]  编辑器界面
    - [ ]  支持自定义布局 类似yuque
    - [ ]  支持Python语法
    - [ ]  支持Markdown语法
    - [ ]  支持Latex语法
    - [ ]  工作空间所有组件插件化，自定义化
        - [ ]  交易数据组件
        - [ ]  因子组件
        - [ ]  策略组件
        - [ ]  编辑器组件
        - [ ]  文档组件
        - [ ]  可视化组件
    - [ ]  支持放置视频链接，并解析为播放窗口,可播放。
    - [ ]  支持虚拟环境构建，启动和调度（Docker&NVIDIA Docker）类似colab和 Kaggle
    - [ ]  支持pdf，图片，图表，插入，显示，简单常用计算，可视化。

---

- 最佳实现

## 阶段三

第三阶段，建立在既有的量化系统良好的服务于因子分析和量化流程，则需要探索新的量化形式

- [ ]  数据相关性探索器

    在，数亿条结构化信息和所有的交易信息面前，可能存在着大量的非显性数据相关存在。例如，中国的存款准备金率，可能和德国的制造企业股价存在关联。

    这也就是所谓的蝴蝶效应。而人类对于此类相关性的挖掘，一直处于很低的程度。

    因此，我们需要设计一套能够自主尝试不同数据因子，不同股票组合，不同板块，不同数据因子，去探索其相关性的方法和策略。

    - [ ]  数据因子池
    - [ ]  策略池
    - [ ]  交易数据池
    - [ ]  剪枝策略
    - [ ]  并行化
- [ ]  非结构化数据转换器，语言模型

    Transformer & Bert & GTP3 展示了语言模型的潜力。因此依靠搜索，语言模型，共同作用把非结构化数据转换为结构化数据的尝试，是极其有价值和必要的。

    - [ ]  市场消息爬虫&监控系统
    - [ ]  非结构化数据与结构化数据转换数据集制作
    - [ ]  尝试语言模型与监控系统共同转换
- [ ]  强化学习环境建设

    强化学习在规定环境下，有着相当高的自主学习能力，且没有监督学习产生的边界问题，AlphaZero在依靠大量对局的情况下，轻松击败了蒙特卡洛树为基础的深度学习模型AlphaGo，并远远超过了人类的水平。因此设计一个合理的loss函数使得强化学习训练过程在指定的池内进行自主学习，有着相当巨大的潜力。

    - [ ]  设计对应算法

---

- 最佳实现

借助因子相关星探索器，找到高效因子，从而实现较为强大的因此组合池供交易策略选择。

# 后端与数据部分相关信息

## 交易接口API

- 证券交易

[](https://www.showdoc.com.cn/linkstock?page_id=1298758476954784)

[ztsec/xtp_api_python](https://github.com/ztsec/xtp_api_python)

- 数字货币交易

[ccxt/ccxt](https://github.com/ccxt/ccxt/tree/master/python)

[Coinbase Pro API Reference](https://docs.pro.coinbase.com/#introduction)

- ~~期货交易(暂缓)~~

## 数据接口API

- A股/港股数据接口

[Tushare大数据社区](https://tushare.pro/document/2)

- 美股/欧洲（国际）数据接口

[yahoofinance](https://python-yahoofinance.readthedocs.io/en/latest/api.html)

- 常规统计操作接口

[LastAncientOne/Stock_Analysis_For_Quant](https://github.com/LastAncientOne/Stock_Analysis_For_Quant)

- 入库出库建库（增删查改）接口

    依据数据库方案而定。

## 回测接口API

- 回测计算API

[OOXXXXOO/rqalpha](https://github.com/OOXXXXOO/rqalpha)

- 结果统计与中间结果生成API

    [API Reference - scikit-learn 0.24.1 documentation](https://scikit-learn.org/stable/modules/classes.html)

[pandas documentation - pandas 1.2.1 documentation](https://pandas.pydata.org/docs/)

## 可视化数据接口API

- 中间数据绘制基础接口

[seaborn: statistical data visualization - seaborn 0.11.1 documentation](http://seaborn.pydata.org/)

## 因子库接口

- 文本信息处理框架
    - NLP Module（Paper：）

    [huggingface/transformers](https://github.com/huggingface/transformers)

- 地理信息处理框架
    - GEE

    [Google Earth Engine](https://earthengine.google.com/)

    - 深度学习框架
        - Pytorch

        [PyTorch](https://pytorch.org/)

        - Visualization

        [TensorBoard | TensorFlow](https://www.tensorflow.org/tensorboard/)

    - 因子分析框架

    [quantopian/alphalens](https://github.com/quantopian/alphalens)

    [Stock Analysis Engine - Stock Analysis Engine 1.0.0 documentation](https://stock-analysis-engine.readthedocs.io/en/latest/index.html)

## 策略库

- 策略库样例

[fmzquant/strategies](https://github.com/fmzquant/strategies.git)

# 前端部分相关信息

## 数据可视化

[D3.js - Data-Driven Documents](https://d3js.org/)

[AntV](https://antv.vision/zh)

## 可交互

[Dash Overview](https://plotly.com/dash/)

## 框架

[vuejs/vue](https://github.com/vuejs/vue)

# Reference

1.量化交易接口样例

[IPython 与 RQAlpha - rqalpha 4.2.x 文档](https://rqalpha.readthedocs.io/zh_CN/latest/notebooks/run-rqalpha-in-ipython.html)

2.架构样例

[OOXXXXOO/XCloud](https://github.com/OOXXXXOO/XCloud)

3.量化策略库样例

[je-suis-tm/quant-trading](https://github.com/je-suis-tm/quant-trading)
