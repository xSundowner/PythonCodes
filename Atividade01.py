notas = []
nome = str(input("Digite o nome do aluno: "))

def break01():
    print("------------------------------")

def calculo_nota():
    resultado = 0
    ind = len(notas)
    print(len(notas))
    for i in notas:
        resultado = resultado + notas[ind - 1]
    print(f"A média do aluno {nome} é de {resultado/len(notas)}")
    if resultado/len(notas) >= 6:
        print("APROVADO\n")
        break01()
    else:
        print("REPROVADO\n")
        break01()


def adição_nota():
    escolha = 1
    while escolha == 1:
        numero = int(input(f"Digite a {len(notas)+1}° nota = "))
        notas.append(numero)
        while True:
            escolha = int(input("- Aperte 1 para adicionar mais uma nota\n- Aperte 0 para ver média\n"))
            if escolha == 0:
                calculo_nota()
            elif escolha == 1:
                adição_nota()
            elif escolha != 1 and escolha != 0:
                print("\nDIGITE UM NÚMERO VÁLIDO\n")

adição_nota()



