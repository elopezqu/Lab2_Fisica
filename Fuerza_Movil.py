import matplotlib.pyplot as plt

print("1) Este programa encontrara la fuerza de un movil en movimiento")
print("2) Este programa graficara el cambio de velocidad de un movil")
print("Datos del cuerpo --->")
masa = float(input("Masa(kg): "))
veloInicial = float(input("Velocidad Iniciald(m/s):  "))
veloFinal = float(input("Velocidad Final(m/s):  "))
tiempo =  float(input("Tiempo(s): "))

print("La fuerza que describe el movil es: ",abs(masa*((veloFinal-veloInicial)/tiempo)),"N")

plt.plot([0,tiempo],[veloInicial,veloFinal])
plt.title('Cambio de velocidad')
plt.xlabel('Tiempo(s)')
plt.ylabel('Velocidad(m/s)')
plt.show()