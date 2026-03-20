from poyo.exceptions import NoMatchException

print("ola mundo")
print(7+4)
print("7+4")
print("7"+"4") #concatenação de strings



#comentarios de 1 çlinha
'''
       comentarios de 
       multiplas linhas
'''

#variaveis
nome = "ALEXANDRE" #string
idade = 26  #inteiro
peso = 76.2 #float

print(nome,idade,peso)
print(f"oiii,{nome}!!!")

#inputs - simulação de forms no cmd
nome = input("digite o seu nome: ")
idade = int(input("digite sua idade:  "))

nova_idade = idade + 1
print(nome,idade)
print(nova_idade)