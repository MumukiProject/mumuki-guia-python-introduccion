import time

class ejercicio_mente():

  @classmethod
  def ahora():
    return datetime.datetime.timestamp(datetime.datetime.now())
  
  
  @classmethod
  def print(entrada):
    time.sleep(1)
    print(str(entrada))
    return None
    
