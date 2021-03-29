from src.leilao.Excecoes import Lance_invalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if not self._valor_eh_valido(valor): # verifica se o valor do lance é maior que o saldo da carteira
            raise Lance_invalido('Valor do lance maior que saldo da carteira')
        else:
            lance = Lance(self, valor)
            leilao.propoe(lance)
            self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_eh_valido(self, valor):
        return valor <= self.__carteira

class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances():
                self.menor_lance = lance.valor

            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise Lance_invalido("Erro ao propor lance")

    @property
    def lances(self):
        return self.__lances[:] # devolve uma cópia rasa da lista

    def _tem_lances(self):
        return self.__lances

    def usuarios_diferentes(self, lance): # verifica se o ultimo lance foi feito por um usuario diferente do que quer fazer
        if self.__lances[-1].usuario != lance.usuario:
            return True
        else:
            raise Lance_invalido('O mesmo usuário não pode dar 2 lances seguidos!')

    def valor_maior_que_lance_anterior(self, lance): # verifica se o lance é maior que o lance anterior
        if lance.valor > self.__lances[-1].valor:
            return True
        else:
            raise Lance_invalido('O Valor do lance deve ser maior que o lance anterior!')

    def _lance_eh_valido(self, lance):
        return not self._tem_lances() or (self.usuarios_diferentes(lance) and
                                   self.valor_maior_que_lance_anterior(lance))








