import pytest
from blackbox.evaluation.evaluation import run_exercise
from blackbox.exceptions import UnsupportedLanguageError, CodeKernelException


def test_success_on_hello_world():
    msg_expected = "PASSED"

    results_expected = ["HELLO WORLD"]

    code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }"""

    msg, results = run_exercise("c++", code, None, ["HELLO WORLD"])

    assert msg == msg_expected

    assert results_expected == results


def test_fail_on_hello_world():
    msg_expected = "FAILED"

    results_expected = ["BYE WORLD"]

    code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }"""

    msg, results = run_exercise("c++", code, None, ["BYE WORLD"])

    assert msg == msg_expected

    assert results_expected != results


def test_compilation_error_on_hello_world():
    msg_expected = "COMPILATION_ERROR"

    results_expected = []

    code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD")
        return 0;
    }"""

    msg, results = run_exercise("c++", code, None, ["HELLO WORLD"])

    assert msg == msg_expected

    assert results_expected == results


def test_success_on_hello_world_py():
    msg_expected = "PASSED"

    results_expected = ["HELLO WORLD"]

    code = """print("HELLO WORLD")"""

    msg, results = run_exercise("python", code, None, ["HELLO WORLD"])

    assert msg == msg_expected

    assert results_expected == results


def test_invalid_language_error():
    code = "Sum a b = a+b"

    try:
        run_exercise("haskell", "Example", None, ["Bye World"])

        pytest.fail("Haskell currently is not a valid language")

    except UnsupportedLanguageError:
        pass

    except CodeKernelException:
        pytest.fail("CodeKernelException is not the expected exception")
