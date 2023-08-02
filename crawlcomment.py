from random import randint

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from flask import Flask

# 1. Khai báo browser
options = webdriver.ChromeOptions()
options.binary_location = "./chromedriver.exe"

browser = webdriver.Chrome(options=options)

# 2. Mở URL của post
browser.get("https://www.facebook.com/groups/824353154969110/posts/1499999540737798/?__cft__[0]=AZUseS44iW3v3w_LXk0GgOvjEp2YsTd0nlb2hsBCwlk4PAtzx83-QnKQp4xllCWx7iQnPIDnoS794EsVJsMTkMKi5jJElSXKbiEvGypDU9iTz-XYF4s-SQPByE0sgrlPSUG8AuT9jhsi2tvZBCz-M8tog6kJZMAPwL__CKJXlTUOO2oh_Wt7n8AtJN9ED_z2HsqsruPCXrAIJIw2twHe4aLbtIYzgUNzzrSgAPuGlMEflOm_N7EfWvTTxv2_5rnIg5Q&__tn__=%2CO%2CP-R")

sleep(5)

#2.a tat bang dang nhap
offlogin_link = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[1]/div")
offlogin_link.click()
sleep(5)

# # 3. Lấy link hiện comment
# showcomment_link = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div[2]")
# showcomment_link.click()
# sleep(5)

# 4. Lấy comment
showmore_link = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div/div/div[4]/div/div/div[2]/div/div[2]/div[1]/div[2]")
showmore_link.click()
sleep(randint(5,10))

showmore_link.click()
sleep(5)

# 5. Tìm tất cả các comment và ghi ra màn hình (hoặc file)
# -> lấy all thẻ div có thuộc tính aria-label='Bình luận'

comment_list = browser.find_elements(By.XPATH, "//div[@class='x1y1aw1k xn6708d xwib8y2 x1ye3gou']")

print(comment_list)

posters = []

# Lặp trong tất cả các comment và hiển thị nội dung comment ra màn hình
for comment in comment_list:
    # hiển thị tên người và nội dung, cách nhau bởi dấu :
    poster = comment.find_element(By.CLASS_NAME, "x3nfvp2")
    # content = comment.find_element(By.XPATH, ".//div[@dir='auto' and @style='text-align: start;']")
    # Text = comment.find_element(By.CLASS_NAME, "x1vvkbs")
    posters.append(poster.text)

    print("*", poster.text)
          # ,":", content.text, "-", Text.text

sleep(20)

app = Flask(__name__)

@app.route('/')
def index():
    return "<br>".join(posters)

if __name__ == "__main__":
  app.run()

sleep(20)

# 6. Đóng browser
browser.close()
