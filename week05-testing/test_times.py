from times import compute_overlap_time, time_range
import pytest 
from pytest import raises
import yaml

# Load the yaml file
with open('week05-testing/fixture.yaml', 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)
    print('Loaded file', fixture)


@pytest.mark.parametrize("test_name", fixture)
# Fixture is a dictionary containing test name and the required parameters
def test_all_edge_cases(test_name):
    # Test name is a dictionary containing range1, range2, and expected
    properties = list(test_name.values())[0]
    first_range = time_range(*properties['time_range_1'])  # with * = All of them
    second_range = time_range(*properties['time_range_2'])
    expected = [(start, stop) for start, stop in properties['expected']]
    assert compute_overlap_time(first_range, second_range) == expected

'''
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    # Choose a different day - no overlap
    short = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00", 2, 60)
    expected = [] # Expect an empty list
    result = compute_overlap_time(large, short)
    assert result == expected

def test_several_intervals():
    # Some test code
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:39:20'), ('2010-01-12 10:40:20', '2010-01-12 10:45:00')]
    assert result  == expected

def test_boundary_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    # Expect an empty list since they do not overlap
    expected = []
    result = compute_overlap_time(large, short)
    assert result == expected
'''    

def test_backwards_time():
    large = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00")

    with raises(ValueError):
        compute_overlap_time(large, short)

def test_empty_range():
    large = time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
    short = []

    with raises(ValueError):
        compute_overlap_time(large, short)


if __name__ == "__main__":

    test_several_intervals()