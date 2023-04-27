import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer

servidor = SimpleXMLRPCServer(('localhost',8000))

# tabuleiro 7x7
tabuleiro = [ ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-']]

def add(x,y):
    return x+ y

servidor.register_function(add, 'add')

para=False

def imprime_matriz():
    for i in range(7):
      for j in range(7):
        print(tabuleiro[i][j], end=' ')
      print()


def verifica_coord(linha, coluna):
  if(tabuleiro[linha-1][coluna-1]):
    return True
  else:
    return False


def le_entrada(cont):
    valores = []
    linha = -1
    coluna = -1
    
    if(cont == 3):
      cont = 1
    while linha < 0 or linha > 6:
      print("Escolha uma posição válida para a linha: ")
      linha = input()
      linha = int(linha)
    
    while coluna < 0 or coluna > 6:
      print("Agora escolha uma posição válida para a coluna: ")
      coluna = input()
      coluna = int(coluna)
    
    valores.append(linha)
    valores.append(coluna)
    valores.append(cont)
    return valores

def verifica_diagonal():
  for i in range(4):
      for j in range(7):
        if((tabuleiro[i][j] and tabuleiro[i+1][j+1] and tabuleiro[i+2][j+2]+tabuleiro[i+3][j+3])):
          print("Vitoria!")
  return


def verifica_hori():
  for i in range(7):
      for j in range(4):
        if((tabuleiro[i][j] == tabuleiro[i][j+1] == tabuleiro[i][j+2]+tabuleiro[i][j+3]) ):
          print("Vitoria!")
          return True
        else:
          return


def verifica_vert():
    for i in range(4):
      for j in range(7):
        if((tabuleiro[j][i] == tabuleiro[j+1][i] == tabuleiro[j+2][i]+tabuleiro[j+3][i]) ):
          print("Vitoria!")
          return True
        else:
          return


def verifica_vitoria():
  # if(verifica_diagonal()):
  #   print("Fim de jogo!")
  if(verifica_hori()):
    print("Fim de jogo!")
    return True
  elif(verifica_vert()):
    print("Fim de jogo!")
    return True
  else:
    return ("erro")
  

def verifica_vazio(linha, coluna):
  i=0
  j=0
  if(tabuleiro[linha-1][coluna-1] == '-'):
    # if (cont % 2 == 1):
    #   tabuleiro[linha-1][coluna-1] = 'x'
    #   para = verifica_vitoria()
    # elif(cont % 2 != 1):
    #   tabuleiro[linha-1][coluna-1] = 'o'
    #   para = verifica_vitoria()
    # elif(verifica_vitoria()):
    #   imprime_matriz()
    #   exit()
    
    para = verifica_vitoria()
    tabuleiro[linha-1][coluna-1] = 'x'
    imprime_matriz()
    return para
    
  else:
    print("Espaço não disponível")

servidor.register_function(verifica_vazio, 'verifica_vazio')

def main():
  # if(verifica_vitoria()):
  #   print( "\n")
  #   print(" Fim de Jogo!")
  #   print( "\n")
  #   imprime_matriz()
  # return
  # jogadas = 49
  cont=1
  n=0
  # for n in range(100):
  while not para:
    jogador = le_entrada(cont)
    if(jogador[2] == 3):
      cont = 1
    else:
      cont = cont +1
    print(jogador)
    resultado = verifica_coord(jogador[0], jogador[1])

    if(resultado == True):
      verifica_vazio(jogador[0], jogador[1], cont)

# main()

servidor.serve_forever()