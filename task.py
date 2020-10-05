# Import the library to work with json files
import json

# Open source_file_2.json as read file
with open('source_file_2.json', 'r') as json_file:
    dados = json.load(json_file)

# Create the list to receive the managers, watchers and projects
lista_projetos = []
lista_prioridade = []

lista_gerentes = [nome_gerente for chave, gerentes in enumerate(dados) for nome_gerente in gerentes['managers']]
lista_expectadores = [nome_expectador for ch, expectadores in enumerate(dados) for nome_expectador in
                      expectadores['watchers']]

# After collect all managers, I eliminate duplicity
lista_gerentes_unicos = list(set(lista_gerentes))
lista_gerentes_unicos.sort()
# After collect all watchers, I eliminate duplicity
lista_expectadores_unicos = list(set(lista_expectadores))
lista_expectadores_unicos.sort()

# Create the dictionary with manager and its projects
arq_managers = {}
arquivo_managers = {}
arq_watchers = {}
arquivo_watchers = {}

for indice in range(len(lista_gerentes_unicos)):
    for chave, gerentes in enumerate(dados):
        if lista_gerentes_unicos[indice] in gerentes['managers']:
            lista_projetos.append(dados[chave]['name'])
            lista_prioridade.append(dados[chave]['priority'])

    todos_projetos = list(zip(lista_prioridade, lista_projetos))
    todos_projetos.sort()

    arq_managers[lista_gerentes_unicos[indice]] = todos_projetos

    lista_projetos.clear()
    lista_prioridade.clear()

# Create and save file managers.json
with open('managers.json', 'w') as json_file_managers:
    for i in range(len(lista_gerentes_unicos)):
        for gerente, projetos in arq_managers.items():
            arquivo_managers[gerente] = [projetos[chave][1] for chave, proj in enumerate(projetos)]
    json.dump(arquivo_managers, json_file_managers, indent=4)

for indice in range(len(lista_expectadores_unicos)):
    for chave, expectadores in enumerate(dados):
        if lista_expectadores_unicos[indice] in expectadores['watchers']:
            lista_projetos.append(dados[chave]['name'])
            lista_prioridade.append(dados[chave]['priority'])

    todos_projetos = list(zip(lista_prioridade, lista_projetos))
    todos_projetos.sort()

    arq_watchers[lista_expectadores_unicos[indice]] = todos_projetos

    lista_projetos.clear()
    lista_prioridade.clear()

# Create and save file watchers.json
with open('watchers.json', 'w') as json_file_watchers:
    for i in range(len(lista_expectadores_unicos)):
        for expectador, projetos in arq_watchers.items():
            arquivo_watchers[expectador] = [projetos[chave][1] for chave, proj in enumerate(projetos)]
    json.dump(arquivo_watchers, json_file_watchers, indent=4)
