from pathlib import Path


# p = Path("work_with_files/test-files/example.txt")
# p.write_text("Hello, world!")
# print(p.read_text())
# print("Exists:", p.exists())


# base_path = Path("/")
# full_path = base_path / "work_with_files" / "test-files"
# print(full_path)


# directory = Path("./work_with_files")

# for path in directory.iterdir():
#     print(path)


# directory = Path("./work_with_files/my_directory/new_folder")
# directory.mkdir(parents=True, exist_ok=True)


# directory = Path("./work_with_files/my_directory/new_folder")
# directory.rmdir()

path = Path("./work_with_files/my_directory")

if path.exists():
    print(f"{path} існує")

if path.is_dir():
    print(f"{path} є директорією")

if path.is_file():
    print(f"{path} є файлом")
