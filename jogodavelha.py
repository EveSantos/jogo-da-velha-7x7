import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer

servidor = SimpleXMLRPCServer(('127.0.0.1',50080), allow_none=True)

# tabuleiro 7x7
tabuleiro = [   ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-'],
                ['-', '-', '-', '-', '-', '-', '-']]

# dicionario
dicionario = {}

vencedor = None

para=False

def armazena_vencedor(nome):
  global vencedor
  vencedor = nome
  return vencedor

def retorna_vencedor():
  global vencedor
  return vencedor

def retorna_matriz():
  return tabuleiro

def le_entrada(linha, coluna):
    if linha < 0 or linha > 6:
      return False

    if coluna < 0 or coluna > 6:
      return False

def verifica_diagonal():
  for i in range(3):
      for j in range(6):
        if((tabuleiro[i][j] == 'x' and tabuleiro[i+1][j+1] == 'x' and tabuleiro[i+2][j+2]== 'x' and tabuleiro[i+3][j+3]) == 'x'):
          return True
        if((tabuleiro[i][j] == 'o' and tabuleiro[i+1][j+1] == 'o' and tabuleiro[i+2][j+2]== 'o' and tabuleiro[i+3][j+3]) == 'o'):
          return True
  # matriz secundaria
  for i in range(3):
      for j in range(6, 2, -1):
        if((tabuleiro[i][j] == 'x' and tabuleiro[i+1][j-1] == 'x' and tabuleiro[i+2][j-2]== 'x' and tabuleiro[i+3][j-3] == 'x')):
          return True
        if (tabuleiro[i][j] == 'o' and tabuleiro[i+1][j-1] == 'o' and tabuleiro[i+2][j-2]== 'o' and tabuleiro[i+3][j-3] == 'o'):
          return True
  
  return False


def verifica_hori():
  for i in range(6):
    for j in range(3):
      if((tabuleiro[i][j] == 'x' and tabuleiro[i][j+1]== 'x' and tabuleiro[i][j+2] == 'x' and tabuleiro[i][j+3]) == 'x'):
        return True
      if((tabuleiro[i][j] == 'o' and tabuleiro[i][j+1]== 'o' and tabuleiro[i][j+2]== 'o' and tabuleiro[i][j+3]) == 'o'):
        return True
  return False

def verifica_vert():
    for i in range(3):
      for j in range(6):
        if((tabuleiro[j][i] == 'x' and tabuleiro[j+1][i] == 'x' and tabuleiro[j+2][i] == 'x' and tabuleiro[j+3][i]) == 'x'):
          return True
        elif((tabuleiro[j][i] == 'o' and tabuleiro[j+1][i] == 'o' and tabuleiro[j+2][i] == 'o' and tabuleiro[j+3][i]) == 'o'):
          return True
    return False

def verifica_vitoria():
  if(verifica_diagonal()):
    return True
  elif(verifica_hori()):
    return True
  elif(verifica_vert()):
    return True
  else:
    return False

def faz_jogada(linha, coluna, nome):
  if(tabuleiro[linha][coluna] == '-'):
    tabuleiro[linha][coluna] = dicionario[nome]["caracter"]
    dicionario[nome]["vez"] = False
    for chave in dicionario:
      if not chave == nome:
        dicionario[chave]["vez"] = True
    return True
  else:
    return False


def cadastra_jogador(nome):
  global dicionario
  if(len(dicionario) == 2):
    return -1
  if dicionario == {}:
    dicionario[nome] = {"caracter":'x', "vez":True}
  elif not nome in dicionario:
    dicionario[nome] = {"caracter":'o', "vez":False}
  else:
    return False 
  return True

def verifica_vez(nome):
  global dicionario
  return dicionario[nome]["vez"]

def status_jogo():
  global dicionario
  if(len(dicionario) == 2 and not verifica_vitoria()):
    return True
  else:
    return False

servidor.register_function(cadastra_jogador, 'cadastra_jogador')
servidor.register_function(faz_jogada, 'faz_jogada')
servidor.register_function(verifica_vitoria, 'verifica_vitoria')
servidor.register_function(verifica_vez, 'verifica_vez')
servidor.register_function(retorna_matriz, 'retorna_matriz')
servidor.register_function(status_jogo, 'status_jogo')
servidor.register_function(retorna_vencedor, 'retorna_vencedor')
servidor.register_function(armazena_vencedor, 'armazena_vencedor')

servidor.serve_forever()