import shutil
import os
'''Este script pega o arquivo que esta na pasta Downloads do usuario copia para a pasta do programa'''

def copiaArquivo(arquivo):
    print("#Copiando arquivo da pasta Download")
    destinoarquivo = 'C:\\projetocsvglpi'
    if os.path.isfile(arquivo):
        shutil.copy2(arquivo, destinoarquivo)
        os.remove(arquivo)
        print("#Feito")
    else:
        print("Erro %s arquivo não encontrado" % arquivo)

def deletaArquivo(arquivo):
    print("Deletando arquivo csv")
    glpicsv = arquivo
    if os.path.isfile(glpicsv):
        os.remove(glpicsv)
    else:
        print("Erro %s arquivo não encontrado" % glpicsv)
    