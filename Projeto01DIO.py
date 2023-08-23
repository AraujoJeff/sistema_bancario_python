menu = '''
[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[0] FINALIZAR OPERAÇÃO 
Escolha uma opção: '''
saldo = 0
LIMITE_SAQUE = 3
limite = 500
extrato = ''
numero_saques = 0
while True:
    opcao = input(menu).strip()

    if opcao == '1':
        valor = float(input('Informe o valor a ser depositado: '.strip()))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito realizado: R${valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso!')
        else:
            print('Valor incorreto, não é possivel executar esta operação!')
    elif opcao == '2':
        valor_saque = float(input('Informe o valor de Saque: '.strip()))
        excedeu_saque = numero_saques >= LIMITE_SAQUE

        if valor_saque > saldo:
            print('Saldo insuficiente!')
        elif valor_saque > limite:
            print('Operação negada! O seu limite de saque é de R$ 500,00 por operação!')
        elif excedeu_saque:
            print('Operação negada! Número maximo de saques realizados!')

        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque realizado: R${valor_saque:.2f}\n"
            print(f'Saque de R$ {valor_saque:.2f} realizado com sucesso!')
        else:
            print('Operação negada, valor incorreto!')
    elif opcao == '3':
        print('{:=^40}'.format(' EXTRATO '))
        print(f'Saques realizados: {numero_saques}')
        print(f'Seu Saldo: R${saldo:.2f}')
        print(extrato)
        print('=' * 40)

    elif opcao == '0':
        print('Operação finalizada, até mais!')
        break
    else:
        print('Opção inválida, tente novamente!')








