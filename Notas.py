import datetime

ano = datetime.date.today()
dados = ['',0]
notas = [0, 0, 0, 0]
x = 0

dados[0] = str(input('Digite nome do aluno: '))
dados[1] = int(input('Digite o ano de nascimento: '))

while x < len(notas):
    notas[x] = float(input(f'Digite a {x + 1}º nota: '))
    x += 1

total = notas[0] + notas[1] + notas[2] + notas[3]
print(f'\nAluno: {dados[0]}\n'
      f'Idade: {ano.year - dados[1]}\n'
      f'Média: {total/4}')

if total/4 < 6:
    print("//REPROVADO")
else:
    print('//APROVADO')