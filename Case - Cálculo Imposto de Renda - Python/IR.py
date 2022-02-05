print('Para saber o valor do imposto de renda a pagar, responda a seguir: ')
renda_anual = float(input('Valor da renda anual: '))

if (renda_anual < 22847.76):
    print('Você está isento da contribuição!')
else:
     if (renda_anual >= 22847.77) and (renda_anual <= 33919.80):
        faixa2 = round((float(renda_anual * 0.075) - (1713.58)), 2)
        print('Base de Cálculo - Faixa 2\nAlíquota = 7,5%\nDedução = R$1713,58')
        print(f'Você deverá contribuir com R${faixa2}') 
        if (renda_anual >= 33919.81) and (renda_anual <= 45012.60):
            print('Base de Cálculo - Faixa 3\nAlíquota = 15%\nDedução = R$4257,57')
            faixa3 = round((float(renda_anual * 0.15) - (4257.57)), 2)
            print(f'Você deverá contribuir com R${faixa3}') 
        if (renda_anual >= 45012.61) and (renda_anual <= 55976.16):
            print('Base de Cálculo - Faixa 4 \nAlíquota = 22,5% \nDedução = R$7633,51')
            faixa4= round((float(renda_anual * 0.225) - (7633.51)), 2)
        print(f'Você deverá contribuir com R${faixa4}')
        if (renda_anual > 55976.16):
            print('Base de Cálculo - Faixa 5 \nAlíquota = 27,5% \nDedução = R$10432,32')
            faixa5 = round((float(renda_anual * 0.275) - (10432.32)), 2)
            print(f'Você deverá contribuir com R${faixa5}')