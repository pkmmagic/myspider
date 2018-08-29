import requests

html = 'http://p3.urlpic.club/picturespace/upload/image/20180205/20509043932.jpg'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': 'a22e7_lastvisit=112%091535505414%09%2F2048%2Fread.php%3Ftid-277185.html; a22e7_lastpos=T277185; a22e7_threadlog=%2C27%2C; a22e7_ol_offset=181487; visid_incap_1639104=SekGbbI1QoC/bXYwjTedTikLcVsAAAAAQUIPAAAAAACkHhHDMrj7ftVbmx02YxtJ; a22e7_readlog=%2C277185%2C; __tins__19410549=%7B%22sid%22%3A%201535505438336%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201535507238336%7D; __51cke__=; __51laig__=1'
    }

result = requests.get(html, headers=headers, timeout = 30)

print(result.text.find('</html>'))
