from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
# 打開瀏覽器(須注意下載對應瀏覽器版本)
driver = webdriver.Chrome()
# 前往網站
driver.get("https://www.nstc.gov.tw/")
# 登入科技部網站
account = "輸入您的帳號"
password = "輸入您的密碼"
driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[3]/div/div/form/input[1]').send_keys(account)
driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[3]/div/div/form/input[2]').send_keys(password)
driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[3]/div/div/form/button').click()
# 自動填入學術著作資料
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
# 0) 切換到新視窗
windows=driver.window_handles
driver.switch_to.window(windows[-1])
# 1) 點擊"學術著作資料(c302)"
driver.find_element(By.XPATH,'//*[@id="zone.SideBarRight"]/div/div/ul/li[2]/a').click()
# 2) 點擊"新增"
driver.find_element(By.XPATH,'//*[@id="zone.content11"]/div/div[3]/div[4]/ul/li[2]/a/img').click()
# 3) 點擊"研討會論文"
driver.find_element(By.XPATH,'//*[@id="addMenu"]/ul/li[1]/ul/li[4]/a').click()
# 4) 輸入論文資訊
# 4-1) 作者
driver.find_element(By.XPATH,'//*[@id="htx_nameChi"]').send_keys(authorName)
# 4-2) 本人為第一作者	 "是"
driver.find_element(By.CSS_SELECTOR,firstAuthor).click()
# 4-3) 本人為通訊作者 "否"
driver.find_element(By.CSS_SELECTOR,crsAuthor).click()
# 4-4) 出版年月
driver.find_element(By.ID,'htx_pubYear').send_keys(pubYear)
select = Select(driver.find_element(By.ID,'htx_pubMonth'))
select.select_by_value(pubMonth)
# 4-5) 研討會論文名稱
driver.find_element(By.ID,'htx_title').send_keys(paperTitle)
# 4-6) 著作語文別
select = Select(driver.find_element(By.ID,'htx_language'))
select.select_by_value(language)
# 4-7) 會議名稱
driver.find_element(By.ID,'htx_conference').send_keys(conferenceName)
# 4-8) 發表狀態
select = Select(driver.find_element(By.ID,'htx_isAccepted'))
select.select_by_value(isAccepted) # 1=已接受 / 0=已發表
# 4-9) 舉辦地點
driver.find_element(By.ID,'htx_confPlace').send_keys(confPlace)
# 4-10) 是否為國際性重要學術會議
select = Select(driver.find_element(By.ID,'htx_vipYn'))
select.select_by_value(vipYn) # Y=是 / N=否

# 5) 儲存
# driver.find_element(By.ID,'submitBtn').click()

