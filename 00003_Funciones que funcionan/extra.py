import time,datetime

class ejercicio_mente():

  @staticmethod
  def ahora():
    return datetime.datetime.timestamp(datetime.datetime.now())
  
  
  @staticmethod
  def pausa_print(entrada):
    time.sleep(1)
    print(str(entrada))
    return None
    
