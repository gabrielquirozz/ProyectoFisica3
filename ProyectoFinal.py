import matplotlib.pyplot as plt
import math
import numpy as np

#Carga y Masa de Particulas
particulasCarga = [-1.60E-27, 1.60E-19, 1.60E-19, 0, 3.2E-19, (2/3)*1.60E-19, 1.60E-19,  (-1/3)*(1.60E-19), -1.60E-19, (-1/3)*(1.60E-19) ]
particulasMasa  = [9.1E-31, 9.10E-31, 1.67E-27, 1.67E-27, 6.64E-27, 307.5E-27, 1.9E-28,  142.61E-30, 3.2E-27,  7.13E-30]

print("Ingrese numero que desea elegir de las particulas disponibles:")
particula = int(input("1.Electron\n2.Positron\n3.Proton\n4.Neutron\n5.Particula alfa\n6.Quark Cima\n7.Muon\n8. Quark Extrano\n9.Tau\n10.Quark abajo\n"))
VelocidadMagnitud = int(input("Ingrese magnitud de la particula (m/s)\n"))
VelocidadDireccion = int(input("Ingrese la direccion (θ)\n"))
IntensidadCampoElectrico = int(input("Ingrese la intensidad del campo electrico (Nm^2/C)\n"))


velocidadx  = VelocidadMagnitud*math.cos(VelocidadDireccion)
velocidady  =  VelocidadMagnitud*math.sin(VelocidadDireccion)
aceleracion = ((particulasCarga[particula-1] * IntensidadCampoElectrico) / particulasMasa[particula-1] )
tiempo = velocidadx / aceleracion

x = []
y = []
i = 0
puntos = tiempo/30
while i<tiempo:
    posicionX = velocidadx * tiempo
    posicionY = (1/2) * aceleracion * tiempo**2
    x.append(posicionX)
    y.append(posicionY)
    i += puntos;

plt.plot(x,y)
plt.show()
    
    
    
    
