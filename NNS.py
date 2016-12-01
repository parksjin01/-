# -*- encoding:utf-8 -*-

from collections import Counter
from konlpy.tag import Twitter
import BeautifulSoup
import urllib
import numpy

kkma = Twitter()

class parse_news():
    def __init__(self, keyword):
        if '://' in keyword:
            self.url = keyword
        else:
            self.keyword = keyword
            self.url = self.search()

    def search(self):
        a = unicode(self.keyword, 'utf-8').encode('euc-kr')

        html = urllib.urlopen('http://news.naver.com/main/search/search.nhn?ie=MS949&query='+a)
        page = unicode(html.read(1000000), 'euc-kr').encode('utf-8')
        soup = BeautifulSoup.BeautifulSoup(page)
        soup = soup.findAll('a', attrs={'class':'go_naver'})
        return soup[0]['href']

    def parsing(self):
        html = urllib.urlopen(self.url)
        html = html.read(10000000)
        if 'meta charset="euc-kr"' in html:
            html = unicode(html, 'euc-kr').encode('utf-8')
            soup = BeautifulSoup.BeautifulSoup(html)
            tag_p = soup.findAll('div', attrs={'id': 'articleBodyContents'})
        elif 'meta charset="UTF-8"' in html:
            soup = BeautifulSoup.BeautifulSoup(html)
            tag_p = soup.findAll('div', attrs={'id': 'newsEndContents'})
        elif 'meta charset="utf-8"' in html:
            soup = BeautifulSoup.BeautifulSoup(html)
            tag_p = soup.findAll('div', attrs={'id': 'articeBody'})
        return tag_p[0].text

class news_summary():
    def __init__(self, string):
        self.string = string

    def preprocessor(self, string):
        a = list(string)
        b = []
        idx = 0
        for i in range(len(a)):
            if a[i] == u'"' and idx == 0:
                idx = 1
            elif a[i] == u'"' and idx == 1:
                idx = 0
            if a[i] == u'.' and idx == 1:
                continue
            elif a[i] == u'.' and idx == 0:
                b.append('.\n')
            else:
                b.append(a[i])
        return ''.join(b)

    def getlen(self, string):
        array = []
        for i in string:
            array.append(len(i))
        a = numpy.mean(array)*(1+numpy.std(array)/100)
        print a
        print numpy.mean(array)
        print numpy.std(array)
        return a


    def summary(self, level=2):
        string = self.preprocessor(self.string)
        noun = kkma.nouns(string)
        noun = Counter(noun).most_common(5)
        n = []
        for i in noun:
            n.append(i[0])
        string = string.split('.')
        avg = self.getlen(string)
        for i in string:
            tmp = kkma.nouns(i)
            for j in tmp:
                if j in n and len(i) <= avg:
                    print i.strip(' ').strip('\n')+'.\n'
                    break

if __name__ == '__main__':
    news = parse_news(raw_input('검색어를 입력하세요: '))
    news = news.parsing()
    summary = news_summary(news)
    summary.summary()
