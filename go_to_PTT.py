from selenium import webdriver#非內建
import time
from selenium.webdriver.common.keys import Keys
# Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="D:/chromedriver_win32/chromedriver.exe"#放你電腦中chromedriver的檔案路徑
#Explicit Waits

driver=webdriver.Chrome(path)

driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")
cookie ={"name": "over18",'value':'1'}#修改cookie，越過是否滿18歲的警告
driver.add_cookie(cookie)
driver.get_cookies()
driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")#修改cookie後需要重整網頁才會被套用
#清單內儲存作者、日期等要爬取的資料，等出迴圈匯入excel
a=[]#存作者author
d=[]#存日期date
t=[]#存標題title
for j in range(10):#次數自己訂，會決定讀取的頁數
    WebDriverWait(driver, 10).until(    #等待直到到作者欄位出來(代表網頁已經載入完畢，可以開始爬取)
            EC.presence_of_element_located((By.CLASS_NAME, "author"))
            )

    author=driver.find_elements_by_class_name('author')
    
    date=driver.find_elements_by_class_name("date")
    
    title=driver.find_elements_by_css_selector('div.title > a')
    br=0#儲存是否略過這一頁的條件，如果值為1會略過這一頁。略過原因請參見第38行註解
    for i in author:#每一頁開始前先判斷有沒有被刪掉的文章(用作者欄位去判斷，如果文章被刪作者欄位會有"-"號)
        if (i.text)=="-":
            br=1
    if br==1:
        next=driver.find_element_by_link_text('‹ 上頁')
        next.click()
        continue#我不知道怎麼處理被刪掉文章的屍體...屍體只會留著日期和被"-"取代的作者名，不好處理，直接捨棄整頁

    #分別把作者、發文日期、標題存入清單。清單a、d、t的第N項會被存入excel表格的同一橫排，也就是同一個人的資訊
    for i in author:
        a.append(i.text)
    for k in date:
        d.append(k.text)
    for q in title:
        t.append(q.text)
    next=driver.find_element_by_link_text('‹ 上頁')#爬完就到下一頁繼續爬
    next.click()

#Excel的部分
from openpyxl import Workbook,load_workbook#非內建
wb=Workbook()
ws=wb.active

title=["日期","ID","標題"]#加入Excel表格的第一橫排，等會日期、ID、標題也會以這個順序以每個橫排的方式插入表格，每個橫排就代表一篇文章的資訊

ws.append(title)
ws.merge_cells('C1:F1')



for data in range(len(a)):
    print(a[int(data)]+"    "+d[int(data)]+t[int(data)])#在終端機一併輸出讀取結果
    temp=[d[int(data)],a[int(data)],t[int(data)]]#用temp這個清單暫存作者、日期、文章標題的第data項
    ws.append(temp)
wb.save("檔名.xlsx")#儲存檔案，檔名可自定義
driver.quit()