# -*- coding: utf-8 -*-
from IndexerWidget import IndexerWidget
from MA import MA
from MACD import MACD
indexer_mapping_dic = {
    'MA': MA,
    'MACD': MACD
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