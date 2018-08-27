headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
'Cookie':'a22e7_c_stamp=1533181577; a22e7_readlog=%2C522626%2C98009%2C522542%2C; a22e7_ol_offset=133472; visid_incap_1639104=Jb5ILxvzTxmJ4cESKs8iTqZ6YlsAAAAAQUIPAAAAAAAAjBuqYIiX7PR9wNyLyeP9; incap_ses_635_1639104=Q5ROMjIz7w3RPRy42vnPCHCOa1sAAAAAstWE22TqFd7nblxlvdRA4g==; a22e7_lastpos=F27; __tins__19410549=%7B%22sid%22%3A%201533775480153%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201533777280153%7D; __51cke__=; __51laig__=1; a22e7_lastvisit=660%091533775559%09%2F2048%2Fthread.php%3Ffid-27.html; a22e7_threadlog=%2C7%2C21%2C27%2C'
}
import requests, urllib.request, myspider, time 
from bs4 import BeautifulSoup
from urllib.request import urlopen

since = time.time()
LibPath, NewPath = 'test2.txt', 'test3.txt'
subpage_url_num_set = set()

import re

def get_num_set(soup,s):
    pattern = 'tid-([\d\D]*?).html'
    for page in soup.find_all('a'):
        if page.has_attr('href'):
            r=re.findall(pattern,page['href'])
            s.add(r)    



url = 'http://www.weiai2048.com/2048/thread.php?fid-27-page-75.html'
result = urlopen(urllib.request.Request(url,headers=headers), timeout=30)
soup = BeautifulSoup(result,'html.parser')
get_num_set(soup,subpage_url_num_set)

print(subpage_url_num_set)