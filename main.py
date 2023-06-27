from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
browser = webdriver.Chrome(options=options)

browser.get('https://gizmodo.uol.com.br')

target = browser.find_elements(By.CLASS_NAME, "list-item")

#print(target[0])
target = target[0].find_element(By.TAG_NAME, "a")
print(target.text)


browser.close()