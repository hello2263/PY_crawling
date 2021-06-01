import requests
from bs4 import BeautifulSoup


word = input("검색할 단어를 적어주세요. >> ")
count = int(input("페이지 개수를 적어주세요. >> "))
for num in range(1, count+1):
    url = ('https://kin.naver.com/search/list.nhn?query='+ word + '&page=' + str((num)))
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('ul.basic1')
        titles = ul.select('li > dl > dt > a')
        for title in titles:
            print(title.get_text())

    else :
        print(response.status_code)





##################한글을 유니코드 8로#####################
# https://kin.naver.com/search/list.nhn?query=\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac
# word_u8 = '파이썬'.encode('utf-8')


################구글에 있는 url 전부 프린트########################
# import urllib.request
# from bs4 import BeautifulSoup
#
# url = "https://www.google.com"
# soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
# a_tags = soup.find_all('a')
# result_list = []
# for i in a_tags:
#     result_list.append(i.get_text())
# print(result_list)
