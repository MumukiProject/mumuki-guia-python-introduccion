#...content...#
#...extra...#


class Test(unittest.TestCase):
      def test_prueba_con_varias_entradas(self):
      for entrada in range(-1, 2):
          salida_esperada=entrada / 2
          salida=leer_mente(entrada)
          self.assertEqual(salida_esperada,salida,f" en otras palabras: la salida de leer_mente({entrada}), fué {salida} , pero <b>esperábamos que fuera {salida_esperada}. Probá nuevamente, #...user_first_name...#</b>")
