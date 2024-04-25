import random
'''
          ~~ Componentes do Grupo: ~~
----------------------------------------------------
|  Augusto Guaschi Morato        |   RA: 22008248  |
|  Daniel Scanavini Rossi        |   RA: 22000787  |
|  Lucas Magaldi                 |   RA: 22004139  |
|  Lucas Valerio Berti           |   RA: 22007440  |
|  Mattheus Gonçalves Anitelli   |   RA: 22011982  |
|  Vinicius Henrique Galassi     |   RA: 22005768  |
----------------------------------------------------

-> Saídas: 

Tamanho da fila: 10
FCFS: 1682821
SCAN: 334489
CSCAN: (249489, 494489) -> Cilindro virtual / Cilindro Fisico
===============================================================

Tamanho da fila: 20
FCFS: 1682821
SCAN: 169724
CSCAN: (125276, 250276) -> Cilindro virtual / Cilindro Fisico
===============================================================

Tamanho da fila: 50
FCFS: 1682821
SCAN: 69999
CSCAN: (52899, 102899) -> Cilindro virtual / Cilindro Fisico
===============================================================

Tamanho da fila: 100
FCFS: 1682821
SCAN: 34951
CSCAN: (27923, 52923) -> Cilindro virtual / Cilindro Fisico
===============================================================

Tamanho da fila: 200
FCFS: 1682821
SCAN: 19995
CSCAN: (15647, 30647) -> Cilindro virtual / Cilindro Fisico
===============================================================

Tamanho da fila: 500
FCFS: 1682821
SCAN: 9994
CSCAN: (8140, 13140) -> Cilindro virtual / Cilindro Fisico
===============================================================

Tamanho da fila: 1000
FCFS: 1682821
SCAN: 4999
CSCAN: (4999, 4999) -> Cilindro virtual / Cilindro Fisico
===============================================================

-> Perguntas e respostas:

comente textualmente o que você observou sobre o comportamento dos algoritmos de 
escalonamento de acordo com o tamanho da fila: que algoritmo(s) é(são) 
melhor(es) em que situação(ões) e por quê?

Resposta: 

FCFS (First-Come, First-Served): Este algoritmo apresenta o mesmo valor para todos os tamanhos de fila. 
Isso indica que o FCFS não é afetado pelo tamanho da fila, pois atende às solicitações na ordem 
em que chegam, independentemente de sua localização no disco.

SCAN (Elevator Algorithm): O tempo de SCAN diminui à medida que o tamanho da fila 
aumenta, indicando uma otimização ao evitar longas viagens entre cilindros. 
SCAN se beneficia de uma maior quantidade de pedidos, oferecendo tempos 
de acesso menores, especialmente em filas maiores

C-SCAN (Circular SCAN): Assim como o SCAN, o C-SCAN também mostra uma tendência de diminuição dos valores 
à medida que o tamanho da fila aumenta. No entanto, o C-SCAN trata o disco como um cilindro circular e, 
após atingir o final, retorna ao início - no caso do braço físico, ele soma 5000 nessa volta devido passar
por todos os elementos que variam de 0 a 4999. CSCAN evita a "starvation" de pedidos, fornecendo 
tempos de acesso mais consistentes e previsíveis, especialmente em filas maiores.

Interessante notar que no ultimo tamanho, que seria de 1000 entradas (o vetor acesso inteiro),
tanto o SCAN quanto o C-SCAN (seja o lógico ou o físico) possuem o mesmo valor de saída.
Isso ocorre devido que a validação dos elementos ocorre apenas em um sentido, 
sem ter a necessidade de retornar ao 0 (no caso do C-SCAN) e nem de mudar a direção do braço 
(no caso do SCAN) ja que o tamanho do subvetor é o mesmo do vetor original

Conclusão: A escolha do melhor algoritmo depende do contexto e das necessidades do sistema.

FCFS é ideal quando a ordem de chegada é o único critério importante.
SCAN é eficiente em filas maiores para otimizar o movimento do braço do disco.
CSCAN é preferível em sistemas com distribuição desigual de pedidos, evitando a 
inanição e oferecendo tempos de acesso mais consistentes

'''
TAMANHO = 1000
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
    posicao_atual = 0
    ValorEscalonado = 0
    cilindrosPercorridos = 0
    qntdFila = acessos[:taman_fila]
    sentido = 1
    

    for j in range(TAMANHO): 
        #Verificando em qual sentido está o escalonamento, irá escalonar o menor ou maior valor dependendo do sentido e da posição
        if(sentido == 1):
            ValorEscalonado = menorValorComp(qntdFila,posicao_atual)
        else:
            ValorEscalonado = maiorValorComp(qntdFila,posicao_atual)

        cilindrosPercorridos += abs(qntdFila[ValorEscalonado] - posicao_atual)
    
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
                sentido = -1
                cilindrosPercorridos += (CILINDRO -posicao_atual-1)
                posicao_atual = CILINDRO-1
                
            #Se escalonador estiver indo para esquerda e o menor elemento já estiver escalonado, troca de sentido
            elif(min(qntdFila)>posicao_atual and sentido == -1):
                sentido = 1
                cilindrosPercorridos +=posicao_atual
                posicao_atual = 0
            
 
    return cilindrosPercorridos



def cscan(acessos, taman_fila):
    posicao_atual = 0
    ValorEscalonado = 0
    cilindrosPercorridos = 0
    cilindroFisico = 0
    qntdFila = acessos[:taman_fila]
    

    for j in range(TAMANHO): 
        #Irá escalonar o menor valor do vetor que estiver acima da posição
        ValorEscalonado = menorValorComp(qntdFila,posicao_atual)
        cilindrosPercorridos += (qntdFila[ValorEscalonado] - posicao_atual)
        cilindroFisico += (qntdFila[ValorEscalonado] - posicao_atual)
        
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
                cilindrosPercorridos += (CILINDRO - 1 - posicao_atual)
                cilindroFisico += (CILINDRO - 1 - posicao_atual)
                posicao_atual = 0
                cilindroFisico += CILINDRO-1
            
    return cilindrosPercorridos, cilindroFisico


# Lista de tamanhos de fila desejados
lista_tamanho = [10,20,50,100,200,500,1000]

# Gerar sequência aleatória de acessos
sequencia_acessos = acesso_processo(TAMANHO)

for tamanho in lista_tamanho:
    # Resultados para o FCFS

    resultado_fcfs = fcfs(sequencia_acessos, tamanho)
    resultadoScan = scan(sequencia_acessos,tamanho)
    resultadoCscan = cscan(sequencia_acessos,tamanho)
    print(f"\nTamanho da fila: {tamanho}")
    print(f"FCFS: {resultado_fcfs}")
    print(f"SCAN: {resultadoScan}")
    print(f"CSCAN: {resultadoCscan} -> Cilindro virtual / Cilindro Fisico")

    print("===============================================================")


   