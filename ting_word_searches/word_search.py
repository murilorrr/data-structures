from ting_file_management.file_process import process
from ting_file_management.queue import Queue


def exists_word(word, instance):
    """Aqui irá sua implementação"""
    word_lower = word.lower()
    arrayOf = []
    tamanho = len(instance)
    for item in range(tamanho):
        elemento = instance.search(item)

        initial_dict = {
            "palavra": word,
            "arquivo": elemento["nome_do_arquivo"],
            "ocorrencias": []
        }

        for index, linha in enumerate(elemento["linhas_do_arquivo"]):
            if word_lower in linha.lower():
                initial_dict["ocorrencias"].append({"linha": index + 1})

        arrayOf.append(initial_dict)
        if initial_dict["ocorrencias"]:
            return arrayOf
    return []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    word_lower = word.lower()
    arrayOf = []
    tamanho = len(instance)
    for item in range(tamanho):
        elemento = instance.search(item)

        initial_dict = {
            "palavra": word,
            "arquivo": elemento["nome_do_arquivo"],
            "ocorrencias": []
        }

        for index, linha in enumerate(elemento["linhas_do_arquivo"]):
            if word_lower in linha.lower():
                initial_dict["ocorrencias"].append({
                    "linha": index + 1,
                    "conteudo": linha
                })

        arrayOf.append(initial_dict)
        if initial_dict["ocorrencias"]:
            return arrayOf
    return []


if(__name__ == "__main__"):
    project = Queue()
    process("statics/nome_pedro.txt", project)
    word = exists_word("pedro", project)
    print(word)
