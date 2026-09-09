"""1. Finalización anticipada de un ciclo: break
La instrucción break finaliza inmediatamente el ciclo for o while más cercano. 
La ejecución continúa en la primera 
instrucción ubicada después de ese ciclo. 
No finaliza por sí sola la función ni el programa completo.
Implementen es_primo(numero) utilizando una variable lógica y break. 
La función deberá retornar False para todo número menor que 2 y detener la búsqueda apenas encuentre un divisor.
a) Prueben con -3, 0, 1, 2, 9, 17 y 25.

b) Indiquen en qué caso se ejecuta break.
El break se ejecuta siempre que se cumple la condicion previa, en este caso, si el resto de la division entera es igual a cero.


c) Expliquen por qué puede evitar iteraciones innecesarias.
En cuanto la operacion detecta un divisior(resto==0), sabemos que el numero es primo por lo que no es necesario seguir validando los numeros restantes.

d) Comparen el resultado con una versión que recorra todos los posibles divisores.

Una version que recorra todos los divisiores deberia devolver el mismo resultado.
El concepto de BREAK, hacen mas eficiente el programa,interrumpiendo las iteraciones en cuanto se cumpla la condicion consultada previamente.

 """

def es_primo(numero):

    
    if numero < 2:
        return False
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
    return primo
        
def main ():
    numero=int(input("Ingrese un numero"))
    if es_primo(numero):
        print("El numero es primo")
    else: 
        print("El numero no es primo")

main()