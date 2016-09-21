#-*- coding:utf-8 -*-
__author__ = 'sml'
from searcher import Searcher
import config,os
import sys
try:
    backdays=int(raw_input('input back days:'))
except ValueError,e:
    backdays=0
except IndexError,e:
    backdays=0
if not os.path.isdir(config.copy_path):
    os.mkdir(config.copy_path)
s=Searcher()
s.find_modified(backdays)
for doc in s.modi_docs:
    doc.copy()
if len(s.modi_docs)>0:
    s.save_docs_info()
