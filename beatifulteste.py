from bs4 import BeautifulSoup

with open("http://www.chamados-estapar.com.br/front/ticket.php?is_deleted=0&search=Pesquisar&itemtype=Ticket&criteria[0][field]=12&criteria[0][searchtype]=equals&criteria[0][value]=notold&criteria[1][link]=AND&criteria[1][field]=8&criteria[1][searchtype]=equals&criteria[1][value]=371&reset=reset") as fp:
    soup = BeautifulSoup(fp)
