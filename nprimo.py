from random import randrange, getrandbits


class GeradorNumeroPrimo:

    def __init__(self):
        self.numero_primo = self.gerar_numero_primo()

    def teste_miller_rabin(self, n, k=128):

        if n < 6:  # válida alguns casos
            return [False, False, True, True, False, True][n]

        if n <= 1 or n % 2 == 0:
            return False

        s = 0
        r = n - 1
        while r & 1 == 0:
            s += 1
            r //= 2

        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, r, n)
            if x != 1 and x != n - 1:
                j = 1
                while j < s and x != n - 1:
                    x = pow(x, 2, n)
                    if x == 1:
                        return False
                    j += 1
                if x != n - 1:
                    return False
        return True

    def tentativa_de_numero(self, tamanho):

        self.numero_primo = getrandbits(tamanho)

        self.numero_primo |= (1 << tamanho - 1) | 1
        return self.numero_primo

    def gerar_numero_primo(self, tamanho=5):

        self.numero_primo = 4

        while not self.teste_miller_rabin(self.numero_primo, 128):
            self.numero_primo = self.tentativa_de_numero(tamanho)
        return self.numero_primo
