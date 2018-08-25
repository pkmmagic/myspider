headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
'Cookie':'a22e7_c_stamp=1533181577; a22e7_readlog=%2C98009%2C; a22e7_lastpos=F21; a22e7_ol_offset=235710; visid_incap_1639104=Jb5ILxvzTxmJ4cESKs8iTqZ6YlsAAAAAQUIPAAAAAAAAjBuqYIiX7PR9wNyLyeP9; incap_ses_635_1639104=tZanZyHFKW4OdGm22vnPCNDmaFsAAAAAEfG/HYkQmgB7VzcTFWctnw==; __tins__19410549=%7B%22sid%22%3A%201533601494624%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201533603294624%7D; __51cke__=; __51laig__=1; a22e7_lastvisit=242%091533601498%09%2F2048%2Fthread.php%3Ffid-21.html; a22e7_threadlog=%2C21%2C'
}
import requests, urllib.request, myspider, time, os 
from bs4 import BeautifulSoup
from urllib.request import urlopen

UrlPath, NewPath,filePath = 'test1.txt', 'test3.txt', r'd:\censor'

master_list = []
num_set = set()
myspider.open2add(NewPath,num_set)
num_list = list(num_set)

def get_url(num,l):
    req = urllib.request.Request('http://www.weiai2048.com/2048/read.php?tid-' + num + '.html',headers=headers)
    result = urlopen(req, timeout=45)
    soup2 = BeautifulSoup(result,'html.parser')
    myspider.get_list(soup2,l)
    print(num +' done')

for num in num_list:
    try:
        image_url_list = []
        image_url_list.append(num)
        since=time.time()
        get_url(num,image_url_list)
        master_list.append(image_url_list)
        time_elapsed = time.time() - since
        print(str(num_list.index(num))+': '+str(round(time_elapsed,2))
    except:
        print('exception')
        
print(len(master_list))

myspider.open2w(UrlPath,master_list)

