__author__ = 'sml'
import config,os,time
from utils import today_midnight,save_ob,load_ob
from doc import Doc

#search the documents need to copy home or copy back.
class Searcher():
    def __init__(self):
        self.file_path=config.file_path
        self.time_range=config.time_range
        self.modi_docs=[]
        self.copy_path=config.copy_path

#find the doc have modified
    def find_modified(self,d=0):
        self.modi_docs=self._find_modified(self.file_path,d)

    def _find_modified(self,path,d):
        file_names=os.listdir(path)
        modi_docs=[]
        last_return_time=load_ob('last_return_time')

        for f in file_names:
            sub_file=path+'/'+f
            print 'sub_file',sub_file
            print 'filetime',os.path.getmtime(sub_file)
            print 'midnight',today_midnight()-86400*d
            if os.path.isdir(sub_file):
                modi_docs=modi_docs+self._find_modified(sub_file,d)
            elif os.path.getmtime(sub_file)>today_midnight()-86400*d and os.path.getmtime(sub_file)>last_return_time+1:
                print self,sub_file
                modi_docs=modi_docs+[Doc(sub_file)]
        return modi_docs

#save the infomation of new copied docs
    def save_docs_info(self):
        doc_info={}
        for doc in self.modi_docs:
            doc_info[doc.doc_name]=doc
        save_ob(doc_info,'docs')


    def find_new_version(self):
        self._load_docs_info()
        last_copy_time=load_ob('last_copy_time')
        file_names=os.listdir(self.copy_path)
        for name in file_names:
            if self.modi_docs.has_key(name) and os.path.getmtime(self.copy_path+name)>last_copy_time+1:
                yield self.modi_docs[name]


    def _load_docs_info(self):
        self.modi_docs=load_ob('docs')

