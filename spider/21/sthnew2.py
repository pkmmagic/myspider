import myspider

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    'Cookie': 'visid_incap_1639104=mhq7QWZpR2GA0I8N0naX1J4XcVsAAAAAQUIPAAAAAADtpe/k2K3rqJNMc2EdFHeb; incap_ses_305_1639104=XXYQLSKD+AuLGSXiDpU7BJ4XcVsAAAAAiK6HBaFvNPO7LvfWTBGqDw==; a22e7_lastvisit=35%091534138295%09%2F2048%2Fthread.php%3Ffid-27.html; a22e7_lastpos=F27; a22e7_ol_offset=231927; a22e7_threadlog=%2C27%2C; __tins__19410549=%7B%22sid%22%3A%201534138284055%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201534140084055%7D; __51cke__=; __51laig__=1'
}
# mainPage = 'love2048.com'
mainPage = 'www.weiai2048.com'

libPath = 'lib2.txt'
errorPath = 'error2.txt'
downloadPath = r'D:\a500\\'
libIndex = 500
pace = 500

if __name__ == '__main__':
    myspider.part_download_go(headers, mainPage, libPath, errorPath, downloadPath, libIndex, pace)
