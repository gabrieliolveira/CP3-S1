# Uma escola está testando um sistema simples de monitoramento ambiental para identificar salas com possível risco de calor excessivo.
# Você recebeu uma matriz em que cada linha representa uma sala e cada coluna representa a temperatura registrada em um horário diferente do dia.
# temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
# Crie um programa em Python que:
#
#  Percorra toda a matriz de temperaturas.
#  Calcule a média de temperatura de cada sala.
#  Identifique quantas vezes cada sala registrou temperatura maior ou igual a 33.
#  Mostre, para cada sala:

#  número da sala;
#  média das temperaturas;
#  quantidade de registros críticos.

#  Ao final, informe qual sala teve a maior quantidade de registros críticos.
# EX.:
# Sala 1
# Média: 31.5
# Registros críticos: 2

salas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]

cont = 0
for sala in salas:
    cont += 1
    cont_critico = 0
    print(sala)
    print(f'Sala:  {cont}')
    print(f'Média: {sum(sala)/len(sala)}')
    for temperatura in sala:
        if temperatura >=33:
            cont_critico+=1
    print(f'Registros críticos:  {cont_critico}\n')
