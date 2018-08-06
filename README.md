# MCOC-Proyecto-0

La pérdida de significancia ocurre cuando el error relativo es mayor al error absoluto. Esto genera un efecto indesaeado al momento de utilizar números del tipo floats cuando se calcula aritméticamente.

Se generan diferencias al calcular con float32 y float64 porque ocupan diferentes cantidades de bits, 32 y 64 respectivamente. Además, float32 tiene una precisión y float64 tiene doble precisión, por lo que float32 puede tener 8 bits exponencial y float64 11 bits exponencial. Lo anterior genera que con float64 se obtengan resultados más precisos.

En este proyecto, se muestra un ejemplo de pérdidad de significancia. Se procedió a realizar un código que calculase la raíz cuadrada del número que se ingresa. Por lo tanto, se procedió a ingresar un número cualquiera que es guardado de dos formas, como número float32 y como número float64. Luego, estos dos números ingresaron a sus listas respectivas, para más tarde convertirse en arreglos.
A cada arreglo se le aplicó la función sqrt() de la librería, y se calculó el error considerando los resultados obtenidos.

Por ejemplo, al ingresar el número 21372.6332598 se muestra:
--*consola*--
Alt_raiz32:  146.19382 Alt_raiz64:  146.19382086736772 Error:  3.728695844529284e-06.
El primero valor corresponde a la raíz cuadrada del número ingresado, considerando float32. El segundo es considerando float64, y por último se observa el error.
