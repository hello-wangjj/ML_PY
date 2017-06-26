#!python3
# -*- coding: utf-8 -*-
import os
import jieba
import chardet
__author__ = 'wangjj'
__mtime__ = '2017 06 25 14:44'
__doc__ = '''
error.txt里面的文件读取
'''


# 保存至文件
def savefile(savepath, content):
    content = str.encode(content)
    fp = open(savepath, 'wb')
    fp.write(content)
    fp.close()


# 读取文件
def readfile(path):
    readbyte = min(1024, os.path.getsize(path))
    raw = open(path, 'rb').read(readbyte)
    result = chardet.detect(raw)
    encoding = result['encoding']
    fhandle = open(path, 'r', encoding=encoding, errors='ignore')
    content = fhandle.read()
    fhandle.close()
    return content


# 未分词的语料库路径
corpus_path = 'E:/document/GitHub/ML_PY/nlp/train_corpus_small_seg/error.txt'
corpus_list = []
with open(corpus_path, 'rb') as f:
    for line in f.readlines():
        line = line.strip().decode()
        corpus_list.append(line)
for path in corpus_list:
    savepath = '/'.join(path.split('/')[0:5]) + \
        '/train_corpus_small_seg/' + '/'.join(path.split('/')[-2:])
    print(savepath)
    content = readfile(path)
    content = content.strip()
    content = content.replace('\r\n', '').strip()
    content_seg = jieba.cut(content)
    content_seg = ' '.join(content_seg)
    # 将处理后的文件保存到分词后的词料目录
    savefile(savepath, content_seg)
print('中文词料分词结束！！！')
