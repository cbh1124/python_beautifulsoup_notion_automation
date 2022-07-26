from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('selenium/chromedriver_win32 (2)/chromedriver.exe')
url = "https://www.notion.so/6b4572ad65dc45dd9795752556b05a95"

#driver를 통해서 해당 url 열기
driver.get(url)

# TODO notion으로 사이트 접속 후 구글 로그인 하기
# TODO 1. 로그인 버튼 누르기 (xpath를 통해서 접근)  (주의점 해당 코드 실행시 html 로드가 완료되지않기때문에 5초정도 딜레이를 줘야됨)

google_login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[1]')))
#element = driver.find_element(By.ID, 'notion-app-inner notion-light-theme')
google_login_btn.click()

# TODO 2. 로그인 아이디 입력하기



#print(element.text)