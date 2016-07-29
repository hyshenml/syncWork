#-*- coding:utf-8 -*-
__author__ = 'sml'
import os, time



def today_midnight():
    now = time.time()
    midnight = now - (now % 86400) + time.timezone
    return midnight

import cPickle as pickle
def pickle_save(x):
    with open('./temp.pk1','wb') as f:
        pickle.dump(x,f,True)

def pickle_load():
    with open('./temp.pk1','rb') as f:
        return pickle.load(f)

