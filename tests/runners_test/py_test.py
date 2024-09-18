import pytest
from tests.mock.file_mocker import generate_file
from blackbox.runners.py_runner import run_py


def test_hello_world():

    expected = ["HELLO WORLD"]

    code = """print("HELLO WORLD");"""

    filename = generate_file(code, "py")

    outputs = run_py(filename, None)

    assert outputs == expected


def test_sum():
    try:
        expected = ["5"]

        inputs = ["2", "3"]

        code = """a = int(input())\nb = int(input())\nprint(a+b)"""

        filename = generate_file(code, ".py")

        outputs = run_py(filename, inputs)

        assert outputs == expected

    except Exception as error:
        pytest.fail(error)
