def test_distance():
    """"
    Test the distance function
    """
    try:
        import pytest
        from mini.mini import calculate_distance
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_data1 = [3,4]
    test_data2 = [6,8]
    test_data3 = [9,12]
    assert 5 == calculate_distance(test_data1)
    assert 10 == calculate_distance(test_data2)
    assert 15 == calculate_distance(test_data3)
