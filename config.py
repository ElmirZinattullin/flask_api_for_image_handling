from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

UPLOAD_FOLDER = BASE_DIR / 'uploads'
RESULT_FOLDER = BASE_DIR / 'results'
WEIGHS_PATH = BASE_DIR / 'weighs.txt'

UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
RESULT_FOLDER.mkdir(parents=True, exist_ok=True)

if not os.path.exists(WEIGHS_PATH):
    print(f"Файл '{WEIGHS_PATH}' не найден")
    # raise OSError(f"Файл '{WEIGHS_PATH}' не найден")