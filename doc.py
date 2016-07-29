#-*- coding:utf-8 -*-
__author__ = 'sml'
import os,time,config,datetime
from utils import today_midnight,pickle_save,pickle_load
class Doc():
    def __init__(self,path):
        self.origin_path=path
        self.doc_name=path.rsplit('/',1)[1]
        self.copy_path=config.copy_path+self.doc_name
        self.modi_time=self._get_modi_time()

    def _get_modi_time(self):
        return os.path.getmtime(self.origin_path)

    def copy(self):
        open(self.copy_path, "wb").write(open(self.origin_path, "rb").read())

    def return_doc(self):
        backup_path=self._prepare_file()
        if os.path.getmtime(self.copy_path)>os.path.getmtime(self.origin_path):
            open(backup_path['old']+'/'+self.doc_name, "wb").write(open(self.origin_path, "rb").read())
            open(self.origin_path, "wb").write(open(self.copy_path, "rb").read())
            open(backup_path['new']+'/'+self.doc_name, "wb").write(open(self.copy_path, "rb").read())

    def _prepare_file(self):
        today_file=config.backup_path+str(datetime.date.today()).replace('-','')
        self.old_backup=today_file+'/old'
        self.new_backup=today_file+'/new'
        if not os.path.isdir(today_file):
            os.mkdir(today_file)
            os.mkdir(self.old_backup)
            os.mkdir(self.new_backup)
        return {'old':self.old_backup,'new':self.new_backup}

class Searcher():
    def __init__(self):
        self.file_path=config.file_path
        self.time_range=config.time_range
        self.modi_docs=[]
        self.copy_path=config.copy_path

    def find_modified(self):
        self.modi_docs=self._find_modified(self.file_path)

    def _find_modified(self,path):
        file_names=os.listdir(path)
        modi_docs=[]
        for f in file_names:
            sub_file=path+'/'+f
            if os.path.isdir(sub_file):
                modi_docs=modi_docs+self._find_modified(sub_file)
            elif os.path.getmtime(sub_file)>today_midnight():
                modi_docs=modi_docs+[Doc(sub_file)]
        return modi_docs

    def save_docs_info(self):
        doc_info={}
        for doc in self.modi_docs:
            doc_info[doc.doc_name]=doc
        pickle_save(doc_info)

    def find_new_version(self):
        self._load_docs_info()
        file_names=os.listdir(self.copy_path)
        for name in file_names:
            if self.modi_docs.has_key(name):
                yield self.modi_docs[name]


    def _load_docs_info(self):
        self.modi_docs=pickle_load()

