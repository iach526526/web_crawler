from selenium import webdriver#非內建
import time
from selenium.webdriver.common.keys import Keys
# Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
path="D:/chromedriver_win32/chromedriver.exe"#放你電腦中chromedriver的檔案路徑
#Excel的部分
from openpyxl import Workbook,load_workbook#非內建
wb=Workbook()
ws=wb.active
title=["回應","標題","ID","日期"]#加入Excel表格的第一橫排，等會日期、ID、標題也會以這個順序以每個橫排的方式插入表格，每個橫排就代表一篇文章的資訊
ws.append(title)

driver=webdriver.Chrome(path)

driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")
cookie ={"name": "over18",'value':'1'}#修改cookie，越過是否滿18歲的警告
driver.add_cookie(cookie)
driver.get_cookies()
driver.get("https://www.ptt.cc/bbs/HatePolitics/index.html")#修改cookie後需要重整網頁才會被套用

for j in range(3):#次數自己訂，會決定讀取的頁數
    WebDriverWait(driver, 10).until(    #等待直到到作者欄位出來(代表網頁已經載入完畢，可以開始爬取)
            EC.presence_of_element_located((By.CLASS_NAME, "author"))
            )
    total=[]#清空total
    div=driver.find_elements_by_class_name('r-ent')#抓取網頁中包覆每個文章的大div
    for q in div:
        total.append(q.text)
    print(total)#終端機輸出，除錯用
    #total輸出範例:['(本文已被刪除) [waynecode]\n-\n5/30', '7\n[討論] 如何滿足在政黑板發文被噓爆的要件?\nwaynecode\n⋯\n5/30', '9\n[討論] 柯粉請
    #進，民進黨到底會不會道歉？\nDoncicInPTT\n⋯\n5/30', '5\n[黑特] 什麼時候要放寬隔離天數？\nmukuro\n⋯\n5/30', '[新聞] 郭彥均事件 
    #延燒！柯文哲：民進黨字典裡沒\na5687920\n⋯\n5/30', '9\nRe: [討論] 3個月內蹦出3個小孩？\nhelba\n⋯\n5/30']
    # 此時total包含那一頁每篇文章的標題、作者、日期等詳細資料

    #找到上面的規則就可以整理他們了
    for i in range(len(total)):
        destruction=total[i].split('\n')#把total陣列每個元素再以\n分隔拆開，拆開後每一項會以清單儲存，這裡命名為destruction
        
        for j in range(len(destruction)-1):
            if destruction[j]=='⋯':#刪除不必要的資訊
                del destruction[j]
        if destruction[0].isdigit()!=True and destruction[0]!="X1" and destruction[0]!="爆":#第零項為空，代表無被推或噓，幫它補一格，輸出試算表才不會有些地方位置亂掉
            destruction.insert(0, '-')
        ws.append(destruction)#把一篇處理過的的文章資訊輸出到Excel
        print(destruction)
    
    
    next=driver.find_element_by_link_text('‹ 上頁')#爬完就到下一頁繼續爬
    next.click()
wb.save("檔名.xlsx")#儲存檔案，檔名可自定義(不要和資料夾現有檔案重複)
driver.quit()