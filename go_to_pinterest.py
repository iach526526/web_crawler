from selenium import webdriver#非內建
import time
from selenium.webdriver.common.keys import Keys
# Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Explicit Waits
#載圖片用
import os
import wget
#載圖片用
import random

path="D:/chromedriver_win32/chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://www.pinterest.com/")#到pinterest


login=driver.find_element_by_xpath('//*[@id="fullpage-wrapper"]/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div')
login.click()


useer=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME,'id'))
    )
useer.clear()
useer.send_keys('你的帳號')#輸入帳號
password=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME,'password'))
    )

password.clear()
password.send_keys('你的密碼')#輸入密碼

login2=driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div[2]/div/div/div/div/div/div[4]/form/div[5]/button/div')
login2.click()
search=WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="searchBoxContainer"]/div/div/div[2]/input'))
    )
keyword='ゼルダの伝説'#要什麼關鍵字自己改，範例是ゼルダの伝説
search.send_keys(keyword)
search.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,'//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/a/div/div/div/div/div'))
    )



count=0#記數用
for j in range(5):
    
    if count==0:
        path=os.path.join(keyword)#目錄和文件名組合成一個路徑
        os.mkdir(path)#創建資料夾
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')#往下滑到最下方
        time.sleep(3)
    else:
        a=random.randrange(3,5)#下滑幾次隨機，一定會有被落掉的圖，為了不要重複讀取已經讀過的圖(下滑夠多上面的會讀不到)。這只是讀取策略，如果你有更好的方法可以每張都讀到請告訴我
        for i in range(a):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
            time.sleep(3)

    catch=driver.find_elements_by_tag_name('img')#抓網頁裡的img標籤
    
    for catch in catch:
        # print(catch.get_attribute("src"))取得屬性"src"
        save=os.path.join(path, keyword+str(count)+'.jpg')
        #參數一:下載到哪個資料夾
        #參數二:檔名
        #參數三:副檔名
        wget.download(catch.get_attribute("src"),save)#參數一傳入圖片位置，下載目的地
        count+=1