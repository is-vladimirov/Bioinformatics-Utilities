# Bioinformatics Utilities

Небольшой набор утилит на Python для преобразования файлов FASTQ, FASTA и BLAST.
Не требует установки сторонних библиотек.

## Структура проекта
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
- `main.py` - основные функции для работы с файлами

- `helpers/fastq.py` - функции чтения, записи и фильтрации FASTQ

- `helpers/bio_files.py` - вспомогательные функции обработки FASTA и BLAST

- `data/` - исходные файлы (уже содержит тестовые файлы для проверки)

- директория для отфильтрованных FASTQ-файлов `filtered/` создаётся автоматически

## Функционал

#### 1. Фильтрация FASTQ

Функция `filter_fastq()` фильтрует риды по следующим параметрам:

- GC-состав последовательности (в процентах)

- Длина последовательности

- Среднее качество нуклеотидов (Phred+33) в последовательности

Результат сохраняется в filtered/result.fastq. Для фильтрации по GC-составу и длине последовательности можно задавать обе границы, или только верхнюю.

Пример использования:
```python 
filter_fastq(
    input_fastq="data/example_fastq.fastq",
    output_fastq="result.fastq",
    gc_bounds=(20, 80),
    length_bounds=(50, 200),
    quality_threshold=30,
)
```

#### 2. Преобразование FASTA

Функция `convert_multiline_fasta_to_one_line()` преобразует многострочные FASTA-последовательности в однострочные.

Аргумент output_fasta необязателен. Если он не указан, создаётся файл с суффиксом _oneline.fasta.

Пример использования:
```python 
convert_multiline_fasta_to_oneline(
    input_fasta="data/example_multiline_fasta", output_fasta="data/oneline.fasta"
)
```

#### 3. Работа с BLAST

Функция `parse_blast_output()` извлекает название лучшего совпадения с базой для каждой последовательности и записывает в файл в алфавитном порядке.

Пример использования:
```python 
parse_blast_output(
    input_file="data/example_blast_results.txt", output_file="data/best_hits.txt"
)
```


## Использование

Требуется Python 3.9 или новее.

Склонируйте или скачайте проект и перейдите в его директорию.

Для использования функций импортируйте их из main.py:
```python
from main import filter_fastq, convert_multiline_fasta_to_oneline, parse_blast_output
```
