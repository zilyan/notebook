import os

####扫描文件路径
def read_file(path):
    file=[]
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            file.append(os.path.join(root,name))
    return file

#####扫描文件名
def read_file1(path):
    return os.listdir(path)