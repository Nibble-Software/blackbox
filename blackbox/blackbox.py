from typing import TypedDict
from .evaluation.evaluation import run_exercise


class BlackBoxResult(TypedDict):
    status: str
    expected: list[str]
    got: list[str]


def blackbox(
    language: str, solution: str, inputs: [str], outputs: [str]
) -> BlackBoxResult:
    status, results = run_exercise(language, solution, inputs, outputs)

    return {"status": status, "expected": outputs, "got": results}
