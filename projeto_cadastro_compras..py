nome = input(' Digite seu nome:')
idade = int(input('Digite sua idade:'))
anoAtual = 2025
anoNascimento = anoAtual - idade

print(f'Olá {nome}, você tem {idade} anos, e nasceu em {anoNascimento}')

print('Digite 3 preço de produtos:')
total = 0
for i in range(1,4):
    preco = float(input(f'Digite {i} preço:'))
    total += preco
media = total / 3
    
if total % 2 == 0:
    print(' O total é par')
else:
    print(' O total é impar') 

mensagem = "Cadastro concluído com sucesso!"
   

    

print(f' O total da compra foi R$ {round(total,2)}')
print(f' A média da compra foi R$ {round(media,2)}')
print(f' Nome do usuario Minusculo: {nome.lower()}')
print(f'Nome do usuario Maiusculo: {nome.upper()}')
print(f' Nome do usuario Minusculo: {nome.lower().title()}')
print(mensagem * 3)

    