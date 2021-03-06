# -*- coding: utf-8 -*-
"""
    @ description：
        修改文件以及文件夹时间戳...win32file等win32相关库使用以下命令进行安装：
            pip install pywin32 (-i https://pypi.tuna.tsinghua.edu.cn/simple)
        
        利用7zip对文件进行解压缩
    @ date:  2020年5月20日13:41:58
    @ author: achange
"""

import os
import time

from pywintypes import Time

import win32timezone
import win32file
from win32file import CreateFile, SetFileTime, GetFileTime, CloseHandle
from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS, CREATE_NEW


def str2time(string):
    """
    将字符串转换为python时间格式
    :param string:
    :return:
    """
    if string == '':
        return False
    else:
        string = string.strip()
        string = string.replace('-', '/')
        if len(string) > 10:
            return time.mktime(time.strptime(string, '%Y/%m/%d %H:%M:%S'))
        else:
            return time.mktime(time.strptime(string, '%Y/%m/%d'))



def change_f_time(f, f_create_time, f_access_time, f_modify_time):
    """
        修改文件或文件夹的时间
        f: 文件/文件夹的路径
        f_create_time, f_access_time, f_modify_time:  文件/文件夹的创建时间、访问时间、修改时间                 
    """
    f_type = 0 if os.path.isfile(f) else FILE_FLAG_BACKUP_SEMANTICS
    file_handle = CreateFile(f, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, f_type, 0)
    # todo: f_type=0表示创建文件，=FILE_FLAG_BACKUP_SEMANTICS 表示创建文件夹！
    f_create_time = Time(f_create_time)
    f_access_time = f_create_time
    f_modify_time = Time(f_modify_time)
    SetFileTime(file_handle, f_create_time, f_access_time, f_modify_time)    # createTimes, accessTimes, modifyTimes
    CloseHandle(file_handle)

    
    
 
# #############   7zip解压缩, 自行百度："最常用的7-zip命令及使用方法"    #######################   
# for example :http://www.pc6.com/edu/53526_all.html
    

def unzip(zipfile, save_dir, overwrite=False):
    """
        zipfile: 压缩包路径;  save_dir解压后保存路径;  overwrite保存路径已存在同名文件是否覆盖
    """
    # todo: 研究一下python调用cmd执行程序的几种方法，获取返回值等信息！！！
    
    tag = " -aoa" if overwrite else ""
    cmd = "7z x {} -o{}{}".format(zipfile, save_dir, tag)  # todo: -aoa  解压时覆盖解压路径下已经存在的同名文件
    os.system(cmd)


def zipped(zip_folder, save_zip_path):
    """
        zip_folder: 待压缩的文件夹下的所有文件;  save_zip_path:  保存的zip包名字及路径
    """
    cmd = "7z a -tzip {} {}".format(save_zip_path, zip_folder)     # todo: 7z a -tzip 压缩包路径(含文件名) 待压缩路径
    os.system(cmd)

    
if __name__ == '__main__':
    change_file_time(
        file="D:/achange/code//tmp.py",
        file_time=str2time("2018/10/20 18:36:36")
    )


