from copia import copiaArquivo
import getpass

def main():
    #Pegar arquivo na pasta download e levar para a pasta onde esta o programa
    copiaArquivo('C:\\Users\%s\Downloads\glpi.csv'%getpass.getuser())
    


if __name__ == "__main__":
    main()