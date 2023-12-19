import os


def print_path_file_iterative(file_name, folder):
    stack = []
    for entry in os.scandir(folder):
        if entry.is_file() and file_name == entry.name:
            print(entry.path)
        elif entry.is_dir():
            stack.append(entry)

    while len(stack) > 0:
        entry = stack.pop()
        for entry in os.scandir(entry.path):
            if entry.is_file() and file_name == entry.name:
                print(entry.path)
            elif entry.is_dir():
                stack.append(entry)


print_path_file_iterative('file01.txt', '.')
