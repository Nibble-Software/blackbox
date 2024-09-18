import platform
import os


def get_tempdir() -> str:
    return os.environ['TEMP'] if 'Windows' in platform.system() else '/tmp'


def get_file_separator() -> str:
    return '\\' if 'Windows' in platform.system() else '/'


def get_os_name() -> str:
    return platform.system()

