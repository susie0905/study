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
driver.get('http://www.naver.com')
title = driver.title #페이지 제목
url = driver.current_url
handle = driver.current_window_handle
time.sleep(1)
driver.get('http://www.google.com')
time.sleep(1)
driver.back() #뒤로가기
time.sleep(1)
driver.forward() #앞으로가기
time.sleep(1)
driver.get('http://instagram.com')
time.sleep(1)
driver.refresh() #새로고침
time.sleep(1)
driver.get('http://www.facebook.com')
time.sleep(3)

driver.close()    # 탭 종료
driver.open()
