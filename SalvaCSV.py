from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
chrome_options = Options()

# faz com que o browser não abra durante o processo
#chrome_options.add_argument("--headless") 

# caminho para o seu webdrive
p = "/home/lucasc/Documentos/PythonPrograms/"
driver = webdriver.Chrome(p + 'chromedriver', options=chrome_options)

driver.get('http://www.chamados-estapar.com.br/front/ticket.php?is_deleted=0&search=Pesquisar&itemtype=Ticket&criteria[0][field]=12&criteria[0][searchtype]=equals&criteria[0][value]=notold&criteria[1][link]=AND&criteria[1][field]=8&criteria[1][searchtype]=equals&criteria[1][value]=371&reset=reset')