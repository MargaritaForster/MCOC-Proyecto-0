# MCOC-Proyecto-0

La pérdida de significancia ocurre cuando el error relativo es mayor al error absoluto. Esto genera un efecto indesaeado al momento de utilizar números del tipo floats cuando se calcula aritméticamente.
En este proyecto, se muestra un ejemplo de pérdidad de significancia. Se procedió a realizar un código que calculase la raíz cuadrada del número que se ingresa. El código transforma el número a float32 y a float64, para luego obtener la raíz cuadrada de los dos casos Más tarde, se muestra porcentualmente el error. 
Se generan diferencias al calcular con float32 y float64 porque ocupan diferentes cantidades de bits, 32 y 64 respectivamente. Además, float32 tiene una precisión y float64 tiene doble precisión, por lo que float32 puede tener 8 bits exponencial y float64 11 bits exponencial. Lo anterior genera que con float64 se obtengan resultados más precisos.
Por ejemplo, al ingresar el número 21372.6332598, se muestra float32: 21372.633 y float64: 21372.6332598.
Se obtiene que la raíz de float32 es 146.193819338 y la raíz de float64 es 146.193820867. Por lo tanto, la diferencia porcentual entre float64 y float32 es 1.04643166492e-06.
Las diferencias son muy pequeñas, pero a medida que el número aumenta, la diferencia se hace mayor.
