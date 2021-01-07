#Código do slide 27 da apostila da Aula 02
#O código apresenta:
#   a entrada de dados *input*
#   a conversão (parse) em número decimal *float()*
#   a soma e média das notas

nome = input("Insira seu nome: ")

nota1 = float(input("Sua primeira nota: "))
nota2 = float(input("Sua segunda nota: "))

print( "Olá", nome, "suas notas foram:")
print(nota1, "e", nota2)

soma = nota1 + nota2
media = soma / 2

print("Sua média é:", media)