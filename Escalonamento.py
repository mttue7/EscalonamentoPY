import random

TAMANHO = 20
CILINDRO = 5000

def acesso_processo(TAMANHO):
    return [random.randint(0, CILINDRO - 1) for _ in range(TAMANHO)]


def menorValorComp(vetor,valorComparado):
    menorValor = 0
    while(vetor[menorValor]<valorComparado):   
        menorValor += 1
        
    for i in range(menorValor,len(vetor)):
        if(vetor[i]<=vetor[menorValor] and vetor[i] >= valorComparado):
            menorValor = i
    return menorValor


def maiorValorComp(vetor,valorComparado):
    maiorValor = 0
    while(vetor[maiorValor]>valorComparado):
        maiorValor += 1
    
    for i in range(maiorValor,len(vetor)):
            if(vetor[i]<=valorComparado and vetor[i]>=vetor[maiorValor]):
                maiorValor = i
                
    return maiorValor



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

def scan(acessos, taman_fila):
    print(acessos)
    posicao_atual = 0
    ValorEscalonado = 0
    cilindrosPercorridos = 0
    qntdFila = acessos[:taman_fila]
    print("qntdFila:", qntdFila)
    sentido = 1
    

    for j in range(TAMANHO): 
        #Verificando em qual sentido está o escalonamento, irá escalonar o menor ou maior valor dependendo do sentido e da posição
        if(sentido == 1):
            ValorEscalonado = menorValorComp(qntdFila,posicao_atual)
        else:
            ValorEscalonado = maiorValorComp(qntdFila,posicao_atual)

        cilindrosPercorridos += abs(qntdFila[ValorEscalonado] - posicao_atual)
    


        print("Esse é o vetor",qntdFila)
        print("O valor escalonado é",qntdFila[ValorEscalonado],"e sua posição atual é",posicao_atual )
        print(cilindrosPercorridos)
        posicao_atual = qntdFila[ValorEscalonado]
        
        #Se o vetor de acessos ainda estiver com requisições, substitui o valor escalonado pelo novo valor
        if((TAMANHO - taman_fila)>j):
           qntdFila[ValorEscalonado] = acessos[j]
        else:
            #Se não estiver com requisições, remove o valor escalonado
            qntdFila.pop(ValorEscalonado)
        
        #Irá ocorrer se vetor de escalonamento não estiver vazio
        if qntdFila:
            #Se o escalonador estiver indo para a direita e o maior elemento já estiver escalonado, troca de sentido
            if(max(qntdFila)<posicao_atual and sentido == 1):
                print(max(qntdFila))
                sentido = -1
                cilindrosPercorridos += (TAMANHO -posicao_atual)
                posicao_atual = CILINDRO
                print("o sentido agora é para esquerda")
                print(posicao_atual)
            #Se escalonador escalonador estiver indo para esquerda e o menor elemento já estiver escalonado, troca de sentido
            elif(min(qntdFila)>posicao_atual and sentido == -1):
                sentido = 1
                cilindrosPercorridos +=posicao_atual
                print("o sentido agora é para direita")
                posicao_atual = 0
            
 

    return cilindrosPercorridos



def cscan(acessos, taman_fila):
    print(acessos)
    posicao_atual = 0
    ValorEscalonado = 0
    cilindrosPercorridos = 0
    cilindroFisico = 0
    qntdFila = acessos[:taman_fila]
    print("qntdFila:", qntdFila)
    

    for j in range(TAMANHO): 
        #Irá escalonar o menor valor do vetor que estiver acima da posição
        ValorEscalonado = menorValorComp(qntdFila,posicao_atual)
        cilindrosPercorridos += (qntdFila[ValorEscalonado] - posicao_atual)
        cilindroFisico += (qntdFila[ValorEscalonado] - posicao_atual)
        print(cilindrosPercorridos)
        

        print("Esse é o vetor",qntdFila)
        print("O valor escalonado é",qntdFila[ValorEscalonado],"e sua posição atual é",posicao_atual )
        posicao_atual = qntdFila[ValorEscalonado]
        
         #Se o vetor de acessos ainda estiver com requisições, substitui o valor escalonado pelo novo valor
        if((TAMANHO - taman_fila)>j):
           qntdFila[ValorEscalonado] = acessos[j]
        else:
             #Se não estiver com requisições, remove o valor escalonado
            qntdFila.pop(ValorEscalonado)
         #Irá ocorrer se vetor de escalonamento não estiver vazio
        if qntdFila:
            #Verificando se o maior valor já foi escalonado
            if(max(qntdFila)<posicao_atual):
                #Volta o escalonador para 0 e adiciona o movimento fisico
                posicao_atual = 0
                cilindroFisico += CILINDRO
            
 

    return cilindrosPercorridos


# Lista de tamanhos de fila desejados
lista_tamanho = [10,20,50]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(TAMANHO)

for tamanho in lista_tamanho:
    # Resultados para o FCFS

    resultado_fcfs = fcfs(sequencia_acessos, tamanho)
    resultadoScan = scan(sequencia_acessos,tamanho)
    resultadoCscan = cscan(sequencia_acessos,tamanho)
    print(f"Tamanho da fila: {tamanho}")
    print(f"FCFS: {resultado_fcfs}\n")
    print(f"SCAN: {resultadoScan}\n")
    print(f"CSCAN: {resultadoCscan}\n")


   