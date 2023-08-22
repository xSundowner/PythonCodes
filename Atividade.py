import datetime

def notas():
    aluno = str(input("Nome do aluno: "))
    notas = [0, 0, 0, 0]
    x = 0

    while x < len(notas):
        notas[x] = float(input(f'Digite a {x + 1}º nota: '))
        x += 1

    total = notas[0] + notas[1] + notas[2] + notas[3]
    print(f'A média do aluno {aluno} foi de {total / 4}')


def calculadora():
    num = [0, 0]
    x = 0

    while x < len(num):
        num[x] = int(input(f"Digite o {x + 1}º número: "))
        x += 1

    print(f"Os resultados das operações são:\n"
          f"{num[0]} + {num[1]} = {num[0] + num[1]}\n"
          f"{num[0]} - {num[1]} = {num[0] - num[1]}\n"
          f"{num[0]} / {num[1]} = {num[0] / num[1]:2.2f}\n"
          f"{num[0]} % {num[1]} = {num[0] % num[1]}\n"
          f"{num[0]} x {num[1]} = {num[0] * num[1]}")

def nascimento():
      ano = datetime.date.today()
      dados = ['',0]
      dados[0] = str(input('Digite seu nome: '))
      dados[1] = int(input('Digite seu ano de nascimento: '))

      print(f'Olá {dados[0]}\n'
            f'Sua idade é de {ano.year - dados[1]} anos')

print("\n- MÉDIA DO ALUNO")
notas()
print("\n- CALCULADORA")
calculadora()
print("\n- DATA DE NASCIMENTO")
nascimento()