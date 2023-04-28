import xmlrpc.client

def imprime_matriz(tabuleiro):
    for i in range(7):
      for j in range(7):
        print(tabuleiro[i][j], end=' ')
      print()

def main():

  cliente = xmlrpc.client.ServerProxy('http://localhost:8000')
  
  print("Digite o seu nome: ")
  nome = input()
  cadastrado = cliente.cadastra_jogador(nome)
  while cadastrado == False:
    print("Digite o seu nome: ")
    nome = input()
    cadastrado = cliente.cadastra_jogador(nome)
  print("Aguardando o outro jogador...")

  # while not cliente.verifica_inicio():
  while not cliente.verifica_vitoria():
    if(cliente.status_jogo()):
      print("Jogo em andamento...")
      if(cliente.verifica_vez(nome)):
          tabuleiro = cliente.retorna_matriz()
          imprime_matriz(tabuleiro)
          linha = input()
          linha = int(linha)
          coluna = input()
          coluna = int(coluna)
          # while (cliente)
          cliente.faz_jogada(linha, coluna, nome)

main()