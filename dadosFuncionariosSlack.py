#LEITURA DO ARQUIVO CSV COM OS MEMBROS DO SLACK E CRIAÇÃO DO DICIONÁRIO
import csv

dados = {}

with open('G:/Meu Drive/Softwares/botDicionario/csvFuncionarios/slack-ssoftex-members.csv', mode='r') as arquivo:
    arquivoFormatado = csv.reader(arquivo)
    dados = {rows[0]:rows[1] for rows in arquivoFormatado}