
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

senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
tentativas = 1
while senha_cadastrada != senha and tentativas < 3:
    print("Vc é hacker? ")
    senha = input("Diga sua senha")
    tentativas += 1
if senha == senha_cadastrada:
    print("Acesso liberado!")
else:
    print("Sai hacker")
idoso = input("Você é idoso? sim ou não: ")
while idoso != "sim" and idoso != "não":
    print("Resposta inválida")
    idoso = input("Você é idoso? sim ou não: ")


idoso = input("Você é idoso? sim ou não: ")
while not (idoso == "sim" or idoso == "não"):
    print("Resposta inválida")
    idoso = input("Você é idoso? sim ou não: ")

if idoso == 'sim':
    print("top")
else:
    print("feio")

i = 0
soma = 0
while True:
    i+=1
    soma += i
    if i == 100:
        break
print(soma)
print('sdjfkdsbf'.isnumeric())
print('123435'.isnumeric())
print('1.23'.isnumeric())
print('12lj332jn'.isnumeric())

idade = input("Diga sua idade: ")
while not idade.isnumeric():
    print("é numero pô")
    idade = input("Diga sua idade: ")
idade = int(idade)
print(type(idade))

while True:
    idade = input("Diga sua idade: ")
    if idade.isnumeric():
        if int(idade) > 0 and int(idade) < 100:
            idade = int(idade)
            break
        print("numero invalido")
    else:
        print("Precisa ser número")
print(f"Vc tem {idade} anos")