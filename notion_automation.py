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
#BeautifulSoup를 통한 웹 크롤링
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
###################################
# pyautogui 사용하기
import pyautogui
# pyautogui는 한글을 지원하지않음 따라서 pyperclip을 활용해서 복사 붙여넣기를 이용하여 한글을 사용한다.
import pyperclip
# 내부 참조 함수
import os

class Notion_automation:
    # 시작하자마자 기본 할당값 실행할때 사용하기

    def __init__(self):
        print("생성자가 생성되었습니다.")

    # in: 크롬 드라이버 경로  out: driver 반환
    def driver_r(self,chromepath):
        subprocess.Popen(chromepath + ' --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')  # 디버거 크롬 구동
        option = Options();
        option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

        chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

        try:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
            return driver
        except:
            chromedriver_autoinstaller.install(True)
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
            return driver

    def pdf(self, driver , targeturl):
        driver.implicitly_wait(3)
        # TODO notion_pyauto ver.2 : 브라우저 쿠키및 캐쉬값을 통한 로그인으로 notion에 접근하기
        # 1. notion으로 브라우저 쿠키 및 캐쉬값을 통한 로그인 접근
        driver.get(targeturl)
        # 2. 오른쪽상단 버튼 누르기 구현
        function_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="notion-app"]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[2]/div[5]')))
        function_btn.click()
        # 3. 내보내기 버튼 누르기
        export_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,
                                                                                    '//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div[1]/div[6]/div[2]')))
        export_btn.click()

        # 4. pdf파일로 변환하기
        # 4.1 pdf파일, html파일, markdown파일이 분리되어있는 그룹 버튼 클릭
        pdf_change_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]')))
        pdf_change_btn.click()

        # 4.2 pdf파일, html파일, markdown파일이 분리되어있음 여기서 선택해야됨
        pdf_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="notion-app"]/div/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[1]')))
        pdf_btn.click()

        # 4.3 pdf파일 내보내기
        pdf_export_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="notion-app"]/div/div[2]/div[2]/div/div[2]/div/div[6]/div[2]')))
        pdf_export_btn.click()

    # class = notion-selectable notion-page-block
    # 노션 DB 서칭 리스트
    def search_p_size(self, driver,url):
        #저장 요소 선언
        try:
            fin = []
            i = 1
            driver.implicitly_wait(3)
            driver.get(url)
            driver.implicitly_wait(3)
            # div.notion-selectable notion-page-block notion-collection-item
            #ele2 = driver.find_element(By.XPATH,'//*[@id="notion-app"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[4]/div[2]/div/div[2]/div')
            element = driver.find_element(By.CSS_SELECTOR,"div.notion-table-view")
            element = driver.find_element(By.CSS_SELECTOR, "div.notion-table-view")
            # 의문점 element 한번 호출하고 element를 한번 더 호출을 해야 밑에 하위 자식같은 표가 값으로 나오게된다. ? why ? 이렇게 안하면 왜 안나옴?
            element.text
            size = element.text.split("\n")
            temp = size[6:]
            print("서칭 ON")
            for idx,val in enumerate(temp):
                if idx == i:
                    i = i + 5
                    fin.append(val)

            return fin
        except ZeroDivisionError as e:
            print("예외 발생" + e)
            return fin
        except IndexError as e:
            print("인덱싱 할 수 없습니다." + e)

    # 게시물 search 반환
    def dir_path(self, path):
        file_list = os.listdir(path)
        file_list_pdf = [file for file in file_list if file.endswith(".pdf")]
        return format(file_list_pdf)

    def dir_compare(self, path):
        file_list = os.listdir(path)
        file_list_pdf = [file for file in file_list if file.endswith(".pdf")]

        test = []
        for i in file_list_pdf:
            test.append(i.replace('_',' '))

        return format(test)

    def solution_pdf(self, driver , targeturl):
        driver.implicitly_wait(3)
        # TODO notion_pyauto ver.2 : 브라우저 쿠키및 캐쉬값을 통한 로그인으로 notion에 접근하기
        # 1. notion으로 브라우저 쿠키 및 캐쉬값을 통한 로그인 접근
        driver.get(targeturl)
        # 2. 오른쪽상단 버튼 누르기 구현
        function_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="notion-app"]/div/div[1]/div[2]/div[2]/div[1]/div[1]/div[3]/div[1]/div/div[4]/div[2]/div/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/a/div')))
        function_btn.click()

