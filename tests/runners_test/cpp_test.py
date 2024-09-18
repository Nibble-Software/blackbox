from pytest import fail


from blackbox.exceptions import CodeTimeoutError, CompilationError, ExecutionError
from blackbox.runners.cpp_runner import run_cpp, __compile_cpp
from tests.mock.file_mocker import generate_file


def test_compile_cpp():

    hello_world: str = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }
    """

    filename = generate_file(hello_world, "cpp")

    __compile_cpp(filename)


def test_hello_world():

    expected: str = "HELLO WORLD"

    hello_world: str = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD");
        return 0;
    }
    """

    filename = generate_file(hello_world, "cpp")

    results: [str] = run_cpp(filename, None)

    assert results[0] == expected


def test_infinite_loop():

    expected: str = "HELLO WORLD"

    hello_world: str = """
        #include <stdio.h>
        int main(){
            while(1);
        }
        """

    filename: str = generate_file(hello_world, "cpp")

    try:
        results: [str] = run_cpp(filename, None)

        fail()

    except CodeTimeoutError:
        pass


def test_addition():

    expected: str = "5"

    inputs: [str] = ["2", "3"]

    code = """
    #include <stdio.h>
    int main(){
        int a,b;
        scanf("%d",&a);
        scanf("%d",&b);
        printf("%d",a+b);
        return 0;
    }
    """

    filename = generate_file(code, "cpp")

    results: [str] = run_cpp(filename, inputs)

    print(results)

    assert results[0] == expected


def test_addition_infinite_loop():

    try:
        expected: str = "5"

        inputs: [str] = ["2,", "3"]

        code = """
            #include <stdio.h>
            int main(){
                int a,b;
                scanf("%d",&a);
                scanf("%d",&b);
                printf("%d",a+b);
                while(1);
                return 0;
            }
            """

        filename = generate_file(code, "cpp")

        results: [str] = run_cpp(filename, inputs)

        fail()

    except CodeTimeoutError as error:
        pass

    except Exception as error2:
        fail("It should raise a timeout")


def test_failed_compilation():
    try:

        code = """
    #include <stdio.h>
    int main(){
        printf("HELLO WORLD")
        return 0;
    }
    """

        filename = generate_file(code, "cpp")

        results = run_cpp(filename, None)

        fail("It should raise a compilation exception")

    except CompilationError as compilation_error:
        pass


def test_failed_execution():

    try:
        expected: str = "5"

        inputs: [str] = ["2,", "3"]

        code = """
               #include <stdio.h>
               int main(){
                   int a,b;
                   scanf("%d",&a);
                   scanf("%d",&b);
                   printf("%d",0/0);
                   return -1;
               }
               """

        filename = generate_file(code, "cpp")

        results: [str] = run_cpp(filename, inputs)

        fail("The tests passes and doesn't have code -1")

    except ExecutionError as error:
        pass

    except Exception as error2:
        fail("It should raise an execution error")
