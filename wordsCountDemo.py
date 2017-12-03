#coding:utf-8
import re
from collections import Counter
FILESOURCE = './letter.txt'

def getMostCommonWord(aticlefilesource):
    '''输入一个英文的纯文本文件，统计其中的单词出现的个数'''
    pattern = r'''[A-Za-z]+|\$?\d+%?$'''
    with open(aticlefilesource) as f:
        r = re.findall(pattern,f.read())
        print r
        print "*"*20
        return Counter(r).most_common()

if __name__ == "__main__":
    print getMostCommonWord(FILESOURCE)