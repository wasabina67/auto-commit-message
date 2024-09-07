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


if __name__ == "__main__":
    main()
