#-*- coding:utf-8 -*-
__author__ = 'sml'
import os,config,datetime,time
from utils import *
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
        t=time.time()
        save_ob(t,'last_copy_time')

    def return_doc(self):
        backup_path=self._prepare_file()
        if os.path.getmtime(self.copy_path)>os.path.getmtime(self.origin_path):
            open(backup_path['old']+'/'+self.doc_name, "wb").write(open(self.origin_path, "rb").read())
            open(self.origin_path, "wb").write(open(self.copy_path, "rb").read())
            open(backup_path['new']+'/'+self.doc_name, "wb").write(open(self.copy_path, "rb").read())
        t=time.time()
        save_ob(t,'last_return_time')

    def _prepare_file(self):
        today_file=config.backup_path+str(datetime.date.today()).replace('-','')
        self.old_backup=today_file+'/old'
        self.new_backup=today_file+'/new'
        if not os.path.isdir(today_file):
            os.mkdir(today_file)
            os.mkdir(self.old_backup)
            os.mkdir(self.new_backup)
        return {'old':self.old_backup,'new':self.new_backup}


