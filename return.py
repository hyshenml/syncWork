#-*- coding:utf-8 -*-
__author__ = 'sml'
from searcher import Searcher
s=Searcher()
for doc in s.find_new_version():
    print doc.doc_name
    doc.return_doc()