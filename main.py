from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


dicionario = {}

options = Options()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

browser.get('https://gizmodo.uol.com.br')

wait = WebDriverWait(browser, 10)
targets = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "list-item")))

try:
    for i in range(10):
        title = targets[i].find_element(By.TAG_NAME, "a")
        date = targets[i].find_element(By.CLASS_NAME, "published.updated")
        date = date.text.split('@')
        summary = targets[i].find_element(By.CLASS_NAME, "postSummary.entry-content")

        dicionario[i + 1] = [title.text, date[0], summary.text]
except IndexError:
    print("Menos de 10 noticias.")

browser.close()

arquivo = 'data.csv'
df = pd.DataFrame.from_dict(dicionario, orient='index', columns=['Titulo', 'Data', 'Resumo'])
df.to_csv(arquivo, index=False, mode='w')