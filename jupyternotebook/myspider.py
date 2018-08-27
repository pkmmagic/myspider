import re, csv

def get_num_set(soup,s):
    pattern = 'tid-([\d\D]*?)-'
    for page in soup.find_all('a'):
        if page.has_attr('href'):
            r=re.findall(pattern,page['href'])
            if len(r)!=0:
                s.add(r[0])    

def readlog(logPath,l):
    csvFile = open(logPath, "r")
    reader = csv.reader(csvFile) 
    for item in reader:
        l.append(item)
    csvFile.close()

def login(logPath,l):
    csvFile = open(logPath,'w', newline='')
    writer = csv.writer(csvFile)
    for sublist in l:
        writer.writerow(sublist)
    csvFile.close()

    
def diff(listA,listB):
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

def open2w(path,l):
    f = open(path , 'w')
    for i in l:
        i = str(i).strip('[').strip(']').replace("'","").replace(' ','')
        f.write(i+'\n')
    f.close()

def open2a(path,l):
    f = open(path , 'a')
    for i in l:
        i = str(i).strip('[').strip(']').strip('{').strip('}').replace("'","").replace(' ','')
        f.write(i+'\n')
    f.close()

def get_list(soup,l):
    for img in soup.find_all('img'):
        if (img.has_attr('src') and img['src'].startswith('http://') 
           and img['src'].find('uploadhouse')==-1
           and img['src'].find('ggpht')==-1
           and img['src'].find('static.flickr')==-1
           and img['src'].find('gif')==-1):
            l.append(img['src'])



            
