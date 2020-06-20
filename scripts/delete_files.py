import os
from pathlib import Path

scanned_directory = "/Users/alazaroc/Downloads"
extension_of_files_to_be_deleted = ".url"


def delete_file(path, extension):
    path_directory = Path(path)
    for file in path_directory.glob("*"):
        if str(file).endswith(extension):
            os.remove(file)
            print(f"Deleted: {file}")


delete_file(scanned_directory, extension_of_files_to_be_deleted)
