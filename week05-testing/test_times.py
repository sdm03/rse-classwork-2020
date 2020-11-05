from times import compute_overlap_time, time_range
import pytest 
from pytest import raises

large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)

# Defining more input ranges
differentday = time_range("2010-01-13 10:30:00", "2010-01-13 10:45:00", 2, 60)
large_3_intervals = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 3, 60)
short_3_intervals = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 3, 60)
short_boundary_overlap = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

# Defining expected
empty = []
large_short = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
large_3_intervals_short_3_intervals = [('2010-01-12 10:30:00', '2010-01-12 10:34:20'), ('2010-01-12 10:35:20', '2010-01-12 10:39:20'), ('2010-01-12 10:40:20', '2010-01-12 10:34:20'), ('2010-01-12 10:40:20', '2010-01-12 10:39:40'), ('2010-01-12 10:40:40', '2010-01-12 10:45:00'), ('2010-01-12 11:20:40', '2010-01-12 10:34:20'), ('2010-01-12 11:20:40', '2010-01-12 10:39:40'), ('2010-01-12 11:20:40', '2010-01-12 10:45:00')]


@pytest.mark.parametrize("large, short, expected",[(large, short, large_short), (large, differentday, empty), (large_3_intervals, short_3_intervals, large_3_intervals_short_3_intervals), (large, short_boundary_overlap, empty )])
def test_all_edge_cases(large, short, expected):
    result = compute_overlap_time(large, short)
    assert result == expected

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
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 3, 60)
    
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:34:20'), ('2010-01-12 10:35:20', '2010-01-12 10:39:20'), ('2010-01-12 10:40:20', '2010-01-12 10:34:20'), ('2010-01-12 10:40:20', '2010-01-12 10:39:40'), ('2010-01-12 10:40:40', '2010-01-12 10:45:00'), ('2010-01-12 11:20:40', '2010-01-12 10:34:20'), ('2010-01-12 11:20:40', '2010-01-12 10:39:40'), ('2010-01-12 11:20:40', '2010-01-12 10:45:00')]
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