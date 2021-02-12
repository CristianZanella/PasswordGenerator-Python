from funcoes import * #Importa funções do arquivo "interface.py"
from interface import * #Importa funções do arquivo "funcoes.py"

cabecalho("GERADOR DE SENHAS")

quant = quant_senhas()
tam = tam_senhas()

senhas = gerador_senhas(quant, tam)

cabecalho("SAINDO...")
