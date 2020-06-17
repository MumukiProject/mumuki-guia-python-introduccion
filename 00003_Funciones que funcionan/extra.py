import time,datetime

class ejercicio_mente():
  
  @staticmethod
  def a_veeer():
    print(globals())
    print(locals())

  

  @staticmethod
  def ahora():
    #return datetime.datetime.timestamp(datetime.datetime.now())
    return 1
  

  
  @staticmethod
  def pausa_print(entrada):
    time.sleep(1)
    print(str(entrada))
    return None
    
