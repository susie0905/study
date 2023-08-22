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
driver.get('https://blog.naver.com/skstbvjcjqj/223189664342') #창 열기
time.sleep(2)

# 아이프레임 때문에 안 됨. 아이프레임을 대상으로 드라이버 전환하여 상호작용
iframe = driver.find_element(By.XPATH, '//*[@id="mainFrame"]')
driver.switch_to.frame(iframe)

#제목
title = driver.find_element(By.XPATH, '//*[@id="SE-033e269f-fe48-489a-9ad1-ed86921a5410"]')
driver.execute_script("arguments[0].innerText = '숙제숙제숙제';", title)   
#이미지
image = driver.find_element(By.XPATH, '//*[@id="SE-43f749c4-2899-4c7a-9a7f-f37c7c43be18"]/div/div/div/a/img')
driver.execute_script("arguments[0].src = 'https://i.namu.wiki/i/1mYu1UhxuMJ-LlEBKTyKx-ZO062Nfsw7nVRZ4aLhpQ-kl54ojVdolxhr2vI6oBB4JqGq-WKOUgrrtAfMdZooxg.webp';", image)   
time.sleep(5)