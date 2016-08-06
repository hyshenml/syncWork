__author__ = 'sml'
import os
from config import *
from utils import save_ob
if not os.path.isdir(copy_path):
    os.mkdir(copy_path)
if not os.path.isdir(backup_path):
    os.mkdir(backup_path)

save_ob(0,'last_copy_time')
save_ob(0,'last_return_time')