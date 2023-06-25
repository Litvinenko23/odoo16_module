import math
from typing import List, Union


def compute_area(shape: Union[List[int], float]) -> float:
    if isinstance(shape, list):
        return shape[0] * shape[1]
    if isinstance(shape, float):
        return math.pi * shape**2


def sorted_sequence(array: List[List[int]]) -> List[List[int]]:
    return sorted(array, key=compute_area)


def test_compute_area_rectangle() -> None:
    shape = [3, 4]
    expected_area = 12
    assert (
        compute_area(shape) == expected_area
    ), "Error: Incorrect rectangle area"


def test_compute_area_circle() -> None:
    radius = 2.5
    expected_area = math.pi * radius**2
    assert (
        compute_area(radius) == expected_area
    ), "Error: Wrong circumference area"


def test_sorted_sequence() -> None:
    array = [[2, 3], [4, 5], [1, 8], [6, 2]]
    expected_sequence = [[6, 2], [2, 3], [4, 5], [1, 8]]
    expected_sequence_sorted = sorted(expected_sequence, key=compute_area)
    assert (
        sorted_sequence(array) == expected_sequence_sorted
    ), "Error: Incorrectly sorted sequence"


test_compute_area_rectangle()
test_compute_area_circle()
test_sorted_sequence()
