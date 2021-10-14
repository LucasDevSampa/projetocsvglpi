from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options  
chrome_options = Options()

# faz com que o browser não abra durante o processo
#chrome_options.add_argument("--headless") 

# caminho para o seu webdrive
p = "/bin/"
driver = webdriver.Chrome(p + 'chromedriver', options=chrome_options)

driver.get('http://www.chamados-estapar.com.br/front/ticket.php?is_deleted=0&search=Pesquisar&itemtype=Ticket&criteria[0][field]=12&criteria[0][searchtype]=equals&criteria[0][value]=notold&criteria[1][link]=AND&criteria[1][field]=8&criteria[1][searchtype]=equals&criteria[1][value]=371&reset=reset')

login = "lchaves.stefanini"
senha = "L8c45@123"

campo_login = driver.find_elements_by_css_selector('#login_name')
driver.implicitly_wait(8)
campo_login[0].send_keys(login)
campo_senha = driver.find_elements_by_css_selector('#login_password')
driver.implicitly_wait(9)
campo_senha[0].send_keys(senha)
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="boxlogin"]/form/p[3]/input').click()

driver.implicitly_wait(10)
#driver.execute_script("arguments[0].setAttribute('select2-container', select2-container select2-dropdown-open select2-container-active)")

driver.find_elements_by_class_name[1]('select2-arrow').click()

driver.implicitly_wait(10)
seleciona = Select(driver.find_element_by_name('display_type'))
seleciona.select_by_value('3')



driver.implicitly_wait(30)
driver.find_element_by_name('export').click()
