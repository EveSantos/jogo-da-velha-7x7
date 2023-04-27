import xmlrpc.client

cliente = xmlrpc.client.ServerProxy('http://localhost:8000')

# resultado = cliente.add(3,4)

jogada = cliente.verifica_vazio(2,3)
print(jogada)
# print(resultado)