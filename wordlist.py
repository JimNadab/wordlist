# Estudo feito pela Axur mostra o perfil de senhas do brasileiro: https://blog.axur.com/pt/infografico-perfil-da-senha-do-brasileiro

from unicodedata import normalize #Para remover acentos e ç dos nomes: Retirado de: https://wiki.python.org.br/RemovedorDeAcentos

print ("""  
+ Criaremos wordlists personalizadas.
+ 06.05.2019
+ Jim Nadab.
            
Forneça os dados que trabalharemos.
            
            """)

# Iniciando a coleta de informações. Afinal, é uma wordlist personalizada.
nome_completo_alvo = input("\nQual o nome completo do alvo? ")

while len(str.split(nome_completo_alvo)) == 0 or not str.isalpha(nome_completo_alvo.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
    nome_completo_alvo = input("\nDigite um nome válido: ") 

nome_completo_alvo =  normalize('NFKD', nome_completo_alvo).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
data_nascimento_alvo = input("\nSabe a data de nascimento? (y/n)")

while (data_nascimento_alvo != 'y' and data_nascimento_alvo != 'n'): #Garantindo que seja digitado apenas y ou n.
    data_nascimento_alvo = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if data_nascimento_alvo == 'y':
    data_nascimento_alvo = input("\nQual a data de nascimento? (DDMMAAAA): ")

    while not str.isnumeric(data_nascimento_alvo): #Verificando se apenas números foram digitados.
        data_nascimento_alvo = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
        if len(data_nascimento_alvo) != 8:
            data_nascimento_alvo = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")
else:
    data_nascimento_alvo = False

casado = str.lower(input("\nO \"alvo\" é casado(a)? (y/n): "))

while (casado != 'y' and casado != 'n'):
    casado = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if casado == 'y':
    casado = True
    nome_completo_conjuge = input("\nQual o nome completo do cônjuge? ")

    while len(str.split(nome_completo_conjuge)) == 0 or not str.isalpha(nome_completo_conjuge.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        nome_completo_conjuge = input("\nDigite um nome válido: ")

    nome_completo_conjuge =  normalize('NFKD', nome_completo_conjuge).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
    data_nascimento_conjuge = input("\nSabe a data de nascimento do cônjuge? (y/n): ")

    while (data_nascimento_conjuge != 'y' and data_nascimento_conjuge != 'n'): #Garantindo que seja digitado apenas y ou n.
        data_nascimento_conjuge = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

    if data_nascimento_conjuge == 'y':
        data_nascimento_conjuge = input("\nQual a data de nascimento do cônjuge? (DDMMAAAA): ")

        while not str.isnumeric(data_nascimento_conjuge): #Verificando se apenas números foram digitados.
            data_nascimento_conjuge = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
            if len(data_nascimento_conjuge) != 8:
                data_nascimento_conjuge = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")
    else:
        data_nascimento_conjuge = False

    data_casamento = input("\nSabe a data de casamento? (y/n): ")
    
    while (data_casamento != 'y' and data_casamento != 'n'): #Garantindo que seja digitado apenas y ou n.
        data_casamento = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))
    
    if data_casamento == 'y':
        data_casamento = input("\nQual a data de casamento? (DDMMAAAA): ")
    
        while not str.isnumeric(data_casamento): #Verificando se apenas números foram digitados.
            data_casamento = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
            if len(data_casamento) != 8:
                data_casamento = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")
    else:
        data_casamento = False
else:
    casado = False

filhos = str.lower(input("\nPossui filhos? (y/n): "))

