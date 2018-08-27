
#examine shuffled b, if two consecutive bigs spotted, move the
#latter one spot to the right

import random

NUM_PROJECTS = 11
WORK_START_INDEX = 9

a = [x for x in range(1,NUM_PROJECTS + 1)]

#a = ['WBF','WZH','LXL','Homo Deus','Python','Writing','XS','WZH','work']

random.shuffle(a)



def sort(b):
    
    l = NUM_PROJECTS
    j = WORK_START_INDEX

    for i in range(l-1):
        if i<l-2 and b[i]>j and b[i+1]>j and b[i+2]>j:
                b[i+1], b[(i+4)%l] = b[(i+4)%l],b[i+1]

        elif b[l-3]>j and b[l-2]>j and b[1-1]>j:
                b[l-2],b[2] = b[2], b[l-2]
                
        elif b[i]>j and b[i+1]>j:
                b[i+1], b[(i+2)%l] = b[(i+2)%l],b[i+1]
                
        elif b[l-2]>j and b[l-1]>j and b[0]>j:
                b[l-1],b[2] = b[2], b[l-1]
                
    return b


def pj(i):
    dic = ['Meditation','WUJUN','WZH','LXL','Fooled by R','WWG',
           'Python','Writing','XS','work','work']
    for each in range(1,NUM_PROJECTS+1):
        j = i[each-1]
        i[each-1] = dic[j-1]
    return i

sort(a)

pj(a)


def getNext():
    c = 0
    def f():
        nonlocal c
        c += 1
        return a[c-1]        
    return f

g = getNext()




