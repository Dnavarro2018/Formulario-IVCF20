from time import sleep
print('='*46)
print('Índice de Vulnerabilidade Clínico-Funcional-20')
print('='*46)
sleep(1)
print('''Responda às perguntas abaixo com a ajuda de um profissional de saúde.
Marque a opção mais apropriada para a sua condição de saúde atual. Todas as
respostas devem ser confirmadas pór alguém que conviva com o paciente.
Para idosos incapazes de responder, utilizar as respostas do cuidador.''')
sleep(1)
print('='*10)
print('IDADE')
print('='*10)
idade = int(input('1.Qual é a sua idade? '))
sumpontos = int(0)

#pontuador da idade
if 60 < idade <= 74:
    sumpontos = sumpontos + 0
elif 75 <= idade <= 84:
    sumpontos = sumpontos + 1
elif idade >= 85:
    sumpontos = sumpontos + 3
print('Sua pontuação atual é de {} pontos.'.format(sumpontos))
print(' ')
sleep(1)
#pontuador da AP da Saúde
print('='*30)
print('Auto-Percepção da Saúde')
print('='*30)
apsaude = int(input('''2.Em geral, comparando com outras pessoas de sua idade,
você diria que sua saúde é:
[ 1 ] Excelente, muito boa ou boa
[ 2 ] Regular ou ruim
Digite sua opção: '''))
if apsaude == 1:
    sumpontos = sumpontos + 0
elif apsaude == 2:
    sumpontos = sumpontos + 1
print('Sua pontuação atual é de {} pontos.'.format(sumpontos))
print(' ')
sleep(1)
#pontuador de atividade diária
print('='*30)
print('Atividades de Vida Diária')
print('='*30)
print('AVD Instrumental')
print('='*30)
print('''Respostas positivas valem 4 pontos por item.
todavia, a pontuação máxima do item é de 4 pontos, ainda
que o paciente tenha respondido 'sim' para as questões
3, 4 e 5.''')
print('='*30)
sleep(1)
#AVD Compras
avdcompras = int(input('''3.Por causa de sua saúde ou condição
física, você deixou de fazer compras?
 [ 1 ] Sim
 [ 2 ] Não
 [ 3 ] Não faz compras por motivos alheios à saúde
 Digite sua opção: '''))
if avdcompras == 1:
    sumpontos = sumpontos + 4
elif avdcompras == 2:
    sumpontos = sumpontos + 0
elif avdcompras == 3:
    sumpontos = sumpontos + 0
print('Sua pontuação atual é de {} pontos.'.format(sumpontos))
print(' ')
#AVD monetario
print('='*30)
avdmonetario = int(input('''4.Por causa de sua saúde ou condição
física, você deixou de controlar seu dinheiro, gastos ou pagar
as contas de sua casa?
[ 1 ] Sim
[ 2 ] Não
[ 3 ] Não controla finanças por motivos alheios à saúde
Digite sua opção: '''))
if avdmonetario == 1 and avdcompras == 1:
    sumpontos = sumpontos
elif avdmonetario == 1 and 2 <= avdcompras <= 3:
    sumpontos = sumpontos + 4
elif avdmonetario == 2 and avdcompras == 1: