from re import T
from ConverteCSV import converte
from TrataArquivoExcel import TratarArquivo


def main():
    converte('/home/lucasc/Downloads/glpi (4).csv')
    TratarArquivo('FieldSP.xlsx')


if __name__ == "__main__":
    main()