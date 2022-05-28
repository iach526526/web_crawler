from selenium import webdriver#非內建
import time
from selenium.webdriver.common.keys import Keys
# Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="D:/chromedriver_win32/chromedriver.exe"
#Explicit Waits

driver=webdriver.Chrome(path)

driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")
cookie ={"name": "over18",'value':'1'}#更動cookie
driver.add_cookie(cookie)
driver.get_cookies()
driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")

for j in range(10):#跑幾頁的PTT
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "author"))
            )
    author=driver.find_elements_by_class_name('author')
    for i in author:
        print(i.text)
    next=driver.find_element_by_link_text('‹ 上頁')
    next.click()
