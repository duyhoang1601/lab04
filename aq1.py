#lab4a Q1
# create a empty text file
fp = open('sales.txt', 'x')
fp.close()
fp = open('sales_2.txt', 'w')
fp.write('first line')
fp.close()

#create file with date time
from datetime import datetime

x = datetime.now()

file_name = x.strftime('%d-%m-%Y.txt')
with open(file_name, 'w') as fp:
    print('created', file_name)

file_name_2 = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_2, 'w') as fp:
    print('created', file_name_2)

file_name_3 = r"E:\demos\files_demos\account\\" + x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name_3, 'w') as fp:
    print('created', file_name_3)

#create file with permission
import os

file_path = r'E:\pynative\account\sample.txt'
# The default umask is 0o22 which turns off write permission of group and others
os.umask(0)
with open(os.open(file_path, os.O_CREAT | os.O_WRONLY, 0o777), 'w') as fh:
    fh.write('content')
