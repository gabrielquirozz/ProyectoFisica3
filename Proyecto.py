import matplotlib.pyplot as plt
import math
import numpy as np

#Carga y Masa
particulas = [[-1.60E-27, 9.1E-31],[1.60E-19, 9.10E-31],[1.60E-19, 1.67E-27],[0, 1.67E-27],[3.2E-19, 6.64E-27],[],[1.60E-19, 1.9E-28],[],[],[]]

print("Ingrese numero que desea elegir de las particulas disponibles:")
particula = int(input("1.Electron\n2.Positron\n3.Proton\n4.Neutron\n5.Particula alfa\n6.Nucleo de deuterio\n7.Muon\n8.Taun\n9.Meson\n10.Barion\n"))
VelocidadMagnitud = int(input("Ingrese magnitud de la particula (m/s)\n"))
VelocidadDireccion = int(input("Ingrese la direccion (θ)\n"))
IntensidadCampoElectrico = int(input("Ingrese la intensidad del campo electrico (Nm^2/C)\n"))
RegionCampoElectrico = int(input("Ingrese Region del campo Electrico\n"))

