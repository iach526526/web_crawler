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
cookie ={"name": "over18",'value':'1'}
driver.add_cookie(cookie)
driver.get_cookies()
driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")
a=[]#迴圈內儲存作者、日期等要爬取的資料，等出迴圈匯入excle
d=[]
t=[]
for j in range(10):#次數自己訂，會決定讀取的頁數
    br=0
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "author"))
            )
    author=driver.find_elements_by_class_name('author')
    
    date=driver.find_elements_by_class_name("date")
    
    title=driver.find_elements_by_css_selector('div.title > a')
    for i in author:
        if (i.text)=="-":
            br=1
    if br==1:
        next=driver.find_element_by_link_text('‹ 上頁')
        next.click()
        continue#我不知道怎麼處理被刪掉文章的屍體...屍體只會留著日期和被"-"取代的作者名，不好處理，直接捨棄整頁

    for i in author:
        a.append(i.text)
    
    for k in date:
        d.append(k.text)
    for q in title:
        t.append(q.text)
    next=driver.find_element_by_link_text('‹ 上頁')
    next.click()

#Excle的部分
from openpyxl import Workbook,load_workbook
wb=Workbook()
ws=wb.active

title=["日期","ID","標題"]

ws.append(title)
ws.merge_cells('C1:F1')



for data in range(len(a)):
    
    print(a[int(data)]+"    "+d[int(data)]+t[int(data)])
    temp=[d[int(data)],a[int(data)],t[int(data)]]
    ws.append(temp)
wb.save("爬蟲測試2.xlsx")#儲存檔案
driver.quit()