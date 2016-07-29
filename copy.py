#-*- coding:utf-8 -*-
__author__ = 'sml'
from doc import Doc,Searcher
import config,os
if not os.path.isdir(config.copy_path):
    os.mkdir(config.copy_path)
s=Searcher()
s.find_modified()
for doc in s.modi_docs:
    doc.copy()
s.save_docs_info()
