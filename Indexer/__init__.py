# -*- coding: utf-8 -*-
from IndexerWidget import IndexerWidget
from MA import MA
from MACD import MACD
from RSI import RSI
from ATR import ATR
from HullMacd import HULL_MACD
from EMA import EMA
from HullRsi import HULL_RSI
from KDJ import KDJ
from DMI import DMI

indexer_mapping_dic = {
    'MA': MA,
    'EMA': EMA,
    'MACD': MACD,
    'HULL_MACD': HULL_MACD,
    'RSI': RSI,
    'ATR': ATR,
    'HULL_RSI': HULL_RSI,
    'KDJ': KDJ,
    'DMI': DMI
}

def get_all_indexer_para_name():
    result_dic = {}
    for indexer_name, indexer in indexer_mapping_dic.items():
        result_dic[indexer_name] = indexer.default_para_dic.keys()
    return result_dic

def get_all_indexer_para_dic():
    result_dic = {}
    for indexer_name, indexer in indexer_mapping_dic.items():
        result_dic[indexer_name] = indexer.default_para_dic
    return result_dic