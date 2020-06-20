import shutil
from pathlib import Path

user_directory = 'alazaroc'
source_path = f"/Users/{user_directory}/Downloads/"
destination_path = f"/Users/{user_directory}/Documents/Videos/"
extension_files = ['.avi', '.mkv', '.mp4']


def move_file(file, destination):
    shutil.move(file.absolute(), destination + file.name)
    print("Moved: ", file.absolute())


def check_files(file, destination, extensions):
    for extension in extensions:
        if str(file).endswith(extension):
            move_file(file, destination)


def move_files(source, destination, extensions):
    path = Path(source)
    for file in path.glob("*"):
        if file.is_dir():
            for file2 in file.glob("*"):
                check_files(file2, destination, extensions)
        else:
            check_files(file, destination, extensions)


move_files(source_path, destination_path, extension_files)
