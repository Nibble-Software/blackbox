from ..exceptions import UnsupportedLanguageError
from typing import Callable, TypedDict, TypeVar
from ..runners.cpp_runner import run_cpp
from ..runners.py_runner import run_py


__all__ = ["get_runner_and_extension"]

Runner = TypeVar("Runner", bound=Callable[[str, list[str]], list[str]])


class __LanguageRunner(TypedDict):
    extension: str
    run: Runner


__supported_languages: dict[str, __LanguageRunner] = {
    "c++": {"extension": "cpp", "run": run_cpp},
    "python": {"extension": "py", "run": run_py},
}


def get_runner_and_extension(
    language: str,
) -> tuple[Runner, str]:
    selected_language = __supported_languages.get(language)

    if selected_language is None:
        raise UnsupportedLanguageError(language)

    return selected_language["run"], selected_language["extension"]
