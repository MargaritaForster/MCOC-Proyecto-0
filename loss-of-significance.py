import numpy as np
import math

#SACAR RAÍZ CUADRADA DE UN NUMERO
numero = raw_input("Ingrese un numero: ")
np.float32(numero)
np.float64(numero)

if numero < 0:
    print "error"
elif numero >= 0 :
    a = math.sqrt(np.float32(numero))
    b = math.sqrt(np.float64(numero))
    print "Float32"
    print a
    print "Float64"
    print b
    if a > b:
        c = ((a-b)/b)*100 
        print "Diferencia porcentual entre float32 y float64"
        print c
    elif a < b:
        d = ((b-a)/b)*100
        print "Diferencia porcentual entre float64 y float32"
        print d
