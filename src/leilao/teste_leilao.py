from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario("Gui")
        self.lance_do_gui = Lance(self.gui, 150.0)
        self.leilao = Leilao("Celular")

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        yuri = Usuario("Yuri")
        lance_do_yuri = Lance(yuri, 100.0)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)



        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_decrescente(self):
        yuri = Usuario("Yuri")
        lance_do_yuri = Lance(yuri, 100.0)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)



        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_varios_lances(self):
        yuri = Usuario("Yuri")
        lance_do_yuri = Lance(yuri, 100.0)
        arthur = Usuario("Arthur")
        lance_do_arthur = Lance(arthur, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_arthur)



        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        yuri = Usuario("Yuri")
        lance_do_yuri = Lance(yuri, 100.0)
        self.leilao.propoe(self.lance_do_gui)


        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)
