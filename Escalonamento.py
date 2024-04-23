import random

TAMANHO = 20
CILINDRO = 5000

def acesso_processo(TAMANHO):
    return [random.randint(0, CILINDRO - 1) for _ in range(TAMANHO)]

def scan(acessos, taman_fila):
    print(acessos)
    posicao_atual = 0
    menor_numero = 0
    cilindros_percorridos = 0
    qntdFila = acessos[:taman_fila]
    print("qntdFila:", qntdFila)
    

    for j in range(taman_fila,TAMANHO-1): 
        for i in range(len(qntdFila) - 1):
            qntdFila[i]

            if(qntdFila[i]>posicao_atual and qntdFila[i]<qntdFila[menor_numero]):
                menor_numero = i

        print("Esse é o vetor",qntdFila)
        print("O menor numero é",qntdFila[menor_numero],"e sua posição atual é",posicao_atual )
        posicao_atual = qntdFila[menor_numero]
        cilindros_percorridos += qntdFila[menor_numero]
        qntdFila[menor_numero] = acessos[j]
        menor_numero = 0
 

     
        

    return cilindros_percorridos


# Lista de tamanhos de fila desejados
lista_tamanho = [10]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(TAMANHO)

for tamanho in lista_tamanho:
    # Resultados para o FCFS
    resultado_fcfs = scan(sequencia_acessos, tamanho)
    print(f"Tamanho da fila: {tamanho}")
    print(f"FCFS: {resultado_fcfs}\n")
    #print(f"SCAN: {resultado_scan}\n")
'''
    # Resultados para o SCAN
    resultado_scan = scan(sequencia_acessos, tamanho)

    # Imprimir os resultados para o tamanho de fila atual
'''
   