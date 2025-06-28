import shutil
from pathlib import Path
import time

source = Path("work_with_files/test-files/example.txt")
destination = Path("work_with_files/my_directory/example-copy.txt")

shutil.copy(source, destination)

file_path = Path(destination)
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів")

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime

print(f"Час створення: {time.ctime(creation_time)}")
print(f"Час модифікації: {time.ctime(modification_time)}")

# file_path.unlink(missing_ok=True)
