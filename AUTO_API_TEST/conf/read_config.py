import configparser
import os

def read_config(conf_file,section,option):
    #传入文件名称，section，option，返回值
    cf = configparser.ConfigParser()
    cf.read(conf_file)
    value = cf.get(section,option)
    return value
