print("1) Este programa encontrara la fuerza de un movil en movimiento")
print("2) Este programa graficara el cambio de velocidad de un movil")
print("Datos del cuerpo --->")
masa = float(input("Masa(kg): "))
veloInicial = float(input("Velocidad Iniciald(m/s):  "))
veloFinal = float(input("Velocidad Final(m/s):  "))
tiempo =  float(input("Tiempo(s): "))

print("La fuerza que describe el movil es: ",masa*((veloFinal-veloInicial)/tiempo),"N")
