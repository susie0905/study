# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
driver.get('http://www.naver.com')