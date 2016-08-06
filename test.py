__author__ = 'sml'
from utils import *
import time
print time.ctime()
print 'last_copy_time',time.localtime(load_ob('last_copy_time'))
print 'last_return_time',time.localtime(load_ob('last_return_time'))
print 'doc',load_ob('docs')
