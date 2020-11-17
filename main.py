from nprimo import GeradorNumeroPrimo
from chaves import Chaves
from cript import *

p = GeradorNumeroPrimo()
numero_p = p.numero_primo
print('\nP :', str(numero_p))

q = GeradorNumeroPrimo()
numero_q = q.numero_primo
print('Q :', str(numero_q), '\n')

chaves = Chaves(numero_p, numero_q)
chaves.gerar_chaves()

escolha_sair = ''
while escolha_sair != 'sair':
    print('1 - Criptografia\n'
          '2 - Descriptografia')
    opcao = int(input('Escolha a opcao desejada: '))
    if opcao == 1:
        encriptamsg = chaves.encripta()
    if opcao == 2:
        msgencrip = input('Digite a mensagem encriptada: ')
        chaves.decripta(msgencrip)
    escolha_sair = str(input('Digite "sair" caso tenha terminado: '))
