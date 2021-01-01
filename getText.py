import os, glob
import requests
from bs4 import BeautifulSoup
import time

def getInternalHead():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    flist = glob.glob(BASE_DIR + '\internal\*.bmc')
    output = []
    for i in flist:
        tmp = i.replace(BASE_DIR+'\\internal\\',"")
        output.append(tmp.replace(".bmc",""))
    return output

def getInternal(num):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    flist = glob.glob(BASE_DIR+'\internal\*.bmc')
    todo = []
    tf = open(flist[num],"rt",encoding='UTF-8')
    txtlist = tf.readlines()
    for j in range(0, len(txtlist)):
        todo.append(txtlist[j].replace("\n", ""))
    return todo

def getNews(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url,headers=headers)
    output = []
    soup = BeautifulSoup(response.content,"html.parser")
    try:
        soup.find('span', {'class': "end_photo_org"}).decompose()
    except:
        print('there is no span to decompose')
    cont = soup.select("._article_body_contents")[0].get_text('\n')
    res = cont.replace('\t',"")
    res = res.split('\n')
    for i in res:
        if i == '' or '▶' in i or '.com' in i or i==' ':
            continue
        else:
            p = i.strip()
            tmp = p.split('다.')
            if len(tmp) > 2:
                for j in range(0,len(tmp)-1):
                    output.append(tmp[j]+'다.')
            else:
                output.append(p)
    return output

def getNewsHead():
    headers = {"User-Agent": "Mozilla/5.0"}
    today = time.strftime('%Y%m%d',time.localtime(time.time()))
    output = []
    outurl = []
    url = 'https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=001&listType=title&date='+today
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    ul = soup.select(".type02")
    for i in range(0,len(ul)):
        tlist = ul[i].select('a')
        writing = ul[i].select('.writing')
        for j in range(0,len(tlist)):
            output.append(tlist[j].get_text() + " | "+writing[j].get_text())
            outurl.append(tlist[j]['href'])
    return output, outurl

def getLyricsHead():
    headers = {"User-Agent": "Mozilla/5.0"}
    output = []
    #top num의 곡명과 가수명 수집
    url = 'https://www.melon.com/chart/index.htm'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    titles = soup.select(".ellipsis.rank01")
    singers = soup.select(".ellipsis.rank02")
    for i in range(0,len(titles)):
        tmp1 = titles[i].get_text()
        tmp1 = tmp1.replace("\n","")
        tmp2 = singers[i].get_text()
        tmp2 = tmp2.replace("\n","")
        tmp2 = tmp2[0:len(tmp2)//2]
        output.append(tmp1+" - "+tmp2)
    return output

def getLyrics(num):
    headers = {"User-Agent": "Mozilla/5.0"}
    #top num의 곡명과 가수명 수집
    url = 'https://www.melon.com/chart/index.htm'
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content,"html.parser")
    title = soup.select(".ellipsis.rank01")[num].get_text()
    singer = soup.select(".ellipsis.rank02")[num].get_text()
    title = title.replace("\n","")
    singer = singer.replace("\n","")
    singer = singer[0:len(singer)//2]
    output = []
    output.append(title+" - "+singer)
    #top num의 가사 수집
    dsn = soup.find_all("tr", {"data-song-no": True})
    songno=[]
    for i in dsn:
        songno.append(i["data-song-no"])
    tosongno=songno[num]
    url = "https://www.melon.com/song/detail.htm?songId=" + tosongno
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    lyr = soup.find("div",{"class":"lyric"}).get_text("\n")
    lyr = lyr.replace("\t","")
    lyr = lyr.replace("\r","")
    lyr = lyr.split("\n")
    lyr = removeValuesFromList(lyr,'')
    for i in lyr:
        output.append(i.strip())
    return output

def removeValuesFromList(list, val):
    return [value for value in list if value != val]