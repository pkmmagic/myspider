import os

#mainpath = r'H:\spider\w\\'
mainpath = r'D:\a500\\'

def getpath(mainpath):
    l = []
    for i in os.listdir(mainpath):
        l.append(mainpath + i + '\\')
    return l
    

def cleandir(path):
    for i in os.listdir(path):
        filepath = path + i
        if os.path.isfile(filepath):
            if (os.path.getsize(filepath) == 0
                or os.path.getsize(filepath) == 49965
                or os.path.getsize(filepath) == 481
                or os.path.getsize(filepath) == 3322
                or os.path.getsize(filepath) == 4807
                or os.path.getsize(filepath) == 535274
                or os.path.getsize(filepath) == 4809):
                os.remove(filepath)
                print(i + ' removed')
                if len(os.listdir(path)) == 0:
                    os.rmdir(path)
                    print('dir rmed')

def go(mainpath):
    l = getpath(mainpath)
    l = l[0:-1]
    for i in l:
        cleandir(i)


go(mainpath)


