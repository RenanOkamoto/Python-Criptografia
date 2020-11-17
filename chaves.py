from cript import Criptografia


class Chaves(Criptografia):

    def __init__(self, p, q):
        self.p = p
        self.q = q

    def gerar_chaves(self):
        n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)

        print("CHAVES PUBLICAS:\n")
        print(str(self.coprimos(phi)) + "\n")  # calculo da chave pública mdc(phi(N), E) == 1
        while True:
            e = int(input('Insira uma chave de sua escolha: '))
            if e not in self.coprimos(phi):
                print(f'{e} nao pode ser uma chave publica...')
                pass
            else:
                break
        d = self.inverso_modular(e, phi)
        return print(
            "\nGuarde esses valores para a descriptografia!\nPúblicas (e=" + str(e) + ", n=" + str(n) + ")" + "\nPrivadas (d=" + str(d) + ", n=" + str(n) + ")\n")

    def mdc(self, a, b):
        while a != 0:
            a, b = b % a, a
        return b

    def inverso_modular(self, a, m):
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        print('Não ha inverso\n')
        return None

    def coprimos(self, a):
        l = []
        for x in range(2, a):
            if self.mdc(a, x) == 1 and self.inverso_modular(x, a) != None:  # MDC(φ(n), e) = 1
                l.append(x)
        for x in l:
            if x == self.inverso_modular(x, a):
                l.remove(x)
        return l
