# Exercício float 1

p1 = 19.90
p2 = 5.75
p3 = 12.40
total = round(p1 + p2 + p3,2)
media = round(total / 3,2)
m = p1 / 2 
m1 = p2 / 2
m2 = p3 / 2
print(f' Valor Total da compra é {total}')
print(f' Valor da média é {media} A media do primeiro produto é {round(m)} do segundo é {round(m1)} do terceiro é {round(m2)}')

# Exercício condicional 1
if int(total) % 2 == 0:
    print('O valor é par')
else:
    print('O valor é impar')   
    