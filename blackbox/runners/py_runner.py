from ..utilities.process import run_code


def run_py(filepath: str, inputs: [str]) -> [str]:
    return run_code('python', [filepath], inputs)
