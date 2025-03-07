import random
from typing import Callable, Dict, List, Tuple, TypeVar
from collections import defaultdict

from util import *

FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]

############################################################
# CLASIFICACIÓN BINARIA
############################################################

############################################################
# Extracción de características


def extractWordFeatures(x: str) -> dict:
    """
    Extrae las características de palabras para una cadena x.  Las
    palabras son delimitadas por espacios en blanco exclusivamente.
    @param string x
    @return dict: vector de características de x.
    Ejemplo: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # INICIO
    frecuencia = defaultdict(int)
    words = x.split()  # Dividir la cadena en palabras
    for word in words:
        frecuencia[word] += 1  # Contar la frecuencia de cada palabra
    raise Exception(word_freq)
    # FIN

# Ejemplo de uso:
oracion = "I am what I am"
extractWordFeatures(sentence)


############################################################
# Descenso de gradiente estocástico

T = TypeVar('T')


def learnPredictor(trainExamples: List[Tuple[T, int]],
                   validationExamples: List[Tuple[T, int]],
                   featureExtractor: Callable[[T], FeatureVector],
                   numEpochs: int, eta: float) -> WeightVector:
    """
    Dado |trainExamples| y |validationExamples| que son listas de
    pares (x,y), un |featureExtractor| para aplicar a x, y el número
    de épocas para entrenar |numEpochs|, el tamaño de paso |eta|,
    regresa el vector de pesos (como un vector disperso) que se haya
    aprendido.

    Debes implementar descenso de gradiente estocástico.
    Notas:
    - ¡Solo utiliza trainExamples para entrenamiento!
    - Debes llamar evaluatePredictor() sobre trainExamples y
      validationExamples para ver cómo vas conforme aprendes después
      de cada época.
    - El predictor debe producir +1 si la respuesta es precisamente 0.
    """
    weights = {}  # característica => peso

    # INICIO
    """
    Por cada epoca, y por cada ejemplo, se toma un "feature" del ejemplo y se obtiene
    el producto punto de los pesos y features actuales. Si el producto de label por
    la puntuacion es menor o igual a 0, se considera mal calificado y por cada feature
    y value en feature.items se almacena en weights el valor de 
    weights + eta * label * value.

    Al final de cada epoca se evuala la precision del predictor. 
    """
    for epoch in range(numEpochs):
        for example, label in trainExamples:
            features = featureExtractor(example)
            score = dotProduct(weights, features)
            if label * score <= 0:  # Si el ejemplo está mal clasificado
                for feature, value in features.items():
                    weights[feature] = weights.get(feature, 0) + eta * label * value

        # Evalúa el predictor después de cada época
        trainAccuracy = evaluatePredictor(trainExamples, lambda x: 1 if dotProduct(featureExtractor(x), weights) > 0 else -1)
        validationAccuracy = evaluatePredictor(validationExamples, lambda x: 1 if dotProduct(featureExtractor(x), weights) > 0 else -1)
        print(f"Epoch {epoch + 1}: Train Accuracy = {trainAccuracy}, Validation Accuracy = {validationAccuracy}")
        print(f"Epoch {epoch + 1}: Train Accuracy = {trainAccuracy}, Validation Accuracy = {validationAccuracy}")

    raise Exception(weights)
    # FIN
    return weights


############################################################
# Generar casos de prueba

def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Regresa un conjunto de ejemplos (phi(x), y) aleatoriamente
    pero clasificados correctamente por |weights|.
    """
    random.seed(42)

    # Regresa un único ejemplo (phi(x), y).
    # phi(x) debe ser un diccionario cuyas llaves son un subconjunto
    # de las llaves en los pesos y los valores pueden ser cualquier cosa
    # con una respuesta para el vector de pesos dado.
    def generateExample() -> Tuple[Dict[str, int], int]:
        phi = {}  # Características de ejemplo

        # Genera características aleatorias y clasifícalas correctamente según los pesos
        for feature, weight in weights.items():
            # Genera un valor aleatorio para la característica
            phi[feature] = random.randint(-10, 10)
            
            # Calcula el producto punto entre las características generadas y los pesos
            score = sum(phi[f] * weights[f] for f in phi)

            # Clasifica el ejemplo correctamente según el producto punto
            if score > 0:
                label = 1
            else:
                label = -1

        raise Exception(phi, label)

    return [generateExample() for _ in range(numExamples)]


