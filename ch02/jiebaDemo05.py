#!python3
# -*- coding: utf-8 -*-
import os
from sklearn.datasets.base import Bunch
import chardet
import pickle
__author__ = 'wangjj'
__mtime__ = '2017 06 26 0:21'

# 读取文件


def readfile(path):
    readbyte = min(1024, os.path.getsize(path))
    raw = open(path, 'rb').read(readbyte)
    result = chardet.detect(raw)
    encoding = result['encoding']
    fp = open(path, 'r', encoding=encoding, errors='ignore')
    content = fp.read()
    fp.close()
    return content

# Bunch类提供一种key value的对象形式
# target_name 所有分类集名称列表
# label每个文件的分类标签列表
# filenames 文件路径
# contents分词后的文件词向量形式
bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])

# 分词后的分类语料库路径
seg_path = '../nlp/train_corpus_small_seg/'
# 分词语料库Bunch对象持久化文件路径
wordbag_path = '../nlp/train_word_bag/train_set.dat'

catelist = os.listdir(seg_path)
bunch.target_name.extend(catelist)
for mydir in catelist:
    class_path = seg_path + mydir + '/'
    file_list = os.listdir(class_path)
    for file_path in file_list:
        fullname = class_path + file_path
        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname).strip())
# Bunch对象持久化
file_obj = open(wordbag_path, 'wb')
pickle.dump(bunch, file_obj)
file_obj.close()

print('构建文本对象结束')
