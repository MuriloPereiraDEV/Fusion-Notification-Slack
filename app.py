#    pip install imap-tools
#    pip install bs4
#    pip install path
#    pip install python-dotenv
#    pip install slack
#    pip install schedule

from datetime import datetime
from imap_tools import MailBox, AND, MailMessageFlags
from login import usuario, senha
from cripto import cripto
from dadosFuncionariosSlack import dados
from bs4 import BeautifulSoup
import padraoEmails
import os
from pathlib import Path
from dotenv import load_dotenv
import slack
import schedule
import time


def start():

    #   ESTABELECE A CONEXAO COM O EMAIL NO-REPLI@SOFTEX.BR
    meu_email = MailBox('imap.gmail.com').login(cripto(usuario), cripto(senha), "[Gmail]/E-mails enviados")

    #   PEGA DATA ATUAL
    dataAux = datetime.now().date()

    dataAuxFormatada = ("SENTON " + dataAux.strftime("%d-%b-%Y"))
    #print(dataAuxFormatada)
    #   VAI PROCURAR EMAILS QUE FORAM ENVIADOS A TODOS OS FUNCIONARIOS DA SOFTEX
    for nick in dados:
        
        for msg in meu_email.fetch(AND(to=dados[nick], date=dataAux, seen=True)):
            #    ACESSA O DOCUMENTO E PEGA O TOKEN NECESSARIO PARA CONEXÃO COM SLACK
            env_path = Path('.') / '.env'
            load_dotenv(dotenv_path=env_path)
            client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

            #    PEGA HTML DO EMAIL PARA SER TRATADO
            soup = BeautifulSoup(msg.html, 'html5lib')

            #    ANALISA PADRAO DE EMAIL PARA DISTINGUIR TIPO DE TRATAMENTO
            if padraoEmails.devolutivaSolicitaçãoPagamento in msg.subject:
                #    PEGA A INFORMAÇÃO DE UMA SEÇÃO ESPECIFICA DO CODIGO HTML
                mailTxtHtml = soup.find('p', attrs={'id': 'ext-gen1368'})
                mailTxtFinal = mailTxtHtml.text + "\nComprovante enviado ao seu e-mail."
                if dados[nick] == "murilo.pereira@softex.br":
                    client.chat_postMessage(channel="@murilo.pereira", text=mailTxtFinal)
            elif (padraoEmails.neomindFusionTarefaAvisoPagamento in msg.subject)|(padraoEmails.neomindFusionTarefaAtrasadaPagamento in msg.subject) | (padraoEmails.tarefaRealocada in msg.subject) | (padraoEmails.novaTarefaDisponívelExecução in msg.subject) | (padraoEmails.tarefaPendente in msg.subject) | (padraoEmails.tarefaAtrasada in msg.subject) | (padraoEmails.tarefaAviso in msg.subject):
                #    PEGA A INFORMAÇÃO DE UMA SEÇÃO ESPECIFICA DO CODIGO HTML
                mailTxtHtml = soup.find('p', attrs={'class': 'mail_txt'})
                mailTxtFinal = mailTxtHtml.text
                if dados[nick] == "murilo.pereira@softex.br":
                    client.chat_postMessage(channel="@murilo.pereira", text=mailTxtFinal)
                #client.chat_postMessage(channel="@"+str(nick), text=mailTxtFinal)

    #   COLOCA A FLAG DE "UNSEEN" EM TODOS OS EMAILS LIDOS PARA AUXILIAR A LEITURA DOS PROXIMOS
    with meu_email as meu:
        meu.flag(meu.uids(dataAuxFormatada), MailMessageFlags.SEEN, False)
    print("terminou")

schedule.every(5).minutes.do(start)

while 1:
    schedule.run_pending()
    time.sleep(1)