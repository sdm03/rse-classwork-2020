from times import compute_overlap_time, time_range

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
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:34:20'), ('2010-01-12 10:35:20', '2010-01-12 10:39:20'), ('2010-01-12 10:40:40', '2010-01-12 10:39:20'), ('2010-01-12 10:40:20', '2010-01-12 10:34:20'), ('2010-01-12 10:40:20', '2010-01-12 10:39:40'), ('2010-01-12 10:40:40', '2010-01-12 10:45:00'), ('2010-01-12 11:20:40', '2010-01-12 10:34:20'), ('2010-01-12 11:20:40', '2010-01-12 10:39:40'), ('2010-01-12 11:20:40', '2010-01-12 10:45:00')]
    assert result == expected

def test_boundary_overlap():
    # Some test code
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")

    expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
    result = compute_overlap_time(large, short)
    assert result == expected
    
if __name__ == "__main__":
    test_boundary_overlap()