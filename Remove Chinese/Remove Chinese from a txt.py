#coding=utf-8

import re
import os

All_list = []

f = open('111.txt' ,'r',encoding = 'utf-8')
for line in f.readlines():
    t = re.sub(r'[^\x00-\x7f]', '', line)
    if len(t)>5:
        All_list.append(t)
f.close()

f = open('222.txt' , 'w')
for i in All_list:
    f.write(i)
f.close()

