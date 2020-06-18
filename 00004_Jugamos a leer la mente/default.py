#...previousSolution...#

def juego_mental():
    print("Pensá un número de 0 a 10, no lo digas")
    print("Ahora sumale 10")
    print("Ahora multiplicalo  por 5")
    print("Ahora restale 50  y decime el resultado")
    entrada = float(input())#numero recibido
    numero_desconocido = leer_mente(entrada)
    print(f"El numero que pensaste es: {numero_desconocido}" )

if __name__ == '__main__':
    juego_mental()

