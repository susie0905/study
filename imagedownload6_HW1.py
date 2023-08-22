# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.get("https://www.google.com/search?sca_esv=559020407&q=%EB%AA%A8%EB%AA%BD%EA%B0%80&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjS0bOI5u-AAxXNbN4KHZ0PD_oQ0pQJegQICxAB&biw=1280&bih=667&dpr=1.5")
time.sleep(2)

for i in range (1, 30):
    el = driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[%s]/a[1]/div[1]/img' %(str(i)))
    el_url = el.get_attribute('src') #img src 주소값을 변수에 저장
    print(el_url)
    request.urlretrieve(el_url, "./downmomong/momongga%s.jpg" %(str(i))) #현재 폴더의 downmomon폴더에 저장
driver.close()