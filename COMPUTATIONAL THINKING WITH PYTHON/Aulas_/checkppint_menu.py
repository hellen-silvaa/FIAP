
vinho1 = 'Chapinha'
vinho2 = 'Cantinho do Vale'
vinho3 = 'Sangue de Boi'
preco1 = 10
preco2 = 20
preco3 = 30
frete = 10
print("Seja bem vindo à vinheria agnello!!!!!!!")
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    print("Que feio!!!! Vc não pode beber!!!")
else:
    endereco = input("Diga seu endereço: ")
    opcao = input(f"Temos os vinhos:\n{vinho1} : R${preco1:.2f}"
                  f"\n{vinho2} : R${preco2:.2f}"
                  f"\n{vinho3} : R${preco3:.2f}.\n Qual você quer? ")
    if opcao == vinho1:
        preco = preco1
    elif opcao == vinho2:
        preco = preco2
    else:
        preco = preco3
    qtd = int(input(f"Diga qts garrafas de {opcao}: "))
    valor = qtd*preco
    if valor > 100:
        print("Frete grátis!")
    else:
        valor += frete
    print(f"Obrigado por comprar na vinheira agnello. Vc levou {qtd}"
          f" garrafas de {opcao} por R${valor:.2f} e será entregue em "
          f"{endereco}")