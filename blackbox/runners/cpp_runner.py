from ..utilities import process
from ..utilities.system import get_tempdir, get_file_separator, get_os_name
from ..exceptions import FailedProcessError, CompilationError


def run_cpp(filepath: str, inputs: [str]) -> [str]:

    executable_path = __compile_cpp(filepath)

    outputs = process.run_code(executable_path, None, inputs)

    return outputs


def __compile_cpp(filepath: str):
    try:
        tempdir = get_tempdir()

        separator = get_file_separator()

        extension = "exe" if get_os_name() == "WINDOWS" else "out"

        executable_path = f"{tempdir}{separator}a.{extension}"

        process.run_process("g++", [filepath, "-o", executable_path])

        return executable_path

    except FailedProcessError:
        raise CompilationError()
