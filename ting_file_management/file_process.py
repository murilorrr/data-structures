import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    lines = txt_importer(path_file)
    dict_process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }
    instance.enqueue(dict_process)
    print(dict_process, file=sys.stdout)
    return dict_process


def remove(instance):
    try:
        removed_item = instance.dequeue()
        name = removed_item["nome_do_arquivo"]
        print(f"Arquivo {name} removido com sucesso", file=sys.stdout)
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        searched_item = instance.search(position)
        print(f"{searched_item}", file=sys.stdout)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
