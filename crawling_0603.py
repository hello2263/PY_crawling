import requests
from bs4 import BeautifulSoup

test = {}
whole_word = []
whole_sentence = []
count_word = {}
count_rank = 0
goal_sentence = input("검색할 문장을 적어주세요. >> ")
count_page = int(input("페이지 개수를 적어주세요. >> "))
rank_word = int(input("몇 등까지 검색할지 적어주세요. >> "))

goal_word = goal_sentence.split(' ')
goal_sentence = '+'.join(goal_word)


####################################################################################################
# 네이버 지식인에서 원하는 문장(goal_sentence)을 원하는 페이지(count_page)만큼 검색하여 whole_sentence에 전부 삽입한다
####################################################################################################
def naver_search(count_page, goal_sentence, whole_sentence):
    for num in range(1, count_page+1):
        url = ('https://kin.naver.com/search/list.nhn?query='+ goal_sentence + '&page=' + str((num)))
        response = requests.get(url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            ul = soup.select_one('ul.basic1')
            titles = ul.select('li > dl > dt > a')
            for title in titles:
                whole_sentence.append(title.get_text())
        else :
            print(response.status_code)
######################################################################################################
naver_search(count_page, goal_sentence, whole_sentence)

for sentence in whole_sentence:
    whole_word = sentence.split(' ')
    for word in whole_word:
        # if (goal_word not in word):
            if (word not in count_word):
                count_word[word] = 1
            else:
                count_word[word] += 1

count_word = sorted(count_word.items(), key = lambda x:x[1], reverse = True)


########################################################################################################################
#몇 등(rank_word)까지 검색할 지 정하고 단어와 등장횟수(count_word)에서 정해진 등수(count_rank)까지 출력한다
#동일한 등장횟수 일 경우 전부 출력이 되게끔 설정
########################################################################################################################
def word_rank_count(rank_word, count_word, count_rank):
    while (count_rank <= rank_word):
        count_rank += 1
        if (count_rank <= rank_word):
            if (count_word != {}):
                first_word = count_word.pop(0)
                print(first_word)
            else:
                break
        elif (count_rank > rank_word):
            if (len(count_word) != 0):
                second_word = count_word.pop(0)
                if (first_word[1] == second_word[1]):
                    print(second_word)
                    count_rank -= 1
            else:
                print("finish")
                break
########################################################################################################################
word_rank_count(rank_word, count_word, count_rank)






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
