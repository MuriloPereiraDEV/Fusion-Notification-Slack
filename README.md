# Fusion-Notification-Slack

Objetivo: Notificar colaboladores de empresas via Slack que utilizam a ferramenta Fusion Platform que possuem atividades novas ou pendentes.

Tecnologias: Python.

Processo: A aplicação entrará em uma caixa de e-mail nos enviados(e-mail que é usado somente para disparos automaticos do Fusion Platform) e lerá todos os e-mail enviados,
pegando o título, as informações do corpo textual e o remetente. Com essas informações ele usará a API do aplicativo Slack para poder comunicar todos os colaboradores que
receberam os e-mails. Esta aplicação sem o objetivo de notificar de maneira mais rapida os funcionarios com a intenção de nao deixar perder prasos já que e-mail são
mais dificeis de serem acessados pelos colaboradores.
