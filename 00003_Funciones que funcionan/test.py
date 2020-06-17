#...content...#
#...extra...#


class Test(unittest.TestCase):
    def test_probamos_con_varias_entradas(self):
      for entrada in range(-1, 2):
          salida_esperada=entrada / 2
          salida=leer_mente(entrada)
          self.assertEqual(salida_esperada,salida,f"la salida de leer_mente({entrada}), es {salida} , pero esperábamos que fuera {salida_esperada}")
