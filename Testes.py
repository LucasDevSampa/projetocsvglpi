'''
#Intera entre as celulas de uma coluna
    i = 1
    while i <= ws1.max_row:
        print(ws1.cell(i,2).value)
        i = i + 1

    #Filtra a Coluna Entidade
   i = 2
    while i != None:
        text = ws1['D' + str(i)].value.split("-")
        ws1['D' + str(i)].value = text[1]    
        i+=1
        
  #  i = 2
    while i <= ws1.max_row:
        print(ws1['D' + str(i)].value)
        i+=1"""

    print()
    criar filtro
  ws1.auto_filter.ref = "A1:D1"

    Salvar A planilha
    wb.save("FieldSP.xlsx")


    Intera entre as celulas de uma coluna versao 2
    
    i = 2
    while i <= ws1.max_row:
        print(ws1['B' + str(i)].value)
        #wb.create_sheet(ws1['B' + str(i)].value)
        i+=1'''