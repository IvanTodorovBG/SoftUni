from os import listdir, path


def traverse_dir(current_path, files_by_ext):
    for el in listdir(current_path):
        if path.isdir(path.join(current_path, el)):
            traverse_dir(path.join(current_path, el), files_by_ext)
        else:
            extension = el.split(".")[-1]
            if extension not in files_by_ext:
                files_by_ext[extension] = []
            files_by_ext[extension].append(el)


files_by_ext = {}
traverse_dir(".", files_by_ext)

for ext, files in sorted(files_by_ext.items()):
    print(f".{ext}")
    for file in sorted(files):
        print(f'---{file}')
