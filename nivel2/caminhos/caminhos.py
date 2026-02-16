#módulo OS (operation System): permite criar interfaces com o sistema operacional

#Caminhos

#absoluto = "/home/jp/dev/estudo/python-do-jeito-certo/python-jeito-certo/nivel2/caminhos/caminhos.py"

#relativo = "python-jeito-certo/nivel2/caminhos/caminhos.py"

import os

#exibir o endereço absoluto de uma pasta/arquivo
# AGREGADOS_DIR = "agregados"
# print(os.path.abspath(AGREGADOS_DIR))

#exibir o arquivo independente do sistema operacional
# caminho = os.path.join(os.path.abspath(AGREGADOS_DIR), "agregados.py")
# print(caminho)

#pedir o nome de todos os arquivos que estejam em um diretório específico

# print(os.listdir("python-jeito-certo/nivel2"))

# modulos_python = []
# for nome in os.listdir("python-jeito-certo/nivel2"):
#     if nome.endswith(".py"):
#         modulos_python.append(nome)

# print(modulos_python)

OUTPUT_DIR = "saidas"
nomearquivo = "mensagem.txt"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    
#achar/criar na pasta "saidas" o arquivo "mensagem.txt"
with open(os.path.join(OUTPUT_DIR, nomearquivo), 'w') as arq:
    arq.write("Vá estudar, vagabundo")
    

#Atividade
#Criar um programa para organizar arquivos em pastas dependendo da extensão deles ou tipos de dados
#ler os nomes, criar as pastas e enviar