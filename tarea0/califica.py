import sys
import pytest
from pytest import approx

import collections
import random
import tarea0

MAX_SECONDS = 5
TOLERANCE = 1e-4

pytestmark = pytest.mark.timeout(MAX_SECONDS)


def test_find_alphabetically_first_word_a():
    assert (
        tarea0.find_alphabetically_first_word(
            "cual es la primer palabra alfabeticamente"
        )
        == "alfabeticamente"
    )
    return


def test_find_alphabetically_first_word_b():
    assert tarea0.find_alphabetically_first_word("cat sun dog") == "cat"
    return


def test_find_alphabetically_first_word_c():
    assert (
        tarea0.find_alphabetically_first_word(" ".join(str(x) for x in range(100000)))
        == "0"
    )
    return


def test_euclidean_distance_a():
    assert tarea0.euclidean_distance((1, 5), (4, 1)) == approx(5, abs=TOLERANCE)
    return


def test_euclidean_distance_b():
    random.seed(42)
    for _ in range(100):
        x1 = random.randint(0, 10)
        y1 = random.randint(0, 10)
        x2 = random.randint(0, 10)
        y2 = random.randint(0, 10)
        ans2 = tarea0.euclidean_distance((x1, y1), (x2, y2))
    return


def test_mutate_sentences_a():
    assert sorted(tarea0.mutate_sentences("a a a a a")) == approx(
        sorted(["a a a a a"]), abs=TOLERANCE
    )
    assert sorted(tarea0.mutate_sentences("the cat")) == approx(
        sorted(["the cat"]), abs=TOLERANCE
    )
    assert sorted(tarea0.mutate_sentences("the cat and the mouse")) == approx(
        sorted(
            [
                "and the cat and the",
                "the cat and the mouse",
                "the cat and the cat",
                "cat and the cat and",
            ]
        ),
        abs=TOLERANCE,
    )
    return


def gen_sentence(alphabet_size, length):
    return " ".join(str(random.randint(0, alphabet_size)) for _ in range(length))


def test_mutate_sentences_b():
    random.seed(42)
    for _ in range(10):
        sentence = gen_sentence(3, 5)
        ans2 = tarea0.mutate_sentences(sentence)
    return


def test_mutate_sentences_c():
    random.seed(42)
    for _ in range(10):
        sentence = gen_sentence(25, 10)
        ans2 = tarea0.mutate_sentences(sentence)
    return


def test_sparse_vector_dot_product_a():
    assert tarea0.sparse_vector_dot_product(
        collections.defaultdict(float, {"a": 5}),
        collections.defaultdict(float, {"b": 2, "a": 3}),
    ) == approx(15, abs=TOLERANCE)
    return


def randvec():
    v = collections.defaultdict(float)
    for _ in range(10):
        v[random.randint(0, 10)] = random.randint(0, 10) + 5
    return v


def test_sparse_vector_dot_product_b():
    random.seed(42)
    for _ in range(10):
        v1 = randvec()
        v2 = randvec()
        ans2 = tarea0.sparse_vector_dot_product(v1, v2)
    return


def test_increment_sparse_vector_a():
    v = collections.defaultdict(float, {"a": 5})
    tarea0.increment_sparse_vector(
        v, 2, collections.defaultdict(float, {"b": 2, "a": 3})
    )
    assert v == approx(collections.defaultdict(float, {"a": 11, "b": 4}), abs=TOLERANCE)
    return


def test_increment_sparse_vector_b():
    random.seed(42)
    for _ in range(10):
        v1a = randvec()
        v1b = v1a.copy()
        v2 = randvec()
        tarea0.increment_sparse_vector(v1b, 4, v2)
        for key in list(v1b):
            if v1b[key] == 0:
                del v1b[key]
    return

def test_find_nonsingleton_words_a():
    assert (
        tarea0.find_nonsingleton_words('the quick brown fox jumps over the lazy fox')
        == {'the', 'fox'}
    )
    return


def stress_find_nonsingleton_words(num_tokens, num_types):
    random.seed(42)
    text = ' '.join(str(random.randint(0, num_types)) for _ in range(num_tokens))
    ans2 = tarea0.find_nonsingleton_words(text)
    return ans2

def test_find_nonsingleton_words_b():
    stress_find_nonsingleton_words(1000, 10)
    return

def test_find_nonsingleton_words_c():
    stress_find_nonsingleton_words(10000, 100)
    return

if __name__ == "__main__":
    sys.exit(pytest.main(["califica.py", "--no-header", "-vv"]))
