print("Bienvenido a la Maquina de Atwood!")
print("-----------------------------")
print("Este programa tiene como entrada las \nmasas de 2 objetos para posteriormente indicar \nla aceleracion y la tension de la cuerda \nen la maquina de Atwood")
print("-----------------------------")
m1 = float(input("Ingrese la masa de primer objeto(kg): "))
m2 = float(input("Ingrese la masa de segundo objeto(kg): "))
gravedad = 9.8
# 3 posibles casos
if(m2 > m1):
  aceleracion = ((m2-m1)*gravedad)/(m1+m2)
  print("La aceleracion es: ",round(aceleracion,2),"m/s^2")
  print("La tension en la cuenda es: ",round((m1*gravedad+m1*aceleracion),2),"N")

