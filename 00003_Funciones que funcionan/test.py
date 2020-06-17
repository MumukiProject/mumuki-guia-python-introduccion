#...content...#
#...extra...#


class Test(unittest.TestCase):
    def test_probamos_la_funcion_leer_mente_con_varias_entradas(self):
      for entrada in range(-1, 2):
            self.assertEqual(entrada / 2, leer_mente(entrada))
