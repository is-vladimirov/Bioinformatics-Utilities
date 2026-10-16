# Bioinformatics Utilities

A small set of Python utilities for converting FASTQ, FASTA, and BLAST files.
No required installation of any additional libraries.

## Project structure
```
Bioinformatics Utilities/
├── main.py
├── helpers/
│   ├── fastq.py
│   └── bio_files.py
├── data/
│   ├── example_fastq.fastq
│   ├── example_multiline_fasta.fasta
│   └── example_blast_results.txt
└── README.md
```
- `main.py` - contain the main functions

- `helpers/fastq.py` - FASTQ reading, writing and filtering

- `helpers/bio_files.py` - supporting functions for FASTA and BLAST

- `data/` - source files (already includes test files for testing)

- the directory for filtered FASTQ files `filtered/` is created automatically

## Functions list

#### 1. FASTQ filtering

`filter_fastq()` filters reads based on the following parameters:

- GC content of the sequence (in percentage)

- Sequence length

- Average nucleotide quality in sequence (Phred+33) 

The result is saved to `filtered/result.fastq`. For filtering based on GC content and sequence length, you can specify both boundaries or just the upper boundary.

Example of use:
```python 
filter_fastq(
    input_fastq="data/example_fastq.fastq",
    output_fastq="result.fastq",
    gc_bounds=(20, 80),
    length_bounds=(50, 200),
    quality_threshold=30,
)
```

#### 2. Multiline FASTA converter

`convert_multiline_fasta_to_one_line()` converts multiline FASTA sequences into single-line sequences.

The `output_fasta` argument is optional. If it is not specified, a file with the suffix `_oneline.fasta` is created.

Example of use:
```python 
convert_multiline_fasta_to_oneline(
    input_fasta="data/example_multiline_fasta", output_fasta="data/oneline.fasta"
)
```

#### 3. BLAST parsing

`parse_blast_output()` extracts the name of the best database match for each sequence and writes it to a file in alphabetical order.

Example of use:
```python 
parse_blast_output(
    input_file="data/example_blast_results.txt", output_file="data/best_hits.txt"
)
```


## How to use

Python 3.9 or later is required.

Clone or download the repository and navigate to main directory.

To use the functions, import them from `main.py`:
```python
from main import filter_fastq, convert_multiline_fasta_to_oneline, parse_blast_output
```
