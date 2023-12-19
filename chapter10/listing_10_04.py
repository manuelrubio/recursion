import os


def print_path_file_recursive(file_name, folder):
    for entry in os.scandir(folder):
        if entry.is_file() and file_name == entry.name:
            print(entry.path)
        elif entry.is_dir():
            print_path_file_recursive(file_name, entry.path)


print_path_file_recursive('file01.txt', '.')
