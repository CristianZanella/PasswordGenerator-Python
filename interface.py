#Mostra uma linha
def linha():
    print("=" * 37)

#Mostra um cabeçalho
def cabecalho(mensagem = "<vazio>"):
    linha()
    print(f"{mensagem:^37}")
    linha()
