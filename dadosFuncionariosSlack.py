import csv

dados = {}

#READING THE CSV FILE WITH SLACK MEMBERS AND CREATION OF THE DICTIONARY
with open('G:/Meu Drive/Softwares/botDicionario/csvFuncionarios/slack-ssoftex-members.csv', mode='r') as arquivo:
    arquivoFormatado = csv.reader(arquivo)
    dados = {rows[0]:rows[1] for rows in arquivoFormatado}
