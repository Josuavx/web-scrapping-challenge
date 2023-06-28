from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome()
browser = webdriver.Chrome(options=options)

browser.get('https://gizmodo.uol.com.br')

targets = browser.find_elements(By.CLASS_NAME, "list-item")

for i in range(10):

    title = targets[i].find_element(By.TAG_NAME, "a")
    date = targets[i].find_element(By.CLASS_NAME, "published.updated")
    date = date.text.split('@')
    summary = targets[i].find_element(By.CLASS_NAME, "postSummary.entry-content")

    print("Nóticia "+ str(i + 1) + ":\n")
    
    print(title.text)
    print(date[0])
    print(summary.text)
    print()


browser.close()