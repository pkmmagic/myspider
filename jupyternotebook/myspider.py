import re, csv, requests, myspider, time, urllib.request, os
from bs4 import BeautifulSoup


def part_1_go(headers, mainPage, section, index, pace, libPath, newPath):
    try:
        since = time.time()
        subpage_url_num_set = subpage(headers, mainPage, section, index, pace)
        print(subpage_url_num_set)
        length = get_lib_write_new(libPath, newPath, subpage_url_num_set)
        print(str(len(subpage_url_num_set)) + ' get and ' + str(length) + ' new numbers')
        time_elapsed = round((time.time() - since), 2)
        print(time_elapsed)
    except Exception as e:
        print(e)


def part_2_go(headers, mainPage, newPath, UrlPath, logPath):
    since = time.time()
    try:
        num_list = get_num_list(newPath)
        print('new num list successfully get from %s' % newPath)
    except Exception as e:
        print(e)
    try:
        master_list = get_from_numlist(num_list, mainPage, headers)
        print('master list successfully get from num_list')
    except Exception as e:
        print(e)
    time_elapsed = round((time.time() - since), 2)
    print(str(len(master_list)) + ' master get. It takes %s seconds.' % str(time_elapsed))
    try:
        open2w(UrlPath, master_list)
        print('master list successfully written')
    except Exception as e:
        print(e)
    try:
        log(logPath, len(num_list), time_elapsed)
        print('get url successfully logged in %s' % logPath)
    except Exception as e:
        print(e)


def part_3_go(masterPath, logPath, censorPath, start_index):
    since = time.time()
    try:
        master_list = []
        open2append(masterPath, master_list)
        print('master list append success from %s' % masterPath)
    except Exception as e:
        print(e)
    n = download(start_index, master_list, censorPath)
    print('%s jpgs download success from master list' % str(n))
    time_elapsed = round((time.time() - since), 2)
    print(time_elapsed)
    try:
        log(logPath, str(len(master_list)), time_elapsed)
        print('logging to %s success' % logPath)
    except Exception as e:
        print(e)


def part_4_go(censorPath, UrlPath, outputPath):
    try:
        censored_num_list = censored_list(censorPath)
        print('censored num list get')
        print(censored_num_list)
    except Exception as e:
        print(e)
    all_list = []
    open2append(UrlPath, all_list)
    print('all num list get')
    try:
        n = cross(outputPath, censored_num_list, all_list)
        print('crossing success: %s get' % str(n))
    except Exception as e:
        print(e)


# part 1
def subpage(headers, mainPage, section, index, pace):  # from index on get pace subpages' url
    s = set()
    for i in range(index, index + pace):
        try:
            url = 'http://' + mainPage + '/2048/thread.php?fid-' + str(section) + '-page-' + str(i) + '.html'
            result = urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30)
            soup = BeautifulSoup(result, 'html.parser')
            get_num_set(soup, s)
        except Exception as e:
            print(e)
    return s


def get_num_set(soup, s):
    pattern = 'tid-([\d\D]*?)-'
    for page in soup.find_all('a'):
        if page.has_attr('href'):
            r = re.findall(pattern, page['href'])
            if len(r) != 0:
                s.add(r[0])


def get_lib_write_new(LibPath, NewPath, subpage_url_num_set):
    s = set()
    open2add(LibPath, s)
    diff = subpage_url_num_set.difference(s)
    open2w(NewPath, list(diff))
    s.update(diff)
    open2w(LibPath, sorted(list(s)))
    return len(diff)


##


# part 2
def get_num_list(newPath):
    num_set = set()
    open2add(newPath, num_set)
    num_list = list(num_set)
    return num_list


def get_from_numlist(num_list, mainPage, headers):
    master_list = []
    for num in num_list:
        try:
            image_url_list = []
            image_url_list.append(num)
            get_url(num, image_url_list, mainPage, headers)
            master_list.append(image_url_list)
            print(str(len(num_list) - num_list.index(num)) + ' left')
        except Exception as e:
            print(e)
    return master_list


