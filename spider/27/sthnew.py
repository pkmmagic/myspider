import myspider, os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Cookie': 'a22e7_threadlog=%2C27%2C; __tins__19410549=%7B%22sid%22%3A%201535372290768%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201535374090768%7D; __51cke__=; __51laig__=1; a22e7_lastvisit=2%091535372398%09%2F2048%2Fck.php'
}
# mainPage = 'love2048.com'
mainPage = 'www.weiai2048.com'

libPath = 'lib.txt'
errorPath = 'error.txt'
downloadPath = 'H:\spider\download\\'
libIndex = 120
pace = 100

if __name__ == '__main__':
    myspider.part_download_go(headers, mainPage, libPath, errorPath, downloadPath, libIndex, pace)
