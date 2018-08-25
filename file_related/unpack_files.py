import os
import shutil

PATH = 'F:\\BaiduNetdiskDownload\\censor21\\'


def get_subpath(PATH):
    l = []
    for i in os.listdir(PATH):
        if os.path.isdir(PATH + i):
            l.append(PATH + i)
    return l


def moveout(PATH, subpath):
    for i in os.listdir(subpath):
        if os.path.isfile(subpath + '\\' + i):
            shutil.move(subpath + '\\' + i, PATH + i)
            print(i + ' moved out')
            if len(os.listdir(subpath)) == 0:
                os.rmdir(subpath)

def go():
    l = get_subpath(PATH)
    for subpath in l:
        moveout(PATH, subpath)

if __name__ == '__main__':
    go()