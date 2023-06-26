import sys
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance: Queue):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    new_file = {
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(txt_importer(path_file)),
        'linhas_do_arquivo': txt_importer(path_file),
    }
    instance.enqueue(new_file)
    print(new_file)


def remove(instance):
    if len(instance) == 0:
        return print("Não há elementos")
    removed_element = instance.dequeue()
    print(f"Arquivo {removed_element['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print('Posição inválida', file=sys.stderr)
