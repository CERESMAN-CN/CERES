# coding: utf-8

import enum
from dataclasses import dataclass
from typing import Optional


@enum.unique
class ListStatus(enum.IntEnum):
    Delist = 0  # 退市
    Listing = 1  # 上市
    Pause = 2  # 暂停上市


@dataclass
class Stock(object):
    ts_code: str  # TS 代码
    symbol: str  # 股票代码
    name: str  # 股票名称
    area: str  # 所在地域
    industry: str  # 所属行业
    fullname: str  # 股票全称
    english_name: str  # 英文全称
    market: str  # 市场类型 （主板 / 中小板 / 创业板 / 科创板 / CDR）
    exchange: str  # 交易所代码
    currency_type: str  # 交易货币
    list_status: ListStatus  # 上市状态： L上市 D退市 P暂停上市
    list_date: str  # 上市日期
    delist_date: Optional[str]  # 退市日期
    is_hs: str  # 是否沪深港通标的，N否 H沪股通 S深股通
