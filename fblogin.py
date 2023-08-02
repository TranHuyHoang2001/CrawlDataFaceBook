from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 1. Khai bao bien browser
options = webdriver.ChromeOptions()
options.binary_location = "./chromedriver.exe"

browser = webdriver.Chrome(options=options)

# 2. Mở thử một trang web
browser.get("http://facebook.com")

# 2a. Điền thông tin vào ô user và pass

txtUser = browser.find_element(By.ID, "email")
txtUser.send_keys("abcxyz") # <---  Điền username thật của các bạn vào đây

txtPass = browser.find_element(By.ID, "pass")
txtPass.send_keys("passwordfake")

# 2b. Submit form

txtPass.send_keys(Keys.ENTER)


# 3. Dừng chương trình 5 giây
sleep(50)

# 4. Đóng trình duyệt
browser.close()