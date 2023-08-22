# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("https://cafe.naver.com/joonggonara/1005170350?q=%ED%82%AC%EB%A7%81%EC%BA%A0%ED%94%84+%EC%A4%91%EA%B3%A0%EB%82%98%EB%9D%BC&rc=&art=ZXh0ZXJuYWwtc2VydmljZS1uYXZlci1zZWFyY2gtdHJhZGUtYXJ0aWNsZQ.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjYWZlVHlwZSI6IkNBRkVfVVJMIiwiY2FmZVVybCI6Impvb25nZ29uYXJhIiwiYXJ0aWNsZUlkIjoxMDA1MTcwMzUwLCJpc3N1ZWRBdCI6MTY5MTQxNDQ3NjAxOX0.gSGhRLrM1zVCRagPK4EukuURQKFQYxUqcWgPG2C-aDI")
time.sleep(1)

# 아이프레임을 대상으로 드라이버 전환하여 상호작용
iframe = driver.find_element(By.XPATH, '//*[@id="cafe_main"]')
driver.switch_to.frame(iframe)

el = driver.find_element(
    By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div/img')
el_url = el.get_attribute('src') #이미지 src 주소값을 변수에 저장
print(el_url)
request.urlretrieve(el_url, "killingcamp.jpg") #현재 폴더에 이 이름으로 파일 생성, 이미지 데이터 저장
driver.close()