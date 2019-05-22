from unicodedata import normalize # Para remover acentos e ç dos nomes: Retirado de: https://wiki.python.org.br/RemovedorDeAcentos

print ("""  
+ Criaremos wordlists personalizadas.
+ 22.05.2019
+ Jim Nadab.
            
Forneça os dados que trabalharemos.
            
            """)

# Iniciando a coleta de informações. Afinal, é uma wordlist personalizada.
tamanho_minimo = input("Qual o tamanho mínimo, das senhas que criaremos? ")

while not str.isnumeric(tamanho_minimo) or int(tamanho_minimo) < 6: # Verificando se apenas números foram digitados.
        tamanho_minimo = input("\nDigite apenas um número inteiro, maior ou igual a 6: ")

nome_completo_alvo = input("\nQual o nome completo do alvo? ")

while len(str.split(nome_completo_alvo)) == 0 or not str.isalpha(nome_completo_alvo.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
    nome_completo_alvo = input("\nDigite um nome válido: ") 

nome_completo_alvo =  normalize('NFKD', nome_completo_alvo).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
data_nascimento_alvo = input("\nSabe a data de nascimento? (y/n): ")

while (data_nascimento_alvo != 'y' and data_nascimento_alvo != 'n'): # Garantindo que seja digitado apenas y ou n.
    data_nascimento_alvo = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if data_nascimento_alvo == 'y':
    data_nascimento_alvo = input("\nQual a data de nascimento? (DDMMAAAA): ")

    while not str.isnumeric(data_nascimento_alvo) or len(data_nascimento_alvo) != 8: # Verificando se apenas números foram digitados.
        data_nascimento_alvo = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
else:
    data_nascimento_alvo = False

casado = str.lower(input("\nO \"alvo\" é casado(a)? (y/n): "))

while (casado != 'y' and casado != 'n'):
    casado = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if casado == 'y':
    casado = True
    nome_completo_conjuge = input("\nQual o nome completo do cônjuge? ")

    while len(str.split(nome_completo_conjuge)) == 0 or not str.isalpha(nome_completo_conjuge.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        nome_completo_conjuge = input("\nDigite um nome válido: ")

    nome_completo_conjuge =  normalize('NFKD', nome_completo_conjuge).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
    data_nascimento_conjuge = input("\nSabe a data de nascimento do cônjuge? (y/n): ")

    while (data_nascimento_conjuge != 'y' and data_nascimento_conjuge != 'n'): # Garantindo que seja digitado apenas y ou n.
        data_nascimento_conjuge = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

    if data_nascimento_conjuge == 'y':
        data_nascimento_conjuge = input("\nQual a data de nascimento do cônjuge? (DDMMAAAA): ")

        while not str.isnumeric(data_nascimento_conjuge) or len(data_nascimento_conjuge) != 8: # Verificando se apenas números foram digitados.
            data_nascimento_conjuge = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
    else:
        data_nascimento_conjuge = False

    data_casamento = input("\nSabe a data de casamento? (y/n): ")
    
    while (data_casamento != 'y' and data_casamento != 'n'): # Garantindo que seja digitado apenas y ou n.
        data_casamento = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))
    
    if data_casamento == 'y':
        data_casamento = input("\nQual a data de casamento? (DDMMAAAA): ")
    
        while not str.isnumeric(data_casamento) or len(data_casamento) != 8: # Verificando se apenas números foram digitados.
            data_casamento = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
    else:
        data_casamento = False
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

        while len(str.split(nome_completo_primeiro_filho)) == 0 or not str.isalpha(nome_completo_primeiro_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_primeiro_filho = input("\nDigite um nome válido: ")

        nome_completo_primeiro_filho =  normalize('NFKD', nome_completo_primeiro_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_primeiro_filho != 'y' and data_nascimento_primeiro_filho != 'n'):
            data_nascimento_primeiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_primeiro_filho == 'y':
            data_nascimento_primeiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_primeiro_filho) or len(data_nascimento_primeiro_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_primeiro_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_primeiro_filho = False
    
    if filhos == 2:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")

        while len(str.split(nome_completo_primeiro_filho)) == 0 or not str.isalpha(nome_completo_primeiro_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_primeiro_filho = input("\nDigite um nome válido: ")

        nome_completo_primeiro_filho =  normalize('NFKD', nome_completo_primeiro_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_primeiro_filho != 'y' and data_nascimento_primeiro_filho != 'n'):
            data_nascimento_primeiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_primeiro_filho == 'y':
            data_nascimento_primeiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_primeiro_filho) or len(data_nascimento_primeiro_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_primeiro_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_primeiro_filho = False

        nome_completo_segundo_filho = input("\nQual o nome do segundo filho? ")

        while len(str.split(nome_completo_segundo_filho)) == 0 or not str.isalpha(nome_completo_segundo_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_segundo_filho = input("\nDigite um nome válido: ")

        nome_completo_segundo_filho =  normalize('NFKD', nome_completo_segundo_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_segundo_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_segundo_filho != 'y' and data_nascimento_segundo_filho != 'n'):
            data_nascimento_segundo_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_segundo_filho == 'y':
            data_nascimento_segundo_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_segundo_filho) or len(data_nascimento_segundo_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_segundo_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_segundo_filho = False

    if filhos == 3:
        nome_completo_primeiro_filho = input("\nQual o nome do primeiro filho? ")

        while len(str.split(nome_completo_primeiro_filho)) == 0 or not str.isalpha(nome_completo_primeiro_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_primeiro_filho = input("\nDigite um nome válido: ")

        nome_completo_primeiro_filho =  normalize('NFKD', nome_completo_primeiro_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_primeiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_primeiro_filho != 'y' and data_nascimento_primeiro_filho != 'n'):
            data_nascimento_primeiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_primeiro_filho == 'y':
            data_nascimento_primeiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_primeiro_filho) or len(data_nascimento_primeiro_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_primeiro_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_primeiro_filho = False

        nome_completo_segundo_filho = input("\nQual o nome do segundo filho? ")

        while len(str.split(nome_completo_segundo_filho)) == 0 or not str.isalpha(nome_completo_segundo_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_segundo_filho = input("\nDigite um nome válido: ")

        nome_completo_segundo_filho =  normalize('NFKD', nome_completo_segundo_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_segundo_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_segundo_filho != 'y' and data_nascimento_segundo_filho != 'n'):
            data_nascimento_segundo_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_segundo_filho == 'y':
            data_nascimento_segundo_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_segundo_filho) or len(data_nascimento_segundo_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_segundo_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_segundo_filho = False

        nome_completo_terceiro_filho = input("\nQual o nome do terceiro filho? ")

        while len(str.split(nome_completo_terceiro_filho)) == 0 or not str.isalpha(nome_completo_terceiro_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_terceiro_filho = input("\nDigite um nome válido: ")

        nome_completo_terceiro_filho =  normalize('NFKD', nome_completo_terceiro_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_terceiro_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_terceiro_filho != 'y' and data_nascimento_terceiro_filho != 'n'):
            data_nascimento_terceiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_terceiro_filho == 'y':
            data_nascimento_terceiro_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_terceiro_filho) or len(data_nascimento_terceiro_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_terceiro_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_terceiro_filho = False

    if filhos > 3: 
        nome_completo_ultimo_filho = input("\nQual o nome do filho mais novo? ")

        while len(str.split(nome_completo_ultimo_filho)) == 0 or not str.isalpha(nome_completo_ultimo_filho.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
            nome_completo_ultimo_filho = input("\nDigite um nome válido: ")

        nome_completo_ultimo_filho =  normalize('NFKD', nome_completo_ultimo_filho).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
        data_nascimento_ultimo_filho = input("\nSabe a data de nascimento? (y/n): ")
        
        while (data_nascimento_ultimo_filho != 'y' and data_nascimento_ultimo_filho != 'n'):
            data_nascimento_terceiro_filho = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

        if data_nascimento_ultimo_filho == 'y':
            data_nascimento_ultimo_filho = input("\nQual a data de nascimento? (DDMMAAAA): ")
            while not str.isnumeric(data_nascimento_ultimo_filho) or len(data_nascimento_ultimo_filho) != 8: # Verificando se apenas números foram digitados.
                data_nascimento_ultimo_filho = input("\nDigite \"OITO\" números com a seguinte formatação \"DDYYAAAA\": ")
        else:
            data_nascimento_ultimo_filho = False
else:
    filhos = False

animal_estimacao = str.lower(input("\nPossui animal de estimação? (y/n): "))

while (animal_estimacao != 'y' and animal_estimacao != 'n'):
    animal_estimacao = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if animal_estimacao == 'y':
    animal = True
    animal_estimacao = input("\nQual o nome? ")

    while len(str.split(animal_estimacao)) == 0 or not str.isalpha(animal_estimacao.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        animal_estimacao = input("\nDigite um nome válido: ")

    animal_estimacao =  normalize('NFKD', animal_estimacao).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
else:
    animal = False

empresa_alvo = str.lower(input("\nO \"alvo\" trabalha? (y/n): "))

while (empresa_alvo != 'y' and empresa_alvo != 'n'):
    empresa_alvo = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if empresa_alvo == 'y':
    empregado = True
    empresa_alvo = input("\n Qual o nome da empresa onde o \"alvo\" trabalha? ")

    while len(str.split(empresa_alvo)) == 0 or not str.isalpha(empresa_alvo.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        empresa_alvo = input("\nDigite um nome válido: ")

    empresa_alvo =  normalize('NFKD', empresa_alvo).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
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

    while len(str.split(time)) == 0 or not str.isalpha(time.replace(' ', '')):  # garantindo que o nome não esteja em branco e contenha caracteres não alfabéticos.
        time = input("\nDigite um nome válido: ")

    time =  normalize('NFKD', time).encode('ASCII', 'ignore').decode('ASCII') # Removido os acentos.
else:
    torcedor = False

# Oranizando os dados para facilitar a manipulação:
print("\nAnalisando os dados fornecidos.")

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
    
    if data_nascimento_primeiro_filho != False:
        dia_primeiro_filho = data_nascimento_primeiro_filho[:2]
        mes_primeiro_filho = data_nascimento_primeiro_filho[2:4]
        ano_primeiro_filho = data_nascimento_primeiro_filho[4:]

if filhos == 2:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    
    if data_nascimento_primeiro_filho != False:
        dia_primeiro_filho = data_nascimento_primeiro_filho[:2]
        mes_primeiro_filho = data_nascimento_primeiro_filho[2:4]
        ano_primeiro_filho = data_nascimento_primeiro_filho[4:]

    lista_nomes_segundo_filho = str.split(nome_completo_segundo_filho)
    
    if data_nascimento_segundo_filho != False:
        dia_segundo_filho = data_nascimento_segundo_filho[:2]
        mes_segundo_filho = data_nascimento_segundo_filho[2:4]
        ano_segundo_filho = data_nascimento_segundo_filho[4:]

if filhos == 3:
    lista_nomes_primeiro_filho = str.split(nome_completo_primeiro_filho)
    
    if data_nascimento_primeiro_filho != False:
        dia_primeiro_filho = data_nascimento_primeiro_filho[:2]
        mes_primeiro_filho = data_nascimento_primeiro_filho[2:4]
        ano_primeiro_filho = data_nascimento_primeiro_filho[4:]

    lista_nomes_segundo_filho = str.split(nome_completo_segundo_filho)
    
    if data_nascimento_segundo_filho != False:
        dia_segundo_filho = data_nascimento_segundo_filho[:2]
        mes_segundo_filho = data_nascimento_segundo_filho[2:4]
        ano_segundo_filho = data_nascimento_segundo_filho[4:]

    lista_nomes_terceiro_filho = str.split(nome_completo_terceiro_filho)
    
    if data_nascimento_terceiro_filho != False:
        dia_terceiro_filho = data_nascimento_terceiro_filho[:2]
        mes_terceiro_filho = data_nascimento_terceiro_filho[2:4]
        ano_terceiro_filho = data_nascimento_terceiro_filho[4:]

if filhos > 3:
    lista_nomes_ultimo_filho = str.split(nome_completo_ultimo_filho)
    
    if data_nascimento_ultimo_filho != False:
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

# O arquivo .txt, que conterá a wordlist terá o primeiro nome do usuário.
arquivo = str.capitalize(lista_nomes_alvo[0]) + '.txt'    

# Hora do show!

lista_gravar = []
gravado = True

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

def nomes(lista, data):

    # Esta função, para o exemplo "Junior Alves Quinto Terceiro", nascido em 18081900, cria os seguintes templates:
    # junior; Junior; jUNIOR; JUNIOR; junioalves; JuniorAlves; JUNIORALVES;
    # juniorterceiro; JuniorTerceiro; JUNIORTERCEIRO; JuniorAT; juniorat; JUNIORAT;
    # junior18; Junior18; jUNIOR18; JUNIOR18; junioalves18; JuniorAlves18; JUNIORALVES18;
    # juniorterceiro18; JuniorTerceiro18; JUNIORTERCEIRO18; JuniorAT18; juniorat18; JUNIORAT18;
    # junior1900; Junior1900; jUNIOR1900; JUNIOR1900; junioalves1900; JuniorAlves1900; JUNIORALVES1900;
    # juniorterceiro1900; JuniorTerceiro1900; JUNIORTERCEIRO1900; JuniorAT1900; juniorat1900; JUNIORAT1900;
    # junior90; Junior90; jUNIOR90; JUNIOR90; junioalves90; JuniorAlves90; JUNIORALVES90;
    # juniorterceiro90; JuniorTerceiro90; JUNIORTERCEIRO90; JuniorAT90; juniorat90; JUNIORAT90;

    tamanho = len(lista)

    for i in range(tamanho):
        
        if lista[i] not in lista_gravar:                                     # garantindo que não existam palavras repetidas no .txt
            lista_gravar.append(str.lower(lista[i]))                         # todas minúsculas    
            lista_gravar.append(str.capitalize(lista[i]))                    # apenas a primeira maiúscula
            lista_gravar.append(str.swapcase(str.capitalize(lista[i])))      # primeira minúscula, o resto maiúscula
            lista_gravar.append(str.upper(lista[i]))                         # todas maiúsculas

            if data:
                lista_gravar.append(str.lower(lista[i]+data[:2]))
                lista_gravar.append(str.capitalize(lista[i]+data[:2])) 
                lista_gravar.append(str.swapcase(str.capitalize(lista[i]+data[:2])))
                lista_gravar.append(str.upper(lista[i]+data[:2]))
                lista_gravar.append(str.lower(lista[i]+data[4:]))
                lista_gravar.append(str.capitalize(lista[i]+data[4:])) 
                lista_gravar.append(str.swapcase(str.capitalize(lista[i]+data[4:])))
                lista_gravar.append(str.upper(lista[i]+data[4:]))  
                lista_gravar.append(str.lower(lista[i]+data[6:]))
                lista_gravar.append(str.capitalize(lista[i]+data[6:])) 
                lista_gravar.append(str.swapcase(str.capitalize(lista[i]+data[6:])))
                lista_gravar.append(str.upper(lista[i]+data[6:]))                  


    if tamanho == 2:
        lista_gravar.append(str.lower(lista[0]+lista[1]))                       # primeiro nome + segundo nome, minúsculos
        lista_gravar.append(str.upper(lista[0]+lista[1]))                       # primeiro nome + segundo nome, maiúsculos
        lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]))  # primeiro nome + segundo nome, com as iniciais maiúsculas

        if data:
            lista_gravar.append(str.lower(lista[0]+lista[1]+data[:2]))                       
            lista_gravar.append(str.upper(lista[0]+lista[1]+data[:2]))                       
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]+data[:2])) 
            lista_gravar.append(str.lower(lista[0]+lista[1]+data[4:]))                       
            lista_gravar.append(str.upper(lista[0]+lista[1]+data[4:]))                       
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]+data[4:]))
            lista_gravar.append(str.lower(lista[0]+lista[1]+data[6:]))                       
            lista_gravar.append(str.upper(lista[0]+lista[1]+data[6:]))                       
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]+data[6:]))    
        

    if tamanho > 2:
        lista_gravar.append(str.lower(lista[0]+lista[1]))                       # primeiro nome + segundo nome, minúsculos
        lista_gravar.append(str.upper(lista[0]+lista[1]))                       # primeiro nome + segundo nome, maiúsculos
        lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]))  # primeiro nome + segundo nome, com as iniciais maiúsculas
        lista_gravar.append(str.lower(lista[0]+lista[-1]))                      # primeiro e último nome, minúsculos
        lista_gravar.append(str.upper(lista[0]+lista[-1]))                      # primeiro e último nome, maiúsculos
        lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[-1])) # primeiro e último nome, com as iniciais maiúsculas

        if data:
            lista_gravar.append(str.lower(lista[0]+lista[1]+data[4:]))                       
            lista_gravar.append(str.upper(lista[0]+lista[1]+data[4:]))                       
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]+data[4:]))  
            lista_gravar.append(str.lower(lista[0]+lista[-1]+data[4:]))                      
            lista_gravar.append(str.upper(lista[0]+lista[-1]+data[4:]))                      
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[-1]+data[4:]))
            lista_gravar.append(str.lower(lista[0]+lista[1]+data[:2]))                       
            lista_gravar.append(str.upper(lista[0]+lista[1]+data[:2]))                       
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]+data[:2]))  
            lista_gravar.append(str.lower(lista[0]+lista[-1]+data[:2]))                      
            lista_gravar.append(str.upper(lista[0]+lista[-1]+data[:2]))                      
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[-1]+data[:2]))
            lista_gravar.append(str.lower(lista[0]+lista[1]+data[6:]))                       
            lista_gravar.append(str.upper(lista[0]+lista[1]+data[6:]))                       
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[1]+data[6:]))  
            lista_gravar.append(str.lower(lista[0]+lista[-1]+data[6:]))                      
            lista_gravar.append(str.upper(lista[0]+lista[-1]+data[6:]))                      
            lista_gravar.append(str.capitalize(lista[0])+str.capitalize(lista[-1]+data[6:]))
        
    temp = str.capitalize(lista[0])

    for a in range(tamanho-1):
        temp += str.upper(lista[a+1][0])

    if temp not in lista_gravar:
        lista_gravar.append(temp)
        lista_gravar.append(str.lower(temp))
        lista_gravar.append(str.upper(temp))

        if data:
            lista_gravar.append(temp+data[:2])
            lista_gravar.append(str.lower(temp+data[:2]))
            lista_gravar.append(str.upper(temp+data[:2]))
            lista_gravar.append(temp+data[4:])
            lista_gravar.append(str.lower(temp+data[4:]))
            lista_gravar.append(str.upper(temp+data[4:]))
            lista_gravar.append(temp+data[6:])
            lista_gravar.append(str.lower(temp+data[6:]))
            lista_gravar.append(str.upper(temp+data[6:]))



nomes(lista_nomes_alvo, data_nascimento_alvo)

if casado:
 nomes(lista_nomes_conjuge, data_nascimento_conjuge)

if filhos == 1:
 nomes(lista_nomes_primeiro_filho, data_nascimento_primeiro_filho)

if filhos == 2:
 nomes(lista_nomes_primeiro_filho, data_nascimento_primeiro_filho)
 nomes(lista_nomes_segundo_filho, data_nascimento_segundo_filho)

if filhos == 3:
 nomes(lista_nomes_primeiro_filho, data_nascimento_primeiro_filho)
 nomes(lista_nomes_segundo_filho, data_nascimento_segundo_filho)
 nomes(lista_nomes_terceiro_filho, data_nascimento_terceiro_filho)

if filhos > 3:
 nomes(lista_nomes_ultimo_filho, data_nascimento_ultimo_filho)    

gravar(lista_gravar)

print("\nGerando wordlist.")

if gravado:
    print("Wordlist " +arquivo+ " criada com sucesso.\n")
else:
    print("Wordlist não pode ser gravada!\n")

