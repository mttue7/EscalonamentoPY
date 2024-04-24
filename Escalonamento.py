import random

TAMANHO = 1000
CILINDRO = 5000

def acesso_processo(TAMANHO):
    return [random.randint(0, CILINDRO - 1) for _ in range(TAMANHO)]

def fcfs(acessos, tamanho_fila):
    posicao_atual = 0
    cilindros_percorridos = 0
    qntd_Fila = acessos[:tamanho_fila]

    for i in range(len(acessos)):
        processo = qntd_Fila[0]  # Pega o primeiro elemento da fila
        distancia = abs(processo - posicao_atual)
        cilindros_percorridos += distancia
        posicao_atual = processo

        # Remover o primeiro elemento da fila
        qntd_Fila.pop(0)

        # Adicionar o próximo elemento dos acessos
        if i + tamanho_fila < len(acessos):
            qntd_Fila.append(acessos[i + tamanho_fila])

    return cilindros_percorridos
'''
def scan(acessos, taman_fila):
    posicao_atual = 0
    cilindros_percorridos = 0
    qntdFila = acessos[:taman_fila]
    print("qntdFila:", qntdFila)

    for i in range(len(qntdFila) - 1):
        processos = qntdFila[i]
        prox_processos = qntdFila[i + 1]

       # print(f"Processo atual: {processos}, Próximo processo: {prox_processos}")
        subvetor = qntdFila[i + 1:]
        minimum = min(subvetor)

        if prox_processos > processos and prox_processos == minimum:

            distancia = prox_processos - posicao_atual
            cilindros_percorridos += distancia
            posicao_atual = prox_processos
            print(cilindros_percorridos)
    
        else:
            print("Condição não atendida. Continuando para o próximo processo.")
         #   print(f"Subvetor: {subvetor}")

            continue

    return cilindros_percorridos
'''
# Lista de tamanhos de fila desejados
lista_tamanho = [10,20,50,100,200,500,1000]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(TAMANHO)

for tamanho in lista_tamanho:
    # Resultados para o FCFS
    print(f"Tamanho da fila: {tamanho}")
    resultado_fcfs = fcfs(sequencia_acessos, tamanho)
    print(f"FCFS: {resultado_fcfs}\n")
    #print(f"SCAN: {resultado_scan}\n")

   # Resultados para o SCAN
  #  resultado_scan = scan(sequencia_acessos, tamanho)

    # Imprimir os resultados para o tamanho de fila atual
   