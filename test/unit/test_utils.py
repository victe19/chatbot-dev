import pytest

import utils

def test_words_to_nums():
    query = "vull picar al sisè número quatre vegades i fins que pugui ser el primer dels 3"
    expected_query = "vull picar al 6 número 4 vegades i fins que pugui ser el 1 dels 3"
    
    output_query = utils.words_to_nums(query)

    assert output_query == expected_query