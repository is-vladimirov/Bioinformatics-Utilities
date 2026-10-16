from pathlib import Path


from helpers.fastq import read_fastq, write_fastq, check_read


from helpers.bio_files import (
    write_one_line_fasta,
    get_best_hits,
    write_sorted_hits,
)


def filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    """Фильтрует риды по GC-составу, длине и качеству"""
    output_dir = Path("filtered")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / output_fastq

    with open(input_fastq, "r") as input_file, open(output_path, "w") as output_file:
        while True:
            read = read_fastq(input_file)

            if read is None:
                break

            if check_read(read, gc_bounds, length_bounds, quality_threshold):
                write_fastq(output_file, read)


def convert_multiline_fasta_to_one_line(input_fasta, output_fasta=None):
    """Преобразует многострочный FASTA в однострочный"""

    if output_fasta is None:
        input_path = Path(input_fasta)
        output_fasta = input_path.with_name(input_path.stem + "_one_line.fasta")

    with open(input_fasta, "r") as input_file, open(output_fasta, "w") as output_file:
        write_one_line_fasta(input_file, output_file)


def parse_blast_output(input_file, output_file):
    """Сохраняет лучшие BLAST-совпадения в алфавитном порядке"""

    with open(input_file, "r") as source:
        hits = get_best_hits(source)

    with open(output_file, "w") as target:
        write_sorted_hits(target, hits)
