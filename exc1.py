'''
Exc 1
Ler nome, sexo e idade. Se sexo for feminino e idade
menor que 25. Imprimir o nome da pessoa e a palavra
ACEITA. Caso contrario imprimir NAO ACEITA.
'''
print("Digite NOME, SEXO(masculino ou feminino) e IDADE (separados por espaço):")
nome, sexo, idade = input().split(' ')

if sexo == 'feminino' and int(idade) < 25:
    print(nome+' ACEITA')
else:
    print(nome+' NAO ACEITA')
