import requests
from bs4 import BeautifulSoup


def namu_crawler():
    url = "https://namu.wiki/RecentChanges"
    response = requests.get(url)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    count = 0
    urls = {}
    for i in soup.findAll('td'):
        if i.a != None:
            if count%2==0:
                urls[i.a.text] = "http://namu.wiki"+i.a['href']
            count += 1
        if len(urls) == 10:
            break
    response.close()
    return urls

def naver_news_crawler():
    url = "https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title"
    response = requests.get(url)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    urls = {}
    for i in soup.findAll('a',{'class':'nclicks(fls.list)'}):
        urls[i.text] = i['href']
        if len(urls) == 10:
            break
    response.close()
    return urls


def dc_crawler():
    url = "http://gall.dcinside.com/board/lists/?id=hit"
    response = requests.get(url)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    urls = {}
    for i in soup.findAll('td',{'class':'gall_tit ub-word'})[2:]:
        urls[i.a.text] = "http://gall.dcinside.com"+i.a['href']
        if len(urls) == 10:
            break
    response.close()
    return urls

def river_temp():
    url = "http://hangang.dkserver.wo.tc"
    response = requests.get(url)
    return response.json()["temp"]


def youtube_crawler():
    url = "https://www.youtube.com"
    response = requests.get(url)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    for i in soup.findAll('a',{'class':' yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link '}):
        print (i)

def dogdrip_crawler():
    url = "https://www.dogdrip.net/?mid=dogdrip&sort_index=popular"
    response = requests.get(url)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    urls = {}
    for i in soup.findAll('a',{'class':'ed link-reset'})[2:]:
        urls[i.span.text] = "https://www.dogdrip.net"+i['href']
        if len(urls) == 10:
            break
    response.close()
    return urls

def korea_bamboo_crawler():
    url="https://www1.president.go.kr/petitions/best"
    response = requests.get(url)
    body = response.text
    soup = BeautifulSoup(body, 'html.parser')
    urls = {}
    for i in soup.findAll('div',{'class':'bl_subject'}):
        try:
            if "?navigation=best" in i.a['href']:
                urls[i.a.text.replace("제목 ","")] = "https://www1.president.go.kr"+i.a['href']
            if len(urls) == 10:
                break
        except:
            pass
    return urls

