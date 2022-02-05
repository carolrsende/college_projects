from random import choice #Importação para função de sortear 

especificacoes = {"Tipo de Jogo": "Quiz/Perguntas e Respostas","Quantidade de Questões": "10","Categoria de Perguntas": "Conhecimentos Gerais","Pontuação Necessária para Ganhar": "1000"} #Dicionário para guardar as especificações do jogo
regras = ('PARA GANHAR O JOGO, VOCÊ PRECISARÁ CONQUISTAR 1000 PONTOS!', 'O VALOR DE CADA PERGUNTA É SORTEADA PELA MÁQUINA!') #Tupla para guardar as regras, que não mudam
vitorias_jogador = 0 #Contador de vitórias do jogador
derrotas_jogador = 0 #Contador de derrotas do jogador
pontuacao = 0 #Irá computar os pontos do jogador
possibilidade_pontos = [100,200,300] #Lista com as possibilidades de pontuação

def hello(meu_nome): # Função de interação com o jogador
  print('Olá,',meu_nome,"! Seja bem vindo(a)!")

while True: # Início da estrutura com o laço de repetição WHILE

    print("--------------------------------------------------------") #Divisão para melhor visualização
    print("                       POINT QUIZ                       ")
    print("--------------------------------------------------------") #Divisão para melhor visualização

    meu_nome = input("Jogador(a), insira seu nome: ") #Variável que recebe informação do nome do jogador

    hello(meu_nome) #Chamando a função 
    print(regras) #Printando as regras
    especificacoes.items() #Mostrando as especificações do jogo
    
    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('1) Qual é a arte chamada de sétima arte?\n[1] O Cinema\n[2] A Música') #Questão
    valor_pontos1 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos1} pontos!') #Resultado do sorteio
    resposta1 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta1 == 1: #Início de condicional da resposta
        pontuacao += valor_pontos1 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta1 == 2: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos
    
    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('2) Quem descobriu a existência da gravidade?\n[1] Albert Einstein\n[2] Isaac Newton') #Questão
    valor_pontos2 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos2} pontos!') #Resultado do sorteio
    resposta2 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta2 == 2: #Início de condicional da resposta
        pontuacao += valor_pontos2 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta2 == 1: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('3) Quem é a única brasileira a ter sido indicada ao Oscar de Melhor Atriz?\n[1] Susana Vieira\n[2] Fernanda Montenegro') #Questão
    valor_pontos3 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos3} pontos!') #Resultado do sorteio
    resposta3 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta3 == 2: #Início de condicional da resposta
        pontuacao += valor_pontos3 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta3 == 1: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('4) Quais são as modalidades esportivas praticadas por um triatleta?\n[1] Natação, ciclismo e corrida\n[2] Natação, corrida e salto com vara') #Questão
    valor_pontos4 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos4} pontos!') #Resultado do sorteio
    resposta4 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta4 == 1: #Início de condicional da resposta
        pontuacao += valor_pontos4 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta4 == 2: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('5) Quem foi o primeiro presidente negro dos Estados Unidos?\n[1] Barack Obama\n[2] Martin Luther King Jr') #Questão
    valor_pontos5 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos5} pontos!') #Resultado do sorteio
    resposta5 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta5 == 1: #Início de condicional da resposta
        pontuacao += valor_pontos5 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta5 == 2: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('6) Qual elemento químico é representado pela sigla Ag na tabela periódica?\n[1] Astato\n[2] Prata') #Questão
    valor_pontos6 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos6} pontos!') #Resultado do sorteio
    resposta6 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta6 == 2: #Início de condicional da resposta
        pontuacao += valor_pontos6 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta6 == 1: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('7) Qual é o livro mais vendido do mundo, depois da Bíblia?\n[1] Romeu e Julieta\n[2] Dom Quixote') #Questão
    valor_pontos7 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos7} pontos!') #Resultado do sorteio
    resposta7 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta7 == 2: #Início de condicional da resposta
        pontuacao += valor_pontos7 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta7 == 1: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos
    
    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('8) Quem foi o primeiro brasileiro a conquistar um cinturão no UFC?\n[1] Junior Cigano\n[2] Murilo Bustamante') #Questão
    valor_pontos8 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos8} pontos!') #Resultado do sorteio
    resposta8 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta8 == 2: #Início de condicional da resposta
        pontuacao += valor_pontos8 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta8 == 1: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('9) Qual é o menor país do mundo?\n[1] Monaco\n[2] Vaticano') #Questão
    valor_pontos9 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos9} pontos!') #Resultado do sorteio
    resposta9 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta9 == 2: #Início de condicional da resposta
        pontuacao += valor_pontos9 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta9 == 1: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização

    print('10) Em que país está localizado o monumento pré-histórico feito de pedras conhecido como Stonehenge?\n[1] Inglaterra\n[2] Alemanha') #Questão
    valor_pontos10 = int(choice(possibilidade_pontos)) #Sorteio de valor da questão
    print(f'Essa pergunta vale {valor_pontos10} pontos!') #Resultado do sorteio
    resposta10 = int(input('Digite o número respectivo da resposta correta: ')) #Resposta do jogador
    if resposta10 == 1: #Início de condicional da resposta
        pontuacao += valor_pontos10 #Se acertar contabilizar os pontos da questão
        print(f'Sua resposta está correta!\nSua pontução atual é: {pontuacao}') #Resultado Positivo
    elif resposta10 == 2: # Se a resposta for a errada
        print(f'Sua resposta está errada!\nSua pontução atual é: {pontuacao}') #Resultado negativo sem computar pontos

    print("--------------------------------------------------------") #Divisão para melhor visualização
    print("                       RESULTADO                        ") 
    print("--------------------------------------------------------") #Divisão para melhor visualização

    if pontuacao >= 1000: #Condicional caso o jogador tenha acumulado a quantidade necessária de pontos para ganhar
        vitorias_jogador +=1 #Adicionar uma vitória ao contador
        print(f"Parabéns, você ganhou!\nPontuação de {meu_nome}: {pontuacao}!") #Mensagem de vitória e total de pontos
        print(f'Vitórias:{vitorias_jogador}') #Print da quantidade de vitórias
        print(f'Derrotas:{derrotas_jogador}') #Print da quantidade de derrotas
        esc_jogador = (input("Você quer jogar novamente? Sim/Nao ")).upper() #Pergunta para continuar o laço de repetição ou não e comando "upper" para padronizar a resposta
        if esc_jogador == "SIM": #Caso escrever "SIM" o jogo se repetirá
            pontuacao = 0 #Pontuação será zerada
            pass #Volta pro inicio
        elif esc_jogador == "NAO": #Caso escrever "NAO" o jogo acabará
            print("Fim do jogo") #Mensagem de fim do jogo
            break #parar o jogo
        else: #Caso a resposta for diferente, o jogo acabará
            print("Fim do jogo") #Mensagem de fim do jogo
            break #parar o jogo
    else: #Condicional caso o jogador não tenha acumulado a quantidade necessária de pontos para ganhar
        derrotas_jogador +=1 #Adicionar uma derrota ao contador
        print(f"Infelizmente você perdeu!\nPontuação de {meu_nome}: {pontuacao}!") #Mensagem de derrota e total de pontos
        print(f'Vitórias:{vitorias_jogador}') #Print da quantidade de vitórias
        print(f'Derrotas:{derrotas_jogador}') #Print da quantidade de derrotas
        esc_jogador = (input("Você quer jogar novamente? Sim/Nao ")).upper() #Pergunta para continuar o laço de repetição ou não e comando "upper" para padronizar a resposta
        if esc_jogador == "SIM": #Caso escrever "SIM" o jogo se repetirá
            pontuacao = 0 #Pontuação será zerada
            pass #Volta pro inicio
        elif esc_jogador == "NAO": #Caso escrever "NAO" o jogo acabará
            print("Fim do jogo") #Mensagem de fim do jogo
            break #parar o jogo
        else: #Caso a resposta for diferente, o jogo acabará
            print("Fim do jogo") #Mensagem de fim do jogo
            break #parar o jogo