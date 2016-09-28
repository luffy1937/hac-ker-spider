#coding=UTF-8
import urllib
import re
import os
CHAR_SET='utf-8'
TITLE_RE='<a href=\"snapshot.php\?p=.{6}(.*)\" target=\"_blank\">'
PAGE_COUNT_RE='pg.pageCount =(\d+);'
def findtitle(pageurl):
    """
    :param pageurl:PageList url
    :return: 本页中的所有title url

    """
    content=downloadPage(pageurl)
    m=re.compile(TITLE_RE)
    terms=re.findall(m,content)
    print(len(terms))
    return [''.join(['http://www.hac-ker.net/url.php?id=',term]) for term in terms]
def downloadPage(url):
    """
    :param url:
    :return: pagecontent
    """
    h=urllib.urlopen(url)
    return h.read()
def saveashtml(urls,path=''):
    if path=='':
        path=os.path.join(os.getcwd(),"data")
    for url in urls:
        with open(os.path.join(path,''.join([url.split('=')[1],'.html'])),'w+') as w:
            w.writelines(downloadPage(url))
def pagecount():
    content=downloadPage("http://www.hac-ker.net/")
    m=re.compile(PAGE_COUNT_RE)
    term=re.findall(m,content)
    print(term)
    return term[0]

if __name__=="__main__":
    count=int(pagecount())
    for pagenum in range(1,count+1):

     content=findtitle(''.join(['http://www.hac-ker.net/?page=',str(pagenum)]))
     saveashtml(content)