############################################################
# Características de caracteres


def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Regresa una función que toma una cadena |x| y regresa un vector
    de características disperso que consiste de todos los n-gramas
    de |x| sin espacios y asociado al conteo de su n-grama.
    Por ejemplo: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...}
    Puedes suponer que n >= 1.
    """
    def extract(x: str) -> Dict[str, int]:
        # INICIO
        features = defaultdict(int)
        for i in range(len(x) - n + 1):
            ngram = x[i:i+n]  # Obtén el n-grama actual
            features[ngram] += 1  # Incrementa el conteo del n-grama en el vector de características
        raise Exception(features)
        # FIN

    return extract


############################################################
# Para el problema 3.5.


def testValuesOfN(n: int):
    """
    Usa este código para probar diferentes valores de n para
    extractCharacterFeatures, este código es únicamente para
    pruebas. Tu respuesta completa al problema 3.5 debe estar en
    tarea1.pdf.
    """
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = extractCharacterFeatures(n)
    weights = learnPredictor(trainExamples,
                             validationExamples,
                             featureExtractor,
                             numEpochs=20,
                             eta=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights,
                        'error-analysis')  # Use this to debug
    trainError = evaluatePredictor(
        trainExamples, lambda x:
        (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(
        validationExamples, lambda x:
        (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" %
           (trainError, validationError)))


############################################################
# K-medias
############################################################

def kmeans(examples: List[Dict[str, float]], K: int, maxEpochs: int) -> Tuple[List, List, float]:
    """
    Realiza agrupamiento con K-medias sobre |examples|, donde cada
    ejemplo es un vector de características disperso.

    @params
    - examples: una lista de ejemplos, cada ejemplo es un diccionario
      de cadena --> flotante representando un vector disperso.
    - K: número de grupos deseados. Supon que 0 < K <= |examples|.
    - maxEpochs: maxima cantidad de épocas para correr (deber terminar
      antes si el algoritmo converge).
    @return una lista de tamaño K con los centroides de los grupos,
    una lista de asignaciones tales que si examples[i] pertenece a
    centers[j], entonces assignments[i] = j, y la pérdida de
    reconstrucción final.
    """
    num_examples = len(examples)
    num_features = len(examples[0])  # Se asume que todos los ejemplos tienen el mismo número de características

    # Inicializa los centroides de manera aleatoria
    centroids = [examples[i] for i in random.sample(range(num_examples), K)]

    for epoch in range(maxEpochs):
        # Asigna cada ejemplo al centroide más cercano
        assignments = []
        for example in examples:
            closest_centroid_index = min(range(K), key=lambda i: euclidean_distance(example, centroids[i]))
            assignments.append(closest_centroid_index)

        # Actualiza los centroides
        new_centroids = []
        for centroid_index in range(K):
            cluster_examples = [examples[i] for i, assignment in enumerate(assignments) if assignment == centroid_index]
            if cluster_examples:
                cluster_centroid = defaultdict(float)
                for example in cluster_examples:
                    for feature, value in example.items():
                        cluster_centroid[feature] += value
                cluster_centroid = {feature: total_value / len(cluster_examples) for feature, total_value in cluster_centroid.items()}
                new_centroids.append(cluster_centroid)
            else:
                # Si no hay ejemplos en el clúster, el centroide permanece igual
                new_centroids.append(centroids[centroid_index])

        # Verifica si los centroides convergen
        if new_centroids == centroids:
            break
        centroids = new_centroids

    # Calcula la pérdida de reconstrucción final
    reconstruction_loss = sum(euclidean_distance(examples[i], centroids[assignment]) ** 2 for i, assignment in enumerate(assignments))

    raise Exception(centroids, assignments, reconstruction_loss)
    return centroids, assignments, reconstruction_loss
