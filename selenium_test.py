from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = "http://127.0.0.1:5000/"
# ブラウザ起動
driver.get(url)

# 入力欄(email)の取得
emailElement = driver.find_element(By.ID,'email')
# emailにログインアドレスを入力
emailElement.send_keys('shim@gmail.com')
# 入力欄(password)の取得
passwordElement = driver.find_element(By.ID,'password')
# passwordにパスワードを入力
passwordElement.send_keys('abcd1234')
# ボタンの取得
buttonElement = driver.find_element(By.ID,'submitBtn')
# ボタンをクリック
buttonElement.click()


# ログイン後
# tableタグを取得
tableElement = driver.find_element(By.TAG_NAME,"table")
trElement = tableElement.find_elements(By.TAG_NAME,"tr")
for i in range(len(trElement)):
    if i != 0:
        tdElement = trElement[i].find_elements(By.TAG_NAME,"td")
        result = {"ID":tdElement[0].text,"NAME":tdElement[1].text,"GENDER":tdElement[2].text,"PREF":tdElement[3].text,"BTYPE":tdElement[4].text}
        print(result)

# 停止時間
time.sleep(6)
# 終了
driver.close()
