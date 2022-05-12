import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        return sys.stderr.write("Formato inválido\n")
    try:
        with open(path_file) as file:
            lines = file.read().split("\n")
            return lines
    except IOError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