while (filhos != 'y' and filhos != 'n'):
    filhos = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if filhos == 'y':
    
    filhos = input("\nQuantos filhos? ")
    
    #Garantindo que "filhos" seja um número positivo.
    while not str.isnumeric(filhos) or int(filhos) < 1:
        filhos = input("\nDigite apenas o número de filhos! E um número positivo! Ex.: 1, 2 ou 7! ")

    filhos = int(filhos)    ###### TRATAR ######    
    
    if filhos == 1:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")

        while len(str.split(nome_completo_primeiro_filho)) == 0 or not str.isalpha(nome_completo_primeiro_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_primeiro_filho = input("\nDigite um nome válido: ")

        nome_completo_primeiro_filho =  normalize('NFKD', nome_completo_primeiro_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_primeiro_filho != 'y' and data_nascimento_primeiro_filho != 'n'):
            data_nascimento_primeiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_primeiro_filho == 'y':
            data_nascimento_primeiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_primeiro_filho): #Verificando se apenas números foram digitados.
                data_nascimento_primeiro_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_primeiro_filho) != 8:
                    data_nascimento_primeiro_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")
    
    if filhos == 2:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")

        while len(str.split(nome_completo_primeiro_filho)) == 0 or not str.isalpha(nome_completo_primeiro_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_primeiro_filho = input("\nDigite um nome válido: ")

        nome_completo_primeiro_filho =  normalize('NFKD', nome_completo_primeiro_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        ata_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_primeiro_filho != 'y' and data_nascimento_primeiro_filho != 'n'):
            data_nascimento_primeiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_primeiro_filho == 'y':
            data_nascimento_primeiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_primeiro_filho): #Verificando se apenas números foram digitados.
                data_nascimento_primeiro_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_primeiro_filho) != 8:
                    data_nascimento_primeiro_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")

        nome_completo_segundo_filho = input("\nQual o nome do segundo filho? ")

        while len(str.split(nome_completo_segundo_filho)) == 0 or not str.isalpha(nome_completo_segundo_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_segundo_filho = input("\nDigite um nome válido: ")

        nome_completo_segundo_filho =  normalize('NFKD', nome_completo_segundo_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        data_nascimento_segundo_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_segundo_filho != 'y' and data_nascimento_segundo_filho != 'n'):
            data_nascimento_segundo_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_segundo_filho == 'y':
            data_nascimento_segundo_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_segundo_filho): #Verificando se apenas números foram digitados.
                data_nascimento_segundo_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_segundo_filho) != 8:
                    data_nascimento_segundo_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")

    if filhos == 3:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")

        while len(str.split(nome_completo_primeiro_filho)) == 0 or not str.isalpha(nome_completo_primeiro_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_primeiro_filho = input("\nDigite um nome válido: ")

        nome_completo_primeiro_filho =  normalize('NFKD', nome_completo_primeiro_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        ata_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_primeiro_filho != 'y' and data_nascimento_primeiro_filho != 'n'):
            data_nascimento_primeiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_primeiro_filho == 'y':
            data_nascimento_primeiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_primeiro_filho): #Verificando se apenas números foram digitados.
                data_nascimento_primeiro_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_primeiro_filho) != 8:
                    data_nascimento_primeiro_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")

        nome_completo_segundo_filho = input("\nQual o nome do segundo filho? ")

        while len(str.split(nome_completo_segundo_filho)) == 0 or not str.isalpha(nome_completo_segundo_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_segundo_filho = input("\nDigite um nome válido: ")

        nome_completo_segundo_filho =  normalize('NFKD', nome_completo_segundo_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        data_nascimento_segundo_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_segundo_filho != 'y' and data_nascimento_segundo_filho != 'n'):
            data_nascimento_segundo_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_segundo_filho == 'y':
            data_nascimento_segundo_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_segundo_filho): #Verificando se apenas números foram digitados.
                data_nascimento_segundo_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_segundo_filho) != 8:
                    data_nascimento_segundo_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")

        nome_completo_terceiro_filho = input("\nQual o nome do terceiro filho? ")

        while len(str.split(nome_completo_terceiro_filho)) == 0 or not str.isalpha(nome_completo_terceiro_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_terceiro_filho = input("\nDigite um nome válido: ")

        nome_completo_terceiro_filho =  normalize('NFKD', nome_completo_terceiro_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        data_nascimento_terceiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_terceiro_filho != 'y' and data_nascimento_terceiro_filho != 'n'):
            data_nascimento_terceiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_terceiro_filho == 'y':
            data_nascimento_terceiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_terceiro_filho): #Verificando se apenas números foram digitados.
                data_nascimento_terceiro_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_terceiro_filho) != 8:
                    data_nascimento_terceiro_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")

    if filhos > 3: 
        nome_completo_ultimo_filho = input("\nQual o nome do filho mais novo? ")

        while len(str.split(nome_completo_ultimo_filho)) == 0 or not str.isalpha(nome_completo_ultimo_filho.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_ultimo_filho = input("\nDigite um nome válido: ")

        nome_completo_ultimo_filho =  normalize('NFKD', nome_completo_ultimo_filho).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
        data_nascimento_ultimo_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_ultimo_filho != 'y' and data_nascimento_ultimo_filho != 'n'):
            data_nascimento_terceiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_ultimo_filho == 'y':
            data_nascimento_ultimo_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_ultimo_filho): #Verificando se apenas números foram digitados.
                data_nascimento_ultimo_filho = input("\nDigite apenas números com a seguinte formatação \"DDYYAAAA\": ")
                if len(data_nascimento_ultimo_filho) != 8:
                    data_nascimento_ultimo_filho = input("\nVocê não digitou 8 dígitos! Corrija a informação: ")
