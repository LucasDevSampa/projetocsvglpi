from selenium import webdriver
from selenium.webdriver.support import select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


navegador = webdriver.Chrome()
navegador.get('http://www.chamados-estapar.com.br/front/ticket.php?is_deleted=0&search=Pesquisar&itemtype=Ticket&criteria[0][field]=12&criteria[0][searchtype]=equals&criteria[0][value]=notold&criteria[1][link]=AND&criteria[1][field]=8&criteria[1][searchtype]=equals&criteria[1][value]=371&reset=reset')

texto_usuario = navegador.find_element_by_xpath('//*[@id="login_name"]')
texto_usuario.send_keys('lchaves.stefanini')
texto_senha = navegador.find_element_by_xpath('//*[@id="login_password"]')
texto_senha.send_keys('L8c45@123')
entrar = navegador.find_element_by_xpath('//*[@id="boxlogin"]/form/p[3]/input')
entrar.click()
navegador.implicitly_wait(10) 
selecao = navegador.find_element(By.CSS_SELECTOR, '#select2-chosen-10')
selecao.click()
navegador.implicitly_wait(10) 
tipo = navegador.find_element(By.CSS_SELECTOR, '#select2-result-label-15')
tipo.click()
navegador.implicitly_wait(10) 
importa = navegador.find_element(By.NAME, 'export')
importa.click()
navegador.implicitly_wait(10) 

