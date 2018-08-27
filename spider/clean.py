import os

mainpath = r'H:\spider\w\\'

def getpath(mainpath):
    l = []
    for i in os.listdir(mainpath):
        l.append(mainpath + i + '\\')
    return l
    

def cleandir(path):
    for i in os.listdir(path):
        filepath = path + i
        if os.path.getsize(filepath) == 0 or os.path.getsize(filepath) == 49965:
            os.remove(filepath)
            print(i + ' removed')


if __name__ == '__main__':
    l = getpath(mainpath)
    for i in l:
        cleandir(i)



