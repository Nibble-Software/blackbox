import tempfile
import os


def create_temp_file(body: str, extension: str) -> str:
    file = tempfile.NamedTemporaryFile(mode="w", suffix=f".{extension}", delete=False)
    filename = file.name
    file.write(body)
    file.close()
    return filename


def delete_temp_file(filepath: str):
    os.remove(filepath)
