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
driver.find_element(By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="top-bar"]/div/nav/div/ul/li[1]/div/ul/li[4]/a').click()  #집행부 문서 클릭
time.sleep(1)
search = driver.find_elements(By.TAG_NAME, 'body') #일치하는 모든 요소들 가져오기
for e in search: #모든 요소 리스트에서 각 요소 가져오기
    print(e.text) #text: 셀레니움 정보 여러 요소중에 텍스트만 가져옴
