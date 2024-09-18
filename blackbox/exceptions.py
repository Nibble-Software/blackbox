class BlackBoxException(Exception):
    def __init__(self, message: str):
        self.message = message


class CodeKernelException(BlackBoxException):
    def __init__(self, details: str):
        super().__init__(f"An error occurred - details {details}")
        self.message = f"An error occurred - details {details}"


class CodeTimeoutError(BlackBoxException):
    def __init__(self):
        super().__init__("Code execution timeout")

    pass


class CompilationError(BlackBoxException):
    def __init__(self):
        super().__init__("Compilation error")

    pass


class ExecutionError(BlackBoxException):
    def __init__(self):
        super().__init__("Execution error")

    pass


class FailedProcessError(BlackBoxException):

    def __init__(self):
        super().__init__("Failed process error")
        pass


class MissingOutputsError(BlackBoxException):

    def __init__(self):
        super().__init__("Outputs cannot be missed")


class UnsupportedLanguageError(BlackBoxException):

    def __init__(self, language: str):
        super().__init__(f"Unsupported language - {language}")
        pass
