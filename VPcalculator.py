nc475,nc1200,nc2300,nc4400,nc5500,nc11500,mon,total = 0, 0, 0, 0, 0, 0, 0, 0 #Variáveis

def conta_user(): #Permite a entrada de dados do usuário
    print('Calculadora de Valorant Point\n- - - - - - - - - - -')
    atual = int(input("Digite quantos VP você possui atualmente:"))
    nc = int(input("- - - - - - - - - - -\nDigite quanto é o pacote ou skin que deseja em VP:"))
    total = nc - atual

    calculo_dinheiro()
    pacotes()
    print('Você gastará um total de', mon, 'R$ e sobrará', total * -1,
          'VP\nNão se esqueça que a melhor forma de economizar é não comprando :3')

def calculo_dinheiro(): #Compara o valor da variável total e adiciona à variável mon
    global nc475, nc1200, nc2300, nc4400, nc5500, nc11500, mon, total
    while total>=11500:
        nc11500 = nc11500 + 1
        total = total - 11500
        mon = mon + 349.90
    while total>=5500:
        nc5500 = nc5500 + 1
        total = total - 5500
        mon = mon + 169.90
    while total>=4400:
        nc4400 = nc4400 + 1
        total = total - 4400
        mon = mon + 139.90
    while total>=2300:
        nc2300 = nc2300 + 1
        total = total - 2300
        mon = mon + 74.90
    while total>=1200:
        nc1200 = nc1200 + 1
        total = total - 1200
        mon = mon + 39.90
    while total>=475 or total>=1:
        nc475 = nc475 + 1
        total = total - 475
        mon = mon + 16.90

        print('- - - - - - - - - - -')
        mon = round(mon, 2)  # Converte o resultado a apenas duas casa decimais após a virgula

def pacotes():#Soma a quantidade de pacotes necessários e os adiciona em suas respectivas variáveis
    if nc11500 >= 1:
        print('-',nc11500,"pacote de 11500 VP")
    if nc5500 >= 1:
        print('-',nc5500,"pacote de 5500 VP")
    if nc4400 >= 1:
        print('-',nc4400,"pacote de 4400 VP")
    if nc2300 >= 1:
        print('-',nc2300,"pacote de 2300 VP")
    if nc1200 >= 1:
        print('-',nc1200,"pacote de 1200 VP")
    if nc475 >= 1:
        print('-',nc475,"pacote de 475 VP")
    else:
        print("Não é necessário comprar nenhum pacote de VP")

conta_user() #inicia o código
