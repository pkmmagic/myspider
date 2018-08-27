import myspider, os

censorPath = r'f:\BaiduNetdiskDownload\censor'
censored_num_list = []

for i in os.listdir(censorPath):
    s = censorPath +'\\'+ i
    censored_num_list.append(s.split('\\').pop().split('/').pop().rsplit('.', 1)[0])

print(censored_num_list)

l = []
myspider.open2append('test1.txt',l)

finalPath = 'text6.txt'

for i in censored_num_list:
    for j in range(len(l)):
        if l[j][0:6]==i:
            print(j)
            final_list = l[j].split(',')[1:]
            myspider.open2a(finalPath,final_list)
