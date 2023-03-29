#programa do IVCF-20 de código simples para eventual upgrade
separador = ('-=' * 34)
print(separador)
print('IVCF-20 - CAIXA DE ASSISTÊNCIA AOS FUNCIONÁRIOS DO BANCO DO BRASIL')
print(separador)
print('''Plena Idade - Instrumento de avaliação do Índice de Vulnerabilidade 
Clínico-Funcional-20 (IVCF-20) - CASSI Copacabana''')
print(separador)
print('''Bem-vindo! As respostas devem ser confirmadas por alguém que conviva
com o paciente. Nos idosos incapazes de responder, utilizar as 
respostas do cuidador.''')
print(separador)
dadosptcp = dict()
pontos = 0
while True:
  dadosptcp['nome'] = str(input('Nome do Participante: '))
  dadosptcp['idade'] = int(input('Idade do Participante: '))
  if 75 < dadosptcp['idade'] < 84:
    pontos += 1
  elif dadosptcp['idade'] >= 85:
    pontos += 3
  
  dadosptcp['2'] = int(input('''2-Em geral, comparando com outras pessoas de sua idade, você
  diria que sua saúde é:
  [1] Excelente, muito boa ou boa
  [2] Regular ou ruim
  R: '''))
  if dadosptcp['2'] == 2:
    pontos += 1
  
  print(separador)
  print('AVD - Atividades de Vida Diária')
  print('''Respostas positivas valem 4 pontos cada. Todavia, a pontuação máxima
  do item é de 4 pontos, mesmo que o participante tenha respondido sim para
  todas as questões 3, 4 e 5.''')
  print(separador)
  dadosptcp['3'] = int(input('''3-Por causa de sua saúde ou condição física,
  você deixou de fazer compras?
  [1] Sim
  [2] Não, ou não faz compras por outros motivos que não sejam saúde
  R: '''))
  
  dadosptcp['4'] = int(input('''4-Por causa de sua saúde ou condição física,
  você deixou de controlar seu dinheiro, gastos ou pagar as contas de sua casa?
  [1] Sim
  [2] Não, ou não controla o dinheiro por outros motivos que não sejam saúde
  R: '''))
  
  dadosptcp['5'] = int(input('''5-Por causa de sua saúde ou condição física,
  você deixou de realizar pequenos trabalhos domésticos, como lavar a louça,
  arrumar a casa ou fazer limpeza leve?
  [1] Sim
  [2] Não, ou não faz mais pequenos trabalhos domésticos por outros motivos
  que não sejam saúde
  R: '''))
  if dadosptcp['3' or '4' or '5'] == 1:
    pontos += 4

  dadosptcp['6'] = int(input('''6-Por causa de sua saúde ou condição física, você
  deixou de tomar banho sozinho?
  [1] Sim
  [2] Não
  R: '''))
  if dadosptcp['6'] == 1:
    pontos += 6
  
  print(separador)
  print('Cognição')
  print(separador)
  dadosptcp['7'] = int(input('''7-Algum familiar ou amigo falou que você está ficando esquecido?
  [1] Sim
  [2] Não
  R: '''))
  if dadosptcp['7'] == 1:
    pontos += 1
    dadosptcp['8'] = int(input('''8-Este esquecimento está piorando nos últimos meses?
    [1] Sim
    [2] Não
    R: '''))
    if dadosptcp['8'] == 1:
      pontos += 1
    
    dadosptcp['9'] = int(input('''9-Este esquecimento está impedindo a realização de alguma
    atividade do cotidiano?
    [1] Sim
    [2] Não
    R: '''))
    if dadosptcp['9'] == 1:
      pontos += 1

  print(separador)
  print('Humor')
  print(separador)
  dadosptcp['10'] = int(input('''10-No último mês você ficou com desânimo, tristeza ou desesperança?
  [1] Sim
  [2] Não
  R: '''))
  if dadosptcp['10'] == 1:
    pontos += 1

  dadosptcp['11'] = int(input('''11-No último mês você perdeu o interesse ou prazer em atividades
  anteriormente prazerosas?
  [1] Sim
  [2] Não
  R: '''))
  if dadosptcp['11'] == 1:
    pontos += 1

  print(separador)
  print('Mobilidade')
  print(separador)
  print('Alcance, preensão e pinça')
  dadosptcp['12'] = int(input('''12-Você é incapaz de elevar os braços acima do nível do ombro?
  [1] Sim
  [2] Não
  R: '''))
  if dadosptcp['12'] == 1:
    pontos += 1
  
  dadosptcp['13'] = int(input('''13-Você é incapaz de manusear ou segurar pequenos objetos?
  [1] Sim
  [2] Não
  R: '''))
  if dadosptcp['13'] == 1:
    pontos += 1
  print(separador)

  print('Capacidade aeróbica e/ou muscular')
  print(' ')
  print(pontos)
  print(dadosptcp)