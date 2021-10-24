from Glpi import copiaArquivo, deletaArquivo
from ListaExcel import cria_excel
from ListaTxt import listar
import copiaCSV
import getpass
import time

def main():
    #começando
    copiaCSV
    time.sleep(13)
    copiaArquivo('C:\\Users\%s\Downloads\glpi.csv'%getpass.getuser())
    cria_excel()
    listar()
    deletaArquivo('C:\\projetocsvglpi\glpi.csv')
 
if __name__ == "__main__":
    main()