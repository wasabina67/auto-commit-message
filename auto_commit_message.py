import subprocess


def get_changes():
    result = subprocess.run(["git", "status", "--short"], stdout=subprocess.PIPE)
    return result.stdout.decode("utf-8").split("\n")


def main():
    changes = get_changes()
    print(changes)


if __name__ == "__main__":
    main()
