import pandas as pd
from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment, Protection
'''Este codigo pega o arquivo csv e transforma em uma versão excel ja filtrado com as informações necessarias'''

def cria_excel():
    print("Criando planilha excel")
    #Carrega o csv bruto do glpi
    chamados_df = pd.read_csv('glpi.csv', sep=';')

    #Cria um novo dataframe apenas com os valores necessarios
    novo_dataframe = chamados_df[["Atribuído para - Técnico", "ID", "Entidade"]]
    novo_dataframe.to_excel("provisorio.xlsx", sheet_name="Chamados Atribuidos")

    wb = load_workbook(filename = 'provisorio.xlsx')
    ws = wb['Chamados Atribuidos']

    ws['A1'].value = 'Quantidade'
    ws.cell(1,1).font = Font(bold= True)
    ws.cell(1,1).alignment = Alignment('center')

    i = 2
    while i <= ws.max_row:
        text = ws['D' + str(i)].value.split("-")
        ws['D' + str(i)].value = text[1]
        i = i + 1

    ws['E1'].value = 'Status'
    ws.cell(1,5).font = Font(bold= True)
    ws.cell(1,5).alignment = Alignment('center')
    ws.auto_filter.ref = "A1:E1"

    i=2
    while i <= ws.max_row:
        ws.cell(i, 1).value += 1
        i+=1
    #Salvar a planilha
    wb.save("provisorio.xlsx")
    print("#Feito")


