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
driver.get('https://radical-alto-0ef.notion.site/2023-5-a27c23fe0b0b433a954d72c954769868') #창 열기
time.sleep(1)

header = driver.find_element(By.CSS_SELECTOR, "h1") #선택한 프레임 또는 창의 현재 컨텍스트에서 자바스크립트 실행
#이게뭐지????ㅠㅠㅠㅠㅠㅠㅠㅠ
driver.execute_script('return arguments[0].innerText', header)#이거 뭐죠???????????????ㅠㅠㅠㅠㅠ

element = driver.find_element(By.XPATH,"//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3")
driver.execute_script("arguments[0].innerText = '반갑습니다';", element)