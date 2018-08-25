#read censored jpg and cross it with the new load
#take the remaining as index to locate all the urls in master then save them in 6.txt for popping
import myspider,os
censoredPath = r'f:\BaiduNetdiskDownload\censor21'

myspider.part_4_go(censoredPath , 'master.txt', 'candidates.txt')

list1 = os.listdir(censoredPath)

for i in list1:
    os.remove(censoredPath+'\\'+i)

os.rmdir(censoredPath)