import datetime
from extra import ejercicio_mente

print=ejercicio_mente.print

class Test(unittest.TestCase):

  def test_leer_mente_div2(self):
    antes=ejercicio_mente.ahora()
    print("impreso a las {}".format(antes))
    despues=ejercicio_mente.ahora()
    print("intervalo: {} segundos".format(despues-antes))
    for entrada in range(-1,2):
      self.assertEqual(entrada/2,leer_mente(entrada))