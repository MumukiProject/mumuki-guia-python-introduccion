/*...extra...*/
/*...content...*/
import datetime


class Test(unittest.TestCase):

  def test_probemos_leer_mente(self):
    ejercicio_mente.a_veeer()
    antes=ejercicio_mente.ahora()
    ejercicio_mente.pausa_print("impreso a las {}".format(antes))
    despues=ejercicio_mente.ahora()
    print("intervalo: {} segundos".format(despues-antes))
    for entrada in range(-1,2):
      self.assertEqual(entrada/2,leer_mente(entrada))