#-*- coding:utf-8 -*-
__author__ = 'sml'
import os, time



def today_midnight():
    now = time.time()
    midnight = now - (now % 86400) + time.timezone
    return midnight

import cPickle as pickle
def save_ob(x,type):
    with open('./'+type+'.pk1','wb') as f:
        pickle.dump(x,f,True)

def load_ob(type):
    with open('./'+type+'.pk1','rb') as f:
        return pickle.load(f)

