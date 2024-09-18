import subprocess
from subprocess import PIPE, TimeoutExpired, Popen
from ..exceptions import FailedProcessError, CodeTimeoutError, ExecutionError


def run_process(process_name: str, args: [str]):
    process = subprocess.Popen([process_name] + args)
    return_code = process.wait()
    if return_code != 0:
        raise FailedProcessError()


def run_code(process_name: str, args: list[str] | None, inputs: list[str] | None) -> list[str]:
    process = (
        Popen([process_name] + args, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        if args is not None
        else Popen([process_name], stdout=PIPE, stdin=PIPE, stderr=PIPE)
    )

    if inputs is None:
        outputs = __no_input_execution(process)
        return outputs

    else:
        outputs = __input_execution(process, inputs)
        return outputs


def __no_input_execution(process: Popen) -> [str]:
    try:
        data = __execute_process(process)

        if process.returncode != 0:
            raise ExecutionError()

        return data

    except TimeoutExpired:
        process.terminate()
        process.communicate()

        raise CodeTimeoutError()


def __input_execution(process: Popen, inputs: [str]) -> [str]:
    try:
        input_string = "".join(input_data + "\n" for input_data in inputs)

        process.stdin.write(input_string.encode("UTF-8"))

        data = __execute_process(process)

        process.terminate()

        print(data)

        if process.returncode != 0:
            raise ExecutionError()

        return data

    except TimeoutExpired:

        process.terminate()
        process.communicate()

        raise CodeTimeoutError()


def __execute_process(process):
    data, error = process.communicate(timeout=10)

    data = data.decode("latin1").split("\n")

    data = [item.replace("\r", "") for item in data if item != ""]

    process.stdin.close()
    process.stdout.close()
    process.stderr.close()

    return data
