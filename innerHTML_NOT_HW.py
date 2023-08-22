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
driver.get('https://www.joongang.co.kr/article/25185245') #창 열기
time.sleep(6)

#Xpath로 찾고 보이는 텍스트를 바꾸기
    #제목
title = driver.find_element(By.XPATH, '//*[@id="container"]/section/article/header/h1')
driver.execute_script("arguments[0].innerText = '폰타인 최고심판관 느비예트, 미모의 일반인과 또…이번엔 폰타인 항구서 포착';", title)   
    #기자
journalist = driver.find_element(By.XPATH, '//*[@id="container"]/section/article/header/div[3]/a')
driver.execute_script("arguments[0].innerText = '샤를로트 기자';", journalist)  

time.sleep(5)