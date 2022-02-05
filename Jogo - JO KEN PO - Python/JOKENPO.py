from random import choice #Importação para função de sortear 

computador_vitorias = 0 #Irá computar as vitórias da máquina
jogador_vitorias = 0 #Irá computar as vitórias do máquina

def hello(meu_nome): # Linhas 6 e 7 = Função de interação com o jogador
  print('Olá,',meu_nome,"! Seja bem vindo(a)!")

while True: # Início da estrutura com o laço de repetição WHILE

    print("--------------------------------------------------------") #Divisão para melhor visualização
    print("                       JO KEN PO!                       ")
    print("--------------------------------------------------------") #Divisão para melhor visualização

    meu_nome = input("Jogador(a), insira seu nome: ") #Variável que recebe informação do nome do jogador

    hello(meu_nome) #Chamando a função da linha 6

    esc_jogador = (input(f"Escolha Pedra, Papel ou Tesoura: ")).upper() #Chamada para jogador inserir sua jogada e comando "upper" para padronizar a resposta
    Opcao_jogador = esc_jogador #Variável que recebe o produto de outra 

    esc_computador = choice(["PEDRA","PAPEL","TESOURA"]) #Computador sorteando sua jogada com comando "choice"
    Opcao_computador = esc_computador #Variável que recebe o produto de outra 
    
    print("--------------------------------------------------------") #Divisão para melhor visualização

    if(esc_jogador == "PAPEL") and (esc_computador == "PEDRA"): # Linhas 27:29 = condição if para resultado positivo para o jogador e contagem de vitória
        print(f"O jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}! \nResultado: Você ganhou!")
        jogador_vitorias +=1
    elif (esc_jogador == "PEDRA") and (esc_computador == "TESOURA"): # Linhas 30:32 = condição elif para resultado positivo para o jogador e contagem de vitória
        print(f"O jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}! \nResultado: Você ganhou!")
        jogador_vitorias +=1
    elif (esc_jogador == "TESOURA") and (esc_computador == "PAPEL"): # Linhas 33:35 = condição elif para resultado positivo para o jogador e contagem de vitória 
        print(f"O jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}! \nResultado: Você ganhou!")
        jogador_vitorias +=1

    elif esc_jogador == esc_computador: # Linhas 37:38 = condição elif para resultado de empate para os participantes
        print(f"O jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}! \nResultado: Houve um empate!")

    else: # Linhas 40:42 = condição else para resultado positivo para a máquina e contagem de vitória 
        print(f"O jogador escolheu {esc_jogador} e a máquina escolheu {esc_computador}! \nResultado: A máquina ganhou!")
        computador_vitorias +=1
    
    print("--------------------------------------------------------") #Divisão para melhor visualização
    print(f"Vitórias de {meu_nome}: {jogador_vitorias}") #Contagem total de vitórias do jogador X
    print(f"Vitórias da máquina: {computador_vitorias}") #Contagem total de vitórias da máquina
    print("--------------------------------------------------------") #Divisão para melhor visualização

    esc_jogador = (input("Você quer jogar novamente? Sim/Nao ")).upper() #Pergunta para continuar o laço de repetição ou não e comando "upper" para padronizar a resposta
    if esc_jogador == "SIM": #Linhas 50:51 = Caso escrever "SIM" o jogo se repetirá
        pass
    elif esc_jogador == "NAO": #Linhas 52:54 = Caso escrever "NAO" o jogo acabará
        print("Fim do jogo")
        break
    else: #Linhas 55:57 = Caso a resposta for diferente, o jogo acabará
        print("Fim do jogo")
        break