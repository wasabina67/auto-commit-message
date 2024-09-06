import subprocess


def main():
    result = subprocess.run(["git", "status", "--short"], stdout=subprocess.PIPE)
    changes = result.stdout.decode("utf-8").split("\n")
    print(changes)


if __name__ == "__main__":
    main()
