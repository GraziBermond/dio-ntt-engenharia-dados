import datetime

global saldo
saldo = 0
global extrato_historico
extrato_historico = []
global HOJE
HOJE = datetime.date.today()
global limite_transacao_quantidade
limite_transacao_quantidade = 0      

def deposito (valor_deposito):
    global saldo
    global extrato_historico
    global limite_transacao_quantidade
    global HOJE
    data_transacao = datetime.datetime.now()
    comparativo_datas = data_transacao.date() == HOJE

    if comparativo_datas == True and limite_transacao_quantidade < 10 and valor_deposito > 0 :
        saldo += valor_deposito
        limite_transacao_quantidade += 1
        extrato_historico.append(data_transacao.strftime("%d/%m/%y %H:%M") + "     DEPÓSITO:     R$ " + str(valor_deposito))
        print(f'''
            ###############   COMPROVANTE DE DEPÓSTO   ###############
                FOI DEPOSITADO O VALOR DE R$ {valor_deposito:.2f}
        ''')
    elif limite_transacao_quantidade >= 10:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                O LIMITE DIÁRIO DE TRANSAÇÕES JÁ FOI ATINGIDO.
            ''')
    else:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                O VALOR DO DEPÓSITO É ABAIXO DO VALOR MÍNIMO PERMITIDO.
            ''')

def saque (valor_saque):
    global saldo
    global extrato_historico
    global limite_transacao_quantidade
    global HOJE
    data_transacao = datetime.datetime.now()
    comparativo_datas = data_transacao.date() == HOJE
    LIMITE_SAQUE_VALOR = 500
    
    if comparativo_datas == True and limite_transacao_quantidade < 10 and valor_saque <= LIMITE_SAQUE_VALOR and valor_saque <= saldo:
        saldo -= valor_saque
        limite_transacao_quantidade += 1
        data_e_hora = datetime.datetime.now()        
        extrato_historico.append(data_e_hora.strftime("%d/%m/%y %H:%M")  + "     SAQUE   :     R$ " + str(valor_saque))
        print(f'''
            ################   COMPROVANTE DE SAQUE   ################
                FOI SACADO O VALOR DE R$ {valor_saque:.2f}
            ''')        
    elif limite_transacao_quantidade >= 10:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                O LIMITE DIÁRIO DE TRANSAÇÕES JÁ FOI ATINGIDO.
            ''')
    elif valor_saque > LIMITE_SAQUE_VALOR:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                O VALOR DO SAQUE É MAIOR DO QUE O LIMITE DE R$ {LIMITE_SAQUE_VALOR}.
            ''')
    elif valor_saque > saldo:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                O VALOR DO SAQUE É MAIOR DO QUE O SALDO EM CONTA.
            ''')

def extrato ():
    print(f'''
            #######################   EXTRATO   ####################### 
                DATA E HORA        TRANSAÇÃO     VALOR
                ____________________________________________________  ''')
    extrato_quantidade_transacoes = len(extrato_historico)
    if extrato_quantidade_transacoes == 0:
         print(f'''                 NENHUMA TRANSAÇÃO REALIZADA ATÉ O MOMENTO.''')
    else:
        i = 0
        while i < extrato_quantidade_transacoes:
            print(f'''                 {extrato_historico[i]}''')
            i += 1
    print(f'''
                ____________________________________________________
                SALDO ATUAL:        R$ {saldo}''')

while True:
    opcao_menu = int(input('''
            ###################   MENU DE OPÇÕES   ###################
                SELECIONE UMA DAS OPÇÕES ABAIXO:
                    [1] - DEPÓSITO
                    [2] - SAQUE
                    [3] - EXTRATO
                    [4] - SAIR
                        
                DIGITE A OPÇÃO DESEJADA: '''))
    
    if opcao_menu == 1:
        deposito(float(input('''
                DIGITE O VALOR DO DEPÓSITO: ''')))
    elif opcao_menu == 2:    
        saque(float(input('''
                DIGITE O VALOR DO SAQUE: ''')))
    elif opcao_menu == 3:
        extrato ()
    elif opcao_menu == 4:
            print(f'''
            ################    ATENDIMENTO FINALIZADO   ################
                    AGRADECEMOS POR UTILIZAR OS NOSSOS SERVIÇOS
            ''')
            break
    else:
            print(f'''
            #################    MENSAGEM DE ALERTA   #################
                                    OPÇÃO INVÁLIDA.
            
            ''')