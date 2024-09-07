import subprocess


def get_commit_message(files_tuple):
    message = ""
    update, create, delete, rename = files_tuple
    for files, action in [(update, "Update"), (create, "Create"), (delete, "Delete"), (rename, "Rename")]:
        if files:
            files_joined = ", ".join(files)
            message = message + f" & {action} {files_joined}" if message else f"{action} {files_joined}"

    return message


def get_changes():
    result = subprocess.run(["git", "status", "--short"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").split("\n")


def main():
    try:
        changes = get_changes()
        if changes == [""]:
            return

        update_files = []
        create_files = []
        delete_files = []
        rename_files = []

        for change in changes:
            if change == "":
                continue

            staging, working, space, file = \
                change[0], change[1], change[2], change[3:]

            if staging == "M" and space == " ":
                update_files.append(file)
            elif staging == "A" and space == " ":
                create_files.append(file)
            elif staging == "D" and space == " ":
                delete_files.append(file)
            elif staging == "R" and space == " ":
                rename_files.append(file)
            elif staging == " " and space == " ":
                continue
            elif staging == "?" and working == "?" and space == " ":
                continue
            else:
                raise Exception(change)

        message = get_commit_message(files_tuple=(update_files, create_files, delete_files, rename_files))
        if message:
            print(message)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
