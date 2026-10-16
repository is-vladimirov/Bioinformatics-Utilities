import re


def write_one_line_fasta(input_file, output_file):
    """Преобразует многострочный FASTA в однострочный"""

    sequence_started = False  # определяет читаем ли мы рид в данный момент, или нет

    for line in input_file:
        line = line.strip()

        if not line:  # пропуск пустых строк
            continue

        if line.startswith(
            ">"
        ):  # если находим следующий заголовок, значит прошлый рид закончился, нужно переносить строку
            if sequence_started:
                output_file.write("\n")

            output_file.write(line + "\n")
            sequence_started = False

        else:
            output_file.write(line)
            sequence_started = True

    if sequence_started:
        output_file.write("\n")


def get_best_hits(input_file):
    """Поиск лучшего совпадения в файле blast_results"""

    best_hits = []
    in_results = False
    header_found = False

    for line in input_file:
        line = line.strip()

        if line.startswith("Query="):  # находим строку с запросом
            in_results = False
            header_found = False

        elif (
            "Sequences producing significant alignments:" in line
        ):  # находим строку с сиквенсом
            in_results = True
            header_found = False

        elif in_results:
            if not line:
                continue

            if not header_found:
                if "Description" in line:  # находим заголовок Description
                    header_found = True
                continue

            columns = re.split(r"\s{2,}", line)

            if columns:
                best_hits.append(columns[0])
                in_results = False

    return best_hits


def write_sorted_hits(output_file, hits):
    """Сортирует совпадения и записывает в файл"""

    for hit in sorted(hits):
        output_file.write(hit + "\n")
