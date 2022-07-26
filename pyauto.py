from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 어느 순간부터 관리하려면 webdriver-manager 사용해야되는듯
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# pyautogui 사용하기
import pyautogui
# pyautogui는 한글을 지원하지않음 따라서 pyperclip을 활용해서 복사 붙여넣기를 이용하여 한글을 사용한다.
import pyperclip

# shutil을 활용해서 쿠키/ 캐쉬를 삭제 // 삭제 안하고 사용할거면 해당 구문 지우기

# try:
#     shutil.rmtree(r"c:\chrometemp")  #쿠키 / 캐쉬파일 삭제
# except FileNotFoundError:
#     pass

# subprocess.Popen은 크롬 브라우저를 실행시키는 명령어
# 일단 chrome.exe 파일이 내 컴퓨터 어디에 위치해 있는지 확인 필요
# –remote-debugging-port=9222 는 구동하는 크롬의 포트를 알려주는 것이다.
# –user-data-dir=”C:\chrometemp” 는 크롬을 사용하여 웹상을 돌아다녔을 때 생기는 쿠키와 캐쉬파일을 저장하는 곳이다.

# 일반 셀레니움은 쿠키와 캐쉬파일을 저장하지 않는다. 저장할 필요가 없기 때문이다. 따라서 셀레니움 드라이버를 구동할때마다
# 쿠키와 캐쉬가 완전히 삭제된 새로운 브라우저창이 열린다. 그러나 우리가 지금 사용하려는 디버거 크롬은 일반 크롬과 동일하기 때문에 쿠키와 캐쉬를 저장한다.
# 만약 디버거 크롬을 사용할 때마다 자동으로 쿠키와 캐쉬파일을 삭제하도록 처리하고 싶다면 C:\chrometemp 폴더 이하 파일들을 삭제해주면 된다.

subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동

option = Options();
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
driver.implicitly_wait(3)

# TODO notion_pyauto ver.1 : 구글 자동로그인 구현하기
# # driver를 통해서 notion 홈페이지 열기
# url = "https://www.notion.so/6b4572ad65dc45dd9795752556b05a95"
# #driver를 통해서 해당 url 열기
# driver.get(url)
# # notion 로그인 접근
# google_login_btn = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div/main/div/div[3]/div[1]')))
# google_login_btn.click()
# driver.implicitly_wait(2)
# # notion 로그인 ID/PW 입력하기 (입력하고 -> 엔터 -> 입력하고 ->엔터)
#
# #pyautogui.write(['H', 'e', 'l', 'l', 'o'], interval=0.2)
# id = '      119vkfks@gmail.com' # 주의 앞에 6칸정도 공백으로 메꿔야 값을 인식함
# password = '      cbhchlqudgh6902'
# pyautogui.write(id, interval=0.25) # 괄호 안의 문자를 타이핑 합니다.
# pyautogui.press('enter') # shift 키를 누릅니다.
# pyautogui.write(password, interval=0.25) # 괄호 안의 문자를 타이핑 합니다.
# pyautogui.press('enter') # shift 키를 누릅니다.

# TODO notion_pyauto ver.2 : 브라우저 쿠키및 캐쉬값을 통한 로그인으로 notion에 접근하기
# 1. notion으로 브라우저 쿠키 및 캐쉬값을 통한 로그인 접근
url = "https://www.notion.so/2022_02_24-79bc4e9442444d03bed40d046751f96b"
driver.get(url)

# 2. 오른쪽상단 버튼 누르기 구현
function_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="notion-app"]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]')))
function_btn.click()
# 3. 내보내기 버튼 누르기
export_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[6]/div[2]')))
export_btn.click()

# 4. pdf파일로 변환하기 //*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div/div[6]/div[2]
# 4.1 pdf파일, html파일, markdown파일이 분리되어있는 그룹 버튼 클릭
pdf_change_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]')))
pdf_change_btn.click()

# 4.2 pdf파일, html파일, markdown파일이 분리되어있음 여기서 선택해야됨
pdf_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="notion-app"]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]')))
pdf_btn.click()

# 4.3 pdf파일 내보내기
pdf_export_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,'//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div/div[6]/div[2]')))
pdf_export_btn.click()
