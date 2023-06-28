from ting_file_management.queue import Queue


def exists_word(word, instance: Queue):
    result = []

    i = 0
    while i < len(instance):
        file = instance.search(i)

        occurrence_list = []

        line_index = 1
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                occurrence_list.append({"linha": line_index})

            line_index += 1

        if occurrence_list:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrence_list
            })
        i += 1

    return result


def search_by_word(word, instance: Queue):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)

        occurrence_list = []

        line_index = 1
        for line in file["linhas_do_arquivo"]:
            if word.lower() in line.lower():
                occurrence_list.append({
                    "linha": line_index,
                    "conteudo": line
                })

            line_index += 1

        if occurrence_list:
            result.append({
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": occurrence_list
            })

    return result
