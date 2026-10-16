def bounds_unification(bounds):
    """Преобразует одно число в 2 границы; если заданы обе границы, возвращает их"""
    if isinstance(bounds, (int, float)):
        return 0, bounds
    return bounds

def read_fastq(file):
    """Читает один рид (4 строки) из FASTQ-файла"""
    header = file.readline()

    if not header:
        return None

    sequence = file.readline()
    separator = file.readline()
    quality = file.readline()


    return header, sequence, separator, quality

def write_fastq(file, read):
    """Записывает один рид в FASTQ-файл"""
    file.writelines(read)



def check_gc(sequence, gc_bounds):
    """Вычисляет GC-состав рида в процентах и сравнивает с допустимыми значениями"""
    lower, upper = bounds_unification(gc_bounds)

    sequence = sequence.strip().upper()

    if not sequence:
        gc_content = 0
    else:
        gc_content = (
            (sequence.count("G") + sequence.count("C"))
            / len(sequence)
            * 100
        )

    return lower <= gc_content <= upper



def check_length(sequence, length_bounds):
    """Проверяет длину рида"""
    lower, upper = bounds_unification(length_bounds)

    length = len(sequence.strip())

    return lower <= length <= upper



def check_quality(quality, quality_threshold):
    """Вычисляет среднее качество рида по шкале Phred+33 и сравнивает с допустимыми значениями"""
    quality = quality.strip()

    if not quality:
        return 0 >= quality_threshold

    mean_quality = sum(ord(char) - 33 for char in quality) / len(quality)

    return mean_quality >= quality_threshold



def check_read(read, gc_bounds, length_bounds, quality_threshold):
    """Проверяет рид на соответствие введенным условиям"""
    sequence = read[1]
    quality = read[3]

    return (
        check_gc(sequence, gc_bounds)
        and check_length(sequence, length_bounds)
        and check_quality(quality, quality_threshold)
    )