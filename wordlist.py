# Estudo feito pela Axur mostra o perfil de senhas do brasileiro: 
# https://blog.axur.com/pt/infografico-perfil-da-senha-do-brasileiro
# Este estudo me fez adicionar outros templates de senha.

# Para remover acentos e ç dos nomes;
# Retirado de: https://wiki.python.org.br/RemovedorDeAcentos
# Medida adotada, pois caracteres assim não são aceitos atualmente
from unicodedata import normalize
from datetime import date

print ("""  
+ Criaremos wordlists personalizadas.
+ 06.05.2019
+ Jim Nadab.
            
Forneça os dados que trabalharemos.
            
            """)

# Iniciando a coleta de informações.
tamanho_minimo = input("Qual o tamanho mínimo, das senhas que criaremos? ")

# Garantindo que apenas numeros tenham sido digitados.
# Por padrão estou exigindo um tamanha mínimo de 6 digitos.
while not str.isnumeric(tamanho_minimo) or int(tamanho_minimo) < 6:
        tamanho_minimo = input("\nDigite apenas um número inteiro, maior ou igual a 6: ")

# Função para garantir a integridade nos nomes.
def bons_nomes (nome):
    
    # Nomes em branco ou com caracteres não alfabéticos não são permitidos
    while len(str.split(nome)) == 0 or not str.isalpha(nome.replace(' ', '')):
        nome = input("\nDigite um nome válido: ")

    # Para remover os acentos e cedilhas.
    nome =  normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')

    return nome

