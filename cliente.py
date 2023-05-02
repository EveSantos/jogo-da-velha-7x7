import xmlrpc.client
import time

def imprime_matriz(tabuleiro):
    print(" | 0 1 2 3 4 5 6")
    print("-----------------")
    for i in range(7):
      for j in range(7):
        if(j == 0):
           print(str(i)+ "| " +tabuleiro[i][j], end=' ')
        else:
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
          entrada = input()
          entrada = entrada.split(",")

          linha = int(entrada[0])
          coluna = int(entrada[1])
          
          jogada_valida = cliente.faz_jogada(linha, coluna, nome)
          while(jogada_valida == False):
            print("Jogada inválida! Faça novamente sua jogada: (linha, coluna)")
            entrada = input()
            entrada = entrada.split(",")
   
            linha = int(entrada[0])
            coluna = int(entrada[1])

            jogada_valida = cliente.faz_jogada(linha, coluna, nome)
          print("\n Aguardando o outro jogador\n")
    vitoria = cliente.verifica_vitoria()
    
    time.sleep(0.5)

  print("Fim de jogo!")
main()