#!python3
# -*- coding: utf-8 -*-
import sys
import os
import jieba
__author__ = 'wangjj'
__mtime__ = '2017 06 24 23:42'
string = '小明1995年毕业于北京清华大学'
seg_list = jieba.cut(string, cut_all=False)
print('Default Mode:', ' '.join(seg_list))

seg_list = jieba.cut(string)
print(' '.join(seg_list))

seg_list = jieba.cut(string, cut_all=True)
print('Full mode:', '/'.join(seg_list))

seg_list = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print('/'.join(seg_list))
