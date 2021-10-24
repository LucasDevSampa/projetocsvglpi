from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


navegador = webdriver.Chrome()

navegador.get('http://www.chamados-estapar.com.br/front/ticket.php?is_deleted=0&search=Pesquisar&itemtype=Ticket&criteria[0][field]=12&criteria[0][searchtype]=equals&criteria[0][value]=notold&criteria[1][link]=AND&criteria[1][field]=8&criteria[1][searchtype]=equals&criteria[1][value]=371&reset=reset')

