from urllib import request

class Spider():
    url = 'http://www.huya.com/g/2793'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        a = 1
    
    def go(self):
        self.__fetch_content()

spider=Spider()
spider.go()