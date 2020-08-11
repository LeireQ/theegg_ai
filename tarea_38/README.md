# Tarea_38

Resolución en Python y diagrama de flujo de los siguientes tres problemas:

El Biólogo
Invertir Palabras
Palíndromos

## El Biólogo

El archivo ElBiologo.png contiene un diagrama de flujo que define los pasos que sigue el programa ElBiologo.py.

En este programa se pide al usuario que introduzca dos secuencias de ADN a comparar. Las secuencias solamente puede contener las
letras ACGT, en caso de que alguna secuencia no cumpla con esta condición se muestra un aviso en pantalla y se piden nuevos valores
de ADN.

El programa va recorriendo de uno en uno las letras que forman la primera secuencia de ADN y las compara con la segunda secuencia. 
A medida de que vayan coincidiendo se almacena la secuencia, en el momento en el que no coincidan se almacena en una variable auxiliar
la secuenci más larga obtenido hasta ahora.

Una vez que se haya terminado la comparación se muestra en pantalla el valor de la variable auxiliar.

## Invertir Palabras

El archivo InvertirPalabras.png contiene un diagrama de flujo que define los pasos que sigue el programa InvertirPalabras.py.

Primero pide al usuario que introduzca el número de frases que se quieren invertir. Después se pide al usuario que introduza de 
uno en uno las frases a invertir. Una vez almacenadas todas se llama a la función Invertir. Esta Función divide transforma la frase
en un array de strings separndo las palabras por los espacios, luego se invierten las posiciones y finalmente se hace otra conversión
donde el array pasa a ser un estring separando cada posición del array con un espacio.

## Palíndromos

El archivo Palíndromo.png contiene un diagrama de flujo que define los pasos que sigue el programa Palindromo.py.

Se pide al usuario que meta un número entre 1 y 1000000, se comprueba que el valor introducido sea correcto. Una vez que se tiene
el número dentro de un bucle se va probando que sea primo y palíndromo, en caso contrario se comprueba el siguiente número hasta llegar
al máximo (1000000). El primer número primo y palíndormo que se encuentre se muestra por pantalla, si no se ha encontrado ninguno se da un
aviso por pantalla.

Para saber si un número es primo, se comprueba que sea divisible por otro número que no sea él mismo.
Para saber si es palíndromo se transforma el número a un array, se invierten las posiciones y se compara si el array inicial y el tranformado son iguales.
