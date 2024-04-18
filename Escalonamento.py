import random

TAMANHO = 1000
CILINDRO = 5000

def acesso_processo(TAMANHO):
  return [random.randint(0, CILINDRO - 1) for _ in range (TAMANHO)]

def fcfs(acesso_processo):
    posicao_atual = 0
    cilindros_percorridos = 0
    processos_restantes = list(acesso_processo)  # Cria uma cópia da lista original

    for processo in processos_restantes:
        distancia = abs(processo - posicao_atual)
        cilindros_percorridos += distancia
        posicao_atual = processo

    return cilindros_percorridos

def scan(acesso_processo):
    posicao_atual1 = 0
    cilindros_percorridos1 = 0
    processos_restantes = list(acesso_processo)  # Cria uma cópia da lista original
    processos_restantes.sort()  # Ordena os processos em ordem crescente
    
    direcao = -1  # Iniciar em direção decrescente

    while processos_restantes:
        if direcao == -1:
            proximos_processos = [p for p in processos_restantes if p <= posicao_atual1]
            if proximos_processos:
                distancia1 = abs(proximos_processos[-1] - posicao_atual1)
                cilindros_percorridos1 += distancia1
                posicao_atual1 = proximos_processos[-1]
                processos_restantes.remove(proximos_processos[-1])
            else:
                direcao = 1  # Mudar para direção crescente
        else:
            proximos_processos = [p for p in processos_restantes if p >= posicao_atual1]
            if proximos_processos:
                distancia1 = abs(proximos_processos[0] - posicao_atual1)
                cilindros_percorridos1 += distancia1
                posicao_atual1 = proximos_processos[0]
                processos_restantes.remove(proximos_processos[0])
            else:
                direcao = -1  # Mudar para direção decrescente

    return cilindros_percorridos1


'''
def c_scan(acesso_processo):
  return
'''
  
# Lista de tamanhos de fila desejados
lista_tamanho = [10, 20, 50, 100, 200, 500, 1000]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(1000)

for tamanho in lista_tamanho:
    # Resultados para o FCFS
    resultado_fcfs = fcfs(acesso_processo,tamanho)

    # Resultados para o SCAN
    resultado_scan = scan(sequencia_acessos[:tamanho])

    # Resultados para o C-SCAN
   # resultado_cscan = c_scan(sequencia_acessos[:tamanho])

    # Imprimir os resultados para o tamanho de fila atual
    print(f"Tamanho da fila: {tamanho}")
    print(f"""FCFS: {resultado_fcfs}\nSCAN: {resultado_scan}\n""")
           