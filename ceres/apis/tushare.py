# coding: utf-8

from typing import Optional

import tushare
from bidict import frozenbidict
from pandas import DataFrame

from ceres.models import ListStatus

token = '5d198053f8882784d333645e1279bc0228a05bb8427dd1cc1f1a0b8b'
ts_client = tushare.pro_api(token)

list_status_converter: frozenbidict[ListStatus, str] = frozenbidict({
    ListStatus.Delist: 'D',
    ListStatus.Listing: 'L',
    ListStatus.Pause: 'P',
})

_stock_fields = ','.join([
    'ts_code', 'symbol', 'name', 'area', 'industry', 'fullname', 'enname', 'market', 'exchange',
    'curr_type', 'list_status', 'list_date', 'delist_date', 'is_hs',
])
_stock_dataframe_column_mapper = {
    'enname': 'english_name',
    'curr_type': 'currency_type',
}


def get_stock_dataframe(list_status: ListStatus = ListStatus.Listing) -> DataFrame:
    result = ts_client.query(
        'stock_basic',
        fields=_stock_fields,
        list_status=list_status_converter.get(list_status, ''),
    )
    result.rename(columns=_stock_dataframe_column_mapper, copy=False, inplace=True)
    return result
