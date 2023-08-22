# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?sca_esv=559012914&q=%EB%AA%A8%EB%AA%BD%EA%B0%80&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjtkO-X3e-AAxW7tlYBHWKIAzcQ0pQJegQIDBAB#imgrc=4MRx4uvSVeYuEM")
time.sleep(3)
el = driver.find_element(
    By.XPATH, '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img')
el_url = el.get_attribute('src') #img src 주소값을 변수에 저장
print(el_url)
request.urlretrieve(el_url, "momongga.jpg") #현재 폴더에 dongguk.jpg라는 이름으로 파일 생성, 이미지 데이터 저장
driver.close()