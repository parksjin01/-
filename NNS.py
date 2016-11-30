# -*- encoding:utf-8 -*-

from collections import Counter
from konlpy.tag import Twitter
import BeautifulSoup
import urllib
kkma = Twitter()

class parse_news():
    def __init__(self, url):
        self.url = url

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
        print tag_p
        return tag_p[0].text


def preprocessor(string):
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

def avg_len(strings):
    s = 0
    for i in strings:
        s+=len(i)
    return s/len(strings)

def summary(string, level=2):
    string = preprocessor(string)
    print string
    noun = kkma.nouns(string)
    noun = Counter(noun).most_common(5)
    n = []
    for i in noun:
        n.append(i[0])
    string = string.split('.')
    avg = avg_len(string)
    for i in string:
        tmp = kkma.nouns(i)
        for j in tmp:
            if j in n and len(i) <= avg*level:
                print i.strip(' ').strip('\n')+'.\n'
                break

if __name__ == '__main__':
    news = parse_news(raw_input('뉴스 url을 입력해주세요'))
    news = news.parsing()
    summary(news, 1)
