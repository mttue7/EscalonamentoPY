import random

TAMANHO = 1000
CILINDRO = 5000

def acesso_processo(TAMANHO):
    return [random.randint(0, CILINDRO - 1) for _ in range(TAMANHO)]

def fcfs(acessos, taman_fila):
    posicao_atual = 0
    cilindros_percorridos = 0
    qntdFila = acessos[:taman_fila]
    print("qntdFila:", qntdFila)

    for i in range(len(qntdFila) - 1):
        processos = qntdFila[i]
        prox_processos = qntdFila[i + 1]

        print(f"Processo atual: {processos}, Próximo processo: {prox_processos}")
        
        
        if prox_processos > processos:
            subvetor = qntdFila[i + 1:]
            print(f"Subvetor: {subvetor}")
            minimum = min(subvetor)

            if prox_processos == minimum:
                distancia = prox_processos - posicao_atual
                cilindros_percorridos += distancia
                posicao_atual = processos
                print(cilindros_percorridos)
            else:
                print("Próximo processo não é o menor. Continuando para o próximo processo.")
                continue
        else:
            print("Condição não atendida. Continuando para o próximo processo.")

            continue

    return cilindros_percorridos

'''
def scan(acessos, tamanho_fila):
    posicao_atual = 0
    cilindros_percorridos = 0
    processos_restantes = list(acessos)  # Cria uma cópia da lista original
    fila = processos_restantes[:tamanho_fila]  # Inicializa a fila com os primeiros elementos
    processos_restantes = processos_restantes[tamanho_fila:]  # Remove os elementos já na fila

    direcao = 1  # Iniciar em direção decrescente

    while fila:
        if direcao == 1:
            proximos_processos = [p for p in fila if p >= posicao_atual]
            if proximos_processos:
                distancia = abs(proximos_processos[0] - posicao_atual)
                cilindros_percorridos += distancia
                posicao_atual = proximos_processos[0]
                fila.remove(proximos_processos[0])
                if processos_restantes:  # Se ainda há processos restantes
                    fila.append(processos_restantes.pop(0))  # Adiciona o próximo processo à fila
            else:
                direcao = -1  # Mudar para direção crescente
        else:
            proximos_processos = [p for p in fila if p <= posicao_atual]
            if proximos_processos:
                distancia = abs(proximos_processos[-1] - posicao_atual)
                cilindros_percorridos += distancia
                posicao_atual = proximos_processos[-1]
                fila.remove(proximos_processos[-1])
                if processos_restantes:  # Se ainda há processos restantes
                    fila.append(processos_restantes.pop(0))  # Adiciona o próximo processo à fila
            else:
                direcao = -1  # Mudar para direção decrescente

    return cilindros_percorridos
'''
# Lista de tamanhos de fila desejados
lista_tamanho = [10]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(TAMANHO)

for tamanho in lista_tamanho:
    # Resultados para o FCFS
    resultado_fcfs = fcfs(sequencia_acessos, tamanho)
    print(f"Tamanho da fila: {tamanho}")
    print(f"FCFS: {resultado_fcfs}\n")
    #print(f"SCAN: {resultado_scan}\n")
'''
    # Resultados para o SCAN
    resultado_scan = scan(sequencia_acessos, tamanho)

    # Imprimir os resultados para o tamanho de fila atual
'''
   