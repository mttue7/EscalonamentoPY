import random

TAMANHO = 1000
CILINDRO = 5000

def acesso_processo(TAMANHO):
  return [random.randint(0, CILINDRO - 1) for _ in range (TAMANHO)]

def fcfs(acessos):
    posicao_atual = 0
    cilindros_percorridos = 0
    processos_restantes = list(acessos)  # Cria uma cópia da lista original

    for processo in processos_restantes:
        distancia = abs(processo - posicao_atual)
        cilindros_percorridos += distancia
        posicao_atual = processo

    return cilindros_percorridos

def scan(acessos, tamanho_fila):
    posicao_atual = 0
    cilindros_percorridos = 0
    processos_restantes = list(acessos)  # Cria uma cópia da lista original
    processos_restantes.sort()  # Ordena os processos em ordem crescente
    fila = processos_restantes[:tamanho_fila]  # Inicializa a fila com os primeiros elementos
    processos_restantes = processos_restantes[tamanho_fila:]  # Remove os elementos já na fila

    direcao = -1  # Iniciar em direção decrescente

    while fila:
        if direcao == -1:
            proximos_processos = [p for p in fila if p <= posicao_atual]
            if proximos_processos:
                distancia = abs(proximos_processos[-1] - posicao_atual)
                cilindros_percorridos += distancia
                posicao_atual = proximos_processos[-1]
                fila.remove(proximos_processos[-1])
                if processos_restantes:  # Se ainda há processos restantes
                    fila.append(processos_restantes.pop(0))  # Adiciona o próximo processo à fila
            else:
                direcao = 1  # Mudar para direção crescente
        else:
            proximos_processos = [p for p in fila if p >= posicao_atual]
            if proximos_processos:
                distancia = abs(proximos_processos[0] - posicao_atual)
                cilindros_percorridos += distancia
                posicao_atual = proximos_processos[0]
                fila.remove(proximos_processos[0])
                if processos_restantes:  # Se ainda há processos restantes
                    fila.append(processos_restantes.pop(0))  # Adiciona o próximo processo à fila
            else:
                direcao = -1  # Mudar para direção decrescente

    return cilindros_percorridos

# Lista de tamanhos de fila desejados
lista_tamanho = [10, 20, 50, 100, 200, 500, 1000]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(TAMANHO)

for tamanho in lista_tamanho:
    # Resultados para o FCFS
    resultado_fcfs = fcfs(sequencia_acessos[:tamanho])

    # Resultados para o SCAN
    resultado_scan = scan(sequencia_acessos[:tamanho], lista_tamanho)

    # Imprimir os resultados para o tamanho de fila atual
    print(f"Tamanho da fila: {tamanho}")
    print(f"""FCFS: {resultado_fcfs}\nSCAN: {resultado_scan}\n""")
