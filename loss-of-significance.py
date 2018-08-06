import numpy as np
import math
from numpy import *
from matplotlib import pyplot

#SACAR RAÍZ CUADRADA DE UN NUMERO

numero = raw_input("Ingrese un numero: ")
float32 = np.float32(numero)
float64 = np.float64(numero)
lista32 = []
lista64 = []
lista32.append(float32)
lista64.append(float64)
#print lista32
#print lista64

a32 = array(lista32)
a64 = array(lista64)
#print a32
#print a64
    
raiz32 = sqrt(a32)
raiz64 = sqrt(a64)
#print raiz32
#print raiz64
    
i = 0
listaError = []
error = raiz64[i]-raiz32[i]
listaError.append(error)
#print listaError
    
print "Alt_raiz32: ", raiz32[i], "Alt_raiz64: ", raiz64[i], "Error: ", listaError[i]

