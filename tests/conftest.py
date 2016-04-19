import pytest
import os

current_path = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def sample():
    with open(os.path.join(current_path, 'sample.txt')) as f:
        content = f.read()
    return content


@pytest.fixture
def result():
    with open(os.path.join(current_path, 'result.txt')) as f:
        content = f.read()
    return content
