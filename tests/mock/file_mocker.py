import tempfile


def generate_file(code: str, extension: str) -> str:
    file = tempfile.NamedTemporaryFile(mode='w', suffix=f'.{extension}', delete=False)

    file.write(code)

    file.close()

    return file.name
