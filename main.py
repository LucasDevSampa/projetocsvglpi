from re import T
import os
from ConverteCSV import converte
from TrataArquivoExcel import TratarArquivo
import shutil


def main():
    arquivocsv = "/home/lucasc/Downloads/glpi.csv"
    destinocsv = "/home/lucasc/Documentos/PythonPrograms/"
    if os.path.isfile(arquivocsv):
        shutil.copy2(arquivocsv, destinocsv)
        #os.remove(arquivocsv)
    else:
        print("Erro %s arquivo não encontrado" % arquivocsv)
    converte('glpi.csv')
    TratarArquivo('FieldSP.xlsx')
    


if __name__ == "__main__":
    main()