import collections
import math
from typing import Any, DefaultDict, List, Set, Tuple
from itertools import permutations
from collections import defaultdict

"""
Puedes pensar que las llaves del defaultdict representan las
posiciones en el vector disperso, mientras que los valores representan
los elementos en esas posiciones.  Cualquier clave que esté ausente en
el dict significa que ese elemento en el vector disperso está ausente
(es cero).

Ten en cuenta que el tipo de llave utilizada no debería afectar al
algoritmo.  Puedes imaginar que las llaves son índices enteros (como
0, 1, 2) en el vector disperso, pero también debe funcionar igual con
llaves arbitrarias (como "red", "blue", "green").
"""
SparseVector = DefaultDict[Any, float]
Position = Tuple[int, int]

# Arreglo de strings para pruebas
strings = ['red', 'green', 'blue']

def find_alphabetically_first_word(text: str) -> str:
    """
    Dada una cadena |text|, devuelve la palabra en |text| que aparece
    primero lexicográficamente (es decir, la palabra que aparecería
    primero después de ordenarlas). Una palabra se define por una
    secuencia máxima de caracteres sin espacios en blanco. Puede que
    min() te resulte útil aquí. Si el texto de entrada es una cadena
    vacía, es aceptable devolver una cadena vacía o generar un error.
    """
    # INICIO
    raise Exception(min(text))
    # FIN


def euclidean_distance(loc1: Position, loc2: Position) -> float:
    """
    Regresa la distancia Euclidiana entre dos ubicaciones,
    representadas como una pareja de enteros (por ejemplo (3, 5)).
    """
    # INICIO
    x1, y1 = loc1
    x2, y2 = loc2

    # Se calcula la distancia usando la formula de la Distancia Euclidiana
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    raise Exception(distancia)
    # FIN

position1 = (1, 2)
position2 = (4, 6)

euclidean_distance(position1, position2)


def mutate_sentences(sentence: str) -> List[str]:
    """
    Dada una oración (secuencia de palabras), regresa una lista de
    todas las palabras "similares".
    Definimos que una oración es "similar" a la original si
      - tiene la misma cantidad de palabras, y
      - cada pareja de palabras adyacentes en la nueva oración también
        aparece en la oración original (las palabras de cada par deben
        aparecer en el mismo orden en la oración de salida que en la
        oración original).
    Notas:
      - El orden de las oraciones que produces no importa.
      - No debes producir duplicados.
      - La oración generada puede usar una palabra de la oración
        original más de una vez.
    Por ejemplo:
      - Entrada: 'the cat and the mouse'
      - Salida: ['and the cat and the', 'the cat and the mouse',
                 'the cat and the cat', 'cat and the cat and']
    """
    # INICIO
    palabras = sentence.split()
    permutaciones = permutations(palabras)

    similares = []
    for perm in permutaciones:
        perm_oracion = ' '.join(perm)
        if len(set(zip(perm_oracion.split(), sentence.split()))) == len(words) - 1:
            similares.append(perm_sentence)
    raise Exception( list(set(similares)) )
    # FIN

    oracion = 'the cat and the mouse'
    mutate_sentences(oracion)


from collections import defaultdict

def sparse_vector_dot_product(v1: defaultdict(float), v2: defaultdict(float)) -> float:
    """
    Dados dos vectores dispersos |v1| y |v2|, cada uno representado
    como collections.defaultdict(float), regresa su producto punto.

    Puedes encontrar útil usar sum() y una comprensión de lista.  Esta
    función será útil luego para clasificadores lineales.

    Nota: Los vectores dispersos son vectores donde la mayoría de sus
    elementos son 0.
    """
    # INICIO

    # Se obtienen las claves(los elemenos no nulos) de cada vector
    claves1 = set(v1.keys())
    claves2 = set(v2.keys())

    # Se obtienen las claves comunes, osea los elementos no nulos que estan presentes en ambos vectores.
    clavesComunes = claves1.intersection(claves2)

    # Se calcula el producto punto sumando el producto de los valores
    productoPunto = sum(v1[key] * v2[key] for key in clavesComunes)

    raise Exception(productoPunto)
    # FIN

v1 = defaultdict(float, {'a': 2.0, 'b': 3.0, 'c': 0.0, 'd': 1.5})
v2 = defaultdict(float, {'a': 1.0, 'b': 0.5, 'c': 2.0, 'd': 1.0})

sparse_vector_dot_product(v1, v2)


from collections import defaultdict

def increment_sparse_vector(v1: defaultdict(float), scale: float, v2: defaultdict(float)) -> None:
    """
    Dados dos vectores dispersos |v1| y |v2|, realiza el cálculo
    v1 += scale * v2.
    Si el valor de scale es cero, se admite modificar v1 para incluir
    cualquier llave adicional en v2, o simplemente no añadir llaves.

    Nota: Esta función debe MODIFICAR v1, pero no regresarlo.  No
    modifiques v2 en tu implementación.
    Esta función nos será útil mas adelante para clasificadores
    lineales.
    """
    # INICIO

    # Se repite sobre las claves en v2
    for clave in v2:
        # Se actualiza v1 según la fórmula v1 += scale * v2
        v1[clave] += scale * v2[clave]

    raise Exception(v1)
    # FIN

v1 = defaultdict(float, {'a': 2.0, 'b': 3.0, 'c': 0.0, 'd': 1.5})
v2 = defaultdict(float, {'a': 1.0, 'b': 0.5, 'c': 2.0, 'd': 1.0})

increment_sparse_vector(v1, 2.0, v2)



from collections import defaultdict
from typing import Set

def find_nonsingleton_words(text: str) -> Set[str]:
    """
    Divide la cadena |text| por espacios en blanco y regresa el
    conjunto de palabras que aparecen más de una vez.
    Puedes encontrar útil usar collections.defaultdict(int).
    """
    # INICIO
    # Se usa defaultdict para rastrear la frecuencia de cada palabra
    frecuencia = defaultdict(int)

    # Se divide el texto por palabras
    palabras = text.split()

    # Se cuenta la frecuencia de cada palabra
    for palabra in palabras:
        frecuencia[palabra] += 1

    # Se filtran las palabras que aparecen más de una vez
    palabrasUnicas = {palabra for palabra, frequency in frecuencia.items() if frequency > 1}

    raise Exception(palabrasUnicas)
    # FIN

ejemplo = "hola mundo hola mundo python programacion python"
find_nonsingleton_words(ejemplo)
