# Estudo feito pela Axur mostra o perfil de senhas do brasileiro: 
# https://blog.axur.com/pt/infografico-perfil-da-senha-do-brasileiro
# Este estudo me fez adicionar outros templates de senha.

# Para remover acentos e ç dos nomes;
# Retirado de: https://wiki.python.org.br/RemovedorDeAcentos
# Medida adotada, pois caracteres assim não são aceitos em redes wifi.
from unicodedata import normalize
from datetime import date

print ("""  
: Criando uma wordlist personalizada.
: 13.06.2019
: Jim Nadab.
            
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

    # Garantindo que os conectivos "do, de, da, dos e das" não sejam levados em conta.
    lista = []
    nome = str.split(nome)
    for i in range(len(nome)):
        if len(nome[i]) == 1:
            pass
        elif (len(nome[i]) == 2) and ((nome[i] == 'do') or (nome[i] == 'de') or (nome[i] == 'da')):
            pass
        elif (len(nome[i]) == 3) and ((nome[i][:3] == 'dos') or (nome[i][:3] == 'das')):
            pass
        else:
            lista.append(nome[i])

    return lista

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

evangelico = str.lower(input("\nO \"alvo\" é evangélico? (y/n): "))
while (evangelico != 'y' and evangelico != 'n'):
    evangelico = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if evangelico == 'y':
    evangelico = True
else:
    evangelico = False

time = str.lower(input("\nO \"alvo\" torce por algum time? (y/n): "))

while (time != 'y' and time != 'n'):
    time = str.lower(input("\nResponda apenas \"y\" ou \"n\": "))

if time == 'y':
    time = input("\nQual? ")
    time = bons_nomes(time)
else:
    time = False

# Caso seja evangélico, será tratado mais a frente.

# O arquivo .txt que conterá a wordlist terá o primeiro nome do usuário.
arquivo = str.capitalize(nome_completo_alvo[0]) + '.txt'    

# Inicio dos trabalhos!
gravado = True
lista_provisoria = []
lista_final = []

def gravar(lista):

    global gravado
    
    # Se a lista estiver vazia, nada será gravado!
    if len(lista) == 0:
        gravado = False
        return
    else:
        f = open(arquivo, 'w')

        for x in range(len(lista)):
            # para que não existam palavras menores que "tamanho_minimo"
            if len(lista[x]) < int(tamanho_minimo):
                pass
            else:
                # para que não existam palavras repetidas na wordlist
                if lista[x] not in lista_final:
                    lista_final.append(lista[x])

        for i in range(len(lista_final)):
            f.write(lista_final[i]+'\n')        
        
        f.close()

def casados(lista1, lista2, data):
    lista_provisoria.append(lista1[0]+'&'+lista2[0])
    
    if data:
        lista_provisoria.append(lista1[0]+'&'+lista2[0]+data)
        lista_provisoria.append(lista1[0]+'&'+lista2[0]+data[-6:])
        lista_provisoria.append(lista1[0]+'&'+lista2[0]+data[-4:])
        lista_provisoria.append(lista1[0]+'&'+lista2[0]+data[:2])

def letras_e_numeros(lista, data):
    
    listavazia = []

    # para adicionar numeros de 1 a 6 as palavras.
    for i in range(len(lista)):
        listavazia.append(lista[i])

        numeros = ''
        z = 1
        while z < 7:
            numeros += str(z) 
            listavazia.append(lista[i]+numeros)
            z += 1

    if data:
        for i in range(len(lista)):
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
            listavazia.append(str.lower(lista[i]))                            # tudo minúsculo    
            listavazia.append(str.capitalize(lista[i]))                       # Primeira maiúscula
            listavazia.append(str.swapcase(str.capitalize(lista[i])))         # primeira minúscula, o resto maiúsculo
            listavazia.append(str.upper(lista[i]))                            # Tudo maiúsculo

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

    # para unir o primeiro nome com as demais iniciais
    temp = str.capitalize(lista[0])                 

    for a in range(tamanho - 1):
        temp += str.upper(lista[a+1][0])        

    if temp not in listavazia:
        listavazia.append(temp)
        listavazia.append(str.lower(temp))
        listavazia.append(str.upper(temp))

    # para unir as iniciais
    temp2 = str.lower(lista[0][0])                  

    for a in range(tamanho - 1):
        temp2 += str.lower(lista[a+1][0])

    if temp2 not in listavazia:
        listavazia.append(temp2)
        listavazia.append(str.upper(temp2))
    
    letras_e_numeros(listavazia, data)


so_letras(nome_completo_alvo, data_nascimento_alvo)

if casado:
    so_letras(nome_completo_conjuge, data_nascimento_conjuge)
    casados(nome_completo_alvo, nome_completo_conjuge, data_casamento)

if filhos == 1:
    so_letras(nome_completo_primeiro_filho, data_nascimento_primeiro_filho)

if filhos == 2:
    so_letras(nome_completo_primeiro_filho, data_nascimento_primeiro_filho)
    so_letras(nome_completo_segundo_filho, data_nascimento_segundo_filho)

if filhos == 3:
    so_letras(nome_completo_primeiro_filho, data_nascimento_primeiro_filho)
    so_letras(nome_completo_segundo_filho, data_nascimento_segundo_filho)
    so_letras(nome_completo_terceiro_filho, data_nascimento_terceiro_filho)

if filhos > 3:
    so_letras(nome_completo_ultimo_filho)

if animal_estimacao != False:
    so_letras(animal_estimacao, False) # Já passando a data como False.

if evangelico != False:

    data_atual = date.today()

    palavras_comuns = ['Jesus', 'jesus', 'Cristo', 'cristo', 'Deus', 'deus', 
        'Jesusvoltara', 'jesusvoltara', 'sojesussalva', 'jesusestavoltando',  
        'soJesussalva', 'Jesusestavoltando', 'EspiritoSanto', 'JesusCristo', 
        'espiritosanto', 'jesuscristo']

    for i in range(len(palavras_comuns)):
        lista_provisoria.append(palavras_comuns[i])

        x = 0

        while x < 4:
            lista_provisoria.append(palavras_comuns[i]+str(data_atual.year - x))
            x += 1

if time != False:

    # unindo os possíveis nomes compostos dos times
    time_junto = ''
    for i in range(len(time)):
        time_junto += time[i]

    # rebaixando a caixa para comparar com as chaves dos dicionarios
    time_junto = time_junto.lower() 

    dicionario_times = {'vasco': ['vasco', 'vascao'], 'saopaulo': ['saopaulo', 'tricolor'], 
        'santos': ['santos', 'peixe'], 'palmeiras': ['palmeiras', 'verdao'], 
        'internacional': ['internacional', 'inter',], 'gremio': ['gremio', 'imortal'], 
        'fluminense': ['fluminense', 'fluzao'], 'flamengo': ['flamengo', 'mengao', 'urubu'], 
        'botafogo': ['botafogo', 'fogao'], 'corinthians': ['corinthians', 'corintias', 'timao']}
    
    # caso o time pertença ao dicionario, ele estrará na wordlist
    if time_junto in dicionario_times:
        so_letras(dicionario_times[time_junto], False)


gravar(lista_provisoria)

print("\nGerando wordlist.")

if gravado:
    print("Wordlist " +arquivo+ " criada com sucesso.\n")
else:
    print("Wordlist não pode ser gravada, pois os dados fornecidos são insuficientes!\n")