# Função para garantir a integridade das datas.
def boas_datas (data):

    # Garantindo que seja digitado apenas y ou n.
    while (data != 'y' and data != 'n'): 
        data = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

    if data == 'y':
        data = input("\nQual a data? (DDMMAAAA): ")
        
        # Verificando se apenas números foram digitados.
        while not str.isnumeric(data) or len(data) != 8:
            data = input("\nDigite apenas \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        
        return data
    else:
        return False

def aniversario (data):
    data_atual = date.today()
    
    if data == False:
        return False
    elif (int(data_atual.year) - int(data[-4:])) <= 0:
        return False
    else:
        return int(data_atual.year) - int(data[-4:])


nome_completo_alvo = input("\nQual o nome completo do alvo? ")
nome_completo_alvo = bons_nomes(nome_completo_alvo)
data_nascimento_alvo = input("\nSabe a data de nascimento? (y/n): ")
data_nascimento_alvo = boas_datas(data_nascimento_alvo)

casado = str.lower(input("\nO \"alvo\" é casado(a)? (y/n): "))
while (casado != 'y' and casado != 'n'):
    casado = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if casado == 'y':
    nome_completo_conjuge = input("\nQual o nome completo do cônjuge? ")
    nome_completo_conjuge = bons_nomes(nome_completo_conjuge)
    data_nascimento_conjuge = input("\nSabe a data de nascimento do cônjuge? (y/n): ")
    data_nascimento_conjuge = boas_datas(data_nascimento_conjuge)
    data_casamento = input("\nSabe a data de casamento? (y/n): ")
    data_casamento = boas_datas(data_casamento)
else:
    casado = False

filhos = str.lower(input("\nPossui filhos? (y/n): "))
while (filhos != 'y' and filhos != 'n'):
    filhos = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if filhos == 'y':
    
    filhos = input("\nQuantos filhos? ")
    
    # Garantindo que "filhos" seja um número positivo.
    while not str.isnumeric(filhos) or int(filhos) < 1:
        filhos = input("\nDigite apenas o número de filhos! E um número positivo! Ex.: 1, 2 ou 7! ")

    filhos = int(filhos)     
    
    if filhos == 1:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")
        nome_completo_primeiro_filho = bons_nomes(nome_completo_primeiro_filho)
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_primeiro_filho = boas_datas(data_nascimento_primeiro_filho)
    
    if filhos == 2:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")
        nome_completo_primeiro_filho = bons_nomes(nome_completo_primeiro_filho)
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_primeiro_filho = boas_datas(data_nascimento_primeiro_filho)

        nome_completo_segundo_filho = input("\nQual o nome do segundo filho? ")
        nome_completo_segundo_filho = bons_nomes(nome_completo_segundo_filho)
        data_nascimento_segundo_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_segundo_filho = boas_datas(data_nascimento_segundo_filho)

    if filhos == 3:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")
        nome_completo_primeiro_filho = bons_nomes(nome_completo_primeiro_filho)
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_primeiro_filho = boas_datas(data_nascimento_primeiro_filho)

        nome_completo_segundo_filho = input("\nQual o nome do segundo filho? ")
        nome_completo_segundo_filho = bons_nomes(nome_completo_segundo_filho)
        data_nascimento_segundo_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_segundo_filho = boas_datas(data_nascimento_segundo_filho)

        nome_completo_terceiro_filho = input("\nQual o nome do terceiro filho? ")
        nome_completo_terceiro_filho = bons_nomes(nome_completo_terceiro_filho)
        data_nascimento_terceiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_terceiro_filho = boas_datas(data_nascimento_terceiro_filho)

    if filhos > 3: 
        nome_completo_ultimo_filho = input("\nQual o nome do filho mais novo? ")
        nome_completo_ultimo_filho = bons_nomes(nome_completo_ultimo_filho)
        data_nascimento_ultimo_filho = input("\nSabe a data de nascimento? (y/n): ")
        data_nascimento_ultimo_filho = boas_datas(data_nascimento_ultimo_filho)
else:
    filhos = False

animal_estimacao = str.lower(input("\nPossui animal de estimação? (y/n): "))
while (animal_estimacao != 'y' and animal_estimacao != 'n'):
    animal_estimacao = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if animal_estimacao == 'y':
    animal_estimacao = input("\nQual o nome? ")
    animal_estimacao = bons_nomes(animal_estimacao)
else:
    animal_estimacao = False

empresa_alvo = str.lower(input("\nO \"alvo\" trabalha? (y/n): "))
while (empresa_alvo != 'y' and empresa_alvo != 'n'):
    empresa_alvo = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if empresa_alvo == 'y':
    empresa_alvo = input("\n Qual o nome da empresa onde o \"alvo\" trabalha? ")
    empresa_alvo = bons_nomes(empresa_alvo)
else:
    empresa_alvo = False

religioso = str.lower(input("\nO \"alvo\" é religioso? (y/n): "))
while (religioso != 'y' and religioso != 'n'):
    religioso = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if religioso == 'y':
    religioso = True
else:
    religioso = False

time = str.lower(input("\nO \"alvo\" torce por algum time? (y/n): "))

while (time != 'y' and time != 'n'):
    time = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if time == 'y':
    time = input("\nQual? ")
    time = bons_nomes(time)
else:
    time = False

# Oranizando os dados para facilitar a manipulação:
print("\nOrganizando os dados fornecidos.")

lista_nomes_alvo = str.split(nome_completo_alvo)

if casado:
    lista_nomes_conjuge = str.split(nome_completo_conjuge)

if filhos == 1:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)

if filhos == 2:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    lista_nomes_segundo_filho = str.split(nome_completo_segundo_filho)

if filhos == 3:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    lista_nomes_segundo_filho = str.split(nome_completo_segundo_filho)
    lista_nomes_terceiro_filho = str.split(nome_completo_terceiro_filho)

if filhos > 3:
    lista_nomes_ultimo_filho = str.split(nome_completo_ultimo_filho)

if animal_estimacao != False:
    lista_animal = str.split(animal_estimacao)

if empresa_alvo != False:
    lista_empresa = str.split(empresa_alvo)

if time != False:
    lista_time = str.split(time)

if religioso:
    palavras_religiosas = ['Jesus', 'Cristo', 'Deus', 'Jesusvoltara', 'soJesussalva', 'Jesusestavoltando', 'EspiritoSanto', 'JesusCristo']

# O arquivo .txt que conterá a wordlist terá o primeiro nome do usuário.
arquivo = str.capitalize(lista_nomes_alvo[0]) + '.txt'    

# Hora do show!
gravado = True
lista_provisoria = []

def gravar(lista):

    global gravado
    
    if len(lista) == 0:
        gravado = False
        return
    else:
        f = open(arquivo, 'w')

        for x in range(len(lista)):
            if len(lista[x]) < int(tamanho_minimo):
                pass
            else:
                f.write(lista[x]+'\n')
        
        f.close()

