'''par = 0
qtd = 0
while qtd < 5:
    num = int(input("Diga um número: "))
    if num%2 == 0:
       par += 1
    qtd += 1
print(f"Vc digitou {par} pares e {5-par} impares")


senha_cadastrada = '1234'
senha = input("Diga sua senha: ")
tentativas = 1
while senha != senha_cadastrada and tentativas  < 3:
    print(f"Vc é hacker? Só mais {3 - tentativas } tentativas")
    senha = input("Diga sua senha: ")
    tentativas += 1
if senha == senha_cadastrada:
    print("Acesso liberado!")
else:
    print("Sai hacker!!!")

i = 0
soma = 0
while i < 100:
    i+=1
    soma += i
print(soma)


idoso = input("Você é idoso? sim ou não: ")
if idoso != "sim" and idoso != "não":
    print("Resposta inválida")
    idoso = input("Você é idoso? sim ou não:")

    if idoso == 'sim':
        print("top")
    else:
        print("feio")


i = 0
soma = 0
#while True significa repita infinitamente
while True:
    i+=1
    soma += i
    if i ==100:
        break
print(soma)



.isnumeric() se todos caracteres forem número será True

print("abcd" .isnumeric())
print("123456" .isnumeric())
print("1.23" .isnumeric())
print("12klj345lkn6" .isnumeric())



idade = input("Digite sua ideia: ")
while not idade.isnumeric():
    print("É número pô")
    idade = input("Diga sua idade: ")
idade = int(idade)
print(type(idade))


#Exercício: peder numero po, obrigar o usuario a digitar um numero que esteja entre o intervalo de 1 e 100
 '''


while True:
    idade = input("Diga sua idade:")
    if idade.isnumeric():
        if int(idade) > 0 and int(idade) < 100:
            idade = int(idade)
            break
print(f"Voce^tem {idade} anos")

while True:
    idade = input("Diga sua idade:")
    if idade.isnumeric():
        if int(idade) > 0 and int(idade) < 100:
            idade = int(idade)
            break
        print("numero invalido")
        if not idade.isnumeric():
    print("precisa ser número")
print(f"Voce^tem {idade} anos")