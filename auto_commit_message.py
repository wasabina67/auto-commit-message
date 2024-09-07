import subprocess


def get_changes():
    result = subprocess.run(["git", "status", "--short"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").split("\n")


def main():
    changes = get_changes()
    print(changes)

    update_files = []
    create_files = []
    delete_files = []
    rename_files = []

    for change in changes:
        if change == "":
            continue

        staging, working, space, file = \
            change[0], change[1], change[2], change[3:]  # noqa

        if staging == " " and space == " ":
            continue
        elif staging == "M" and space == " ":
            update_files.append(file)
        elif staging == "A" and space == " ":
            create_files.append(file)
        elif staging == "D" and space == " ":
            delete_files.append(file)
        elif staging == "R" and space == " ":
            rename_files.append(file)
        else:
            raise Exception("aaa")

    print(update_files, create_files, delete_files, rename_files)


if __name__ == "__main__":
    main()
