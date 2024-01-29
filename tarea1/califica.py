import sys
import pytest
from pytest import approx
import tarea1
import util
import string
from util import *

MAX_SECONDS = 16
TOLERANCE = 1e-4

pytestmark = pytest.mark.timeout(MAX_SECONDS)

def test_extractWordFeatures_a():
    ans = {"a":2, "b":1}
    assert (
        tarea1.extractWordFeatures("a b a")
        == ans
    )
    return

def test_extractWordFeatures_b():
    random.seed(42)
    sentence = ' '.join([random.choice(['a', 'aa', 'ab', 'b', 'c']) for _ in range(100)])
    submission_ans = tarea1.extractWordFeatures(sentence)
    return

def test_learnPredictor_a():
    trainExamples = (("hello world", 1), ("goodnight moon", -1))
    testExamples = (("hello", 1), ("moon", -1))
    featureExtractor = tarea1.extractWordFeatures
    weights = tarea1.learnPredictor(trainExamples, testExamples, featureExtractor, numEpochs=20, eta=0.01)
    assert weights["hello"] > 0
    assert weights["moon"] < 0
    return

def test_learnPredictor_b():
    trainExamples = (("hi bye", 1), ("hi hi", -1))
    testExamples = (("hi", -1), ("bye", 1))
    featureExtractor = tarea1.extractWordFeatures
    weights = tarea1.learnPredictor(trainExamples, testExamples, featureExtractor, numEpochs=20, eta=0.01)
    assert weights["hi"] < 0
    assert weights["bye"] > 0
    return

def test_learnPredictor_c():
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = tarea1.extractWordFeatures
    weights = tarea1.learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=20, eta=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights, 'error-analysis')  # Para debuggear
    trainError = evaluatePredictor(trainExamples, lambda x : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(validationExamples, lambda x : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" % (trainError, validationError)))
    assert trainError < 0.04
    assert validationError < 0.3
    return

def test_generateDataset_a():
    weights = {"hello": 1, "world": 1}
    data = tarea1.generateDataset(5, weights)
    for datapt in data:
        assert (dotProduct(datapt[0], weights) >= 0) == (datapt[1] == 1)
    return

def test_generateDataset_b():
    weights = {}
    for _ in range(100):
        k = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        v = random.uniform(-1, 1)
        weights[k] = v
    data = tarea1.generateDataset(100, weights)
    for phi, y in data:
        assert (util.dotProduct(phi, weights) >= 0) == (y == +1)
    return

def test_extractCharacterFeatures_a():
    fe = tarea1.extractCharacterFeatures(3)
    sentence = "hello world"
    ans = {"hel":1, "ell":1, "llo":1, "low":1, "owo":1, "wor":1, "orl":1, "rld":1}
    assert ans == fe(sentence)
    return

def test_extractCharacterFeatures_b():
    random.seed(42)
    for i in range(10):
        sentence = ' '.join([random.choice(['a', 'aa', 'ab', 'b', 'c']) for _ in range(100)])
        for n in range(1, 4):
            submission_ans = tarea1.extractCharacterFeatures(n)(sentence)
    return

def test_kmeans_a():
    random.seed(42)
    x1 = {0:0, 1:0}
    x2 = {0:0, 1:1}
    x3 = {0:0, 1:2}
    x4 = {0:0, 1:3}
    x5 = {0:0, 1:4}
    x6 = {0:0, 1:5}
    examples = [x1, x2, x3, x4, x5, x6]
    centers, assignments, totalCost = tarea1.kmeans(examples, 2, maxEpochs=10)
    assert len(assignments) == len(examples)
    for assignment in assignments:
        assert (assignment in [0, 1])
    # (there are two stable centroid locations)
    assert (round(totalCost, 3) == 4 or round(totalCost, 3) == 5.5 or round(totalCost, 3) == 5.0)
    return

def test_kmeans_b():
    random.seed(42)
    K = 6
    bestCenters = None
    bestAssignments = None
    bestTotalCost = None
    examples = generateClusteringExamples(numExamples=1000, numWordsPerTopic=3, numFillerWords=1000)
    centers, assignments, totalCost = tarea1.kmeans(examples, K, maxEpochs=100)
    return


def test_kmeans_c():
    random.seed(42)
    K = 6
    bestCenters = None
    bestAssignments = None
    bestTotalCost = None
    examples = generateClusteringExamples(numExamples=1000, numWordsPerTopic=3, numFillerWords=1000)
    centers, assignments, totalCost = tarea1.kmeans(examples, K, maxEpochs=100)
    return



def test_kmeans_d():
    random.seed(42)
    K = 6
    bestCenters = None
    bestAssignments = None
    bestTotalCost = None
    examples = generateClusteringExamples(numExamples=10000, numWordsPerTopic=3, numFillerWords=10000)
    centers, assignments, totalCost = tarea1.kmeans(examples, K, maxEpochs=100)
    assert totalCost < 10e6
    averages = []
    for center in centers:
        xs = [examples[i] for i in range(len(examples)) if centers[assignments[i]] == center]
        allWords = []
        for x in xs:
            for key in list(x.keys()):
                if key not in allWords:
                    allWords.append(key)
        wordVals = [(word, sum([x[word] for x in xs])*1.0/len(xs)) for word in allWords]
        avg = dict(wordVals)
        averages.append(avg)
    return


if __name__ == "__main__":
    sys.exit(pytest.main(["califica.py", "--no-header", "-vv"]))
