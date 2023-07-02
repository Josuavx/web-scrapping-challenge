# Desafio de Web Scraping

Este código é parte de um desafio de web scraping que tem como objetivo extrair informações de notícias do site [Gizmodo](https://gizmodo.uol.com.br). O código utiliza a biblioteca Selenium para automatizar o processo de navegação e extração dos dados.

## Pré-requisitos

Antes de executar o código, é necessário realizar as seguintes etapas de configuração:

1. Clone este repositório para sua máquina local:
```python
   git clone https://github.com/Josuavx/web-scrapping-challenge
```
3. Verifique se você possui o Google Chrome na versão 114. Caso contrário, atualize-o para essa versão.

4. Baixe o chromedriver compatível com a versão do seu Google Chrome a partir do [site oficial do chromedriver](https://chromedriver.chromium.org/downloads).

## Instalação

Após clonar o repositório, instale as dependências necessárias executando o seguinte comando no terminal:
```python
pip install -r requirements.txt
```
## Uso

Para executar o código e extrair as informações das notícias, siga os passos a seguir:

1. Abra o terminal e navegue até o diretório do projeto.

2. Execute o seguinte comando:
```python
python main.py
```
Isso iniciará a execução do código, que acessará o site do Gizmodo e extrairá os títulos, datas e resumos das 10 primeiras notícias.

3. Após a execução, os dados serão armazenados em um arquivo CSV chamado `data.csv` no mesmo diretório do projeto.

## Observações

- Se o número de notícias encontradas for inferior a 10, será exibida uma mensagem informando que há menos de 10 notícias disponíveis.

- O código utiliza o modo headless do Selenium, o que significa que a execução ocorrerá em segundo plano, sem abrir uma janela do navegador.

- Certifique-se de que o chromedriver esteja localizado no mesmo diretório do arquivo `main.py`.

---

Espero que este arquivo README.md seja útil para entender e utilizar o código. Se tiver alguma dúvida adicional, sinta-se à vontade para perguntar!
