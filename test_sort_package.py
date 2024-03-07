from sort_package import sort_package

def test_standard_package():
    assert sort_package(50, 50, 50, 10) == "STANDARD"

def test_special_package_bulky():
    assert sort_package(150, 50, 50, 10) == "SPECIAL"
    assert sort_package(50, 150, 50, 10) == "SPECIAL"
    assert sort_package(50, 50, 150, 10) == "SPECIAL"
    assert sort_package(100, 100, 100, 10) == "SPECIAL"

def test_special_package_heavy():
    assert sort_package(50, 50, 50, 20) == "SPECIAL"

def test_rejected_package():
    assert sort_package(150, 100, 100, 20) == "REJECTED"
    assert sort_package(100, 150, 100, 20) == "REJECTED"
    assert sort_package(100, 100, 150, 20) == "REJECTED"
    assert sort_package(100, 100, 100, 20) == "REJECTED"

def test_edge_cases():
    # Edge cases exactly at the threshold
    assert sort_package(150, 100, 100, 19) == "SPECIAL" # Bulky by dimension
    assert sort_package(90, 90, 90, 20) == "SPECIAL" # Heavy but not bulky by dimension
    assert sort_package(100, 100, 100, 20) == "REJECTED" # Heavy and bulky
    assert sort_package(50, 50, 50, 19) == "STANDARD" # Just below thresholds
