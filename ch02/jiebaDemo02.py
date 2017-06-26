#!python3
# -*- coding: utf-8 -*-
import sys
import os
import jieba
import chardet

__author__ = 'wangjj'
__mtime__ = '2017 06 24 23:50'


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
    try:
        fp = open(path, 'r', encoding=encoding)
        content = fp.read()
    except UnicodeDecodeError:
        print(path, UnicodeDecodeError)
        fhandle = open(
            'E:/document/GitHub/ML_PY/nlp/train_corpus_small_seg/error.txt',
            'a+', encoding='utf-8')
        fhandle.write(path+'\n')
        fhandle.close()
        return 'file error'
    fp.close()
    return content
# 未分词的语料库路径
corpus_path = 'E:/document/GitHub/ML_PY/nlp/train_corpus_small/'
# 分词后的语料库路径
seg_path = 'E:/document/GitHub/ML_PY/nlp/train_corpus_small_seg/'
# 获取corpus_path下的所有子目录
catelist = os.listdir(corpus_path)
# 获取每个目录下的所有文件
for mydir in catelist:
    class_path = corpus_path + mydir + '/'
    seg_dir = seg_path + mydir + '/'
    if not os.path.exists(seg_dir):
        os.makedirs(seg_dir)
    # 获取目录下所有文件
    file_list = os.listdir(class_path)
    for file_path in file_list:
        # 拼全文件路径
        fullname = class_path + file_path
        content = readfile(fullname)
        if content == 'file error':
            continue
        content = content.strip()
        content = content.replace('\r\n', '').strip()
        content_seg = jieba.cut(content)
        content_seg = ' '.join(content_seg)
        # 将处理后的文件保存到分词后的词料目录
        savefile(seg_dir + file_path, content_seg)
print('中文词料分词结束！！！')
