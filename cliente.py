import xmlrpc.client

def imprime_matriz(tabuleiro):
    for i in range(7):
      for j in range(7):
        print(tabuleiro[i][j], end=' ')
      print()

def main():

  cliente = xmlrpc.client.ServerProxy('http://127.0.0.1:50080')
  
  print("Digite o seu nome: ")
  nome = input()
  cadastrado = cliente.cadastra_jogador(nome)
  while cadastrado == False:
    print("Digite o seu nome: ")
    nome = input()
    cadastrado = cliente.cadastra_jogador(nome)
  print("Aguardando o outro jogador...")

  vitoria = cliente.verifica_vitoria()
  while not vitoria:
    if(cliente.status_jogo()):
      if(cliente.verifica_vez(nome)):
          tabuleiro = cliente.retorna_matriz()
          imprime_matriz(tabuleiro)

          print("\n Faça sua jogada: (linha, coluna)")
          linha = input()
          linha = int(linha)

          coluna = input()
          coluna = int(coluna)
          
          jogada_valida = cliente.faz_jogada(linha, coluna, nome)
          while(jogada_valida == False):
            print("Jogada inválida! Faça novamente sua jogada: (linha, coluna)")
            linha = input()
            linha = int(linha)

            coluna = input()
            coluna = int(coluna)
            jogada_valida = cliente.faz_jogada(linha, coluna, nome)
            
    vitoria = cliente.verifica_vitoria()

  print("Fim de jogo!")
main()