def get_url_from_numlist_download(num_list, mainPage, headers):
    for num in num_list:
        try:
            image_url_list = []
            get_url(num, image_url_list, mainPage, headers)
            try:
                n = 1
                for url in image_url_list:
                    download_1pic(num, str(n), url)
                    n += 1

            except Exception as e:
                print(e)

            print(num + ' done')

        except Exception as e:
            print(e)


def get_url(num, l, mainPage, headers):
    req = urllib.request.Request('http://' + mainPage + '/2048/read.php?tid-' + num + '.html', headers=headers)
    result = urllib.request.urlopen(req, timeout=45)
    soup2 = BeautifulSoup(result, 'html.parser')
    get_list(soup2, l)


def get_list(soup, l):
    for img in soup.find_all('img'):
        if (img.has_attr('src') and img['src'].startswith('http://')
                and img['src'].find('uploadhouse') == -1
                and img['src'].find('ggpht') == -1
                and img['src'].find('static.flickr') == -1
        ):
            l.append(img['src'])


##


# part3
def download(start_index, master_list, censorPath):
    n = 0
    for i in range(start_index, len(master_list)):
        if len(master_list[i].split(',')) > 3:
            try:
                res = requests.get(master_list[i].split(',')[3], timeout=30)
                with open(censorPath + '\\%s.jpg' % master_list[i].split(',')[0], 'wb') as f:
                    f.write(res.content)
                n += 1
                print(str(len(master_list) - i) + ',' + str(i))
            except Exception as e:
                print('download ' + master_list[i].split(',')[0] + ' failed: ' + str(e))
    return n


def master2candidates(master_list, candidatesPath):
    n = 0
    for i in range(len(master_list)):
        if len(master_list[i].split(',')) > 2:
            l = master_list[i].split(',')[2:]
            open2a(candidatesPath, l)
            n += 1
    return n


##


# part4
def censored_list(censorPath):
    l = []
    for i in os.listdir(censorPath):
        s = censorPath + '\\' + i
        l.append(s.split('\\').pop().split('/').pop().rsplit('.', 1)[0])
    return l


def cross(outputPath, l1, l2):
    n = 0
    for i in l1:
        for j in range(len(l2)):
            if l2[j][0:6].strip(',') == i:
                n += 1
                final_list = l2[j].split(',')[1:]
                myspider.open2a(outputPath, final_list)
    return n


##


def download_1pic(dirname, filename, html, hearders):
    try:
        if not os.path.exists('D:\py\\' + dirname):
            os.makedirs('D:\py\\' + dirname)

        with open('D:\py\{}\{}.jpg'.format(dirname, filename), 'wb') as f:
            req = urllib.request.Request(html, headers=headers)
            result = urlopen(req)
            f.write(result.read())
    except Exception as e:
        print('Download failed ��', e)


def log(logPath, length, time_elapsed):
    time_list = []
    readlog(logPath, time_list)
    time_list.append([str(time.time()), length, str(time_elapsed)])
    login(logPath, time_list)


def readlog(logPath, l):
    csvFile = open(logPath, "r")
    reader = csv.reader(csvFile)
    for item in reader:
        l.append(item)
    csvFile.close()


def login(logPath, l):
    csvFile = open(logPath, 'w', newline='')
    writer = csv.writer(csvFile)
    for sublist in l:
        writer.writerow(sublist)
    csvFile.close()


def diff(listA, listB):
    retE = [i for i in listA if i not in listB]
    return retE


def open2add(path, s):
    f = open(path, 'r')
    for line in f.readlines():
        linestrip = line.strip()
        s.add(linestrip)
    f.close()


def open2append(path, l):
    f = open(path, 'r')
    for line in f.readlines():
        linestrip = line.strip()
        l.append(linestrip)
    f.close()


def open2w(path, l):
    f = open(path, 'w')
    for i in l:
        i = str(i).strip('[').strip(']').replace("'", "").replace(' ', '')
        f.write(i + '\n')
    f.close()


def open2a(path, l):
    f = open(path, 'a')
    for i in l:
        i = str(i).strip('[').strip(']').strip('{').strip('}').replace("'", "").replace(' ', '')
        f.write(i + '\n')
    f.close()
