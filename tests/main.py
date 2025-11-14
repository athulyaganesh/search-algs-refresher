from algorithms.bfs_iterative import bfs_iterative
from algorithms.bfs_recursive import bfs_recursive
from algorithms.dfs_iterative import dfs_iterative
from algorithms.djikstras_algorithm import djikstras_algorithm
from algorithms.kruskals_algorithm import kruskals_algorithm
from algorithms.prims_algorithm import prims_algorithm
from algorithms.top_sort import top_sort
from algorithms.union_find import union_find


#example pytest test cases

import pytest

# Function to be tested
def add(a, b):
    return a + b

# Parametrized test function
@pytest.mark.parametrize("num1, num2, expected_sum", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, 20, 30)
])
def test_add_function(num1, num2, expected_sum):
    assert add(num1, num2) == expected_sum


@pytest.fixture(params=[10, 20, 30])
def sample_data(request):
    return request.param

def test_with_fixture_data(sample_data):
    assert sample_data > 5