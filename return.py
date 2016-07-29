#-*- coding:utf-8 -*-
from doc import Doc,Searcher
import config,os
if not os.path.isdir(config.backup_path):
    os.mkdir(config.backup_path)
s=Searcher()
for doc in s.find_new_version():
    print doc.doc_name,doc.origin_path
    doc.return_doc()

