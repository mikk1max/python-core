import shutil

shutil.make_archive(
    "work_with_files/out/example-zip", "zip", root_dir="work_with_files/folder-to-zip"
)
shutil.make_archive(
    "work_with_files/out/example-gztar",
    "gztar",
    root_dir="work_with_files/folder-to-zip",
)
