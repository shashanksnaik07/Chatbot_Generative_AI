import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] : %(message)s:')

list_of_files = [
    'src/__init__.py',  # constructor file
    'src/helper.py',  # functionality (hugging tokenization)
    'src/prompt.py',  # Prompts
    '.env',
    "setup.py",
    "app.py",
    "research/trails.ipynb"
]

for filepath_str in list_of_files:
    filepath = Path(filepath_str)
    filedir, filename = os.path.split(filepath)

    if filedir and not os.path.exists(filedir):
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'Creating directory: {filedir} for the file: {filename}')

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            logging.info(f'Creating empty file: {filepath}')

    else:
        logging.info(f'{filename} already exists')
