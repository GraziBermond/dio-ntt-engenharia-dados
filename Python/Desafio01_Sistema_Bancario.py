global saldo
saldo = 0
global limite_saque_quantidade
limite_saque_quantidade = 1
global extrato_historico
extrato_historico = []

def deposito (valor_deposito):
    global saldo
    global extrato_historico
    if valor_deposito > 0 :
        saldo += valor_deposito
        extrato_historico.append("DEPÓSITO: R$ " + str(valor_deposito))
        print(f'''
            ###############   COMPROVANTE DE DEPÓSTO   ###############
                FOI DEPOSITADO O VALOR DE R$ {valor_deposito:.2f}
        ''')
    else:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                O VALOR DO DEPÓSITO É ABAIXO DO VALOR MÍNIMO PERMITIDO.
            ''')

def saque (valor_saque):
    global saldo
    global limite_saque_quantidade
    LIMITE_SAQUE_VALOR = 500
    
    if valor_saque <= LIMITE_SAQUE_VALOR and valor_saque <= saldo and limite_saque_quantidade <= 3 :
        saldo -= valor_saque
        limite_saque_quantidade += 1
        extrato_historico.append("SAQUE   : R$ " + str(valor_saque))
        print(f'''
            ################   COMPROVANTE DE SAQUE   ################
                FOI SACADO O VALOR DE R$ {valor_saque:.2f}
            ''')        
    elif limite_saque_quantidade > 3:
        print(f'''
            #################    MENSAGEM DE ALERTA   #################
                TRANSAÇÃO NÃO REALIZADA.
                A QUANTIDADE MÁXIMA DE SAQUES DIÁRIO JÁ FOI ATINGIDA.
                POR FAVOR, TENTE NOVAMENTE EM OUTRO DIA.
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
            print(f'''
            #######################   EXTRATO   #######################''')
            extrato_quantidade_transacoes = len(extrato_historico)
            if extrato_quantidade_transacoes == 0:
                 print(f'''                 Nenhuma transação realizada até o momento.''')
            else:
                i = 0
                while i < extrato_quantidade_transacoes:
                    print(f'''                 {extrato_historico[i]}''')
                    i += 1
            print(f'''
                ____________________________________________________
                SALDO ATUAL: R$ {saldo}''')

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