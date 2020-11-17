
def encripta(self):
    s = input("Digite a mensagem: \t")
    print('=' * 5 + ' Digite as chaves públicas: ' + '=' * 5)
    e = int(input("Chave e: \t"))
    n = int(input("Chave n: \t"))
    encri = ''.join(chr(self.criptografia(ord(x), e, n)) for x in s)
    print('Texto a ser cifrado', encri, '\n')
    return encri


def decripta(self, s):
    self.s = s
    print('=' * 5 + ' Chaves privadas : ' + '=' * 5)
    d = int(input("Chave d: \t"))
    n = int(input("Chave n: \t"))
    decri = ''.join(chr(self.descriptografia(ord(x), d, n)) for x in s)
    return print('Simples ', decri, '\n')


class Criptografia(object):

    def criptografia(self, m, e, n):
        c = (m ** e) % n
        return c

    def descriptografia(self, c, d, n):
        m = c ** d % n
        return m

    def encripta(self):
        s = input("Digite a mensagem: \t")
        print('=' * 5 + ' Digite as chaves públicas: ' + '=' * 5)
        e = int(input("Chave e: \t"))
        n = int(input("Chave n: \t"))
        encri = ''.join(chr(self.criptografia(ord(x), e, n)) for x in s)
        print('Texto a ser cifrado', encri, '\n')
        return encri

    def decripta(self, s):
        self.s = s
        print('=' * 5 + ' Chaves privadas : ' + '=' * 5)
        d = int(input("Chave d: \t"))
        n = int(input("Chave n: \t"))
        decri = ''.join(chr(self.descriptografia(ord(x), d, n)) for x in s)
        return print('Simples ', decri, '\n')
