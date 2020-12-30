import pytest
import sys

# To run the pytest:
#    1) Open the PyTest folder in Terminal, right-click > Open in > Terminal.
#    2) Type: pytest test_demo_skip.py -v (for verbose)
#    3) Type: pytest test_demo_skip.py -k demo_3 -v (only test functions named demo_3 will be run. All other test functions will be skipped)


# test functions with @pytest.mark.skip(reason = " ") will be skipped
@pytest.mark.skip(reason = "Not included in this build")
def test_demo_1():
    assert True

# test functions with @pytest.mark.skipif(sys.version.info > (3,6), reason = "requires python 3.6 or lower") will be skipped if condition is satisfied
@pytest.mark.skipif(sys.version_info > (3,6), reason = "requires python 3.6 or lower")
def test_demo_2():
    assert True

def test_demo_3():
    assert True

# Only test functions marked with a name, ex: @pytest.mark.windows, will be run when this command is used: pytest test_demo_skip.py -m windows -v
@pytest.mark.windows
def test_windows_1():
    assert True

@pytest.mark.windows
def test_windows_2():
    assert True

# Only test functions marked with a name, ex: @pytest.mark.mac, will be run when this command is used: pytest test_demo_skip.py -m mac -v
@pytest.mark.mac
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True