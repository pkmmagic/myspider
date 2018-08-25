# coding: utf-8

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
'Cookie':'a22e7_c_stamp=1533181577; a22e7_readlog=%2C98009%2C; a22e7_lastpos=F21; a22e7_ol_offset=235710; visid_incap_1639104=Jb5ILxvzTxmJ4cESKs8iTqZ6YlsAAAAAQUIPAAAAAAAAjBuqYIiX7PR9wNyLyeP9; incap_ses_635_1639104=tZanZyHFKW4OdGm22vnPCNDmaFsAAAAAEfG/HYkQmgB7VzcTFWctnw==; __tins__19410549=%7B%22sid%22%3A%201533601494624%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201533603294624%7D; __51cke__=; __51laig__=1; a22e7_lastvisit=242%091533601498%09%2F2048%2Fthread.php%3Ffid-21.html; a22e7_threadlog=%2C21%2C'
}
import requests, urllib.request, myspider, time 
from bs4 import BeautifulSoup
from urllib.request import urlopen

since = time.time()
LibPath, NewPath = 'd:\\img\\2.txt', 'd:\\img\\3.txt'

#url = 'http://www.weiai2048.com/2048/thread.php?fid-21-page-144.html'
#url = 'http://www.weiai2048.com/2048/thread.php?fid-24.html'
subpage_url_num_set = set()
for i in range(230,240):
    try:
        url = 'http://www.weiai2048.com/2048/thread.php?fid-21-page-'+str(i)+'.html'
        result = urlopen(urllib.request.Request(url,headers=headers), timeout=30)
        soup = BeautifulSoup(result,'html.parser')
        myspider.get_num_set5(soup,subpage_url_num_set)
    except Exception as e:
        pass
print(subpage_url_num_set)

All_set = set()
myspider.open2add(LibPath,All_set)
diff = subpage_url_num_set.difference(All_set)
myspider.open2w(NewPath,list(diff))

print(str(len(subpage_url_num_set))+' get and '+ str(len(diff))+ ' new numbers')

All_set.update(diff)
myspider.open2w(LibPath,sorted(list(All_set)))
time_elapsed = time.time() - since
print (time_elapsed)


