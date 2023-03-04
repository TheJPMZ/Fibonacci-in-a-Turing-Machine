# Proyecto Algoritmos
Para este proyecto se tuvo que diseñar una implementación de una maquina de turing que con un archivo de configuración pueda leer una cadena y encontrar el numero correspondiente al fibonacci de la cadena.

## Convenciones
* La sucesión de fibonacci empieza en 0.
* La maquina de turing admite una cadena de entrada compuesta de 1's. El numero de 1's en la cadena es el numero de la sucesión de fibonacci que se desea encontrar. Ejemplo: 1111 es el numero 4 de la sucesión de fibonacci.
* La maquina de turing regresa igualmente una cadena de 1's, o el numero 0 si la cadena de entrada es vacia.
* Al momento de simular la maquina de turing, el caracter "□" representa el espacio en blanco. Y el puntero de la maquina de turing se representa por el caracter rodeado de corchetes "[ ]".
* Para declarar la maquina de turing el simbolo 

## Ejecución
Para ejecutar el programa se debe de ejecutar el archivo "main.py" con python 3.6 o superior. 
Se requiere un archivo json de configuración para la maquina de turing, el cual debe de tener la siguiente estructura:
```json
{
    "Q": "States",
    "Σ": "Alphabet",
    "Γ": "Estados de la maquina de turing",
    "S": "Initial state",
    "b": "Blank symbol",
    "F": "Final states",
    "transitions":{
        "State": {"Symbol": ["Next state", "Symbol to write", "Direction"]},
    }
}
```
Asimismo se debe de tener un archivo de texto con las cadenas de entrada que se desean simular. Cada cadena debe de estar en una linea diferente. Ejemplo:
```txt
1
111
1111111
```
Para ejecutar el programa se debe de ejecutar el siguiente comando:
```bash
python main.py
```
EL programa mostrará la simulación de la maquina de turing para cada cadena de entrada. Al finalizar el programa se generará un archivo de texto con el nombre "output.txt" en el cual se mostrará el resultado de cada cadena de entrada. 

## Grafo de la maquina de turing
![imagen](https://user-images.githubusercontent.com/64183934/222681481-9f0250d6-cfd9-449b-99fd-007849d6c9ae.png)
