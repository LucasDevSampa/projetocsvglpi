import shutil
import os

def copiaArquivo(arquivo):
    print("#Copiando arquivo da pasta Download")
    destinoarquivo = 'C:\\projetocsvglpi'
    if os.path.isfile(arquivo):
        shutil.copy2(arquivo, destinoarquivo)
        os.remove(arquivo)
        print("#Feito")
    else:
        print("Erro %s arquivo não encontrado" % arquivo)

if __name__ == "__main__":
    copiaArquivo()