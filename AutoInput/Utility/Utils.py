import os


def make_directory(path, name):
    os.path.join(path)

    if not os.path.exists(name):
        os.mkdir(name)


def make_directories_to_target(target):
    if not os.path.exists(target):
        os.makedirs(target)