else:
    filhos = False

animal_estimacao = str.lower(input("\nPossui animal de estimação? (y/n): "))

while (animal_estimacao != 'y' and animal_estimacao != 'n'):
    animal_estimacao = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if animal_estimacao == 'y':
    animal = True
    animal_estimacao = input("\nQual o nome? ")

    while len(str.split(animal_estimacao)) == 0 or not str.isalpha(animal_estimacao.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        animal_estimacao = input("\nDigite um nome válido: ")

    animal_estimacao =  normalize('NFKD', animal_estimacao).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
else:
    animal = False

empresa_alvo = str.lower(input("\nO \"alvo\" trabalha? (y/n): "))

while (empresa_alvo != 'y' and empresa_alvo != 'n'):
    empresa_alvo = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if empresa_alvo == 'y':
    empregado = True
    empresa_alvo = input("\n Qual o nome da empresa onde o \"alvo\" trabalha? ")

    while len(str.split(empresa_alvo)) == 0 or not str.isalpha(empresa_alvo.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        empresa_alvo = input("\nDigite um nome válido: ")

    empresa_alvo =  normalize('NFKD', empresa_alvo).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
else:
    empregado = False

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
    torcedor = True
    time = input("\nQual? ")

    while len(str.split(time)) == 0 or not str.isalpha(time.replace(' ', '')):  #garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        time = input("\nDigite um nome válido: ")

    time =  normalize('NFKD', time).encode('ASCII', 'ignore').decode('ASCII') #Removido os acentos.
else:
    torcedor = False

# Coletado as informaçoes mais importantes.
print("\nObrigado pelas informações fornecidas.")

# Oranizando os dados para facilitar a manipulação:
print("\nOrganizando as informações passadas: ")

lista_nomes_alvo = str.split(nome_completo_alvo)

if data_nascimento_alvo != False:
    dia_alvo = data_nascimento_alvo[:2]
    mes_alvo = data_nascimento_alvo[2:4]
    ano_alvo = data_nascimento_alvo[4:]

if casado:
    lista_nomes_conjuge = str.split(nome_completo_conjuge)
    
    if data_nascimento_conjuge != False:
    
        dia_conjuge = data_nascimento_conjuge[:2]
        mes_conjuge = data_nascimento_conjuge[2:4]
        ano_conjuge = data_nascimento_conjuge[4:]

    if data_casamento != False:
        dia_casamento = data_casamento[:2]
        mes_casamento = data_casamento[2:4]
        ano_casamento = data_casamento[4:]

if filhos == 1:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    dia_primeiro_filho = data_nascimento_primeiro_filho[:2]
    mes_primeiro_filho = data_nascimento_primeiro_filho[2:4]
    ano_primeiro_filho = data_nascimento_primeiro_filho[4:]

if filhos == 2:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    dia_primeiro_filho = data_nascimento_primeiro_filho[:2]
    mes_primeiro_filho = data_nascimento_primeiro_filho[2:4]
    ano_primeiro_filho = data_nascimento_primeiro_filho[4:]

    lista_nomes_segundo_filho = str.split(nome_completo_segundo_filho)
    dia_segundo_filho = data_nascimento_segundo_filho[:2]
    mes_segundo_filho = data_nascimento_segundo_filho[2:4]
    ano_segundo_filho = data_nascimento_segundo_filho[4:]

if filhos == 3:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    dia_primeiro_filho = data_nascimento_primeiro_filho[:2]
    mes_primeiro_filho = data_nascimento_primeiro_filho[2:4]
    ano_primeiro_filho = data_nascimento_primeiro_filho[4:]

    lista_nomes_segundo_filho = str.split(nome_completo_segundo_filho)
    dia_segundo_filho = data_nascimento_segundo_filho[:2]
    mes_segundo_filho = data_nascimento_segundo_filho[2:4]
    ano_segundo_filho = data_nascimento_segundo_filho[4:]

    lista_nomes_terceiro_filho = str.split(nome_completo_terceiro_filho)
    dia_terceiro_filho = data_nascimento_terceiro_filho[:2]
    mes_terceiro_filho = data_nascimento_terceiro_filho[2:4]
    ano_terceiro_filho = data_nascimento_terceiro_filho[4:]

if filhos > 3:
    lista_nomes_ultimo_filho = str.split(nome_completo_ultimo_filho)
    dia_ultimo_filho = data_nascimento_ultimo_filho[:2]
    mes_ultimo_filho = data_nascimento_ultimo_filho[2:4]
    ano_ultimo_filho = data_nascimento_ultimo_filho[4:]

if animal:
    lista_animal = str.split(animal_estimacao)

if empregado:
    lista_empresa = str.split(empresa_alvo)

if torcedor:
    lista_time = str.split(time)

if religioso:
    palavras_religiosas = ['Jesus', 'Cristo', 'Deus', 'Jesusvoltara', 'soJesussalva', 'Jesusestavoltando', 'EspiritoSanto', 'JesusCristo']

#O arquivo .txt, que conterá a wordlist terá o primeiro nome do usuário.
arquivo = lista_nomes_alvo[0] + '.txt'    

#Hora do show!
def so_nomes(lista):

    f = open(arquivo, 'a')

    i = 0
    j = 0

    while i < len(lista):
        if len(lista[i]) < 6:                                                #garantindo que as senhas tenham no mínino 6 dígitos
            pass
        else:
            f.write(str.lower(lista[i]+'\n'))                                #todas minúsculas
            f.write(str.capitalize(lista[i]+'\n'))                           #apenas a primeira maiúscula
            f.write(str.upper(lista[i]+'\n'))                                #todas maiúsculas
            f.write(str.lower(lista[i][j])+str.upper(lista[i][j+1:])+'\n')   #primeira minúscula, o resto maiúscula
        i += 1
                    #### usar str.swapcase() acima e garantir que não hajam nomes iguais!

    f.close() 

so_nomes(lista_nomes_alvo)
#so_nomes(lista_nomes_conjuge)
#so_nomes(lista_nomes_primeiro_filho)       ###### TRATAR NOMES IGUAIS ##### 









"""def misturador_com_numeros(nome):
    
    #abcdario = 'i, j, k'
    # tenho que tratar o caso de receber nomes maiores!
    #for x = 0 < len(abcdario):

    i = 0
    j = 0
    k = 0
    words = ''

    for i in 10:

        n = 0 #ponteiro que vai colocar os número em seu lugar.
        l = 0 #ponteiro que vai colocar as letras em seu lugar.

        while l < len(nome):
            words[n] = i
            words[n+1] = nome[l]
            n += 2
            l += 1

        words[l] = '\n'

        for k in 10: """