def letras_e_datas(lista, data):
    
    listavazia = []

    if data:
        for i in range(len(lista)):
            listavazia.append(lista[i])
            listavazia.append(lista[i]+data[:])
            listavazia.append(lista[i]+data[:2])
            listavazia.append(lista[i]+data[-4:])
            listavazia.append(lista[i]+data[-2:])

            idade = aniversario(data)
            x = 0

            while x < 5 and idade > 0:
                listavazia.append(lista[i]+str(idade))
                x += 1
                idade -= 1
    else:
        for i in range(len(lista)):
            listavazia.append(lista[i])

    for i in range(len(listavazia)):
        lista_provisoria.append(listavazia[i])


def so_letras (lista, data):

    tamanho = len(lista)
    listavazia = []

    for i in range(tamanho):
        
        if lista[i] not in listavazia:                                        # garantindo que não existam palavras repetidas no .txt
            listavazia.append(str.lower(lista[i]))                            # junior, alves, quinto, terceiro    
            listavazia.append(str.capitalize(lista[i]))                       # Junior, Alves, Quinto, Terceiro
            listavazia.append(str.swapcase(str.capitalize(lista[i])))         # jUNIOR, aLVES, qUINTO, tERCEIRO
            listavazia.append(str.upper(lista[i]))                            # JUNIOR, ALVES, QUINTO, TERCEIRO

    if tamanho == 2:
        listavazia.append(str.lower(lista[0]+lista[1]))                       # primeiro nome + segundo nome, minúsculos
        listavazia.append(str.upper(lista[0]+lista[1]))                       # primeiro nome + segundo nome, maiúsculos
        listavazia.append(str.capitalize(lista[0])+str.capitalize(lista[1]))  # primeiro nome + segundo nome, com as iniciais maiúsculas

    if tamanho > 2:
        listavazia.append(str.lower(lista[0]+lista[1]))                       # primeiro nome + segundo nome, minúsculos
        listavazia.append(str.upper(lista[0]+lista[1]))                       # primeiro nome + segundo nome, maiúsculos
        listavazia.append(str.capitalize(lista[0])+str.capitalize(lista[1]))  # primeiro nome + segundo nome, com as iniciais maiúsculas
        listavazia.append(str.lower(lista[0]+lista[-1]))                      # primeiro e último nome, minúsculos
        listavazia.append(str.upper(lista[0]+lista[-1]))                      # primeiro e último nome, maiúsculos
        listavazia.append(str.capitalize(lista[0])+str.capitalize(lista[-1])) # primeiro e último nome, com as iniciais maiúsculas    

    temp = str.capitalize(lista[0])                 # para unir o primeiro nome com as demais iniciais

    for a in range(tamanho - 1):
        temp += str.upper(lista[a+1][0])        

    if temp not in listavazia:
        listavazia.append(temp)
        listavazia.append(str.lower(temp))
        listavazia.append(str.upper(temp))

    temp2 = str.lower(lista[0][0])                  # para unir as iniciais

    for a in range(tamanho - 1):
        temp2 += str.lower(lista[a+1][0])

    if temp2 not in listavazia:
        listavazia.append(temp2)
        listavazia.append(str.upper(temp2))
    
    letras_e_datas(listavazia, data)


so_letras(lista_nomes_alvo, data_nascimento_alvo)

if casado:
    so_letras(lista_nomes_conjuge, data_nascimento_conjuge)

if filhos == 1:
    so_letras(lista_nomes_primeiro_filho, data_nascimento_primeiro_filho)

if filhos == 2:
    so_letras(lista_nomes_primeiro_filho, data_nascimento_primeiro_filho)
    so_letras(lista_nomes_segundo_filho, data_nascimento_segundo_filho)

if filhos == 3:
    so_letras(lista_nomes_primeiro_filho, data_nascimento_primeiro_filho)
    so_letras(lista_nomes_segundo_filho, data_nascimento_segundo_filho)
    so_letras(lista_nomes_terceiro_filho, data_nascimento_terceiro_filho)

if filhos > 3:
    so_letras(lista_nomes_ultimo_filho)

gravar(lista_provisoria)

print("\nGerando wordlist.")

if gravado:
    print("Wordlist " +arquivo+ " criada com sucesso.\n")
else:
    print("Wordlist não pode ser gravada!\n")
