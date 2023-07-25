#숙제: 크롬 개발자 도구 element 주로 살펴보기, 네트워크 보기
# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
List=[]
Dictionary={}
for i in range (1, 21):
    driver.get('http://wikidocs.net/%s' %(str(i)))
    #딕셔너리 만들기
    Dictionary['title']=driver.title
    Dictionary['url']=driver.current_url
    Dictionary['handle']=driver.current_window_handle
    List.append(Dictionary)
print(List)
print(len(List))