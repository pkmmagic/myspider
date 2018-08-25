import os
import shutil

PATH = 'd:\\censor21\\'

NUM_FILE = 50

def mdir(PATH, NUM_FILE):
    num_dir = int(len(os.listdir(PATH)) / NUM_FILE) + 1
    dir_list = []
    for i in range(num_dir):
        if os.path.exists((PATH + str(i + 1))) == False:
            os.makedirs(PATH + str(i + 1))
            print (PATH + str(i + 1) + ' created')
        dir_list.append(PATH + str(i + 1))
    return dir_list


def move(PATH, newpath):
    for i in os.listdir(PATH):
        if os.path.isfile(PATH + i):
            shutil.move(PATH + i, newpath + '\\' + i)
            print(i + ' move to ' + newpath)
            if len(os.listdir(newpath)) == NUM_FILE:
                break

def go():
    dir_list = mdir(PATH, NUM_FILE)
    for i in dir_list:
        move(PATH, i)


if __name__ == '__main__':
    go()