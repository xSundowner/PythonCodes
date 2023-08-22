historico =[]
valores = [0,0,0]
operação = ''
escolha = 1
def conta():
    valores[0] = int(input("\nDigite o primeiro valor: "))
    operação = str(input('Digite a operação que deseja fazer\n'
                         'x, -, +, : ')).lower()
    if operação == 'x':
        valores[1] = int(input("Digite o segundo valor: "))
        valores[2] = valores[0]*valores[1]
        historico.append(f'{valores[0]} x {valores[1]} = {valores[2]}')
        print(f'O resultado da operação {valores[0]} x {valores[1]} é {valores[2]}')
        escolha = int(input("\n- Aperte 1 para fazer outra conta\n"
                            "- Aperte 2 para conferir o histórico de operações\n"
                            "- Aperte 3 ou outro número para sair\n"))
        if escolha == 1:
            conta()
        elif escolha == 2:
            historico_de_operações()
        else:
            fim()

    elif operação == '-':
        valores[1] = int(input("Digite o segundo valor: "))
        valores[2] = valores[0]-valores[1]
        historico.append(f'{valores[0]} - {valores[1]} = {valores[2]}')
        print(f'O resultado da operação {valores[0]} - {valores[1]} é {valores[2]}')
        escolha = int(input("\n- Aperte 1 para fazer outra conta\n"
                            "- Aperte 2 para conferir o histórico de operações\n"
                            "- Aperte 3 para sair ou outro número para sair\n"))
        if escolha == 1:
            conta()
        elif escolha == 2:
            historico_de_operações()
        else:
            fim()

    elif operação == '+':
        valores[1] = int(input("Digite o segundo valor: "))
        valores[2] = valores[0]+valores[1]
        historico.append(f'{valores[0]} + {valores[1]} = {valores[2]}')
        print(f'O resultado da operação {valores[0]} + {valores[1]} é {valores[2]}')
        escolha = int(input("\n- Aperte 1 para fazer outra conta\n"
                            "- Aperte 2 para conferir o histórico de operações\n"
                            "- Aperte 3 para sair ou outro número para sair\n"))
        if escolha == 1:
            conta()
        elif escolha == 2:
            historico_de_operações()
        else:
            fim()

    else:
        print('Digite um operador válido')
        conta()
def historico_de_operações():
    x=1
    print("\n- HISTÓRICO DE OPERAÇÕES (últimos 10)")
    while len(historico)>10:
        del historico[0]
    for i in historico:
        print(f'[{x}] - {i}')
        x+=1
    escolha = int(input("\n- Aperte 1 para fazer outra conta\n"
                        "- Aperte 2 para conferir o histórico de operações\n"
                        "- Aperte 3 para sair ou outro número para sair\n"))
    if escolha == 1:
        conta()
    elif escolha == 2:
        historico_de_operações()
    else:
        fim()
def fim():
    print('-----------------------------------------------')
conta()