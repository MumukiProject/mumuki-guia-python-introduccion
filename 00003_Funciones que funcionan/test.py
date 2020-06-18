#...content...#
#...extra...#
#...user_first_name...#


class Test(unittest.TestCase):
  def test_probamos_con_varias_entradas(self):
    for entrada in range(-1, 2):
      salida_esperada=entrada / 5
      salida=leer_mente(entrada)
      self.assertEqual(salida_esperada,salida,f" en otras palabras: la salida de leer_mente({entrada}), fué {salida} , pero esperábamos que fuera {salida_esperada}")
