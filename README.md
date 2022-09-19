# MOST-Update-Tool
MOST-Update-Tool能自動化、大量幫助輸入科技部學術著作資料(c302)，對於常常發表文獻，需要更新論文、著作發表的學者們，可以自行延伸應用，免去一項一項手動輸入的麻煩！

## 使用方式

### Step 1：MOST_update.py中的`account`及`password`替換自己的帳號密碼
```
account = "abc123"
password = "abc456"
```

### Step 2：下載對應版本的chromedriver.exe
方法：前往 https://chromedriver.chromium.org/downloads 網站下載符合自己瀏覽器版本的exe檔(範例使用`ChromeDriver 104.0.5112.79`版本)
![image](https://user-images.githubusercontent.com/111637364/187375231-b8d4c5dc-ff65-4cc6-b9e5-7a60d376b939.png)

### Step 3：修改MOST_update.py中的`authorName` `pubYear` `pubMonth` `paperTitle` `conferenceName` `confPlace`等論文資訊，若大量可使用list寫法
```
authorName = "輸入作者名稱"
firstAuthor = 'input[name="firstAuthorYn"][value="1"]'   # 本人為第一作者："1"=是 / "0"=否
crsAuthor = 'input[name="crsAuthorYn"][value="0"]'   # 本人為通訊作者："1"=是 / "0"=否
pubYear = "發表年分"
pubMonth = "發表月份"
paperTitle = "發表標題"
language = "外文"
conferenceName = "發表研討會名稱"
isAccepted = "1" # 1=已接受 / 0=已發表
confPlace = "USA, CA"
vipYn = "Y" # 是否為國際性重要學術會議：Y=是 / N=否
```

### Step 4：執行MOST_update.py檔案，自動進入科技部學術著作資料(c302)，填入論文發表資訊
```
$ python MOST_update.py
```
