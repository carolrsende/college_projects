resp = True
saida = input('Deseja calcular a area da casa? (S/N)')
if saida.upper() == 'N' :
    resp = False
while resp :
    nome_comodo = input('Informe o nome do cômodo: ')
    largura = float(input(f'Informa a largura do cômodo {nome_comodo}: '))
    comprimento = float(input(f'Informa o comprimento do cômodo {nome_comodo}: '))
    area = largura * comprimento
    print(f'A area do comodo {nome_comodo} é {area}m²!')
    saida = input('Deseja calcular a area de mais algum cômodo? (S/N): ')
    if saida.upper() == 'N' :
        resp = False
print('Fim do Programa')