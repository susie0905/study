# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
driver.get('http://capszzang.gq/wiki/') #창 열기
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="search"]').send_keys('장준혁') #검색어 입력
driver.find_element(By.XPATH, '/html/body/section[2]/div[1]/form/button').click()  #검색 버튼 클릭
time.sleep(1)
search = driver.find_elements(By.TAG_NAME, 'body') #일치하는 모든 요소들 가져오기
for e in search: #모든 요소 리스트에서 각 요소 가져오기
    print(e.text) #왜죠