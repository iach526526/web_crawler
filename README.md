# how to use go_to_PTT?
在開始執行程式前，請先確認您已安裝以下套件及Python

*     selenium
*     openpyxl
   如果沒有以上兩個，請在CMD視窗輸入pip install+套件名稱
*     webdriver(這裡使用ChromeDriver)

---
在go_to_PTT這支程式中將會到PTT的政治板由新到舊把文章的聲量、作者、文章標題、發布日期、用網路爬蟲爬下來並輸出在Excel表格，輸出成品如下圖(請自行把B排拉開查看完整標題):
![](https://i.imgur.com/QwOzgp2.png)

---

# how to use go_to_pinterest?
go_to_pinterest會到pinterest把特定關鍵字的圖片下載下來，執行此程式，你需要注意以下幾點:
*    你需要有自己的pinterest帳號
*    記得把帳密分別打在28行和34行
*    41行可以更改搜尋關鍵字