from ..evaluation import language as supported_languages
from ..exceptions import (
    CompilationError,
    ExecutionError,
    CodeTimeoutError,
    UnsupportedLanguageError,
    CodeKernelException,
)
from .temp_files import create_temp_file
from .status import TestStatus


def run_exercise(
    language: str, solution: str, inputs: [str], outputs: [str]
) -> tuple[str, [str]]:
    try:
        runner, extension = supported_languages.get_runner_and_extension(language)
        filename = create_temp_file(solution, extension)

        results = runner(filename, inputs)

        if outputs == results:
            return TestStatus.PASSED, results
        else:
            return TestStatus.FAILED, results

    except CompilationError:
        return TestStatus.COMPILATION_ERROR, []

    except ExecutionError:
        return TestStatus.EXECUTION_ERROR, []

    except CodeTimeoutError:
        return TestStatus.TIMEOUT_ERROR, []

    except UnsupportedLanguageError:
        raise UnsupportedLanguageError(language)

    except Exception as exception:
        raise CodeKernelException(str(exception))
