from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

dicionario = {}

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

    dicionario[i] = [title.text, date[0], summary.text]

    print("Dicionario: "+ str(i) + " " + str(dicionario[i]))


browser.close()